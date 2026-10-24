import json
import os

manifest_path = os.path.join("docs", "data", "courses_manifest.json")
with open(manifest_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Find if cnxhkh already exists, remove or update
data["courses"] = [c for c in data["courses"] if c["id"] != "cnxhkh"]

cnxhkh_course = {
    "id": "cnxhkh",
    "code": "CNXHKH",
    "title": "Chủ Nghĩa Xã Hội Khoa Học",
    "description": "Giáo trình chuẩn Bộ GD&ĐT: Sứ mệnh lịch sử giai cấp công nhân, CNXH và thời kỳ quá độ, dân chủ & nhà nước XHCN, cơ cấu giai cấp, dân tộc, tôn giáo và gia đình.",
    "status": "active",
    "books": [
        {
            "id": "giao_trinh_chuan",
            "title": "Giáo trình Chủ nghĩa xã hội khoa học (Bộ GD&ĐT - NXB Chính trị quốc gia Sự thật)",
            "chapters": [
                {
                    "id": "chuong_1",
                    "number": 1,
                    "title": "Nhập môn Chủ nghĩa xã hội khoa học",
                    "full_title": "Chương 1: Nhập môn Chủ nghĩa xã hội khoa học",
                    "summary": "Điều kiện kinh tế - xã hội, ba tiền đề KHTN và lý luận, ba phát kiến vĩ đại của Mác - Ăngghen, cống hiến của Lênin.",
                    "theory": "data/cnxhkh/chuong_1_theory.md",
                    "exercises": "data/cnxhkh/chuong_1_exercises.json",
                    "counts": {
                        "multiple_choice": 30,
                        "short_answers": 8,
                        "essays": 4
                    }
                },
                {
                    "id": "chuong_2",
                    "number": 2,
                    "title": "Sứ mệnh lịch sử của giai cấp công nhân",
                    "full_title": "Chương 2: Sứ mệnh lịch sử của giai cấp công nhân",
                    "summary": "Khái niệm, hai phương diện xác định GCCN, nội dung kinh tế - chính trị - tư tưởng, điều kiện khách quan, nhân tố chủ quan và GCCN Việt Nam.",
                    "theory": "data/cnxhkh/chuong_2_theory.md",
                    "exercises": "data/cnxhkh/chuong_2_exercises.json",
                    "counts": {
                        "multiple_choice": 30,
                        "short_answers": 8,
                        "essays": 4
                    }
                },
                {
                    "id": "chuong_3",
                    "number": 3,
                    "title": "Chủ nghĩa xã hội và thời kỳ quá độ lên chủ nghĩa xã hội",
                    "full_title": "Chương 3: Chủ nghĩa xã hội và thời kỳ quá độ lên chủ nghĩa xã hội",
                    "summary": "Hai giai đoạn hình thái CSCN, đặc trưng CNXH, tính tất yếu thời kỳ quá độ, con đường quá độ bỏ qua chế độ TBCN và 8 đặc trưng ở Việt Nam.",
                    "theory": "data/cnxhkh/chuong_3_theory.md",
                    "exercises": "data/cnxhkh/chuong_3_exercises.json",
                    "counts": {
                        "multiple_choice": 30,
                        "short_answers": 8,
                        "essays": 4
                    }
                },
                {
                    "id": "chuong_4",
                    "number": 4,
                    "title": "Dân chủ xã hội chủ nghĩa và Nhà nước xã hội chủ nghĩa",
                    "full_title": "Chương 4: Dân chủ xã hội chủ nghĩa và Nhà nước xã hội chủ nghĩa",
                    "summary": "Lịch sử các nền dân chủ, bản chất dân chủ XHCN, chức năng nhà nước XHCN, mối quan hệ biện chứng và Nhà nước pháp quyền XHCN Việt Nam.",
                    "theory": "data/cnxhkh/chuong_4_theory.md",
                    "exercises": "data/cnxhkh/chuong_4_exercises.json",
                    "counts": {
                        "multiple_choice": 30,
                        "short_answers": 8,
                        "essays": 4
                    }
                },
                {
                    "id": "chuong_5",
                    "number": 5,
                    "title": "Cơ cấu xã hội - giai cấp và liên minh giai cấp, tầng lớp trong thời kỳ quá độ",
                    "full_title": "Chương 5: Cơ cấu xã hội - giai cấp và liên minh giai cấp, tầng lớp trong thời kỳ quá độ lên CNXH",
                    "summary": "Vị trí trung tâm cơ cấu giai cấp, tính tất yếu liên minh, 3 nội dung liên minh (kinh tế, chính trị, văn hóa) và đặc điểm liên minh ở Việt Nam.",
                    "theory": "data/cnxhkh/chuong_5_theory.md",
                    "exercises": "data/cnxhkh/chuong_5_exercises.json",
                    "counts": {
                        "multiple_choice": 30,
                        "short_answers": 8,
                        "essays": 4
                    }
                },
                {
                    "id": "chuong_6",
                    "number": 6,
                    "title": "Vấn đề dân tộc và tôn giáo trong thời kỳ quá độ lên chủ nghĩa xã hội",
                    "full_title": "Chương 6: Vấn đề dân tộc và tôn giáo trong thời kỳ quá độ lên chủ nghĩa xã hội",
                    "summary": "Hai xu hướng phát triển dân tộc, Cương lĩnh dân tộc Lênin, bản chất & nguồn gốc tôn giáo, chính sách dân tộc và tôn giáo ở Việt Nam.",
                    "theory": "data/cnxhkh/chuong_6_theory.md",
                    "exercises": "data/cnxhkh/chuong_6_exercises.json",
                    "counts": {
                        "multiple_choice": 30,
                        "short_answers": 8,
                        "essays": 4
                    }
                },
                {
                    "id": "chuong_7",
                    "number": 7,
                    "title": "Vấn đề gia đình trong thời kỳ quá độ lên chủ nghĩa xã hội",
                    "full_title": "Chương 7: Vấn đề gia đình trong thời kỳ quá độ lên chủ nghĩa xã hội",
                    "summary": "Khái niệm, vị trí, 4 chức năng cơ bản của gia đình, cơ sở xây dựng gia đình XHCN, chế độ hôn nhân tiến bộ và biến đổi gia đình Việt Nam.",
                    "theory": "data/cnxhkh/chuong_7_theory.md",
                    "exercises": "data/cnxhkh/chuong_7_exercises.json",
                    "counts": {
                        "multiple_choice": 30,
                        "short_answers": 8,
                        "essays": 4
                    }
                }
            ]
        }
    ],
    "topics": [
        {
            "id": "su_ra_doi_va_phat_trien_cnxhkh",
            "title": "Chuyên đề: Sự ra đời và các giai đoạn phát triển của CNXHKH (Xuất từ NotebookLM)",
            "file": "data/cnxhkh/topics/su_ra_doi_va_phat_trien_cnxhkh_summary.md"
        },
        {
            "id": "su_menh_lich_su_giai_cap_cong_nhan",
            "title": "Chuyên đề: Sứ mệnh lịch sử của giai cấp công nhân & GCCN Việt Nam (Xuất từ NotebookLM)",
            "file": "data/cnxhkh/topics/su_menh_lich_su_giai_cap_cong_nhan_summary.md"
        },
        {
            "id": "chu_nghia_xa_hoi_va_thoi_ky_qua_do",
            "title": "Chuyên đề: Chủ nghĩa xã hội và thời kỳ quá độ lên CNXH ở Việt Nam (Xuất từ NotebookLM)",
            "file": "data/cnxhkh/topics/chu_nghia_xa_hoi_va_thoi_ky_qua_do_summary.md"
        },
        {
            "id": "dan_chu_va_nha_nuoc_phap_quyen_xhcn",
            "title": "Chuyên đề: Dân chủ XHCN và Nhà nước pháp quyền XHCN Việt Nam (Xuất từ NotebookLM)",
            "file": "data/cnxhkh/topics/dan_chu_va_nha_nuoc_phap_quyen_xhcn_summary.md"
        },
        {
            "id": "co_cau_giai_cap_va_lien_minh_cong_nong_tri",
            "title": "Chuyên đề: Cơ cấu xã hội - giai cấp & liên minh Công - Nông - Trí (Xuất từ NotebookLM)",
            "file": "data/cnxhkh/topics/co_cau_giai_cap_va_lien_minh_cong_nong_tri_summary.md"
        },
        {
            "id": "van_de_dan_toc_va_ton_giao",
            "title": "Chuyên đề: Vấn đề dân tộc, tôn giáo & khối đại đoàn kết dân tộc (Xuất từ NotebookLM)",
            "file": "data/cnxhkh/topics/van_de_dan_toc_va_ton_giao_summary.md"
        },
        {
            "id": "xay_dung_gia_dinh_thoi_ky_qua_do",
            "title": "Chuyên đề: Xây dựng gia đình tiến bộ, ấm no, hạnh phúc thời kỳ quá độ (Xuất từ NotebookLM)",
            "file": "data/cnxhkh/topics/xay_dung_gia_dinh_thoi_ky_qua_do_summary.md"
        }
    ]
}

# Insert cnxhkh right after active course he_qtcsdl
data["courses"].insert(1, cnxhkh_course)

with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("Updated docs/data/courses_manifest.json with CNXHKH course successfully!")
