# Giáo trình Công nghệ Phần mềm - Chương 2: Quy trình phát triển phần mềm
<!-- Nguồn: TS. Trần Văn Long - Khoa Tin học, Đại học Sư phạm, Đại học Huế -->

<!-- PAGE 1 -->
## A. Mục tiêu Bài học
1. Phân biệt được ưu và nhược điểm của các mô hình phát triển phần mềm truyền thống (Thác nước, Chữ V).
2. Trình bày và giải thích được 4 giá trị cốt lõi và 12 nguyên tắc của triết lý Agile.
3. Mô tả được các vai trò, sự kiện và tạo tác (artifacts) chính trong quy trình Scrum.
4. Áp dụng được luồng làm việc cộng tác trên GitHub (`Branch` -> `Commit` -> `Push` -> `Pull Request` -> `Merge`) để phát triển tính năng trong đồ án nhóm.

<!-- PAGE 4 -->
## B. Nội dung Chi tiết

### I. Các Mô hình Quy trình Truyền thống
- **Mô hình Thác nước (Waterfall Model):**
  - Tuần tự từ Yêu cầu $	o$ Thiết kế $	o$ Lập trình $	o$ Kiểm thử $	o$ Triển khai $	o$ Bảo trì.
  - Hạn chế: Khó phản ứng khi yêu cầu thay đổi, chi phí sửa lỗi muộn cực cao, khách hàng không thấy được sản phẩm sớm.
- **Mô hình Chữ V (V-Model):**
  - Nhánh trái: Phân rã và thiết kế; Nhánh phải: Tích hợp và kiểm định.
  - Nguyên lý song hành: Mỗi pha thiết kế đều có một pha kiểm thử đối ứng tương ứng.

### II. Triết lý Phát triển Phần mềm Linh hoạt (Agile)
- Bối cảnh ra đời của Tuyên ngôn Agile (2001).
- 4 Giá trị căn bản: Cá nhân & tương tác > Quy trình & công cụ; Phần mềm chạy tốt > Tài liệu đồ sộ; Cộng tác khách hàng > Đàm phán hợp đồng; Thích ứng thay đổi > Bám sát kế hoạch.
- Khái niệm bước lặp (Iteration) và phân phối tăng tiến (Incremental Delivery).

### III. Khung Làm việc Scrum Chi tiết
- **3 Vai trò:** Product Owner (chịu trách nhiệm về giá trị sản phẩm), Scrum Master (bảo vệ quy trình và loại bỏ rào cản), Development Team (trực tiếp tạo ra sản phẩm).
- **4 Sự kiện:** Sprint Planning, Daily Scrum (15 phút), Sprint Review, Sprint Retrospective.
- **3 Tạo tác:** Product Backlog, Sprint Backlog, Increment kèm Definition of Done (DoD).
- Công cụ trực quan hóa: Bảng Kanban/Scrum Board (To Do, In Progress, In Review, Done) và Biểu đồ Burndown Chart.

### IV. Quy trình Làm việc Nhóm với GitHub
- Luồng rẽ nhánh Feature Branch.
- Thao tác tạo và thẩm định Pull Request (PR).
- Quy chuẩn xử lý xung đột gộp (Merge Conflict).
