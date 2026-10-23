# SKILL: CHAPTER STUDY PACK GENERATOR
## Chuyển hóa Chương Giáo trình Markdown thành Module Học tập & Khảo thí Toàn diện

---

## 1. MỤC TIÊU & BỐI CẢNH (OBJECTIVE & CONTEXT)
Skill `chapter_study_pack_generator` được thiết kế để chuẩn hóa quy trình chuyển đổi một chương bài giảng giáo trình (đã bóc tách sang Markdown) cùng các ghi chú tóm tắt NotebookLM thành một **Gói học liệu hoàn chỉnh (Interactive Study Pack)** tương thích 100% với môi trường hiển thị Docsify / GitHub Pages.

---

## 2. QUY CHUẨN ĐẦU VÀO (INPUT SPECIFICATION)
- **Primary Input:** `data/parsed_markdown/{subject_code}/{chapter_file}.md` (Nội dung chi tiết chương, có phân cấp H1-H4, block code SQL/ngôn ngữ lập trình, công thức LaTeX, bảng dữ liệu và thẻ `<!-- PAGE X -->`).
- **Secondary Input (Optional):** `data/notebook_exports/{subject_code}/{summary_file}.md` (Các ý niệm cốt lõi, mindmaps, điểm nhấn trọng tâm từ Google NotebookLM).
- **Target Output Path:** `docs/courses/{subject_code}/{target_file}.md`.

---

## 3. CẤU TRÚC ĐẦU RA BẮT BUỘC (MANDATORY 4-SECTION STANDARD)
Mỗi file học liệu chương được sinh ra bắt buộc phải chứa đúng 4 phần theo cấu trúc sau:

### PHẦN 1: TÓM TẮT CỐT LÕI (EXECUTIVE SUMMARY)
- **Sơ đồ tư duy trực quan (Mermaid.js):** Sơ đồ quan hệ thực thể, cây phân cấp, luồng xử lý hoặc kiến trúc (`graph TD`, `classDiagram`, `erDiagram`).
- **Hệ thống khái niệm then chốt:** Định nghĩa hình thức và ý nghĩa trực giác.
- **Công thức & Quy tắc cốt lõi:** Biểu diễn chuẩn LaTeX (`$...$` hoặc `$$...$$`), bảng tra cứu quy tắc hoặc cú pháp lệnh.

### PHẦN 2: BÀI TẬP TRẮC NGHIỆM (MULTIPLE CHOICE - TỐI THIỂU 10 CÂU)
- Mỗi câu gồm 4 phương án độc lập: `A.`, `B.`, `C.`, `D.`.
- Toàn bộ đáp án đúng và phần phân tích/giải thích chi tiết được giấu trong thẻ tương tác:
```html
<details>
<summary><b>Xem đáp án & Giải thích</b></summary>

- **Đáp án đúng:** [A/B/C/D]
- **Giải thích chi tiết:** [Phân tích vì sao phương án này đúng và chỉ ra sai sót của 3 phương án còn lại]
- **Căn cứ giáo trình:** [Tên chương / Mục / Số trang tham chiếu]
</details>
```

### PHẦN 3: CÂU HỎI TRẢ LỜI NGẮN (SHORT ANSWER - TỐI THIỂU 5 CÂU)
- Tập trung vào năng lực thao tác nhanh: Viết biểu thức Đại số quan hệ, câu lệnh SQL, tính bao đóng thuộc tính $X^+$, xác định khóa, phân loại dạng chuẩn.
- Lời giải đáp ngắn gọn, xúc tích nằm trong thẻ `<details>`:
```html
<details>
<summary><b>Xem đáp án & Hướng dẫn</b></summary>

- **Đáp án:** [Biểu thức / Câu lệnh / Kết quả chính xác]
- **Ghi chú lý thuyết:** [Lưu ý mấu chốt tránh nhầm lẫn]
</details>
```

### PHẦN 4: BÀI TẬP TỰ LUẬN & THIẾT KẾ (ESSAY / PROBLEM SOLVING - TỐI THIỂU 3 BÀI)
- Đề bài tổng hợp yêu cầu tư duy thiết kế, chứng minh, tính toán nhiều bước hoặc viết thủ tục/Trigger hoàn chỉnh.
- Lời giải chi tiết từng bước (Step-by-step Solution) bám sát các thuật toán chính quy được ẩn trong thẻ `<details>`:
```html
<details>
<summary><b>Xem lời giải chi tiết từng bước</b></summary>

#### Bước 1: [Tên bước]
...
#### Bước 2: [Tên bước]
...
#### Kết luận:
...
</details>
```

---

## 4. QUY TẮC BẢO ĐẢM HỌC THUẬT (STRICT QUALITY RULES)
1. **100% Căn cứ giáo trình:** Không tạo câu hỏi ngoài phạm vi kiến thức đã được nạp trong `data/parsed_markdown/`.
2. **Ký hiệu toán học & Mã nguồn chuẩn:**
   - Dùng đúng ký hiệu toán: $\sigma, \pi, \bowtie, \div, \rho, \cup, \cap, \to, \twoheadrightarrow, \vDash, \vdash$.
   - Mã lệnh SQL phải đặt trong ` ```sql `.
3. **Tính tương tác trên Web tĩnh:** Giữ nguyên cú pháp HTML `<details>` và `<summary>` chuẩn để tương thích với Docsify trên GitHub Pages.
