# Thư mục chứa Giáo trình PDF gốc (Raw Academic PDFs)

## Hướng dẫn tổ chức:
Hãy đặt các file PDF giáo trình của từng môn học vào các thư mục con tương ứng theo mã môn hoặc tên môn:
```text
data/raw_pdfs/
├── cnpm/
│   ├── chuong_1_tong_quan_cnpm.pdf
│   ├── chuong_1_hdth_phan_1.pdf
│   ├── chuong_1_hdth_phan_2.pdf
│   ├── chuong_2_quy_trinh_phat_trien_phan_mem.pdf
│   ├── chuong_2_hdth.pdf
│   ├── chuong_3_quan_ly_yeu_cau_va_lap_ke_hoach.pdf
│   ├── chuong_3_hdth.pdf
│   ├── chuong_4_phat_trien_tich_hop_va_dam_bao_chat_luong.pdf
│   ├── chuong_4_bai_giang_chi_tiet.pdf
│   ├── chuong_4_hdth.pdf
│   ├── chuong_5_trien_khai_bao_tri_va_devops.pdf
│   └── chuong_5_bai_giang_chi_tiet.pdf
├── he_qtcsdl/
│   ├── giao_trinh_he_co_so_du_lieu_tap_1.pdf
│   └── giao_trinh_he_co_so_du_lieu_tap_2.pdf
└── chu_nghia_xa_hoi_khoa_hoc.pdf
```

Sau khi copy file PDF vào đây, bạn có thể chạy Agent Skill `pdf_ingestor` hoặc pipeline để tự động bóc tách sang Markdown được lưu tại `data/parsed_markdown/`.
