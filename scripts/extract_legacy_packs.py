"""Tách các gói học liệu Markdown cũ (docs/courses/he_qtcsdl/*.md) thành:
  - build/legacy/{chapter_id}_theory.md      (PHẦN 1)
  - build/legacy/{chapter_id}_legacy.json    (MCQ / short / essay cũ)
Dữ liệu cũ sau đó được gộp với phần bổ sung (scripts/chapter_data/*.json)
bởi scripts/build_lms_data.py để đạt 30 trắc nghiệm / 8 trả lời ngắn / 4 tự luận.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "courses" / "he_qtcsdl"
OUT = ROOT / "build" / "legacy"

MAP = {
    "q1_chuong_1": "q1_chuong_1_tong_quan.md",
    "q1_chuong_2": "q1_chuong_2_mo_hinh_quan_he.md",
    "q1_chuong_3": "q1_chuong_3_dai_so_quan_he.md",
    "q1_chuong_4": "q1_chuong_4_ngon_ngu_sql.md",
    "q1_chuong_5": "q1_chuong_5_rang_buoc_toan_ven.md",
    "q1_chuong_6": "q1_chuong_6_to_chuc_vat_ly_toi_uu.md",
    "q2_chuong_1": "q2_chuong_1_mo_hinh_er.md",
    "q2_chuong_2": "q2_chuong_2_phu_thuoc_ham_va_khoa.md",
    "q2_chuong_3": "q2_chuong_3_chuan_hoa_1nf_bcnf.md",
    "q2_chuong_4": "q2_chuong_4_phan_tach_luoc_do.md",
    "q2_chuong_5": "q2_chuong_5_phu_thuoc_da_tri_4nf.md",
}

DETAILS = re.compile(r"<details>.*?</details>", re.S)


def split_sections(text):
    parts = re.split(r"^## PHẦN (\d)[^\n]*\n", text, flags=re.M)
    secs = {}
    for i in range(1, len(parts), 2):
        secs[int(parts[i])] = parts[i + 1]
    return secs


def blocks(sec, header_re):
    idx = [m for m in re.finditer(header_re, sec, flags=re.M)]
    for i, m in enumerate(idx):
        end = idx[i + 1].start() if i + 1 < len(idx) else len(sec)
        yield m, sec[m.end():end]


def clean_tail(s):
    return re.sub(r"\n---\s*$", "", s.strip()).strip()


def parse_mcq(sec):
    out = []
    for n, (m, body) in enumerate(blocks(sec, r"^### Câu \d+\s*$"), 1):
        dm = DETAILS.search(body)
        head = body[: dm.start()] if dm else body
        det = dm.group(0) if dm else ""
        opts = {}
        qlines = []
        for ln in head.strip().splitlines():
            mo = re.match(r"^- ([ABCD])\.\s*(.*)$", ln)
            if mo:
                opts[mo.group(1)] = mo.group(2).strip()
            else:
                qlines.append(ln)
        ans = re.search(r"\*\*Đáp án đúng:\*\*\s*([ABCD])", det)
        exp = re.search(r"\*\*Giải thích[^:]*:\*\*\s*(.*?)(?=\n- \*\*Căn cứ|\n</details>)", det, re.S)
        out.append({
            "id": n,
            "difficulty": "easy",
            "question": "\n".join(qlines).strip(),
            "options": opts,
            "correct_answer": ans.group(1) if ans else "",
            "explanation": (exp.group(1).strip() if exp else ""),
        })
    return out


def parse_short(sec):
    out = []
    for n, (m, body) in enumerate(blocks(sec, r"^### Câu \d+\s*$"), 1):
        dm = DETAILS.search(body)
        q = (body[: dm.start()] if dm else body).strip()
        det = dm.group(0) if dm else ""
        det = re.sub(r"</?details>|<summary>.*?</summary>", "", det, flags=re.S).strip()
        det = re.sub(r"^- \*\*Đáp án:\*\*\s*", "", det).strip()
        out.append({
            "id": n,
            "question": q,
            "expected_answer": det,
            "explanation": "Đối chiếu đáp án chuẩn ở trên với bài làm của bạn; chú ý các ký hiệu và thứ tự thao tác.",
        })
    return out


def parse_essay(sec):
    out = []
    for n, (m, body) in enumerate(blocks(sec, r"^### Bài \d+:\s*(.*)$"), 1):
        title = m.group(1).strip()
        dm = DETAILS.search(body)
        problem = (body[: dm.start()] if dm else body).strip()
        det = dm.group(0) if dm else ""
        det = re.sub(r"</?details>|<summary>.*?</summary>", "", det, flags=re.S).strip()
        # 1. Tách theo ####
        steps = [s.strip() for s in re.split(r"^#### ", det, flags=re.M) if s.strip()]
        # 2. Nếu < 2, thử tách theo đánh số mục 1. 2. hoặc Bước k
        if len(steps) < 2:
            alt_steps = [s.strip() for s in re.split(r"\n(?=(?:\d+\.\s+|Bước\s+\d+|-\s+\*\*))", det) if s.strip()]
            if len(alt_steps) >= 2:
                steps = alt_steps
        # 3. Nếu vẫn < 2, thử tách theo đoạn văn kép \n\n+
        if len(steps) < 2:
            paras = [p.strip() for p in re.split(r"\n\s*\n", det) if p.strip()]
            if len(paras) >= 2:
                steps = [
                    "Phân tích yêu cầu & cơ sở lý thuyết:\n" + paras[0],
                    "Thực hiện chi tiết & kết luận:\n" + "\n\n".join(paras[1:])
                ]
            else:
                steps = [
                    "Phân tích bài toán:\n" + (problem or title),
                    "Lời giải chi tiết:\n" + det
                ]
        out.append({"id": n, "title": title, "problem": problem, "solution_steps": steps})
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for cid, fn in MAP.items():
        text = (SRC / fn).read_text(encoding="utf-8")
        secs = split_sections(text)
        first_line = text.splitlines()[0].lstrip("# ").strip()
        theory = "# " + first_line + "\n\n" + clean_tail(secs[1]) + "\n"
        (OUT / f"{cid}_theory.md").write_text(theory, encoding="utf-8")
        legacy = {
            "title": first_line,
            "multiple_choice": parse_mcq(secs[2]),
            "short_answers": parse_short(secs[3]),
            "essays": parse_essay(secs[4]),
        }
        (OUT / f"{cid}_legacy.json").write_text(
            json.dumps(legacy, ensure_ascii=False, indent=1), encoding="utf-8")
        print(cid, len(legacy["multiple_choice"]), len(legacy["short_answers"]), len(legacy["essays"]))


if __name__ == "__main__":
    main()
