# SKILL: COURSE UI ADAPTATION & PEDAGOGICAL LOCALIZATION
## Thích ứng Giao diện & Ngữ cảnh Sư phạm Đa môn học cho Semester Hub LMS
> Phiên bản 2.0.0 - Chuẩn hóa giao diện Modern Academic Bento, Dynamic Course Palette & Sequential Step-by-Step Quiz Engine

---

## 1. Mục tiêu & Bối cảnh Vấn đề (Core Purpose)
Semester Hub LMS là hệ thống học tập tĩnh (Static SPA LMS) đa môn học phục vụ sinh viên đại học. Trước đây, một số thành phần giao diện bị gắn cứng văn phong và khái niệm của môn **Hệ quản trị Cơ sở Dữ liệu** (ví dụ: *"Tự gõ biểu thức đại số quan hệ, câu lệnh SQL, hoặc tính toán bao đóng..."*, font monospace, badge *"Tự luận & Thiết kế"*). Khi đưa các môn học thuộc khối khác vào (như **Chủ nghĩa Xã hội Khoa học**, **Công nghệ Phần mềm**, **Tâm lý học 2**, Toán cao cấp...), giao diện cũ gây mâu thuẫn ngữ cảnh học thuật và làm giảm trải nghiệm người học.

Skill này định hình quy chuẩn thích ứng giao diện theo từng nhóm môn học thông qua cơ chế cấu hình động (**Declarative UI Profiles & Dynamic Adaptation**) trên cả 3 trụ cột:
1. **Bảng màu nhận diện & Biểu tượng đặc trưng (Visual Theme & Brand Identity)**.
2. **Cơ chế Trắc nghiệm Tuần tự Từng câu (Sequential Step-by-Step Quiz Engine)**: Giao diện tập trung 1 câu hỏi, Question Palette khóa liên hoàn và Streak khích lệ học tập.
3. **Văn phong Sư phạm & Tương tác từng Tab** (Lý thuyết có Sticky TOC, Trả lời ngắn có kiểm tra đáp án, Tự luận phân tích nhiều bước).

---

## 2. Ma trận Phân loại Hồ sơ Giao diện (Course UI Profiles)

| Nhóm môn học | Profile Key | Bảng màu & Icon | Tab 3: Trả lời ngắn (Short Answer) | Tab 4: Tự luận (Essay) | Kiểu Input |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kỹ thuật & Cơ sở dữ liệu** | `technical_database` / `he_qtcsdl` | Indigo - Cyan (`#4f46e5` / `#06b6d4`)<br>Icon: `🗄️` | **Tiêu đề:** Luyện tập Trả lời ngắn & Thao tác hình thức<br>**Giới thiệu:** Tự gõ biểu thức đại số quan hệ, câu lệnh SQL, hoặc tính toán bao đóng trước khi bấm "Kiểm tra & Đối chiếu"...<br>**Label:** Nhập câu trả lời / Biểu thức ĐSQH / Câu lệnh SQL của bạn: | **Badge:** Tự luận & Thiết kế<br>**Tiêu đề:** Bài Tập Tự Luận & Thiết Kế Lớn<br>**Giới thiệu:** Bài toán tổng hợp đòi hỏi tư duy thiết kế, chứng minh, tính toán nhiều bước bám sát các thuật toán chính quy... | `font-mono` (thuận tiện cho SQL, đại số quan hệ) |
| **Lý luận chính trị & KHXH** | `political_theory` / `cnxhkh` | Rose - Amber (`#e11d48` / `#f59e0b`)<br>Icon: `🏛️` | **Tiêu đề:** Luyện tập Trả lời ngắn & Khái niệm Cốt lõi<br>**Giới thiệu:** Tự suy ngẫm, tóm tắt định nghĩa, tiền đề hoặc luận điểm chính trước khi bấm "Kiểm tra & Đối chiếu"...<br>**Label:** Nhập câu trả lời / Tóm tắt luận điểm của bạn: | **Badge:** Tự luận & Phân tích lý luận<br>**Tiêu đề:** Bài Tập Tự Luận & Phân Tích Chuyên Sâu<br>**Giới thiệu:** Đề bài tự luận tổng hợp yêu cầu phân tích quy luật khách quan, chứng minh luận điểm khoa học và liên hệ thực tiễn... | Font tiêu chuẩn (tối ưu cho đoạn văn nghị luận) |
| **Kỹ nghệ phần mềm & Hệ thống** | `software_engineering` / `cnpm` | Violet - Emerald (`#7c3aed` / `#10b981`)<br>Icon: `⚙️` | **Tiêu đề:** Luyện tập Trả lời ngắn & Kỹ thuật Phần mềm<br>**Giới thiệu:** Tự viết User Story, ca kiểm thử, lệnh Git/CI-CD hoặc phân tích kiến trúc trước khi bấm "Kiểm tra & Đối chiếu"...<br>**Label:** Nhập câu trả lời / Cú pháp / Ca kiểm thử / Lệnh của bạn: | **Badge:** Tự luận & Thiết kế Phần mềm<br>**Tiêu đề:** Bài Tập Tự Luận & Thiết Kế Kiến Trúc / Quy Trình<br>**Giới thiệu:** Bài toán tổng hợp đòi hỏi phân tích yêu cầu SRS, thiết kế kiến trúc hệ thống, hoạch định Sprint và xây dựng chiến lược kiểm thử... | `font-mono` (thuận tiện cho cú pháp & ca test) |
| **Tâm lý học & Sư phạm** | `pedagogical_psychology` / `tam_ly_hoc_2` | Teal - Coral (`#0d9488` / `#f97316`)<br>Icon: `🧠` | **Tiêu đề:** Luyện tập Trả lời ngắn & Khái niệm Tâm lý Sư phạm<br>**Giới thiệu:** Tự suy ngẫm, định nghĩa quy luật tâm lý, đặc điểm lứa tuổi hoặc xử lý tình huống sư phạm trước khi bấm "Kiểm tra & Đối chiếu"...<br>**Label:** Nhập câu trả lời / Luận điểm tâm lý sư phạm của bạn: | **Badge:** Tự luận & Ứng dụng Sư phạm<br>**Tiêu đề:** Bài Tập Tự Luận & Tình Huống Sư Phạm<br>**Giới thiệu:** Bài tập tự luận tổng hợp yêu cầu phân tích bản chất tâm lý lứa tuổi, đề xuất phương pháp giáo dục khoa học và giải quyết tình huống thực tiễn... | Font tiêu chuẩn |
| **Toán học & Khoa học cơ bản** | `mathematics_natural_science` / `giai_tich_1` | Blue - Indigo (`#2563eb` / `#6366f1`)<br>Icon: `📐` | **Tiêu đề:** Luyện tập Trả lời ngắn & Tính toán Số học<br>**Giới thiệu:** Tự biến đổi đại số, tính đạo hàm, tích phân hoặc xác suất trước khi bấm "Kiểm tra & Đối chiếu"...<br>**Label:** Nhập kết quả tính toán / Biểu thức toán của bạn: | **Badge:** Tự luận & Chứng minh<br>**Tiêu đề:** Bài Tập Tự Luận & Chứng Minh Toán Học<br>**Giới thiệu:** Bài toán giải tích/đại số đòi hỏi các bước biến đổi chặt chẽ, định lý và điều kiện hội tụ... | `font-mono` hoặc LaTeX |
| **Học thuật chung (Mặc định)** | `general_academic` / `default` | Indigo - Cyan (`#4f46e5` / `#06b6d4`)<br>Icon: `🎓` | **Tiêu đề:** Luyện tập Trả lời ngắn & Tự kiểm tra<br>**Giới thiệu:** Tự ghi câu trả lời hoặc tóm tắt ý chính của bạn trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.<br>**Label:** Nhập câu trả lời của bạn: | **Badge:** Tự luận & Vận dụng<br>**Tiêu đề:** Bài Tập Tự Luận & Giải Quyết Vấn Đề<br>**Giới thiệu:** Bài tập tổng hợp đòi hỏi phân tích, chứng minh và giải quyết vấn đề nhiều bước bám sát nội dung giáo trình. | Font tiêu chuẩn |

---

## 3. Quy chuẩn Tab 2: Cơ Chế Trắc Nghiệm Tuần Tự (Sequential Step-by-Step Quiz Engine)

### 3.1. Nguyên lý Vận hành Trắc nghiệm
1. **Single-Question Focused Stage:** Tại một thời điểm chỉ hiển thị duy nhất 1 câu hỏi trên sân khấu chính.
2. **Khóa Liên Hoàn (Sequential Unlock Chain):**
   - Người học **phải hoàn thành câu hỏi hiện tại** thì nút *"Câu tiếp theo →"* mới được kích hoạt và câu kế tiếp trong Question Palette mới được mở khóa (`unlocked`).
   - Các câu hỏi chưa tới lượt bắt buộc ở trạng thái `locked` (`disabled`, con trỏ cấm, mờ 50%).
3. **Hai Chế Độ Học Tập:**
   - **Luyện tập tức thì (`instant`):** Khi chọn đáp án, hệ thống chốt câu hỏi (`lockedQuestions[qId] = true`), hiển thị ngay trạng thái Đúng (xanh) / Sai (đỏ), mở hộp giải thích chi tiết bám sát giáo trình, và cập nhật Streak counter 🔥.
   - **Thi thử (`exam`):** Người học chọn phương án và đi tiếp tuần tự, đáp án và lời giải được bảo mật cho đến khi bấm *"Hoàn thành & Nộp bài"*.
4. **Bảng Điều Hướng (Question Palette):**
   - Cho phép người học tự do click quay lại xem lại bất kỳ câu hỏi nào trong dải `0 .. maxUnlockedIndex`.
   - Hiển thị trực quan: Đang xem (`current`), Đúng (`correct`), Sai (`incorrect`), Đã trả lời (`answered`), Chưa mở khóa (`locked`).

---

## 4. Kiến trúc Cài đặt trong Hệ thống

### 4.1. Khai báo trong `docs/data/courses_manifest.json`
Mỗi môn học có thể khai báo `ui_profile` tương ứng hoặc ghi đè chi tiết từng tab bằng `tabs_config`:
```json
{
  "id": "cnxhkh",
  "code": "CNXHKH",
  "title": "Chủ Nghĩa Xã Hội Khoa Học",
  "status": "active",
  "ui_profile": "political_theory"
}
```

### 4.2. Động hóa trong `docs/assets/js/app.js`
Ứng dụng sử dụng hàm phân giải `getCourseUIConfig(state.currentCourse)` với thứ tự ưu tiên:
1. `course.tabs_config` (nếu khai báo trực tiếp trong manifest).
2. `COURSE_PROFILES[course.ui_profile]` (nếu khai báo profile).
3. `COURSE_PROFILES[course.id]` (fallback theo mã môn học).
4. `COURSE_PROFILES.default` (fallback an toàn cho môn mới).

---

## 5. Checklist Thực hiện khi Thêm Môn học Mới
1. **Xác định nhóm ngành & Bảng màu:** Chọn `ui_profile` phù hợp (`technical_database`, `political_theory`, `software_engineering`, `pedagogical_psychology`, `mathematics_natural_science` hoặc `general_academic`).
2. **Khai báo trong Manifest:** Thêm thuộc tính `"ui_profile": "<profile_key>"` vào đối tượng môn học trong `docs/data/courses_manifest.json`.
3. **Kiểm tra Tab 1 (Lý thuyết):** Đảm bảo các tiêu đề H2, H3 chuẩn mực để hệ thống tự động sinh Mục lục nổi (Sticky TOC).
4. **Kiểm tra Tab 2 (Trắc nghiệm):** Xác nhận đủ 30 câu (hoặc số lượng chuẩn), các câu hỏi mở khóa tuần tự, giải thích hiển thị chính xác.
5. **Kiểm tra Tab 3 & 4 (Trả lời ngắn & Tự luận):** Xác nhận văn phong dẫn nhập, nhãn label và font chữ (mono vs standard) phù hợp với phương pháp luận của môn.
6. **Chạy kiểm thử:** Chạy `python scripts/verify_lms_integrity.py` để đảm bảo hệ thống vượt qua 100% các tiêu chí toàn vẹn.
