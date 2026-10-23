# Thư mục Giáo trình đã chuyển đổi sang Markdown (Parsed Markdown Textbooks)

## Cấu trúc lưu trữ:
Thư mục này chứa toàn bộ giáo trình PDF đã được `pdf_ingestor` xử lý thành Markdown chuẩn:
- Giữ nguyên cấu trúc cây đề mục (`#`, `##`, `###`).
- Giữ nguyên công thức toán LaTeX (`$...$`, `$$...$$`).
- Đánh dấu trang dạng `<!-- PAGE <number> -->` để hỗ trợ trích dẫn chính xác số trang khi giải bài tập.

```text
data/parsed_markdown/
├── giai_tich_1/
│   ├── chuong_1_ham_so_va_gioi_han.md
│   └── chuong_2_dao_ham_va_vi_phan.md
├── he_qtcsdl/
│   ├── quyen_1_nhap_mon_chuong_1.md
│   ├── quyen_1_nhap_mon_chuong_2.md
│   ├── quyen_1_nhap_mon_chuong_3.md
│   ├── quyen_1_nhap_mon_chuong_4.md
│   ├── quyen_1_nhap_mon_chuong_5.md
│   ├── quyen_1_nhap_mon_chuong_6.md
│   ├── quyen_2_thiet_ke_chuong_1.md
│   ├── quyen_2_thiet_ke_chuong_2.md
│   ├── quyen_2_thiet_ke_chuong_3.md
│   ├── quyen_2_thiet_ke_chuong_4.md
│   └── quyen_2_thiet_ke_chuong_5.md
└── cau_truc_du_lieu/
    ├── cay_nhi_phan.md
    └── do_thi.md
```

