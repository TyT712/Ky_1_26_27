# SKILL: COURSE UI ADAPTATION & PEDAGOGICAL LOCALIZATION
## Thích ứng Giao diện & Ngữ cảnh Sư phạm Đa môn học cho Semester Hub LMS

> Phiên bản 1.0.0 - Chuẩn hóa giao diện tĩnh SPA LMS không bị dính chặt (hardcoded) vào bất kỳ một môn học cụ thể nào.

---

## 1. Mục tiêu & Vấn đề giải quyết
Semester Hub LMS được xây dựng để phục vụ toàn bộ các môn học đại học của sinh viên. Trong phiên bản đầu, một số chuỗi ký tự giao diện bị gắn cứng theo môn **Hệ quản trị Cơ sở Dữ liệu**:
- Lời dẫn nhập Tab 3: *"Tự gõ biểu thức đại số quan hệ, câu lệnh SQL, hoặc tính toán bao đóng trước khi bấm 'Kiểm tra & Đối chiếu'..."*
- Nhãn ô nhập Tab 3: *"Nhập câu trả lời / Biểu thức ĐSQH / Câu lệnh SQL của bạn:"*
- Huy hiệu và mô tả Tab 4: *"Tự luận & Thiết kế"*, *"bám sát các thuật toán chính quy"*
- Dropdown chọn chương: Ép buộc hiển thị *"Quyển 1"* / *"Quyển 2"*.

Khi mở rộng sang môn **Chủ nghĩa Xã hội Khoa học (CNXHKH)** và các môn lý luận/khoa học khác, việc để nguyên các câu dẫn trên làm mất tính chuẩn mực học thuật. Skill này quy định kiến trúc hồ sơ giao diện (`COURSE_PROFILES`) và quy trình tích hợp môn mới.

---

## 2. Các Hồ sơ Giao diện Chuẩn (UI Profiles)

### 2.1. `technical_database` (Dành cho Hệ QTCSDL, Nhập môn CSDL...)
- **Tab 3 Short Answer:**
  - Tiêu đề: *Luyện tập Trả lời ngắn & Thao tác hình thức*
  - Hướng dẫn: *Tự gõ biểu thức đại số quan hệ, câu lệnh SQL, hoặc tính toán bao đóng trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.*
  - Label: *Nhập câu trả lời / Biểu thức ĐSQH / Câu lệnh SQL của bạn:*
  - Placeholder: *Gõ câu trả lời, biểu thức hoặc câu lệnh của bạn vào đây để tự rèn luyện...*
  - Font: `font-mono` (monospace)
- **Tab 4 Essay:**
  - Badge: *Tự luận & Thiết kế*
  - Tiêu đề: *Bài Tập Tự Luận & Thiết Kế Lớn*
  - Hướng dẫn: *Bài toán tổng hợp đòi hỏi tư duy thiết kế, chứng minh, tính toán nhiều bước bám sát các thuật toán chính quy của giáo trình.*

### 2.2. `political_theory` (Dành cho CNXHKH, Triết học, Tư tưởng HCM, Lịch sử Đảng...)
- **Tab 3 Short Answer:**
  - Tiêu đề: *Luyện tập Trả lời ngắn & Khái niệm Cốt lõi*
  - Hướng dẫn: *Tự suy ngẫm, tóm tắt định nghĩa, tiền đề hoặc luận điểm chính trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.*
  - Label: *Nhập câu trả lời / Tóm tắt luận điểm của bạn:*
  - Placeholder: *Gõ câu trả lời, định nghĩa hoặc tóm tắt luận điểm của bạn vào đây để tự rèn luyện...*
  - Font: Font tiêu chuẩn (sans-serif, dễ đọc cho câu chữ lý luận)
- **Tab 4 Essay:**
  - Badge: *Tự luận & Phân tích lý luận*
  - Tiêu đề: *Bài Tập Tự Luận & Phân Tích Chuyên Sâu*
  - Hướng dẫn: *Đề bài tự luận tổng hợp yêu cầu phân tích quy luật khách quan, chứng minh luận điểm khoa học và liên hệ thực tiễn bám sát giáo trình chuẩn Bộ GD&ĐT.*

### 2.3. `general_academic` (Hồ sơ Dự phòng Toàn hệ thống)
Áp dụng cho mọi môn học mới khi chưa có profile tùy biến:
- **Tab 3 Short Answer:**
  - Tiêu đề: *Luyện tập Trả lời ngắn & Tự kiểm tra*
  - Hướng dẫn: *Tự ghi câu trả lời hoặc tóm tắt ý chính của bạn trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.*
  - Label: *Nhập câu trả lời của bạn:*
  - Placeholder: *Gõ câu trả lời của bạn vào đây để tự rèn luyện...*
- **Tab 4 Essay:**
  - Badge: *Tự luận & Vận dụng*
  - Tiêu đề: *Bài Tập Tự Luận & Giải Quyết Vấn Đề*
  - Hướng dẫn: *Bài tập tổng hợp đòi hỏi phân tích, chứng minh và giải quyết vấn đề nhiều bước bám sát nội dung giáo trình.*

---

## 3. Quy chuẩn Khai báo & Thực thi

1. **Tại `docs/data/courses_manifest.json`:**
   Mỗi khóa học bổ sung trường `"ui_profile"`:
   ```json
   {
     "id": "cnxhkh",
     "ui_profile": "political_theory",
     ...
   }
   ```
2. **Tại `docs/assets/js/app.js`:**
   - Dùng hàm `getCourseUIConfig(state.currentCourse)` để tự động tra cứu cấu hình theo thứ tự:
     `course.tabs_config` $\to$ `COURSE_PROFILES[course.ui_profile]` $\to$ `COURSE_PROFILES[course.id]` $\to$ `COURSE_PROFILES.default`.
   - Dropdown chọn chương phân biệt môn có nhiều quyển (`q1`, `q2`) và môn giáo trình đơn khối.
   - Thẻ ghi chú thi theo lô hiển thị đúng `${totalCount}` câu trắc nghiệm.

---

## 4. Kiểm định
Mỗi khi sửa đổi hoặc thêm môn học:
```bash
python scripts/verify_lms_integrity.py
```
Toàn bộ asset, manifest và question bank phải trả về trạng thái **PASS 100%**.
