# Thư mục chứa Giáo trình PDF gốc (Raw Academic PDFs)

## Hướng dẫn tổ chức:
Hãy đặt các file PDF giáo trình của từng môn học vào các thư mục con tương ứng theo mã môn hoặc tên môn:
```text
data/raw_pdfs/
├── giai_tich_1/
│   ├── giao_trinh_giai_tich_1.pdf
│   └── bai_tap_giai_tich_1.pdf
├── cau_truc_du_lieu/
│   └── data_structures_and_algorithms.pdf
└── triet_hoc_mac_lenin/
    └── giao_trinh_triet_hoc.pdf
```

Sau khi copy file PDF vào đây, bạn có thể chạy Agent Skill `pdf_ingestor` để tự động bóc tách sang Markdown được lưu tại `data/parsed_markdown/`.
