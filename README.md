# Semester Hub

Semester Hub là ứng dụng web tĩnh giúp quản lý học phần, nội dung theo chương và task trong học kỳ. Ứng dụng chạy bằng HTML, CSS và JavaScript thuần, không cần cài đặt hoặc chạy bước build.

## Tính năng

- Xem các học phần và điều hướng theo cấu trúc **Môn học → Chương → Nội dung hoặc Task**.
- Đọc nội dung chương được viết bằng Markdown.
- Xem danh sách task trong từng chương; mở task ở trang riêng để đọc yêu cầu và cập nhật trạng thái.
- Xem task toàn kỳ theo danh sách hoặc Kanban; lọc theo trạng thái/hạn, chọn học phần và sắp xếp task.
- Thêm task, đặt hạn, chọn ưu tiên và trạng thái.
- Tải một tệp bài làm cho mỗi task lên Google Drive cá nhân bằng Google Sign-In.
- Theo dõi số học phần, task, task khẩn cấp và tiến độ hoàn thành.
- Chuyển giao diện sáng/tối và xuất dữ liệu để đồng bộ lại với Git.

## Chạy tại máy

Mở `index.html` bằng trình duyệt. Không cần Node.js hay lệnh build. Trang tải Tailwind CSS, Lucide, Marked và DOMPurify từ CDN, vì vậy cần kết nối Internet để các thư viện và giao diện được tải đầy đủ.

## Cấu trúc dự án

```text
semester-hub/
├── index.html                  # Giao diện ứng dụng
├── css/styles.css              # Kiểu dáng bổ sung
├── js/app.js                   # Điều hướng và xử lý tương tác
├── data/courses.js             # Dữ liệu học kỳ, học phần, chương và task
└── .github/workflows/deploy.yml # Tự động triển khai GitHub Pages
```

## Cập nhật dữ liệu

Nguồn dữ liệu ban đầu nằm trong `data/courses.js`. Mỗi học phần có danh sách `chapters`; mỗi chương có tiêu đề, nội dung Markdown và danh sách task.

```js
{
   id: "software-engineering",
   name: "Công nghệ phần mềm",
   chapters: [
      {
         id: "software-engineering-chapter-1",
         title: "Chương 1: Tổng quan",
         content: "## Nội dung chương",
         tasks: [
            {
               id: "task-se-ch1-01",
               title: "Tên task",
               note: "Yêu cầu và mục tiêu của task",
               deadline: "2026-10-20",
               priority: "medium",
               status: "todo"
            }
         ]
      }
   ]
}
```

- `content` và `note` hỗ trợ Markdown.
- `deadline` có thể bỏ trống; nếu có, dùng định dạng `YYYY-MM-DD`.
- `priority` nhận `high`, `medium` hoặc `low`.
- `status` nhận `todo`, `in-progress` hoặc `done`.
- Giữ `id` duy nhất cho từng học phần, chương và task.
- Học phần chưa có nội dung có thể dùng `chapters: []`.

## Trạng thái trên trình duyệt và đồng bộ Git

Task tạo từ giao diện, trạng thái task và lựa chọn giao diện được lưu trong LocalStorage của trình duyệt hiện tại; các dữ liệu này không tự đồng bộ giữa các thiết bị. Để đưa thay đổi giao diện vào mã nguồn, chọn **Đồng bộ Git**, sao chép dữ liệu đã xuất hoặc tải file, rồi cập nhật `data/courses.js`.

Sau khi cập nhật mã nguồn:

```bash
git add data/courses.js
git commit -m "Cập nhật dữ liệu học phần"
git push
```

## Nộp bài lên Google Drive

Tính năng nộp bài dùng Google Identity Services và Google Drive API với scope `drive.file`. Mỗi task lưu một file ID và link trong LocalStorage của trình duyệt; tải lại bài cho cùng task sẽ cập nhật file đã nộp trước đó. Tệp mới được tạo riêng tư trong Drive của tài khoản đã chọn và không tự động chia sẻ với giảng viên. Metadata liên kết không đồng bộ sang trình duyệt/thiết bị khác.

### Cấu hình Google OAuth

1. Trong Google Cloud Console, tạo/chọn project và bật **Google Drive API**.
2. Cấu hình OAuth consent screen. Nếu ứng dụng ở chế độ Testing, thêm tài khoản Google sẽ dùng để nộp bài vào danh sách test users.
3. Tạo OAuth Client ID loại **Web application**. Thêm origin đang chạy vào **Authorized JavaScript origins**, ví dụ `http://localhost:8000` và `https://<username>.github.io`. Chỉ điền origin, không thêm đường dẫn trang.
4. Dán Client ID vào thuộc tính `content` của thẻ `meta[name="google-oauth-client-id"]` trong `index.html`.
5. Chạy trang qua HTTP/HTTPS, không mở trực tiếp bằng `file://`. Có thể chạy `python -m http.server 8000` từ thư mục dự án rồi truy cập `http://localhost:8000`.

Client ID không phải bí mật và có thể nằm trong frontend; không đưa OAuth client secret vào repository. Khi tải bài, trình duyệt xin scope `drive.file`, chỉ cho phép ứng dụng truy cập các tệp do ứng dụng tạo/chọn, không phải toàn bộ Drive. Người nộp cần tự chia sẻ file từ Google Drive nếu muốn giảng viên truy cập.

## Triển khai GitHub Pages

Workflow `.github/workflows/deploy.yml` triển khai trang khi có push lên nhánh `main` hoặc `master`, và hỗ trợ chạy thủ công.

1. Đẩy mã nguồn lên repository GitHub.
2. Trong repository, mở **Settings → Pages** và chọn **GitHub Actions** làm nguồn triển khai.
3. Push lên `main`/`master` hoặc chạy workflow **Deploy to GitHub Pages** trong tab **Actions**.
4. Mở URL Pages được hiển thị trong workflow sau khi deploy thành công.
