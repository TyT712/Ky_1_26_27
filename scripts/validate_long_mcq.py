# -*- coding: utf-8 -*-
"""Kiểm tra chất lượng riêng cho môn dùng ngân hàng 100 câu / chương, đáp án dài, lý thuyết Cornell.

Usage: python scripts/validate_long_mcq.py <course_id> [chapter_id ...]
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
MIN_MCQ = 100
MIN_OPT_CHARS = 60
MIN_OPT_WORDS = 10
BANNED = ["tất cả các đáp án trên", "tất cả đáp án trên", "cả a, b", "không có đáp án nào", "cả ba đáp án"]


def check_chapter(course_id, ch):
    d = ROOT / "docs" / "data" / course_id
    errs = []
    jf, tf = d / f"{ch}_exercises.json", d / f"{ch}_theory.md"
    if not jf.exists() or not tf.exists():
        return [f"thiếu file {jf.name} hoặc {tf.name}"]
    data = json.loads(jf.read_text(encoding="utf-8"))
    mcq = data["multiple_choice"]
    if len(mcq) < MIN_MCQ:
        errs.append(f"chỉ có {len(mcq)}/{MIN_MCQ} câu trắc nghiệm")
    if len(data["short_answers"]) < 8:
        errs.append("thiếu câu trả lời ngắn (<8)")
    if len(data["essays"]) < 4:
        errs.append("thiếu tự luận (<4)")
    ids = [q["id"] for q in mcq]
    if ids != list(range(1, len(mcq) + 1)):
        errs.append("id trắc nghiệm phải liên tục 1..N")
    seen = set()
    longest_correct = 0
    dist = Counter()
    diff = Counter()
    for q in mcq:
        qid = q["id"]
        qt = re.sub(r"\s+", " ", q["question"]).strip()
        if len(qt) < 25 or qt in seen:
            errs.append(f"câu {qid}: câu hỏi quá ngắn hoặc trùng")
        seen.add(qt)
        if q.get("difficulty") not in ("easy", "medium", "hard"):
            errs.append(f"câu {qid}: difficulty không hợp lệ")
        diff[q.get("difficulty")] += 1
        o = q["options"]
        if set(o) != {"A", "B", "C", "D"}:
            errs.append(f"câu {qid}: thiếu phương án")
            continue
        lens = {}
        for k, v in o.items():
            v = str(v).strip()
            lens[k] = len(v)
            if len(v) < MIN_OPT_CHARS or len(v.split()) < MIN_OPT_WORDS:
                errs.append(f"câu {qid} phương án {k} quá ngắn ({len(v)} ký tự, {len(v.split())} từ)")
            if any(b in v.lower() for b in BANNED):
                errs.append(f"câu {qid} phương án {k} chứa cụm cấm")
        if len({str(v).strip() for v in o.values()}) < 4:
            errs.append(f"câu {qid}: có phương án trùng nhau")
        if q["correct_answer"] not in o:
            errs.append(f"câu {qid}: correct_answer sai")
            continue
        dist[q["correct_answer"]] += 1
        if lens[q["correct_answer"]] == max(lens.values()):
            longest_correct += 1
        if len(str(q.get("explanation", "")).strip()) < 40:
            errs.append(f"câu {qid}: explanation quá ngắn")
    n = max(len(mcq), 1)
    for k in "ABCD":
        if not (0.18 <= dist[k] / n <= 0.32):
            errs.append(f"phân bố đáp án đúng lệch: {dict(dist)}")
            break
    if longest_correct / n > 0.45:
        errs.append(f"đáp án đúng quá thường là phương án dài nhất ({longest_correct}/{n})")
    for lvl in ("easy", "medium", "hard"):
        if diff[lvl] < 15:
            errs.append(f"độ khó {lvl} quá ít ({diff[lvl]})")
    theory = tf.read_text(encoding="utf-8")
    if len(theory) < 4000:
        errs.append("lý thuyết quá ngắn (<4000 ký tự)")
    for marker in ("Cornell", "Từ khóa", "Ghi chú", "Tóm tắt"):
        if marker not in theory:
            errs.append(f"lý thuyết thiếu thành phần Cornell: '{marker}'")
    print(f"  {ch}: MCQ={len(mcq)} dist={dict(dist)} diff={dict(diff)} longest_correct={longest_correct} theory={len(theory)} chars")
    return errs


if __name__ == "__main__":
    course = sys.argv[1]
    chapters = sys.argv[2:] or [f"chuong_{i}" for i in range(1, 8)]
    bad = False
    for ch in chapters:
        errs = check_chapter(course, ch)
        if errs:
            bad = True
            print(f"[FAIL] {ch}: {len(errs)} lỗi")
            for e in errs[:40]:
                print("    -", e)
        else:
            print(f"[PASS] {ch}")
    sys.exit(1 if bad else 0)

