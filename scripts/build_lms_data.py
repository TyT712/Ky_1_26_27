# -*- coding: utf-8 -*-
"""Xây dựng dữ liệu cho Static SPA LMS (docs/data/) theo skill `lms_chapter_pack_generator`.

Đầu vào:
  - build/legacy/{cid}_theory.md, {cid}_legacy.json   (tạo bởi scripts/extract_legacy_packs.py)
  - scripts/chapter_data/{cid}.py                     (bổ sung 20 trắc nghiệm, 3 trả lời ngắn, 1 tự luận)
  - data/notebook_exports/he_qtcsdl/*_summary.md      (chuyên đề tổng hợp)
Đầu ra:
  - docs/data/courses_manifest.json
  - docs/data/he_qtcsdl/{cid}_theory.md, {cid}_exercises.json
  - docs/data/he_qtcsdl/topics/*.md
Mục tiêu mỗi chương: >= 30 trắc nghiệm (10 easy + 12 medium + 8 hard), >= 8 trả lời ngắn, >= 4 tự luận.
"""
import importlib.util
import json
import random
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGACY = ROOT / "build" / "legacy"
EXTRA = ROOT / "scripts" / "chapter_data"
NOTEBOOK = ROOT / "data" / "notebook_exports" / "he_qtcsdl"
OUT = ROOT / "docs" / "data"
OUT_COURSE = OUT / "he_qtcsdl"

CHAPTERS = [
    # (id, book, số chương, tiêu đề, tóm tắt ngắn)
    ("q1_chuong_1", 1, 1, "Tổng quan về CSDL & kiến trúc ANSI/SPARC",
     "DBMS, ba mức trừu tượng, độc lập dữ liệu, DDL/DML/DCL và tính chất ACID."),
    ("q1_chuong_2", 1, 2, "Mô hình thực thể - liên kết (E-R) & chuyển đổi sang mô hình quan hệ",
     "Thực thể, thuộc tính, bản số, thực thể yếu và 7 quy tắc ánh xạ E-R sang quan hệ."),
    ("q1_chuong_3", 1, 3, "Mô hình quan hệ & Đại số quan hệ",
     "Các phép toán σ, π, ∪, ∩, −, ×, ⋈, ÷ và quy tắc biến đổi biểu thức."),
    ("q1_chuong_4", 1, 4, "Ngôn ngữ truy vấn SQL toàn diện",
     "DDL/DML/DQL, JOIN, GROUP BY - HAVING, truy vấn con và thứ tự thực thi."),
    ("q1_chuong_5", 1, 5, "Tổ chức vật lý dữ liệu & chỉ mục B/B+",
     "Hệ số kết khối, tệp đống/tuần tự/băm, chỉ mục chính-phụ-gom cụm và cây B+."),
    ("q1_chuong_6", 1, 6, "Xử lý & tối ưu hóa câu hỏi truy vấn",
     "Cây truy vấn, tối ưu heuristic, tối ưu theo chi phí và các thuật toán join."),
    ("q2_chuong_1", 2, 1, "Ràng buộc toàn vẹn & kỹ thuật cài đặt Trigger",
     "Bốn yếu tố của RBTV, bảng tầm ảnh hưởng, bảng ảo INSERTED/DELETED, Trigger T-SQL."),
    ("q2_chuong_2", 2, 2, "Phụ thuộc hàm, bao đóng & thuật toán tìm khóa",
     "Hệ tiên đề Armstrong, bao đóng, tìm khóa và phủ tối thiểu."),
    ("q2_chuong_3", 2, 3, "Lý thuyết phân tách lược đồ & bảo toàn thông tin",
     "Bộ giả, điều kiện nối không mất thông tin, bảng Chase, bảo toàn phụ thuộc hàm."),
    ("q2_chuong_4", 2, 4, "Chuẩn hóa CSDL (1NF-BCNF) & thuật toán Bernstein",
     "Định nghĩa 1NF/2NF/3NF/BCNF, phân tách BCNF và tổng hợp 3NF."),
    ("q2_chuong_5", 2, 5, "Phụ thuộc đa trị (MVD) & dạng chuẩn 4NF",
     "MVD, luật bù, định lý Fagin và chuẩn hóa 4NF."),
]

TARGET = {"multiple_choice": 30, "short_answers": 8, "essays": 4}
REF_RE = re.compile(r"(?<![A-Za-zÀ-ỹ])(Ý|ý|Phương án|phương án|Đáp án|đáp án)\s+([ABCD](?:\s*(?:,|và|hoặc)\s*[ABCD])*)(?![A-Za-zÀ-ỹ])")


def load_extra(cid):
    spec = importlib.util.spec_from_file_location(cid, EXTRA / f"{cid}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def shuffle_options(item, cid):
    """Xáo trộn thứ tự phương án (xác định theo seed) và đổi lại các tham chiếu 'ý X' trong lời giải."""
    letters = ["A", "B", "C", "D"]
    old = item["options"]
    order = letters[:]
    random.Random(f"{cid}-{item['id']}").shuffle(order)  # order[i] = chữ cái cũ đặt tại vị trí mới i
    new_opts = {letters[i]: old[order[i]] for i in range(4)}
    mapping = {order[i]: letters[i] for i in range(4)}
    item["options"] = new_opts
    item["correct_answer"] = mapping[item["correct_answer"]]
    item["explanation"] = REF_RE.sub(
        lambda m: m.group(1) + " " + re.sub(r"[ABCD]", lambda x: mapping[x.group(0)], m.group(2)),
        item["explanation"])


def build_chapter(cid, title):
    legacy = json.loads((LEGACY / f"{cid}_legacy.json").read_text(encoding="utf-8"))
    extra = load_extra(cid)

    mcq = []
    for q in legacy["multiple_choice"]:
        q = dict(q)
        q["difficulty"] = "easy"
        mcq.append(q)
    for diff, question, opts, ans, exp in extra.MCQ:
        mcq.append({"difficulty": diff, "question": question,
                    "options": dict(zip("ABCD", opts)), "correct_answer": ans, "explanation": exp})
    for i, q in enumerate(mcq, 1):
        q["id"] = i
        shuffle_options(q, cid)

    short = list(legacy["short_answers"])
    for question, expected, expl in extra.SHORT:
        short.append({"question": question, "expected_answer": expected, "explanation": expl})
    for i, q in enumerate(short, 1):
        q["id"] = i

    essays = list(legacy["essays"])
    for etitle, problem, steps in extra.ESSAY:
        essays.append({"title": etitle, "problem": problem, "solution_steps": steps})
    for i, q in enumerate(essays, 1):
        q["id"] = i

    return {
        "chapter_id": cid,
        "chapter_title": title,
        "multiple_choice": mcq,
        "short_answers": short,
        "essays": essays,
    }


def main():
    OUT_COURSE.mkdir(parents=True, exist_ok=True)
    (OUT_COURSE / "topics").mkdir(exist_ok=True)

    manifest_chapters = {1: [], 2: []}
    for cid, book, num, title, summary in CHAPTERS:
        full_title = f"Quyển {book} - Chương {num}: {title}"
        data = build_chapter(cid, full_title)
        (OUT_COURSE / f"{cid}_exercises.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        shutil.copyfile(LEGACY / f"{cid}_theory.md", OUT_COURSE / f"{cid}_theory.md")
        manifest_chapters[book].append({
            "id": cid,
            "number": num,
            "title": title,
            "full_title": full_title,
            "summary": summary,
            "theory": f"data/he_qtcsdl/{cid}_theory.md",
            "exercises": f"data/he_qtcsdl/{cid}_exercises.json",
            "counts": {k: len(data[k]) for k in TARGET},
        })

    topics = []
    for f in sorted(NOTEBOOK.glob("*_summary.md")):
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, flags=re.M)
        title = m.group(1).strip() if m else f.stem
        shutil.copyfile(f, OUT_COURSE / "topics" / f.name)
        topics.append({"id": f.stem.replace("_summary", ""), "title": title,
                       "file": f"data/he_qtcsdl/topics/{f.name}"})

    manifest = {
        "version": 1,
        "courses": [
            {
                "id": "he_qtcsdl",
                "code": "HQTCSDL",
                "title": "Hệ Quản Trị Cơ Sở Dữ Liệu",
                "description": "Nhập môn CSDL, mô hình E-R, đại số quan hệ, SQL, tối ưu truy vấn, ràng buộc toàn vẹn và lý thuyết chuẩn hóa.",
                "status": "active",
                "books": [
                    {"id": "quyen_1", "title": "Quyển 1: Nhập môn CSDL (Chương 1 - 6)", "chapters": manifest_chapters[1]},
                    {"id": "quyen_2", "title": "Quyển 2: Thiết kế CSDL (Chương 1 - 5)", "chapters": manifest_chapters[2]},
                ],
                "topics": topics,
            },
            {
                "id": "giai_tich_1",
                "code": "GT1",
                "title": "Giải Tích 1",
                "description": "Giới hạn, đạo hàm và ứng dụng. Học liệu đang được chuẩn bị.",
                "status": "coming_soon",
                "books": [],
                "topics": [],
            },
        ],
    }
    (OUT / "courses_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    total = sum(c["counts"]["multiple_choice"] for b in manifest_chapters.values() for c in b)
    print("Built chapters:", sum(len(v) for v in manifest_chapters.values()), "| MCQ total:", total)


if __name__ == "__main__":
    main()
