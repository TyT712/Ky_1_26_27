# AGENT EXECUTION SPEC: Tạo Học Liệu Tương Tác Môn Hệ QTCSDL, Triển Khai GitHub Pages & Đóng Gói Skill

## 1. Mục tiêu tối thượng (Objective)
1. **Chuẩn hóa Quy trình Lặp (Skill Creation):** Đóng gói quy trình "Chuyển hóa Chương bài giảng Markdown thành Module Học tập & Kiểm tra (Summary + Quiz + Short Answer + Essay)" thành một **Agent Skill** tái sử dụng được, đăng ký vào `.antigravity/skills_registry.json`.
2. **Sinh Học Liệu Toàn Diện (Content Generation):** Áp dụng Skill vừa tạo cho toàn bộ 11 chương trong `data/parsed_markdown/he_qtcsdl/` (kết hợp tham chiếu 9 file trong `data/notebook_exports/he_qtcsdl/`).
3. **Triển khai Giao diện Tĩnh (GitHub Pages):** Xây dựng hệ thống hiển thị tĩnh tại thư mục `docs/` (sử dụng Docsify hoặc HTML/JS nhẹ tích hợp sẵn MathJax/KaTeX) để chạy trực tiếp trên GitHub Pages mà không cần bước build phức tạp.

---

## 2. Nguồn dữ liệu đầu vào (Input Sources)
- **Danh sách 11 chương bắt buộc xử lý (`data/parsed_markdown/he_qtcsdl/`):**
  - Quyển 1 (Nhập môn): `quyen_1_nhap_mon_chuong_1.md` đến `quyen_1_nhap_mon_chuong_6.md`.
  - Quyển 2 (Thiết kế): `quyen_2_thiet_ke_chuong_1.md` đến `quyen_2_thiet_ke_chuong_5.md`.
- **Tài liệu tóm tắt bổ trợ (`data/notebook_exports/he_qtcsdl/`):**
  - Toàn bộ 9 file `*_summary.md` hiện có.

---

## 3. Quy trình thực thi tuần tự (Execution Steps)
> **CHỈ THỊ CHO AGENT:** Thực hiện nghiêm ngặt từng bước từ Bước 1 đến Bước 5.

### [ ] Bước 1: Hình thành Skill cho các tác vụ lặp lại (Skill Extraction & Registration)
Do quy trình tạo học liệu cho mỗi chương (và các môn học khác trong tương lai) có cấu trúc giống hệt nhau, Agent BẮT BUỘC phải tạo Skill trước khi sinh nội dung:
1. Đọc file `.antigravity/skills_registry.json` và `.antigravity/context.md` để nắm chuẩn định nghĩa Skill của dự án.
2. Tạo thư mục/file hướng dẫn Skill tại `.antigravity/skills/chapter_study_pack_generator.md` (hoặc theo chuẩn đường dẫn trong `skills_registry.json`) với quy tắc đầu vào/đầu ra chuẩn hóa:
   - **Input:** Đường dẫn file chương (`parsed_markdown/{mon_hoc}/{ten_chuong}.md`) + File summary liên quan (nếu có).
   - **Output Standard (4 phần bắt buộc cho mỗi chương):**
     1. **Phần 1 - Tóm tắt cốt lõi (Executive Summary):** Sơ đồ tư duy (Mermaid.js), các định nghĩa, định lý/thuật toán, công thức/cú pháp trọng tâm.
     2. **Phần 2 - Bài tập Trắc nghiệm (Multiple Choice - tối thiểu 10 câu/chương):** Có 4 phương án A, B, C, D. Đáp án đúng và giải thích chi tiết phải được đặt trong thẻ `<details><summary>Xem đáp án & Giải thích</summary>...</details>` để người học tự luyện tập trên GitHub Pages.
     3. **Phần 3 - Câu hỏi Trả lời ngắn (Short Answer - tối thiểu 5 câu/chương):** Tập trung vào việc viết nhanh một biểu thức Đại số quan hệ, một câu truy vấn SQL, xác định dạng chuẩn, hoặc tìm bao đóng $X^+$. Có thẻ `<details>` ẩn đáp án.
     4. **Phần 4 - Bài tập Tự luận & Thiết kế (Essay / Problem Solving - tối thiểu 3 bài/chương):** Bài toán tổng hợp (Thiết kế ER, chuyển đổi lược đồ, tìm khóa tối tiểu, phân tách bảo toàn thông tin/phụ thuộc hàm, viết Trigger/Procedure). Kèm lời giải từng bước (step-by-step) trong thẻ `<details>`.
3. Cập nhật `.antigravity/skills_registry.json` để đăng ký skill `chapter_study_pack_generator` và cập nhật `.antigravity/context.md`.

### [ ] Bước 2: Thực thi Skill tạo nội dung cho toàn bộ 11 Chương môn Hệ QTCSDL
Áp dụng chuẩn đầu ra của Skill ở Bước 1, tiến hành đọc từng file trong `data/parsed_markdown/he_qtcsdl/` và xuất các file học liệu hoàn chỉnh vào thư mục `docs/courses/he_qtcsdl/`:
- **Quyển 1 - Nhập môn CSDL:**
  - `docs/courses/he_qtcsdl/q1_chuong_1_tong_quan.md` (từ `quyen_1_nhap_mon_chuong_1.md`)
  - `docs/courses/he_qtcsdl/q1_chuong_2_mo_hinh_quan_he.md` (từ `quyen_1_nhap_mon_chuong_2.md`)
  - `docs/courses/he_qtcsdl/q1_chuong_3_dai_so_quan_he.md` (từ `quyen_1_nhap_mon_chuong_3.md`)
  - `docs/courses/he_qtcsdl/q1_chuong_4_ngon_ngu_sql.md` (từ `quyen_1_nhap_mon_chuong_4.md`)
  - `docs/courses/he_qtcsdl/q1_chuong_5_rang_buoc_toan_ven.md` (từ `quyen_1_nhap_mon_chuong_5.md`)
  - `docs/courses/he_qtcsdl/q1_chuong_6_to_chuc_vat_ly_toi_uu.md` (từ `quyen_1_nhap_mon_chuong_6.md`)
- **Quyển 2 - Thiết kế CSDL:**
  - `docs/courses/he_qtcsdl/q2_chuong_1_mo_hinh_er.md` (từ `quyen_2_thiet_ke_chuong_1.md`)
  - `docs/courses/he_qtcsdl/q2_chuong_2_phu_thuoc_ham_va_khoa.md` (từ `quyen_2_thiet_ke_chuong_2.md`)
  - `docs/courses/he_qtcsdl/q2_chuong_3_chuan_hoa_1nf_bcnf.md` (từ `quyen_2_thiet_ke_chuong_3.md`)
  - `docs/courses/he_qtcsdl/q2_chuong_4_phan_tach_luoc_do.md` (từ `quyen_2_thiet_ke_chuong_4.md`)
  - `docs/courses/he_qtcsdl/q2_chuong_5_phu_thuoc_da_tri_4nf.md` (từ `quyen_2_thiet_ke_chuong_5.md`)
- **Lưu ý chất lượng chuyên môn:** Dữ liệu bài tập phải bám sát 100% nội dung và ký hiệu trong giáo trình đã parse, không bịa đặt kiến thức ngoài luồng.

### [ ] Bước 3: Thiết lập Giao diện Tĩnh cho GitHub Pages (`docs/`)
Để hiển thị tĩnh ngay lập tức trên GitHub Pages (nhánh `main`, thư mục `/docs`) mà không cần Node.js build pipeline phức tạp, sử dụng **Docsify**:
1. Tạo file `docs/.nojekyll` (để GitHub Pages không bỏ qua các file bắt đầu bằng dấu gạch dưới).
2. Tạo file `docs/index.html` tích hợp sẵn CDN của:
   - `docsify` (giao diện đọc tài liệu chuẩn, hỗ trợ thanh tìm kiếm `search`).
   - `docsify-katex` hoặc `MathJax` (bắt buộc để render chuẩn các ký hiệu $\sigma, \pi, \bowtie, X \rightarrow Y, X \twoheadrightarrow Y$).
   - `prism-sql.min.js` (syntax highlighting cho các khối lệnh SQL).
   - `mermaid.min.js` (render sơ đồ ER và lưu đồ thuật toán).
   - CSS tùy chỉnh nhẹ giúp các thẻ `<details>` (ẩn/hiện đáp án trắc nghiệm, trả lời ngắn, tự luận) hiển thị đẹp như một nút bấm tương tác.
3. Tạo file điều hướng `docs/_sidebar.md` và trang chủ `docs/README.md` liệt kê đầy đủ cấu trúc môn **Hệ Quản Trị CSDL** (11 chương + phần tổng hợp từ `notebook_exports`) và sẵn sàng mở rộng cho môn **Giải tích 1**.

### [ ] Bước 4: Dọn dẹp Repository & Kiểm soát File lớn
- Kiểm tra `.gitignore`: Đảm bảo `data/raw_pdfs/**/*.pdf` đã được đưa vào `.gitignore` (và chạy `git rm --cached data/raw_pdfs/He_QTCSDL/quyen_1_nhap_mon.pdf` nếu file PDF nặng này đang bị git track) để tránh lỗi vượt giới hạn băng thông khi deploy GitHub Pages.

## 4. Tự kiểm tra & Xác thực (Self-Verification)
Sau khi hoàn thành, Agent BẮT BUỘC chạy các lệnh kiểm chứng sau trên Terminal:
1. **Kiểm tra số lượng & dung lượng file đầu ra:**
   - Chạy `ls -la docs/courses/he_qtcsdl/` để xác nhận đủ 11 file chương.
   - Đảm bảo mỗi file đều có đủ 4 phần: Tóm tắt, Trắc nghiệm ($\ge 10$ câu), Trả lời ngắn ($\ge 5$ câu), Tự luận ($\ge 3$ bài).
2. **Kiểm tra cú pháp JSON & HTML:**
   - Chạy `python -m json.tool .antigravity/skills_registry.json > /dev/null` để đảm bảo file cấu hình Skill không bị lỗi cú pháp JSON.
   - Kiểm tra `docs/index.html` và `docs/_sidebar.md` đảm bảo không có đường dẫn (link) nào bị gãy (broken links).
3. **Chạy thử Local Server (Dry-run):**
   - Chạy thử `python -m http.server 8000 --directory docs` ở chế độ kiểm tra nhanh (hoặc dùng `curl -I http://localhost:8000`) để xác nhận trang tĩnh phản hồi HTTP 200 OK.

## 5. Điều kiện hoàn tất (Definition of Done)
- Skill tạo học liệu chương đã được lưu trữ và đăng ký chính thức vào `.antigravity/skills_registry.json`.
- Đầy đủ 11 chương môn Hệ QTCSDL trong `docs/courses/he_qtcsdl/` có tóm tắt, trắc nghiệm, trả lời ngắn, tự luận kèm đáp án ẩn/hiện.
- Thư mục `docs/` sẵn sàng để bật GitHub Pages (Settings -> Pages -> Deploy from a branch -> `main` / `/docs`).