# -*- coding: utf-8 -*-
"""
Build script for Course: Công Nghệ Phần Mềm (CNPM)
Sinh ra toàn bộ dữ liệu học tập:
- data/parsed_markdown/cnpm/
- data/notebook_exports/cnpm/
- docs/data/cnpm/ (theory.md, exercises.json, topics/)
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

DOCS_DIR = os.path.join(ROOT_DIR, "docs", "data", "cnpm")
TOPICS_DIR = os.path.join(DOCS_DIR, "topics")
PARSED_DIR = os.path.join(ROOT_DIR, "data", "parsed_markdown", "cnpm")
EXPORTS_DIR = os.path.join(ROOT_DIR, "data", "notebook_exports", "cnpm")
MANIFEST_PATH = os.path.join(ROOT_DIR, "docs", "data", "courses_manifest.json")

# Import chapter data
from scripts.cnpm_data import chuong_1, chuong_2, chuong_3, chuong_4, chuong_5

CHAPTERS_MODULES = [
    {
        "num": 1,
        "id": "chuong_1",
        "title": "Tổng quan về Công nghệ phần mềm & Kỹ nghệ hệ thống",
        "full_title": "Chương 1: Tổng quan về Công nghệ phần mềm & Kỹ nghệ hệ thống",
        "summary": "Bản chất phần mềm, khủng hoảng phần mềm, nguyên lý IEEE, mô hình chi phí và kỹ nghệ hệ thống.",
        "slug": "tong_quan_cnpm_va_ky_nghe_he_thong",
        "topic_title": "Chuyên đề: Tổng quan Công nghệ phần mềm & Kỹ nghệ hệ thống (Xuất từ NotebookLM)",
        "module": chuong_1,
        "md_filename": "chuong_1_tong_quan_cnpm.md"
    },
    {
        "num": 2,
        "id": "chuong_2",
        "title": "Các mô hình quy trình phát triển phần mềm & Agile/Scrum",
        "full_title": "Chương 2: Các mô hình quy trình phát triển phần mềm & Agile/Scrum",
        "summary": "Thác nước, V-Model, Tăng trưởng, Xoắn ốc, Tuyên ngôn Agile, khung Scrum và Kanban.",
        "slug": "mo_hinh_quy_trinh_phan_mem_va_agile",
        "topic_title": "Chuyên đề: Quy trình phát triển phần mềm & Phương pháp luận Agile/Scrum (Xuất từ NotebookLM)",
        "module": chuong_2,
        "md_filename": "chuong_2_quy_trinh_phat_trien_phan_mem.md"
    },
    {
        "num": 3,
        "id": "chuong_3",
        "title": "Kỹ nghệ yêu cầu & Lập kế hoạch dự án phần mềm",
        "full_title": "Chương 3: Kỹ nghệ yêu cầu & Lập kế hoạch dự án phần mềm",
        "summary": "Yêu cầu chức năng/phi chức năng, SRS theo IEEE 830, Use Case, User Story, WBS, PERT/CPM và COCOMO.",
        "slug": "ky_nghe_yeu_cau_va_ke_hoach_du_an",
        "topic_title": "Chuyên đề: Kỹ nghệ yêu cầu SRS & Hoạch định dự án phần mềm (Xuất từ NotebookLM)",
        "module": chuong_3,
        "md_filename": "chuong_3_quan_ly_yeu_cau_va_lap_ke_hoach.md"
    },
    {
        "num": 4,
        "id": "chuong_4",
        "title": "Phát triển, Tích hợp & Đảm bảo chất lượng phần mềm",
        "full_title": "Chương 4: Phát triển, Tích hợp & Đảm bảo chất lượng phần mềm",
        "summary": "Kiến trúc hệ thống, nguyên lý SOLID, Git branching, kiểm thử Hộp đen/Hộp trắng, Unit/Integration/System test, CI và QA vs QC.",
        "slug": "kien_truc_solid_va_kiem_thu_phan_mem",
        "topic_title": "Chuyên đề: Kiến trúc phần mềm, Nguyên lý SOLID & Chiến lược kiểm thử (Xuất từ NotebookLM)",
        "module": chuong_4,
        "md_filename": "chuong_4_phat_trien_tich_hop_va_dam_bao_chat_luong.md"
    },
    {
        "num": 5,
        "id": "chuong_5",
        "title": "Triển khai, Bảo trì phần mềm & Văn hóa DevOps",
        "full_title": "Chương 5: Triển khai, Bảo trì phần mềm & Văn hóa DevOps",
        "summary": "Môi trường Dev/Staging/Prod, chiến lược Blue-Green/Canary/Rolling, 4 loại bảo trì, quy luật Lehman, văn hóa CAMS và DORA metrics.",
        "slug": "trien_khai_bao_tri_va_van_hoa_devops",
        "topic_title": "Chuyên đề: Triển khai, 4 loại hình bảo trì & Văn hóa DevOps (Xuất từ NotebookLM)",
        "module": chuong_5,
        "md_filename": "chuong_5_trien_khai_bao_tri_va_devops.md"
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
    print("=== BẮT ĐẦU XÂY DỰNG KHÓA HỌC: CÔNG NGHỆ PHẦN MỀM (CNPM) ===")
    
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
        
        # 3. Sao chép summary sang docs/data/cnpm/topics/
        topic_doc_path = os.path.join(TOPICS_DIR, f"{ch['slug']}_summary.md")
        shutil.copyfile(export_path, topic_doc_path)
        print(f"  [OK] Topic docs: {topic_doc_path}")
        
        # 4. Ghi docs/data/cnpm/chuong_{num}_theory.md
        theory_doc_path = os.path.join(DOCS_DIR, f"chuong_{num}_theory.md")
        with open(theory_doc_path, "w", encoding="utf-8") as f:
            f.write(mod.THEORY_MD)
        print(f"  [OK] Theory docs: {theory_doc_path}")
        
        # 5. Chuẩn hóa & Ghi docs/data/cnpm/chuong_{num}_exercises.json
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
            "theory": f"data/cnpm/chuong_{num}_theory.md",
            "exercises": f"data/cnpm/chuong_{num}_exercises.json",
            "counts": {
                "multiple_choice": len(mod.MULTIPLE_CHOICE),
                "short_answers": len(mod.SHORT_ANSWERS),
                "essays": len(mod.ESSAYS)
            }
        })
        
        # Cấu hình topic cho manifest
        manifest_topics.append({
            "id": ch["slug"],
            "title": ch["topic_title"],
            "file": f"data/cnpm/topics/{ch['slug']}_summary.md"
        })

    # Cập nhật manifest courses_manifest.json
    print("\n--- CẬP NHẬT COURSES MANIFEST ---")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)
    
    cnpm_course_obj = {
        "id": "cnpm",
        "code": "CNPM",
        "title": "Công Nghệ Phần Mềm",
        "description": "Vòng đời phần mềm, quy trình Agile/Scrum, kỹ nghệ yêu cầu SRS, kiến trúc SOLID, chiến lược kiểm thử, CI/CD và văn hóa DevOps.",
        "status": "active",
        "books": [
            {
                "id": "giao_trinh_cnpm",
                "title": "Giáo Trình Công Nghệ Phần Mềm (Chương 1 - 5)",
                "chapters": manifest_chapters
            }
        ],
        "topics": manifest_topics,
        "ui_profile": "software_engineering"
    }
    
    # Kiểm tra xem cnpm đã tồn tại chưa
    courses_list = manifest_data.get("courses", [])
    existing_idx = None
    for idx, c in enumerate(courses_list):
        if c.get("id") == "cnpm":
            existing_idx = idx
            break
            
    if existing_idx is not None:
        courses_list[existing_idx] = cnpm_course_obj
        print("  [UPDATE] Đã cập nhật môn cnpm hiện có trong courses_manifest.json")
    else:
        # Chèn trước môn coming_soon (như giai_tich_1)
        insert_idx = len(courses_list)
        for idx, c in enumerate(courses_list):
            if c.get("status") == "coming_soon":
                insert_idx = idx
                break
        courses_list.insert(insert_idx, cnpm_course_obj)
        print(f"  [INSERT] Đã chèn môn cnpm vào vị trí {insert_idx} trong courses_manifest.json")
        
    manifest_data["courses"] = courses_list
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=1)
    print(f"  [OK] Đã ghi thành công vào {MANIFEST_PATH}")
    
    print("\n=== HOÀN TẤT BUILD KHÓA HỌC CNPM ===")

if __name__ == "__main__":
    main()
