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
├── cnxhkh/
│   ├── chuong_1_nhap_mon_cnxhkh.md
│   ├── chuong_2_su_menh_lich_su_giai_cap_cong_nhan.md
│   ├── chuong_3_chu_nghia_xa_hoi_va_thoi_ky_qua_do.md
│   ├── chuong_4_dan_chu_xhcn_va_nha_nuoc_xhcn.md
│   ├── chuong_5_co_cau_xa_hoi_giai_cap_va_lien_minh.md
│   ├── chuong_6_van_de_dan_toc_va_ton_giao.md
│   └── chuong_7_van_de_gia_dinh.md
├── cnpm/
│   ├── chuong_1_tong_quan_cnpm.md
│   ├── chuong_2_quy_trinh_phat_trien_phan_mem.md
│   ├── chuong_3_quan_ly_yeu_cau_va_lap_ke_hoach.md
│   ├── chuong_4_phat_trien_tich_hop_va_dam_bao_chat_luong.md
│   └── chuong_5_trien_khai_bao_tri_va_devops.md
└── cau_truc_du_lieu/
    ├── cay_nhi_phan.md
    └── do_thi.md
```

