# Giáo trình Công nghệ Phần mềm - Chương 4: Phát triển, Tích hợp và Đảm bảo Chất lượng
<!-- Nguồn: TS. Trần Văn Long - Khoa Tin học, Đại học Sư phạm, Đại học Huế -->

<!-- PAGE 1 -->
## A. Mục tiêu Bài học
1. Tham gia hiệu quả vào các sự kiện Scrum: Sprint Planning, Sprint Review, Sprint Retrospective.
2. Vận dụng nguyên lý thiết kế kiến trúc phân tầng (Layered Architecture) và xây dựng RESTful API cho User Story.
3. Thành thạo quy trình quản lý mã nguồn với Git (Feature Branch, Pull Request, Resolving Conflicts).
4. Thực hiện Code Review chuyên nghiệp để đảm bảo chất lượng kỹ thuật mã nguồn.
5. Hiểu sâu các cấp độ kiểm thử trong Kim tự tháp kiểm thử và áp dụng thành thạo TDD (Test-Driven Development) bằng Unit Tests.

<!-- PAGE 3 -->
## B. Nội dung Chi tiết

### I. Sprint Planning & Phân rã Công việc (Task Breakdown)
- Xác định Mục tiêu Sprint (Sprint Goal).
- Phân rã User Story thành các nhiệm vụ kỹ thuật cụ thể (Technical Tasks có kích thước từ 2 đến 8 giờ làm việc).
- Ước lượng năng lực nhóm (Team Capacity).

### II. Thiết kế Kiến trúc Đúng lúc (Just-in-Time Design)
- Phân tầng Controller - Service - Repository.
- Thiết kế Data Transfer Object (DTO) và Entities.
- Chuẩn hóa RESTful API (HTTP Verbs: GET, POST, PUT, DELETE, PATCH; Status Codes: 200, 201, 400, 401, 403, 404, 500).

### III. Chuẩn mực Lập trình Clean Code & Tái cấu trúc (Refactoring)
- Nguyên tắc đặt tên biến, hàm, lớp.
- Tránh Code Smells: Long Method, Large Class, Feature Envy, Primitive Obsession, Dead Code.
- Nguyên lý DRY, KISS và Boy Scout Rule.

### IV. Chiến lược Kiểm thử Phần mềm & TDD
- Kim tự tháp kiểm thử: Unit Test, Integration Test, E2E Test.
- Quy chuẩn viết Unit Test theo cấu trúc AAA (Arrange, Act, Assert).
- Chu trình TDD Red - Green - Refactor.
- Sử dụng Test Doubles: Mock, Stub, Fake.

### V. Thẩm duyệt Mã nguồn & Kết thúc Sprint
- Quy trình mở và phê duyệt Pull Request (PR) trên GitHub.
- Các tiêu chí kiểm tra trong Code Review Checklist.
- Tổ chức Sprint Review (Demo sản phẩm đạt DoD) và Sprint Retrospective (Kế hoạch hành động cải tiến).
