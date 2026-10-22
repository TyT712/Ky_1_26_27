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
└── cau_truc_du_lieu/
    ├── danh_sach_lien_ket_key_points.md
    └── do_phuc_tap_thuat_toan_notes.md
```

Hệ thống RAG của `knowledge_retriever` sẽ dùng các file này làm **Lớp chỉ mục ngữ nghĩa mức cao (High-level Index)** trước khi đối chiếu chi tiết vào giáo trình gốc.
