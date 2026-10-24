# Thư mục chứa Bản ghi chú xuất từ NotebookLM (NotebookLM Exports)

## Hướng dẫn sử dụng:
1. Trong Google NotebookLM, mở notebook của môn học.
2. Sao chép hoặc xuất (Export) các bản tóm tắt, mindmap, study guide, FAQ dưới định dạng Markdown (`.md`).
3. Lưu các file `.md` vào thư mục này theo môn học:

```text
data/notebook_exports/
├── giai_tich_1/
│   ├── chuong_1_gioi_han_va_lien_tuc_summary.md
│   └── study_guide_giua_ky.md
├── he_qtcsdl/
│   ├── tong_quan_csdl_va_kien_truc_summary.md
│   ├── mo_hinh_er_va_chuyen_doi_summary.md
│   ├── dai_so_quan_he_va_rang_buoc_summary.md
│   ├── ngon_ngu_sql_va_truy_van_nang_cao_summary.md
│   ├── to_chuc_vat_ly_va_toi_uu_cau_hoi_summary.md
│   ├── rang_buoc_toan_ven_va_trigger_summary.md
│   ├── phu_thuoc_ham_va_thuat_toan_tim_khoa_summary.md
│   ├── ly_thuyet_phan_tach_va_bao_toan_summary.md
│   ├── chuan_hoa_csdl_1nf_2nf_3nf_bcnf_summary.md
│   └── phu_thuoc_da_tri_va_4nf_summary.md
├── cnxhkh/
│   ├── su_ra_doi_va_phat_trien_cnxhkh_summary.md
│   ├── su_menh_lich_su_giai_cap_cong_nhan_summary.md
│   ├── chu_nghia_xa_hoi_va_thoi_ky_qua_do_summary.md
│   ├── dan_chu_va_nha_nuoc_phap_quyen_xhcn_summary.md
│   ├── co_cau_giai_cap_va_lien_minh_cong_nong_tri_summary.md
│   ├── van_de_dan_toc_va_ton_giao_summary.md
│   └── xay_dung_gia_dinh_thoi_ky_qua_do_summary.md
└── cau_truc_du_lieu/
    ├── danh_sach_lien_ket_key_points.md
    └── do_phuc_tap_thuat_toan_notes.md
```

Hệ thống RAG của `knowledge_retriever` sẽ dùng các file này làm **Lớp chỉ mục ngữ nghĩa mức cao (High-level Index)** trước khi đối chiếu chi tiết vào giáo trình gốc.
