# Chuyên Đề: Tổng quan SDLC & Quản Lý Mã Nguồn với Git

## 1. Khủng hoảng Phần mềm và Sự cần thiết của Quy trình Kỹ nghệ
- Khủng hoảng phần mềm bắt nguồn từ sự phức tạp ngày càng tăng của hệ thống trong khi phương pháp phát triển mang tính thủ công, thiếu kiểm soát.
- Kỹ nghệ phần mềm (Software Engineering) ra đời nhằm chuyển đổi việc viết phần mềm từ "nghệ thuật cá nhân" thành một "ngành kỹ thuật có quy chuẩn", có khả năng dự đoán chi phí, thời gian và chất lượng.

## 2. Vòng đời SDLC & Trục Đánh giá Chất lượng
- SDLC định hình đường đi của một phần mềm từ lúc khởi tạo ý tưởng đến khi ngừng hoạt động.
- Trục chất lượng phần mềm không chỉ nằm ở "chạy đúng chức năng" mà phải thỏa mãn đồng thời:
  - Chất lượng bên ngoài: Độ tin cậy, thời gian phản hồi, tính bảo mật, trải nghiệm người dùng.
  - Chất lượng bên trong: Dễ đọc (Readability), Dễ bảo trì (Maintainability), Dễ mở rộng (Extensibility) và Khả năng kiểm thử (Testability).

## 3. Kiến trúc Không gian Làm việc của Git
- Git theo mô hình phân tán (Distributed Version Control System - DVCS), mỗi lập trình viên sở hữu toàn bộ lịch sử commit tại máy cục bộ.
- Chu trình làm việc chuẩn: Chỉnh sửa tại Working Directory $	o$ `git add` vào Staging Area $	o$ `git commit` lưu vào Local Repo $	o$ `git push` đồng bộ lên Remote Repo (GitHub/GitLab).
