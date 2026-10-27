# -*- coding: utf-8 -*-
"""
Build script for Course: Tâm Lý Học 2 (TLH2)
Tâm lý học lứa tuổi và Tâm lý học sư phạm.
Sinh ra toàn bộ dữ liệu học tập:
- data/parsed_markdown/tam_ly_hoc_2/
- data/notebook_exports/tam_ly_hoc_2/
- docs/data/tam_ly_hoc_2/ (theory.md, exercises.json, topics/)
- Cập nhật docs/data/courses_manifest.json
"""

import os
import sys
import json
import shutil

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

DOCS_DIR = os.path.join(ROOT_DIR, "docs", "data", "tam_ly_hoc_2")
TOPICS_DIR = os.path.join(DOCS_DIR, "topics")
PARSED_DIR = os.path.join(ROOT_DIR, "data", "parsed_markdown", "tam_ly_hoc_2")
EXPORTS_DIR = os.path.join(ROOT_DIR, "data", "notebook_exports", "tam_ly_hoc_2")
MANIFEST_PATH = os.path.join(ROOT_DIR, "docs", "data", "courses_manifest.json")

# Import chapter data
from scripts.tlh2_data import chuong_1, chuong_2, chuong_3, chuong_4, chuong_5

CHAPTERS_MODULES = [
    {
        "num": 1,
        "id": "chuong_1",
        "title": "Những vấn đề chung của Tâm lý học lứa tuổi và Tâm lý học sư phạm",
        "full_title": "Chương 1: Những vấn đề chung của Tâm lý học lứa tuổi và Tâm lý học sư phạm",
        "summary": "Đối tượng, nhiệm vụ, phương pháp nghiên cứu; quan niệm về trẻ em, phê phán các thuyết sai lầm; quan điểm CNDVBC; điều kiện, động lực và các quy luật phát triển tâm lý trẻ em.",
        "slug": "nhung_van_de_chung_tlh2",
        "topic_title": "Chuyên đề: Bản chất biện chứng của phát triển tâm lý & Vai trò của giáo dục (Xuất từ NotebookLM)",
        "module": chuong_1,
        "md_filename": "chuong_1_nhung_van_de_chung.md"
    },
    {
        "num": 2,
        "id": "chuong_2",
        "title": "Tâm lý học trẻ em trước tuổi học",
        "full_title": "Chương 2: Tâm lý học trẻ em trước tuổi học",
        "summary": "Đặc điểm tâm lý trẻ sơ sinh và hài nhi; trẻ ấu nhi (hoạt động với đồ vật, khủng hoảng tuổi lên 3); trẻ mẫu giáo (trò chơi đóng vai theo chủ đề); bước ngoặt 6 tuổi và chuẩn bị tâm lý vào lớp 1.",
        "slug": "tam_ly_hoc_truoc_tuoi_hoc",
        "topic_title": "Chuyên đề: Tâm lý học trẻ em trước tuổi học - Khủng hoảng tuổi lên 3 & Bước ngoặt 6 tuổi (Xuất từ NotebookLM)",
        "module": chuong_2,
        "md_filename": "chuong_2_truoc_tuoi_hoc.md"
    },
    {
        "num": 3,
        "id": "chuong_3",
        "title": "Tâm lý học lứa tuổi đi học",
        "full_title": "Chương 3: Tâm lý học lứa tuổi đi học",
        "summary": "Tâm lý học sinh tiểu học (hoạt động học tập là chủ đạo); học sinh THCS - lứa tuổi thiếu niên (khủng hoảng dậy thì, cảm nhận làm người lớn, giao tiếp bạn bè); học sinh THPT - đầu thanh niên (thế giới quan, tình yêu học trò, hướng nghiệp).",
        "slug": "tam_ly_hoc_tuoi_di_hoc",
        "topic_title": "Chuyên đề: Tâm lý học lứa tuổi đi học - Nhi đồng, Thiếu niên và Đầu thanh niên (Xuất từ NotebookLM)",
        "module": chuong_3,
        "md_filename": "chuong_3_tuoi_di_hoc.md"
    },
    {
        "num": 4,
        "id": "chuong_4",
        "title": "Tâm lý học dạy học",
        "full_title": "Chương 4: Tâm lý học dạy học",
        "summary": "Khái niệm, đặc điểm và yếu tố tâm lý của hoạt động dạy; đặc điểm và cấu trúc của hoạt động học (động cơ bên trong vs bên ngoài, mục đích, 4 hành động học tập); dạy học và phát triển trí tuệ (chỉ số trí tuệ, lý thuyết Vygotsky về ZPD và hai hướng phát triển trí tuệ).",
        "slug": "tam_ly_hoc_day_hoc",
        "topic_title": "Chuyên đề: Bản chất hoạt động dạy học & Cơ chế phát triển trí tuệ theo Davydov (Xuất từ NotebookLM)",
        "module": chuong_4,
        "md_filename": "chuong_4_tam_ly_hoc_day_hoc.md"
    },
    {
        "num": 5,
        "id": "chuong_5",
        "title": "Tâm lý học nhân cách người giáo viên",
        "full_title": "Chương 5: Tâm lý học nhân cách người giáo viên",
        "summary": "Sự cần thiết trau dồi nhân cách người giáo viên; cấu trúc nhân cách (thế giới quan, lý tưởng nghề nghiệp, lòng yêu trẻ, yêu nghề; nhóm năng lực dạy học & nhóm năng lực giáo dục); uy tín người giáo viên (uy tín chân chính vs uy tín giả, con đường xây dựng uy tín).",
        "slug": "tam_ly_hoc_nhan_cach_nguoi_giao_vien",
        "topic_title": "Chuyên đề: Cấu trúc nhân cách & Nghệ thuật xây dựng uy tín chân chính của người giáo viên (Xuất từ NotebookLM)",
        "module": chuong_5,
        "md_filename": "chuong_5_nhan_cach_nguoi_giao_vien.md"
    }
]

def normalize_mcq(raw_list):
    import re
    normalized = []
    for idx, q in enumerate(raw_list):
        opts = q.get("options")
        clean_opts = {}
        if isinstance(opts, list):
            for item in opts:
                item_str = str(item).strip()
                match = re.match(r"^([A-D])[\.\:\)]\s*(.*)$", item_str, re.DOTALL)
                if match:
                    clean_opts[match.group(1)] = match.group(2).strip()
                else:
                    letter = chr(ord('A') + len(clean_opts))
                    clean_opts[letter] = item_str
        elif isinstance(opts, dict):
            clean_opts = opts
            
        ans = q.get("correct_answer") or q.get("answer") or "A"
        
        diff = q.get("difficulty")
        if not diff:
            if idx < 10:
                diff = "easy"
            elif idx < 22:
                diff = "medium"
            else:
                diff = "hard"
                
        normalized.append({
            "id": q.get("id", idx + 1),
            "difficulty": diff,
            "question": q.get("question", "").strip(),
            "options": clean_opts,
            "correct_answer": ans,
            "explanation": q.get("explanation", "").strip()
        })
    return normalized

def main():
    print("=== BẮT ĐẦU XÂY DỰNG KHÓA HỌC: TÂM LÝ HỌC 2 (TLH2) ===")
    
    os.makedirs(PARSED_DIR, exist_ok=True)
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    os.makedirs(DOCS_DIR, exist_ok=True)
    os.makedirs(TOPICS_DIR, exist_ok=True)
    
    manifest_chapters = []
    manifest_topics = []
    
    for ch in CHAPTERS_MODULES:
        num = ch["num"]
        mod = ch["module"]
        print(f"\n--- Xử lý Chương {num}: {ch['title']} ---")
        
        # 1. Ghi parsed markdown
        parsed_path = os.path.join(PARSED_DIR, ch["md_filename"])
        with open(parsed_path, "w", encoding="utf-8") as f:
            f.write(mod.PARSED_MARKDOWN)
        print(f"  [OK] Parsed markdown: {parsed_path}")
        
        # 2. Ghi notebook export summary
        export_path = os.path.join(EXPORTS_DIR, f"{ch['slug']}_summary.md")
        with open(export_path, "w", encoding="utf-8") as f:
            f.write(mod.TOPIC_SUMMARY)
        print(f"  [OK] Export summary: {export_path}")
        
        # 3. Sao chép summary sang docs/data/tam_ly_hoc_2/topics/
        topic_doc_path = os.path.join(TOPICS_DIR, f"{ch['slug']}_summary.md")
        shutil.copyfile(export_path, topic_doc_path)
        print(f"  [OK] Topic docs: {topic_doc_path}")
        
        # 4. Ghi docs/data/tam_ly_hoc_2/chuong_{num}_theory.md
        theory_doc_path = os.path.join(DOCS_DIR, f"chuong_{num}_theory.md")
        with open(theory_doc_path, "w", encoding="utf-8") as f:
            f.write(mod.THEORY_MD)
        print(f"  [OK] Theory docs: {theory_doc_path}")
        
        # 5. Chuẩn hóa & Ghi docs/data/tam_ly_hoc_2/chuong_{num}_exercises.json
        norm_mcq = normalize_mcq(mod.MULTIPLE_CHOICE)
        exercises_doc_path = os.path.join(DOCS_DIR, f"chuong_{num}_exercises.json")
        exercises_payload = {
            "chapter_id": ch["id"],
            "chapter_title": ch["full_title"],
            "multiple_choice": norm_mcq,
            "short_answers": mod.SHORT_ANSWERS,
            "essays": mod.ESSAYS
        }
        with open(exercises_doc_path, "w", encoding="utf-8") as f:
            json.dump(exercises_payload, f, ensure_ascii=False, indent=2)
        print(f"  [OK] Exercises JSON: {exercises_doc_path} (MCQ: {len(norm_mcq)}, Short: {len(mod.SHORT_ANSWERS)}, Essay: {len(mod.ESSAYS)})")
        
        # Cấu hình chapter cho manifest
        manifest_chapters.append({
            "id": ch["id"],
            "number": num,
            "title": ch["title"],
            "full_title": ch["full_title"],
            "summary": ch["summary"],
            "theory": f"data/tam_ly_hoc_2/chuong_{num}_theory.md",
            "exercises": f"data/tam_ly_hoc_2/chuong_{num}_exercises.json",
            "counts": {
                "multiple_choice": len(norm_mcq),
                "short_answers": len(mod.SHORT_ANSWERS),
                "essays": len(mod.ESSAYS)
            }
        })
        
        # Cấu hình topic cho manifest
        manifest_topics.append({
            "id": ch["slug"],
            "title": ch["topic_title"],
            "file": f"data/tam_ly_hoc_2/topics/{ch['slug']}_summary.md"
        })

    # Cập nhật manifest courses_manifest.json
    print("\n--- CẬP NHẬT COURSES MANIFEST ---")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)
    
    tlh2_course_obj = {
        "id": "tam_ly_hoc_2",
        "code": "TLH2",
        "title": "Tâm Lý Học 2",
        "description": "Tâm lý học lứa tuổi và tâm lý học sư phạm: Quy luật phát triển tâm lý từ sơ sinh đến THPT, bản chất hoạt động dạy học, trí tuệ và nhân cách người giáo viên.",
        "status": "active",
        "books": [
            {
                "id": "giao_trinh_tam_ly_hoc_2",
                "title": "Giáo Trình Tâm Lý Học Lứa Tuổi & Tâm Lý Học Sư Phạm",
                "chapters": manifest_chapters
            }
        ],
        "topics": manifest_topics,
        "ui_profile": "pedagogical_psychology"
    }
    
    courses_list = manifest_data.get("courses", [])
    existing_idx = None
    for idx, c in enumerate(courses_list):
        if c.get("id") == "tam_ly_hoc_2":
            existing_idx = idx
            break
            
    if existing_idx is not None:
        courses_list[existing_idx] = tlh2_course_obj
        print("  [UPDATE] Đã cập nhật môn tam_ly_hoc_2 hiện có trong courses_manifest.json")
    else:
        # Chèn trước môn coming_soon nếu có
        insert_idx = len(courses_list)
        for idx, c in enumerate(courses_list):
            if c.get("status") == "coming_soon":
                insert_idx = idx
                break
        courses_list.insert(insert_idx, tlh2_course_obj)
        print(f"  [INSERT] Đã chèn môn tam_ly_hoc_2 vào vị trí {insert_idx} trong courses_manifest.json")
        
    manifest_data["courses"] = courses_list
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=1)
    print(f"  [OK] Đã ghi thành công vào {MANIFEST_PATH}")
    
    print("\n=== HOÀN TẤT BUILD KHÓA HỌC TÂM LÝ HỌC 2 ===")

if __name__ == "__main__":
    main()
