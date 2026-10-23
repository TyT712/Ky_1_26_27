# SKILL: LMS CHAPTER PACK GENERATOR
## Biến đổi chương giáo trình Markdown thành gói học liệu tách biệt (`_theory.md` + `_exercises.json`) cho Static SPA LMS

> Phiên bản 2.0 - kế thừa và nâng cấp `chapter_study_pack_generator` (gói Markdown đơn khối, 10 trắc nghiệm).
> Skill này dùng chung cho **mọi môn học**; môn mới chỉ cần thêm thư mục dữ liệu và khai báo trong `courses_manifest.json`.

---

## 1. Đầu vào / Đầu ra

| Hạng mục | Đường dẫn |
| :--- | :--- |
| Giáo trình đã bóc tách | `data/parsed_markdown/{subject_code}/{chapter_file}.md` |
| Tóm tắt NotebookLM (tùy chọn) | `data/notebook_exports/{subject_code}/*_summary.md` |
| Lý thuyết của chương (đầu ra 1) | `docs/data/{subject_code}/{chapter_id}_theory.md` |
| Ngân hàng bài tập (đầu ra 2) | `docs/data/{subject_code}/{chapter_id}_exercises.json` |
| Danh mục môn học | `docs/data/courses_manifest.json` |

## 2. Quy tắc Tách File
Mỗi chương **bắt buộc** xuất ra đúng hai tệp:
1. `{chapter_id}_theory.md`: tóm tắt cốt lõi gồm sơ đồ Mermaid, định nghĩa, công thức LaTeX (`$...$`, `$$...$$`), bảng quy tắc, cú pháp SQL.
2. `{chapter_id}_exercises.json`: ngân hàng câu hỏi theo schema ở Mục 3. Tuyệt đối không nhúng đáp án vào Markdown lý thuyết.

## 3. JSON Schema của `_exercises.json`
```json
{
  "chapter_id": "q1_chuong_1",
  "chapter_title": "Quyển 1 - Chương 1: ...",
  "multiple_choice": [
    { "id": 1, "difficulty": "easy|medium|hard", "question": "... ($LaTeX$, `code`)",
      "options": {"A": "", "B": "", "C": "", "D": ""},
      "correct_answer": "B", "explanation": "Vì sao B đúng, vì sao A/C/D sai" }
  ],
  "short_answers": [ { "id": 1, "question": "", "expected_answer": "", "explanation": "" } ],
  "essays": [ { "id": 1, "title": "", "problem": "", "solution_steps": ["Bước 1: ...", "Bước 2: ..."] } ]
}
```

## 4. Ma trận 30 câu trắc nghiệm / chương
| Nhóm | Số câu | Nội dung |
| :--- | :---: | :--- |
| **Easy** (nhận biết, thông hiểu) | 10 | Khái niệm, định nghĩa, kiến trúc, ký hiệu |
| **Medium** (vận dụng) | 12 | Đọc/viết SQL, biểu thức đại số quan hệ, bao đóng $X^+$, tìm khóa, xác định 1NF/2NF/3NF/BCNF |
| **Hard** (vận dụng cao, phân tích) | 8 | Bẫy tư duy, tối ưu cây truy vấn, bảo toàn thông tin ($\bowtie$) và phụ thuộc hàm, MVD $X \twoheadrightarrow Y$, 4NF |

Tổng tối thiểu mỗi chương: **30 trắc nghiệm + 8 trả lời ngắn + 4 tự luận**.
Toàn môn Hệ QTCSDL (11 chương): $\ge 330$ trắc nghiệm, $\ge 88$ trả lời ngắn, $\ge 44$ tự luận.

## 5. Quy tắc chất lượng
1. **Bám giáo trình:** ký hiệu, định nghĩa, thuật toán đúng theo `data/parsed_markdown`; không tự suy diễn.
2. **Anti-Laziness:** cấm câu hỏi placeholder, trùng lặp (`question` không được lặp trong một chương) hoặc cắt dưới 30 câu.
3. **Hợp lệ dữ liệu:** mỗi câu trắc nghiệm có đủ 4 phương án `A-D`, `correct_answer` hợp lệ, `explanation` không rỗng.
4. **Giải thích đầy đủ:** nêu vì sao đáp án đúng và chỉ ra sai sót của các phương án còn lại; các tham chiếu "ý X" được tự động đổi khi xáo trộn phương án.
5. **Chấm điểm theo lô (Batch Submission):** giao diện KHÔNG hiển thị đúng/sai khi chọn đáp án; chỉ hiển thị sau khi nộp bài.
6. **Tính toán số học phải được kiểm chứng** (hệ số kết khối, chi phí I/O, bao đóng, khóa) trước khi ghi vào đáp án.

## 6. Quy trình tái sử dụng cho môn mới
1. `python scripts/extract_legacy_packs.py` (nếu có gói Markdown cũ) hoặc tự soạn `{chapter_id}_theory.md`.
2. Soạn bổ sung câu hỏi vào `scripts/chapter_data/{chapter_id}.py` (`MCQ`, `SHORT`, `ESSAY`).
3. `python scripts/build_lms_data.py` để gộp, xáo trộn phương án, xuất JSON và cập nhật manifest.
4. `python scripts/verify_lms_integrity.py` phải báo **PASS 100%** trước khi deploy GitHub Pages.
