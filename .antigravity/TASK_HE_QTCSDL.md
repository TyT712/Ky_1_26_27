# AGENT EXECUTION SPEC: Xử lý Học liệu Môn Hệ Quản Trị CSDL (He_QTCSDL)

## 1. Mục tiêu (Objective)
Thực thi pipeline chuyển đổi tài liệu PDF dung lượng lớn của môn **Hệ Quản trị Cơ sở dữ liệu** từ thư mục `data/raw_pdfs/he_qtcsdl/` sang định dạng Markdown có cấu trúc chuẩn tại `data/parsed_markdown/` và tạo bản tổng hợp kiến thức tại `data/notebook_exports/`, tuân thủ nghiêm ngặt kiến trúc sẵn có của dự án `Ky_1_26_27`.

## 2. Ngữ cảnh & Chuẩn hóa Đường dẫn (Paths & Conventions)
- **Thư mục nguồn (Input):** `data/raw_pdfs/He_QTCSDL/` (Hiện có: `quyen_1_nhap_mon.pdf` và các file PDF bổ sung sau này).
- **Thư mục đích 1 - Bản bóc tách chi tiết (Parsed Output):** `data/parsed_markdown/he_qtcsdl/`
- **Thư mục đích 2 - Bản tóm tắt/Ghi chú (Summary Output):** `data/notebook_exports/he_qtcsdl/`
- **File tham chiếu mẫu (Reference Formatting):** 
  - Đọc `data/parsed_markdown/giai_tich_1/giao_trinh_giai_tich_chuong_1.md` để học cách định dạng cấu trúc file bóc tách.
  - Đọc `data/notebook_exports/giai_tich_1/gioi_han_va_dao_ham_summary.md` để học cách trình bày bản tóm tắt.

## 3. Quy trình thực thi tuần tự (Execution Steps)
> **CHỈ THỊ CHO AGENT:** Thực hiện tuần tự từ Bước 1 đến Bước 5. Không bỏ qua bước đối chiếu mẫu.

### [ ] Bước 1: Đọc cấu hình và Phân tích mẫu (Context & Pattern Matching)
1. Đọc `.antigravity/context.md`, `README.md`, `data/parsed_markdown/README.md`, và `data/notebook_exports/README.md` để nắm toàn bộ quy tắc riêng của workspace.
2. Kiểm tra cấu trúc heading, metadata của môn `giai_tich_1` để áp dụng đồng nhất cho môn `he_qtcsdl`.
3. Tạo 2 thư mục đích nếu chưa tồn tại:
   - `data/parsed_markdown/he_qtcsdl/`
   - `data/notebook_exports/he_qtcsdl/`

### [ ] Bước 2: Trích xuất PDF dung lượng lớn theo cơ chế Streaming (PDF Parsing)
1. Viết script Python (lưu vào thư mục `scripts/` hoặc chạy cục bộ) sử dụng thư viện tối ưu như `pymupdf4llm` hoặc `pdfplumber`.
2. **Xử lý chống tràn RAM:** Đọc file `data/raw_pdfs/He_QTCSDL/quyen_1_nhap_mon.pdf` (và các file `.pdf` khác trong cùng thư mục) theo từng cụm trang (batch/page-by-page), tuyệt đối không load toàn bộ cấu trúc nhị phân vào bộ nhớ cùng lúc.
3. **Chia nhỏ theo Chương (Chunking):** Tự động nhận diện ranh giới các Chương/Bài trong giáo trình để tách thành các file riêng biệt theo chuẩn đặt tên:
   - `data/parsed_markdown/he_qtcsdl/quyen_1_nhap_mon_chuong_1.md`
   - `data/parsed_markdown/he_qtcsdl/quyen_1_nhap_mon_chuong_2.md`
   - *(Tiếp tục cho đến hết các chương)*

### [ ] Bước 3: Làm sạch và Bảo toàn Ngữ nghĩa Đặc thù CSDL (Domain-Specific Cleaning)
Trong quá trình chuyển đổi sang Markdown, bắt buộc áp dụng các bộ lọc sau:
1. **Loại bỏ rác hiển thị:** Xóa số trang rời rạc, header/footer lặp lại ở đầu/cuối mỗi trang PDF, và các ký tự lỗi font tiếng Việt.
2. **Định dạng khối lệnh SQL:** Mọi câu truy vấn (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `ALTER`, `DROP`...) phải được đóng khung vào code block ` ```sql ... ``` `.
3. **Định dạng Đại số quan hệ & Lý thuyết:** Chuyển đổi các ký hiệu phép chọn ($\sigma$), phép chiếu ($\pi$), phép kết ($\bowtie$), phép chia ($\div$), phụ thuộc hàm ($X \rightarrow Y$) sang định dạng LaTeX (`$...$`) tương tự như cách làm ở môn `giai_tich_1`.
4. **Bảo toàn Bảng quan hệ (Relational Tables):** Mọi bảng dữ liệu mẫu và lược đồ cơ sở dữ liệu phải được dựng lại thành bảng Markdown chuẩn (`| Cột 1 | Cột 2 |`).

### [ ] Bước 4: Tạo bản Tóm tắt Học tập (Summary Generation)
Từ các file đã bóc tách ở `data/parsed_markdown/he_qtcsdl/`, tổng hợp các kiến thức cốt lõi (Khái niệm CSDL, Các mô hình dữ liệu, Kiến trúc hệ QTCSDL, Ngôn ngữ truy vấn, Ràng buộc toàn vẹn) thành các file tóm tắt cô đọng lưu tại:
- `data/notebook_exports/he_qtcsdl/[ten_chu_de]_summary.md` (Tuân thủ format của `gioi_han_va_dao_ham_summary.md`).

### [ ] Bước 5: Cập nhật Tài liệu Hệ thống & Git Ignore
1. Cập nhật `data/parsed_markdown/README.md` và `data/notebook_exports/README.md` để bổ sung danh mục môn Hệ QTCSDL.
2. Kiểm tra file `.gitignore` ở thư mục gốc: Đảm bảo thêm quy tắc ignore các file tạm sinh ra trong quá trình parse và cân nhắc ignore `data/raw_pdfs/**/*.pdf` (hoặc dùng Git LFS) để tránh làm nặng repository.

## 4. Tự kiểm tra & Xác thực (Self-Verification)
Agent BẮT BUỘC chạy kiểm tra bằng lệnh Terminal sau khi hoàn tất:
1. **Kiểm tra sự tồn tại và dung lượng file:** Chạy lệnh liệt kê `ls -lh data/parsed_markdown/he_qtcsdl/` và `ls -lh data/notebook_exports/he_qtcsdl/`. Đảm bảo không có file `.md` nào bị rỗng (0 KB).
2. **Kiểm tra lỗi cú pháp Markdown/LaTeX:** Quét nhanh các file `.md` vừa tạo để đảm bảo số lượng dấu ` ``` ` là số chẵn (không bị hở code block) và không còn ký tự rác nhị phân (non-UTF8 characters).
3. **Tự sửa lỗi (Self-Healing):** Nếu phát hiện chương nào bị cắt sai vị trí hoặc lỗi font, tự động điều chỉnh Regex trong script Python và chạy lại cho đến khi văn bản đầu ra sạch hoàn toàn.

## 5. Điều kiện hoàn tất (Definition of Done)
- Các file chương bài giảng nằm gọn trong `data/parsed_markdown/he_qtcsdl/`.
- Các file tóm tắt ôn tập nằm gọn trong `data/notebook_exports/he_qtcsdl/`.
- Xuất báo cáo ngắn gọn trên Terminal: Danh sách các file đã tạo, số lượng chương tách được từ `quyen_1_nhap_mon.pdf` và tổng dung lượng các file `.md` sau xử lý.