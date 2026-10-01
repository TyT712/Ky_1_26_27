# 🎓 Semester Hub - Cổng Quản Lý Học Phần & Deadline Cá Nhân

Một trang web tĩnh (Static Web App) hiện đại, tinh gọn và tối ưu hoàn toàn để triển khai miễn phí trên **GitHub Pages**. Giúp sinh viên quản lý toàn bộ nội dung bài giảng, đề cương, link tài liệu và danh sách công việc/deadline trong học kỳ theo triết lý **Git-based** (chỉnh sửa qua Git hoặc tương tác trực tiếp trên giao diện).

---

## ✨ Điểm Nổi Bật & Tính Năng

- 🚀 **Zero-Build & Chạy Ngay Lập Tức**: Không cần cài đặt Node.js hay chạy lệnh build phức tạp. Mở file `index.html` lên là chạy trực tiếp hoặc kích hoạt GitHub Pages trong 30 giây.
- 📁 **Quản Lý Dữ Liệu Qua Git (`data/courses.js`)**:
  - Dễ dàng thêm môn học mới, chỉnh sửa thông tin giảng viên, phòng học, lịch học, link Google Classroom, Google Drive, GitHub.
  - Viết ghi chú bài giảng bằng **Markdown** (hỗ trợ định dạng in đậm, danh sách, khối code, trích dẫn, công thức).
  - Thêm / cập nhật hạn chót bài tập (deadlines) và mức độ ưu tiên.
- 🗓️ **Thời Khóa Biểu Tuần Thông Minh**: Tự động tổng hợp và hiển thị lịch học từ Thứ 2 đến Thứ 7, tự động phát hiện và làm nổi bật ngày hôm nay.
- 📊 **Dashboard Thống Kê**:
  - Tự động đếm tổng số môn học và tổng số tín chỉ đăng ký.
  - Tự động tính toán số ngày còn lại đến hạn chót (Cảnh báo: *Quá hạn*, *Hạn hôm nay*, *Còn 1 ngày*, *Còn N ngày*).
  - Thanh tiến độ hoàn thành bài tập trực quan theo thời gian thực.
- 📋 **Bảng Quản Lý Task & Deadline Linh Hoạt**:
  - Form **"+ Thêm Task Mới"** trực tiếp trên web: thêm việc nhanh chóng mà không cần gõ code.
  - Sắp xếp task đa năng: Theo hạn chót gần nhất, độ ưu tiên cao nhất, theo môn học hoặc theo bảng chữ cái.
  - Bộ lọc task đa năng: Tất cả, Quá hạn, Hôm nay, 7 ngày tới, Đã hoàn thành.
  - 2 chế độ hiển thị: **Nhóm theo Học phần** hoặc **Bảng Kanban 3 cột** (Cần làm / Đang làm / Đã hoàn thành).
  - Tương tác checkbox lưu trữ ngay vào `LocalStorage` trên trình duyệt.
- 🔄 **Nút "Đồng Bộ Git" & Tải File Tiện Lợi**:
  - Nút **Sao chép mã nguồn** để dán đè vào `data/courses.js`.
  - Nút **Tải file courses.js** để tải trực tiếp file về máy và thay thế chỉ với 1 cú click!
- 🌗 **Giao Diện Hiện Đại & Dark Mode**: Tự động nhận diện theme hệ thống hoặc tùy chọn Sáng/Tối với 1 cú click. Tối ưu hoàn hảo cho cả máy tính và điện thoại.

---

## 🚀 Hướng Dẫn Triển Khai Lên GitHub Pages

### Bước 1: Khởi tạo và đẩy code lên GitHub Repository

1. Đăng nhập vào [GitHub](https://github.com) và tạo một repository mới (ví dụ: `semester-hub` hoặc `my-semester`). Đặt ở chế độ **Public**.
2. Mở terminal (PowerShell / Git Bash) tại thư mục `semester-hub`:

```bash
git init
git add .
git commit -m "Khởi tạo Semester Hub"
git branch -M main
git remote add origin https://github.com/<tai-khoan-github-cua-ban>/<ten-repo>.git
git push -u origin main
```

### Bước 2: Bật GitHub Pages

Có 2 cách cực kỳ đơn giản để web hoạt động:

#### Cách 1 (Khuyên dùng - Nhanh nhất qua Branch):
1. Trên giao diện GitHub của repository, vào **Settings** -> Mục bên trái chọn **Pages**.
2. Tại phần **Build and deployment**:
   - **Source**: Chọn `Deploy from a branch`.
   - **Branch**: Chọn `main` (hoặc `master`), thư mục giữ nguyên `/ (root)`.
3. Bấm **Save**.
4. Chờ khoảng 1-2 phút, GitHub sẽ hiển thị đường link trang web của bạn:
   👉 `https://<tai-khoan-github-cua-ban>.github.io/<ten-repo>/`

#### Cách 2 (Qua GitHub Actions):
- File `.github/workflows/deploy.yml` đã được cấu hình sẵn.
- Trong **Settings** -> **Pages** -> Chọn **Source: GitHub Actions**. GitHub sẽ tự động triển khai mỗi khi bạn `git push`.

---

## 🛠️ Hướng Dẫn Tùy Chỉnh Nội Dung Cho Học Kỳ Mới

Toàn bộ dữ liệu nằm trong file **`data/courses.js`**. Bạn có thể mở file này bằng VS Code, Notepad hoặc sửa trực tiếp trên giao diện GitHub Web:

### 1. Thay đổi thông tin cá nhân & học kỳ
```javascript
window.SEMESTER_DATA = {
  semesterInfo: {
    title: "Học Kỳ 1 - Năm Học 2026 - 2027",
    studentName: "Nguyễn Văn A",
    studentId: "22020000",
    major: "Công Nghệ Thông Tin",
    targetGPA: "3.6 / 4.0",
    announcement: "📌 Tuần thi giữa kỳ dự kiến bắt đầu từ 20/10/2026!"
  },
  // ...
}
```

### 2. Thêm hoặc sửa một học phần (Course)
Chỉ cần sao chép một đối tượng trong mảng `courses`:
```javascript
{
  id: "ten-mon-viet-tat", // Mã id duy nhất (không dấu, cách nhau dấu gạch ngang)
  code: "INT3306",         // Mã học phần
  name: "Phát Triển Ứng Dụng Web", // Tên môn học
  credits: 3,              // Số tín chỉ
  badgeColor: "indigo",    // Màu sắc: indigo, emerald, rose, sky, purple, amber
  schedule: "Thứ 3 (Tiết 3 - 5) • Phòng 302-G2",
  instructor: {
    name: "TS. Trần Minh Hoàng",
    email: "hoangtm@university.edu.vn",
    office: "Phòng 415 - Nhà E3"
  },
  grading: {
    attendance: "10%",
    midterm: "30%",
    final: "60%"
  },
  links: [
    { title: "Google Classroom", url: "https://classroom.google.com", type: "classroom" },
    { title: "Drive Bài Giảng", url: "https://drive.google.com", type: "drive" }
  ],
  description: "Mô tả ngắn gọn về mục tiêu và nội dung học phần.",
  syllabus: [
    { week: 1, topic: "Tổng quan học phần", status: "completed" },
    { week: 2, topic: "Lý thuyết tuần 2", status: "in-progress" },
    { week: 3, topic: "Lý thuyết tuần 3", status: "upcoming" }
  ],
  notes: `
### 📌 Ghi Chú Môn Học
- Bạn có thể viết ghi chú bài giảng bằng **Markdown** tại đây.
- Hỗ trợ công thức hoặc mã nguồn: \`const a = 10;\`
  `,
  tasks: [
    {
      id: "task-1",
      title: "Nộp bài tập tuần 1",
      deadline: "2026-10-15", // Định dạng YYYY-MM-DD
      priority: "high",       // high, medium, low
      status: "todo",         // todo, in-progress, done
      note: "Ghi chú thêm về yêu cầu bài tập"
    }
  ]
}
```

Sau khi sửa xong, bạn chỉ cần gõ lệnh:
```bash
git commit -am "Cập nhật deadline và ghi chú môn học"
git push
```
Trang web GitHub Pages sẽ tự cập nhật ngay tức thì!

---

## 📁 Cấu Trúc Thư Mục Dự Án

```
semester-hub/
├── index.html                   # Giao diện chính (Dashboard SPA)
├── data/
│   └── courses.js               # File cấu hình dữ liệu môn học, task & ghi chú (Git-based)
├── css/
│   └── styles.css               # Phong cách giao diện, font chữ, hoạt ảnh modal & markdown
├── js/
│   └── app.js                   # Xử lý tương tác, tính deadline, filter, dark mode, export
├── .github/
│   └── workflows/
│       └── deploy.yml           # Tự động hóa deploy GitHub Pages qua GitHub Actions
├── .nojekyll                    # Đảm bảo GitHub Pages nhận đầy đủ các file tĩnh
└── README.md                    # Hướng dẫn chi tiết
```

---

Chúc bạn có một học kỳ mới học tập hiệu quả, quản lý deadline xuất sắc và đạt kết quả GPA như mong đợi! 🎯
