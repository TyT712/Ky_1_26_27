# -*- coding: utf-8 -*-
"""Verification & Self-Healing Audit Script for Semester Hub LMS.
Checks:
  1. Skill Registry & Config (.antigravity/skills_registry.json)
  2. Question Banks for 11 Chapters in docs/data/he_qtcsdl/ (>= 30 MCQ, >= 8 Short, >= 4 Essay, valid options/keys/explanations, no duplicates)
  3. Theory files in docs/data/he_qtcsdl/*_theory.md (all 11 exist and non-empty)
  4. Local HTTP server static asset verification (index.html, app.js, style.css, courses_manifest.json)
"""

import http.server
import json
import re
import socketserver
import sys
import threading
import urllib.request
from pathlib import Path

# Fix Windows console UTF-8 output
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DATA = DOCS / "data" / "he_qtcsdl"

CHAPTERS = [
    "q1_chuong_1", "q1_chuong_2", "q1_chuong_3", "q1_chuong_4", "q1_chuong_5", "q1_chuong_6",
    "q2_chuong_1", "q2_chuong_2", "q2_chuong_3", "q2_chuong_4", "q2_chuong_5"
]

def audit_skill_config():
    print("[1/4] Kiểm tra Cấu hình Agent Skill...")
    reg_path = ROOT / ".antigravity" / "skills_registry.json"
    if not reg_path.exists():
        raise AssertionError("Không tìm thấy .antigravity/skills_registry.json")
    
    with open(reg_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    skills = {s["id"]: s for s in data.get("skills", [])}
    if "lms_chapter_pack_generator" not in skills:
        raise AssertionError("Skill 'lms_chapter_pack_generator' chưa được đăng ký trong skills_registry.json")
    
    skill = skills["lms_chapter_pack_generator"]
    guide_path = ROOT / skill.get("guide", "")
    if not guide_path.exists():
        raise AssertionError(f"Tệp hướng dẫn skill không tồn tại: {guide_path}")
    
    print("  -> OK: Skill 'lms_chapter_pack_generator' hợp lệ và hướng dẫn tồn tại.")

def audit_question_banks():
    print("\n[2/4] Kiểm tra Ngân hàng Câu hỏi 11 Chương môn Hệ QTCSDL...")
    total_mcq = 0
    total_short = 0
    total_essay = 0

    for cid in CHAPTERS:
        json_file = DATA / f"{cid}_exercises.json"
        theory_file = DATA / f"{cid}_theory.md"

        if not json_file.exists():
            raise AssertionError(f"Thiếu file bài tập: {json_file}")
        if not theory_file.exists() or theory_file.stat().st_size < 100:
            raise AssertionError(f"File lý thuyết thiếu hoặc quá ngắn: {theory_file}")

        with open(json_file, "r", encoding="utf-8") as f:
            d = json.load(f)

        mcq = d.get("multiple_choice", [])
        short = d.get("short_answers", [])
        essay = d.get("essays", [])

        # Count checks
        if len(mcq) < 30:
            raise AssertionError(f"Chương {cid} chỉ có {len(mcq)}/30 câu trắc nghiệm!")
        if len(short) < 8:
            raise AssertionError(f"Chương {cid} chỉ có {len(short)}/8 câu trả lời ngắn!")
        if len(essay) < 4:
            raise AssertionError(f"Chương {cid} chỉ có {len(essay)}/4 bài tự luận!")

        # Quality checks: no duplicates, valid 4 options, valid correct answer, non-empty explanation
        seen_questions = set()
        for q in mcq:
            qid = q.get("id")
            q_text = q.get("question", "").strip()
            if not q_text:
                raise AssertionError(f"Chương {cid} câu {qid}: question rỗng")
            
            clean_q = re.sub(r"\s+", " ", q_text)
            if clean_q in seen_questions:
                raise AssertionError(f"Chương {cid} phát hiện trùng câu hỏi trắc nghiệm: {clean_q[:60]}...")
            seen_questions.add(clean_q)

            opts = q.get("options", {})
            if set(opts.keys()) != {"A", "B", "C", "D"}:
                raise AssertionError(f"Chương {cid} câu {qid}: phương án không đủ 4 A,B,C,D: {opts.keys()}")
            
            for k, v in opts.items():
                if not str(v).strip():
                    raise AssertionError(f"Chương {cid} câu {qid} phương án {k} bị rỗng")

            ans = q.get("correct_answer")
            if ans not in {"A", "B", "C", "D"}:
                raise AssertionError(f"Chương {cid} câu {qid}: correct_answer không hợp lệ ({ans})")

            expl = q.get("explanation", "").strip()
            if not expl:
                raise AssertionError(f"Chương {cid} câu {qid}: explanation bị rỗng")

        # Short answer quality checks
        seen_short = set()
        for s in short:
            sid = s.get("id")
            sq = s.get("question", "").strip()
            if not sq or sq in seen_short:
                raise AssertionError(f"Chương {cid} câu trả lời ngắn {sid} rỗng hoặc trùng lặp")
            seen_short.add(sq)
            if not s.get("expected_answer", "").strip():
                raise AssertionError(f"Chương {cid} câu trả lời ngắn {sid} thiếu expected_answer")

        # Essay checks
        for e in essay:
            eid = e.get("id")
            if not e.get("title", "").strip() or not e.get("problem", "").strip():
                raise AssertionError(f"Chương {cid} bài tự luận {eid} thiếu title hoặc problem")
            steps = e.get("solution_steps", [])
            if not steps or len(steps) < 2:
                raise AssertionError(f"Chương {cid} bài tự luận {eid} solution_steps phải có ít nhất 2 bước")

        total_mcq += len(mcq)
        total_short += len(short)
        total_essay += len(essay)
        print(f"  -> Chương {cid}: {len(mcq)} trắc nghiệm, {len(short)} trả lời ngắn, {len(essay)} tự luận (PASS)")

    print(f"\n  TỔNG CỘNG 11 CHƯƠNG: {total_mcq} câu trắc nghiệm (>= 330), {total_short} trả lời ngắn (>= 88), {total_essay} tự luận (>= 44).")

def audit_static_server():
    print("\n[3/4] Kiểm tra Static HTTP Server tại docs/...")

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(DOCS), **kwargs)
        def log_message(self, format, *args):
            pass # Im lặng log

    port = 8765
    server = socketserver.TCPServer(("127.0.0.1", port), QuietHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    assets = [
        "index.html",
        "assets/css/style.css",
        "assets/js/app.js",
        "data/courses_manifest.json",
        "data/he_qtcsdl/q1_chuong_1_exercises.json",
        "data/he_qtcsdl/q1_chuong_1_theory.md",
        "data/he_qtcsdl/q2_chuong_5_exercises.json",
        ".nojekyll"
    ]

    try:
        for a in assets:
            url = f"http://127.0.0.1:{port}/{a}"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=5) as res:
                if res.status != 200:
                    raise AssertionError(f"Tải asset thất bại: {url} (HTTP {res.status})")
                data_len = len(res.read())
                print(f"  -> HTTP 200: {a} ({data_len} bytes)")
    finally:
        server.shutdown()
        server.server_close()

def audit_gitignore():
    print("\n[4/4] Kiểm tra tối ưu Repository & .gitignore...")
    gi_path = ROOT / ".gitignore"
    if not gi_path.exists():
        raise AssertionError("Thiếu .gitignore")
    content = gi_path.read_text(encoding="utf-8")
    if "*.pdf" not in content and "data/raw_pdfs" not in content:
        raise AssertionError("Chưa loại trừ file PDF trong .gitignore")
    print("  -> OK: .gitignore đã loại trừ file PDF và các file không cần thiết.")

def main():
    print("================================================================")
    print("   SEMESTER HUB LMS - TỰ ĐỘNG KIỂM ĐỊNH TÍNH TOÀN VẸN (INTEGRITY)")
    print("================================================================")
    try:
        audit_skill_config()
        audit_question_banks()
        audit_static_server()
        audit_gitignore()
        print("\n================================================================")
        print(">>> KẾT QUẢ KIỂM ĐỊNH: TOÀN BỘ 11/11 CHƯƠNG ĐẠT CHUẨN PASS 100%! <<<")
        print("================================================================")
        return 0
    except Exception as e:
        print(f"\n[LỖI KIỂM ĐỊNH]: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
