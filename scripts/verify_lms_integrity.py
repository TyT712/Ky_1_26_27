# -*- coding: utf-8 -*-
"""Verification & Self-Healing Audit Script for Semester Hub LMS.
Checks:
  1. Skill Registry & Config (.antigravity/skills_registry.json)
  2. Question Banks & Theory for all active courses:
     - he_qtcsdl: 11 Chapters
     - cnxhkh: 7 Chapters
     - cnpm: 5 Chapters
     All chapters must satisfy: >= 30 MCQ, >= 8 Short, >= 4 Essay, valid options/keys/explanations, no duplicates.
  3. Local HTTP server static asset verification (index.html, app.js, style.css, courses_manifest.json, sample theory & exercise files).
  4. Repository & .gitignore verification.
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

COURSES_TO_AUDIT = [
    {
        "id": "he_qtcsdl",
        "name": "Hệ Quản Trị Cơ Sở Dữ Liệu",
        "dir": DOCS / "data" / "he_qtcsdl",
        "chapters": [
            "q1_chuong_1", "q1_chuong_2", "q1_chuong_3", "q1_chuong_4", "q1_chuong_5", "q1_chuong_6",
            "q2_chuong_1", "q2_chuong_2", "q2_chuong_3", "q2_chuong_4", "q2_chuong_5"
        ]
    },
    {
        "id": "cnxhkh",
        "name": "Chủ Nghĩa Xã Hội Khoa Học",
        "dir": DOCS / "data" / "cnxhkh",
        "chapters": [
            "chuong_1", "chuong_2", "chuong_3", "chuong_4", "chuong_5", "chuong_6", "chuong_7"
        ]
    },
    {
        "id": "cnpm",
        "name": "Công Nghệ Phần Mềm",
        "dir": DOCS / "data" / "cnpm",
        "chapters": [
            "chuong_1", "chuong_2", "chuong_3", "chuong_4", "chuong_5"
        ]
    }
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

def audit_course_questions(course_info):
    cid_course = course_info["id"]
    cname = course_info["name"]
    cdir = course_info["dir"]
    chapters = course_info["chapters"]

    print(f"\n--- Kiểm tra Ngân hàng câu hỏi môn: {cname} ({len(chapters)} chương) ---")
    course_mcq = 0
    course_short = 0
    course_essay = 0

    for ch in chapters:
        json_file = cdir / f"{ch}_exercises.json"
        theory_file = cdir / f"{ch}_theory.md"

        if not json_file.exists():
            raise AssertionError(f"[{cid_course}] Thiếu file bài tập: {json_file}")
        if not theory_file.exists() or theory_file.stat().st_size < 100:
            raise AssertionError(f"[{cid_course}] File lý thuyết thiếu hoặc quá ngắn: {theory_file}")

        with open(json_file, "r", encoding="utf-8") as f:
            d = json.load(f)

        mcq = d.get("multiple_choice", [])
        short = d.get("short_answers", [])
        essay = d.get("essays", [])

        # Count checks
        if len(mcq) < 30:
            raise AssertionError(f"[{cid_course} - {ch}] chỉ có {len(mcq)}/30 câu trắc nghiệm!")
        if len(short) < 8:
            raise AssertionError(f"[{cid_course} - {ch}] chỉ có {len(short)}/8 câu trả lời ngắn!")
        if len(essay) < 4:
            raise AssertionError(f"[{cid_course} - {ch}] chỉ có {len(essay)}/4 bài tự luận!")

        # Quality checks: no duplicates, valid 4 options, valid correct answer, non-empty explanation
        seen_questions = set()
        for q in mcq:
            qid = q.get("id")
            q_text = q.get("question", "").strip()
            if not q_text:
                raise AssertionError(f"[{cid_course} - {ch}] câu {qid}: question rỗng")
            
            clean_q = re.sub(r"\s+", " ", q_text)
            if clean_q in seen_questions:
                raise AssertionError(f"[{cid_course} - {ch}] phát hiện trùng câu hỏi trắc nghiệm: {clean_q[:60]}...")
            seen_questions.add(clean_q)

            opts = q.get("options", {})
            if set(opts.keys()) != {"A", "B", "C", "D"}:
                raise AssertionError(f"[{cid_course} - {ch}] câu {qid}: phương án không đủ 4 A,B,C,D: {opts.keys()}")
            
            for k, v in opts.items():
                if not str(v).strip():
                    raise AssertionError(f"[{cid_course} - {ch}] câu {qid} phương án {k} bị rỗng")

            ans = q.get("correct_answer")
            if ans not in {"A", "B", "C", "D"}:
                raise AssertionError(f"[{cid_course} - {ch}] câu {qid}: correct_answer không hợp lệ ({ans})")

            expl = q.get("explanation", "").strip()
            if not expl:
                raise AssertionError(f"[{cid_course} - {ch}] câu {qid}: explanation bị rỗng")

        # Short answer quality checks
        seen_short = set()
        for s in short:
            sid = s.get("id")
            sq = s.get("question", "").strip()
            if not sq or sq in seen_short:
                raise AssertionError(f"[{cid_course} - {ch}] câu trả lời ngắn {sid} rỗng hoặc trùng lặp")
            seen_short.add(sq)
            if not s.get("expected_answer", "").strip():
                raise AssertionError(f"[{cid_course} - {ch}] câu trả lời ngắn {sid} thiếu expected_answer")

        # Essay checks
        for e in essay:
            eid = e.get("id")
            if not e.get("title", "").strip() or not e.get("problem", "").strip():
                raise AssertionError(f"[{cid_course} - {ch}] bài tự luận {eid} thiếu title hoặc problem")
            steps = e.get("solution_steps", [])
            if not steps or len(steps) < 2:
                raise AssertionError(f"[{cid_course} - {ch}] bài tự luận {eid} solution_steps phải có ít nhất 2 bước")

        course_mcq += len(mcq)
        course_short += len(short)
        course_essay += len(essay)
        print(f"  -> Chương {ch}: {len(mcq)} trắc nghiệm, {len(short)} trả lời ngắn, {len(essay)} tự luận (PASS)")

    print(f"  TỔNG {cname}: {course_mcq} trắc nghiệm, {course_short} trả lời ngắn, {course_essay} tự luận.")
    return course_mcq, course_short, course_essay

def audit_all_courses():
    print("\n[2/4] Kiểm tra Ngân hàng Câu hỏi cho toàn bộ các môn học đang Active...")
    total_mcq = 0
    total_short = 0
    total_essay = 0

    for c in COURSES_TO_AUDIT:
        m, s, e = audit_course_questions(c)
        total_mcq += m
        total_short += s
        total_essay += e

    total_chapters = sum(len(c["chapters"]) for c in COURSES_TO_AUDIT)
    print(f"\n================================================================")
    print(f"  TỔNG TOÀN BỘ {total_chapters} CHƯƠNG ({len(COURSES_TO_AUDIT)} MÔN HỌC):")
    print(f"  - Trắc nghiệm: {total_mcq} câu")
    print(f"  - Trả lời ngắn: {total_short} câu")
    print(f"  - Tự luận: {total_essay} bài")
    print(f"================================================================")

def audit_static_server():
    print("\n[3/4] Kiểm tra Static HTTP Server tại docs/...")

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(DOCS), **kwargs)
        def log_message(self, format, *args):
            pass

    port = 8766
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
        "data/cnxhkh/chuong_1_exercises.json",
        "data/cnxhkh/chuong_1_theory.md",
        "data/cnpm/chuong_1_exercises.json",
        "data/cnpm/chuong_1_theory.md",
        "data/cnpm/chuong_5_exercises.json",
        "data/cnpm/chuong_5_theory.md",
        "data/cnpm/topics/tong_quan_cnpm_va_ky_nghe_he_thong_summary.md",
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
        audit_all_courses()
        audit_static_server()
        audit_gitignore()
        print("\n================================================================")
        print(">>> KẾT QUẢ KIỂM ĐỊNH: TOÀN BỘ CÁC MÔN HỌC ĐẠT CHUẨN PASS 100%! <<<")
        print("================================================================")
        return 0
    except Exception as e:
        print(f"\n[LỖI KIỂM ĐỊNH]: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
