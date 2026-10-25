---
name: course-ui-adaptation
description: Quy chuẩn và hướng dẫn thích ứng giao diện học tập (Pedagogical UI Adaptation & Content Localization) cho từng môn học trong Semester Hub LMS. Dùng khi thêm môn học mới, điều chỉnh văn phong giới thiệu các tab (Trắc nghiệm, Trả lời ngắn, Tự luận) hoặc cấu hình nhãn nhập liệu, font chữ và điều hướng theo đặc thù môn học (Kỹ thuật/CSDL, Lý luận chính trị/Khoa học xã hội, Toán học/KHTN).
---

# SKILL: COURSE UI ADAPTATION & PEDAGOGICAL LOCALIZATION

## 1. Mục tiêu & Bối cảnh Vấn đề (Core Purpose)
Semester Hub LMS là hệ thống học tập tĩnh (Static SPA LMS) đa môn học phục vụ sinh viên đại học. Trước đây, một số thành phần giao diện bị gắn cứng văn phong và khái niệm của môn **Hệ quản trị Cơ sở Dữ liệu** (ví dụ: *"Tự gõ biểu thức đại số quan hệ, câu lệnh SQL, hoặc tính toán bao đóng..."*, font monospace, badge *"Tự luận & Thiết kế"*). Khi đưa các môn học thuộc khối khác vào (như **Chủ nghĩa Xã hội Khoa học**, Triết học Mác - Lênin, Tư tưởng Hồ Chí Minh, Toán cao cấp...), giao diện cũ gây mâu thuẫn ngữ cảnh học thuật và làm giảm trải nghiệm người học.

Skill này định hình quy chuẩn thích ứng giao diện theo từng nhóm môn học thông qua cơ chế cấu hình động (**Declarative UI Profiles & Dynamic Adaptation**).

---

## 2. Ma trận Phân loại Hồ sơ Giao diện (Course UI Profiles)

| Nhóm môn học | Profile Key | Ví dụ môn | Tab 3: Trả lời ngắn (Short Answer) | Tab 4: Tự luận (Essay) | Định dạng Input |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kỹ thuật & Cơ sở dữ liệu** | `technical_database` | Hệ QTCSDL, Nhập môn CSDL, Hệ điều hành | **Tiêu đề:** Luyện tập Trả lời ngắn & Thao tác hình thức<br>**Giới thiệu:** Tự gõ biểu thức đại số quan hệ, câu lệnh SQL, hoặc tính toán bao đóng trước khi bấm "Kiểm tra & Đối chiếu"...<br>**Label:** Nhập câu trả lời / Biểu thức ĐSQH / Câu lệnh SQL của bạn: | **Badge:** Tự luận & Thiết kế<br>**Tiêu đề:** Bài Tập Tự Luận & Thiết Kế Lớn<br>**Giới thiệu:** Bài toán tổng hợp đòi hỏi tư duy thiết kế, chứng minh, tính toán nhiều bước... | `font-mono` (thuận tiện cho code, SQL, công thức hình thức) |
| **Lý luận chính trị & KHXH** | `political_theory` | Chủ nghĩa xã hội khoa học, Triết học Mác-Lênin, Lịch sử Đảng, Kinh tế chính trị | **Tiêu đề:** Luyện tập Trả lời ngắn & Khái niệm Cốt lõi<br>**Giới thiệu:** Tự suy ngẫm, tóm tắt định nghĩa, tiền đề hoặc luận điểm chính trước khi bấm "Kiểm tra & Đối chiếu"...<br>**Label:** Nhập câu trả lời / Tóm tắt luận điểm của bạn: | **Badge:** Tự luận & Phân tích lý luận<br>**Tiêu đề:** Bài Tập Tự Luận & Phân Tích Chuyên Sâu<br>**Giới thiệu:** Đề bài tự luận tổng hợp yêu cầu phân tích quy luật khách quan, chứng minh luận điểm khoa học và liên hệ thực tiễn... | Font chữ chuẩn (sans/prose, tối ưu cho việc soạn thảo đoạn văn phân tích) |
| **Toán học & Khoa học cơ bản** | `mathematics_natural_science` | Giải tích, Đại số tuyến tính, Xác suất thống kê, Vật lý đại cương | **Tiêu đề:** Luyện tập Trả lời ngắn & Tính toán Số học<br>**Giới thiệu:** Tự biến đổi đại số, tính đạo hàm, tích phân hoặc xác suất trước khi bấm "Kiểm tra & Đối chiếu"...<br>**Label:** Nhập kết quả tính toán / Biểu thức toán của bạn: | **Badge:** Tự luận & Chứng minh<br>**Tiêu đề:** Bài Tập Tự Luận & Chứng Minh Toán Học<br>**Giới thiệu:** Bài toán giải tích/đại số đòi hỏi các bước biến đổi chặt chẽ, định lý và điều kiện hội tụ... | `font-mono` hoặc LaTeX input |
| **Học thuật chung (Mặc định)** | `general_academic` / `default` | Bất kỳ môn học mới nào chưa có profile riêng | **Tiêu đề:** Luyện tập Trả lời ngắn & Tự kiểm tra<br>**Giới thiệu:** Tự ghi câu trả lời hoặc tóm tắt ý chính của bạn trước khi bấm "Kiểm tra & Đối chiếu" để so sánh với đáp án chuẩn.<br>**Label:** Nhập câu trả lời của bạn: | **Badge:** Tự luận & Vận dụng<br>**Tiêu đề:** Bài Tập Tự Luận & Giải Quyết Vấn Đề<br>**Giới thiệu:** Bài tập tổng hợp đòi hỏi phân tích, chứng minh và giải quyết vấn đề nhiều bước bám sát nội dung giáo trình. | Font chữ tiêu chuẩn |

---

## 3. Kiến trúc Cài đặt trong Hệ thống

### 3.1. Khai báo trong `docs/data/courses_manifest.json`
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
Hoặc tùy biến sâu (nếu môn học có yêu cầu đặc biệt):
```json
{
  "id": "mon_dac_thu",
  "title": "Môn học đặc thù",
  "ui_profile": "general_academic",
  "tabs_config": {
    "short_answer": {
      "title": "Tiêu đề tùy chỉnh cho Tab Trả lời ngắn",
      "intro": "Lời dẫn nhập riêng biệt...",
      "label": "Nhãn ô nhập...",
      "placeholder": "Gợi ý placeholder...",
      "isMono": false
    },
    "essay": {
      "badge": "Nhãn huy hiệu",
      "title": "Tiêu đề tự luận",
      "intro": "Mô tả tự luận..."
    }
  }
}
```

### 3.2. Động hóa trong `docs/assets/js/app.js`
Ứng dụng sử dụng hàm phân giải `getCourseUIConfig(state.currentCourse)` với thứ tự ưu tiên:
1. `course.tabs_config` (nếu khai báo trực tiếp trong manifest).
2. `COURSE_PROFILES[course.ui_profile]` (nếu khai báo profile).
3. `COURSE_PROFILES[course.id]` (fallback theo mã môn học).
4. `COURSE_PROFILES.default` (fallback an toàn cho môn mới).

### 3.3. Điều hướng & Nhãn danh mục (Chapter Dropdown & Navigation)
- Đối với môn có phân chia Quyển (như Hệ QTCSDL: `q1`, `q2`), nhãn dropdown hiển thị: `Quyển 1/2 - Chương X: [Tên chương]`.
- Đối với môn giáo trình đơn khối không chia quyển (như CNXHKH, Triết học...), nhãn dropdown hiển thị trực tiếp: `Chương X: [Tên chương]` hoặc `full_title`, tuyệt đối không gắn nhầm `Quyển 2` do suy diễn mã chương.
- Tab Trắc nghiệm (Batch Quiz) hiển thị số câu thực tế `${totalCount}` thay vì gắn cứng `30 câu`.

---

## 4. Checklist Thực hiện khi Thêm hoặc Hiệu chỉnh Môn học Mới
Khi tích hợp một môn học mới vào Semester Hub:
1. **Xác định nhóm ngành:** Chọn `ui_profile` phù hợp (`technical_database`, `political_theory`, `mathematics_natural_science` hoặc `general_academic`).
2. **Khai báo trong Manifest:** Thêm thuộc tính `"ui_profile": "<profile_key>"` vào đối tượng môn học trong `docs/data/courses_manifest.json`.
3. **Kiểm tra Tab 3 (Trả lời ngắn):**
   - Tiêu đề card dẫn nhập có đúng tính chất môn học không?
   - Nhãn `label` và placeholder của ô textarea có tự nhiên, phù hợp với thao tác sinh viên cần làm không?
   - Ô textarea có cần `font-mono` (cho code/SQL/toán) hay font thường (cho bài nghị luận, lý luận)?
4. **Kiểm tra Tab 4 (Tự luận):**
   - Huy hiệu `badge` (ví dụ: *Tự luận & Thiết kế* vs *Tự luận & Phân tích lý luận*).
   - Mô tả hướng dẫn có phản ánh đúng yêu cầu phương pháp luận của môn không?
5. **Kiểm tra Dropdown chuyển chương:** Xác nhận không có tiền tố "Quyển" thừa đối với giáo trình không chia quyển.
6. **Chạy kiểm thử:** Chạy `python scripts/verify_lms_integrity.py` để đảm bảo hệ thống vượt qua 100% các tiêu chí toàn vẹn.
