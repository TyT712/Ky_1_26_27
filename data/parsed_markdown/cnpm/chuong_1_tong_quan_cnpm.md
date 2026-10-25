# Giáo trình Công nghệ Phần mềm - Chương 1: Tổng quan về Công nghệ Phần mềm
<!-- Nguồn: TS. Trần Văn Long - Khoa Tin học, Đại học Sư phạm, Đại học Huế -->

<!-- PAGE 1 -->
## A. Mục tiêu Bài học
1. Trình bày được bối cảnh lịch sử, định nghĩa và tầm quan trọng của ngành Công nghệ Phần mềm (CNPM).
2. Mô tả các hoạt động cốt lõi trong Vòng đời Phát triển Phần mềm (SDLC) và các thuộc tính chất lượng của sản phẩm phần mềm.
3. Hiểu rõ các vai trò nghề nghiệp trong dự án phần mềm và ý nghĩa của mô hình kỹ năng chữ T (T-shaped skills).
4. Cài đặt, cấu hình và sử dụng thành thạo các lệnh Git cơ bản (`init`, `status`, `add`, `commit`, `log`, `diff`) để quản lý phiên bản mã nguồn cục bộ.
5. Nhận thức rõ sự khác biệt mang tính sống còn giữa phát triển kỹ thuật có quy chuẩn và làm việc tự phát.

<!-- PAGE 3 -->
## B. Nội dung Chi tiết

### I. Các khái niệm Cơ bản về Phần mềm & CNPM
- **Phần mềm là gì?** Phần mềm không đơn thuần là các dòng mã nguồn (source code) mà là một tập hợp hoàn chỉnh gồm: Chương trình máy tính thực thi, cấu trúc dữ liệu lưu trữ và tài liệu kỹ thuật/hướng dẫn sử dụng.
- **Đặc trưng phân biệt phần mềm với phần cứng:**
  - Phần mềm được kỹ nghệ hóa (software is engineered), không chế tạo theo dây chuyền vật lý.
  - Phần mềm không bị mòn cơ học theo thời gian mà suy thoái (deteriorates) do sự biến đổi của môi trường và các lần sửa lỗi chắp vá thiếu kiểm soát.
  - Khó đo lường độ phức tạp và tiến độ bằng trực quan thông thường.

### II. Khủng hoảng Phần mềm (Software Crisis)
- Nguyên nhân sâu xa: Độ phức tạp của phần mềm tăng theo hàm mũ, sự phụ thuộc quá mức vào các cá nhân "ngôi sao", thiếu quy trình kiểm thử và quản lý yêu cầu.
- Hậu quả: Nhiều dự án thất bại hoàn toàn, chi phí bảo trì chiếm hơn 70-80% tổng chi phí vòng đời của một hệ thống phần mềm.
- Giải pháp: Định hình ngành Công nghệ Phần mềm (NATO Science Committee, Garmisch, 1968) áp dụng nguyên lý công nghệ vào phần mềm.

### III. Vòng đời Phát triển Phần mềm (SDLC)
- Các công đoạn cốt lõi: Phân tích yêu cầu $	o$ Thiết kế hệ thống $	o$ Lập trình $	o$ Kiểm thử $	o$ Triển khai $	o$ Vận hành & Bảo trì.
- Các thuộc tính chất lượng: Độ tin cậy (Reliability), Hiệu năng (Efficiency), Bảo mật (Security), Khả dụng (Usability), Dễ bảo trì (Maintainability), Tương thích (Portability).

### IV. Vai trò và Kỹ năng Lập trình viên
- Đội ngũ dự án: Project Manager, Product Owner, Business Analyst, Software Architect, Software Engineer, QA/QC Tester, DevOps Engineer.
- Tư duy kỹ năng chữ T (T-shaped): Kết hợp sự am hiểu rộng rãi về quy trình, giao tiếp, kiểm thử và năng lực chuyên sâu vào một công nghệ mũi nhọn.

### V. Quản lý Phiên bản Mã nguồn với Git
- Khái niệm hệ thống quản lý phiên bản phân tán (DVCS).
- Ba khu vực làm việc: Working Tree, Staging Area, Local Repository.
- Thao tác thực hành cơ bản: Cấu hình danh tính, khởi tạo repo, theo dõi trạng thái, ghi nhận snapshot.
