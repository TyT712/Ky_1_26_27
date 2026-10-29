# Academic Knowledge & Study System
### Hệ thống Quản lý Học tập & Trợ lý Học thuật Thông minh (Antigravity Agent)

Hệ thống quản lý tri thức và trợ lý học thuật thông minh, lấy dữ liệu cốt lõi từ **tập hợp giáo trình PDF chính quy của các môn học** kết hợp với **các bản ghi chú/tóm tắt học tập xuất từ Google NotebookLM**. 

Hệ thống được thiết kế theo kiến trúc **Dual-Layer RAG** (Retrieval-Augmented Generation hai tầng), đảm bảo nguyên tắc **Strict Grounding** (100% căn cứ giáo trình, không bịa đặt/hallucination) nhằm phục vụ sinh viên ôn tập thi cử, làm bài tập và nắm vững đề cương môn học.

---

## 1. Cấu Trúc Dự Án (Project Structure)

```text
semester-hub/
├── .antigravity/                 # Cấu hình Agent & Context của IDE
│   ├── context.md                # Mô tả bối cảnh dự án và quy tắc hoạt động học thuật
│   ├── skills_registry.json      # Định nghĩa các Agent Skills (Schema & Capabilities)
│   └── skills/                   # Tài liệu hướng dẫn chi tiết các kỹ năng Agent
│       ├── course_ui_adaptation.md
│       └── lms_chapter_pack_generator.md
├── .agents/skills/               # Bản đăng ký Agent Skills tương thích Antigravity
│   └── course-ui-adaptation/SKILL.md
├── data/
│   ├── raw_pdfs/                 # Chứa file PDF giáo trình gốc (phân theo thư mục từng môn)
│   ├── notebook_exports/         # Chứa các file .md xuất ra từ Google NotebookLM của người dùng
│   └── parsed_markdown/          # Chứa nội dung giáo trình đã được bóc tách từ PDF sang Markdown
├── docs/                         # Static SPA LMS Web Portal (Sẵn sàng cho GitHub Pages)
│   ├── index.html                # Modern Academic Bento Layout & Responsive Frame
│   ├── .nojekyll                 # Đảm bảo GitHub Pages phục vụ file tĩnh nguyên bản
│   ├── assets/
│   │   ├── css/style.css         # Modern Bento tokens, Glassmorphism & Keyframe Animations
│   │   └── js/app.js             # Sequential Quiz State Machine & SPA Router
│   └── data/
│       ├── courses_manifest.json # Danh mục môn học, chương & cấu hình UI profile
│       └── [course_id]/          # Dữ liệu tách biệt: {chapter_id}_theory.md & {chapter_id}_exercises.json
├── scripts/
│   ├── build_lms_data.py         # Pipeline nạp & đồng bộ ngân hàng câu hỏi
│   └── verify_lms_integrity.py   # Script kiểm định tự động tính toàn vẹn 100%
├── src/
│   ├── skills/                   # Mã nguồn thực thi của các Agent Skills
│   │   ├── __init__.py
│   │   ├── pdf_ingestor.py       # Bóc tách PDF sang Markdown giữ nguyên cấu trúc
│   │   ├── knowledge_retriever.py# Tìm kiếm ngữ nghĩa / từ khóa trong kho giáo trình
│   │   └── study_assistant.py    # Trợ lý sinh câu hỏi & giải bài tập bám sát tài liệu
│   └── utils/
│       ├── __init__.py
│       ├── text_processing.py    # Chuẩn hóa văn bản, trích xuất đề mục & chunking
│       └── gemini_client.py      # Kết nối Gemini API
├── requirements.txt              # Thư viện phụ thuộc
└── README.md
```

---

## 2. Điểm Nhấn Giao Diện: Modern Bento UI & Sequential Quiz Engine

Semester Hub LMS được xây dựng theo phong cách **Modern Academic Bento & Glassmorphism**, tối ưu hóa trải nghiệm tự học và thi thử cá nhân hóa cho sinh viên đại học:

### 2.1. Cổng Thông Tin Bento & Nhận Diện Đa Môn Học
- **Bento Hero & Thống Kê Học Kỳ:** Hiển thị 3 chỉ số tổng quan (Số chương đã hoàn thành trên toàn bộ 28 chương, Tổng số câu trắc nghiệm đã làm đúng, Điểm trung bình hệ 10).
- **Học tiếp gần nhất (1-Click Resume):** Tự động phát hiện và hiển thị lối tắt vào ngay chương bạn đang học dở qua `localStorage`.
- **Dynamic Course Color Palette:** Mỗi môn học mang một tông màu nhận diện và biểu tượng riêng:
  - 🗄️ **Hệ Quản Trị CSDL:** Indigo - Cyan (`#4f46e5` / `#06b6d4`).
  - 🏛️ **Chủ Nghĩa Xã Hội Khoa Học:** Rose - Amber (`#e11d48` / `#f59e0b`).
  - ⚙️ **Công Nghệ Phần Mềm:** Violet - Emerald (`#7c3aed` / `#10b981`).
  - 🧠 **Tâm Lý Học 2:** Teal - Coral (`#0d9488` / `#f97316`).
  - 📐 **Giải Tích 1 / Cơ bản:** Blue - Indigo (`#2563eb` / `#6366f1`).

### 2.2. Cơ Chế Trắc Nghiệm Tuần Tự Từng Câu (Sequential Step-by-Step Quiz Engine)
- **Tập trung Từng Câu Hỏi (Single-Question Focused Stage):** Tại một thời điểm chỉ hiển thị duy nhất 1 câu hỏi trên sân khấu chính, loại bỏ sự xao nhãng của danh sách tràn dài.
- **Khóa Liên Hoàn (Sequential Unlock Chain):** Người học **phải hoàn thành câu hỏi hiện tại thì câu tiếp theo mới được mở khóa**. Các câu hỏi phía sau trên Question Palette bị khóa (`locked`) cho đến khi làm tuần tự tới đó.
- **Hai Chế Độ Học Tập Tương Tác:**
  - ⚡ **Luyện tập tức thì (Instant Feedback):** Kiểm tra Đúng/Sai ngay lập tức, đếm chuỗi trả lời đúng liên tiếp (**Streak Counter 🔥**), và hiển thị hộp giải thích chi tiết cùng trích dẫn giáo trình gốc.
  - 📋 **Thi thử (Exam Mode):** Làm bài liên tục tuần tự, bảo mật đáp án và chỉ chấm điểm sau khi hoàn thành toàn bộ đề.
- **Question Palette Trực Quan:** Bảng điều hướng 30 câu hiển thị trạng thái `Đang xem (current)`, `Khóa (locked)`, `Đúng (correct)`, `Sai (incorrect)`.
- **Bảng Tổng Kết Bento & Xem Lại:** Biểu đồ đồng hồ SVG Donut trực quan, xếp loại Xuất sắc / Giỏi / Khá, kỷ lục Streak và bộ lọc xem lại chỉ các câu làm sai.

### 2.3. Trải Nghiệm Học Lý Thuyết & Tự Luận Chuyên Sâu
- **Thanh Tiến Độ Đọc (Reading Progress Bar):** Hiển thị ở đỉnh trang khi người học cuộn đọc lý thuyết.
- **Mục Lục Nổi (Sticky Table of Contents - TOC):** Tự động bóc tách các đề mục H2, H3 của chương để sinh cây điều hướng nhanh.
- **Tab 3 Trả lời ngắn & Tab 4 Tự luận:** Thích ứng sư phạm theo từng nhóm môn học (`course-ui-adaptation`), hỗ trợ tự rèn luyện và đối chiếu lời giải chi tiết từng bước.

---

## 3. Các Kỹ Năng Cốt Lõi (Core Agent Skills)

### 3.1. `pdf_ingestor`
Bóc tách các file PDF giáo trình trong `data/raw_pdfs/` sang tài liệu Markdown chuẩn hóa trong `data/parsed_markdown/`:
- Giữ nguyên cấu trúc cây phân cấp đề mục (`#`, `##`, `###`).
- Giữ nguyên công thức toán/lý dạng LaTeX (`$...$` và `$$...$$`).
- Đánh dấu số trang `<!-- PAGE X -->` để phục vụ trích dẫn chính xác.

### 3.2. `knowledge_retriever`
Truy xuất thông tin đối chiếu 2 tầng (Dual-Layer Retrieval):
- **Tầng 1:** Đọc hiểu nhanh bản đồ ý niệm từ tóm tắt của NotebookLM (`data/notebook_exports/`).
- **Tầng 2:** Tra cứu chuyên sâu chi tiết định lý, công thức, số trang trong giáo trình gốc (`data/parsed_markdown/`).

### 3.3. `study_assistant`
Trợ lý học thuật giúp ôn thi và làm bài tập bám sát 100% đề cương:
- **Giải bài tập (`solve`):** Giải từng bước chuẩn mực 4 bước, trích dẫn định lý giáo trình.
- **Tạo câu hỏi trắc nghiệm (`quiz`):** Sinh đề ôn tập có đáp án và giải thích chi tiết.
- **Giải thích khái niệm (`explain`):** Giảng giải trực quan lý thuyết khó.

---

## 4. Các Môn Học Đã Đưa Lên Semester Hub LMS (Active Courses)

| STT | Mã môn | Tên môn học | Số chương | Trắc nghiệm | Trả lời ngắn | Tự luận | Tinh hoa lý thuyết | Bảng màu nhận diện |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | **HQTCSDL** | Hệ Quản Trị Cơ Sở Dữ Liệu | 11 chương | 331 câu | 88 câu | 44 bài | Tích hợp vào 11 chương | Indigo - Cyan 🗄️ |
| 2 | **CNXHKH** | Chủ Nghĩa Xã Hội Khoa Học | 7 chương | 210 câu | 56 câu | 28 bài | Tích hợp vào 7 chương | Rose - Amber 🏛️ |
| 3 | **CNPM** | Công Nghệ Phần Mềm | 5 chương | 150 câu | 40 câu | 20 bài | Tích hợp vào 5 chương | Violet - Emerald ⚙️ |
| 4 | **TLH2** | Tâm Lý Học 2 (Lứa Tuổi & Sư Phạm) | 5 chương | 150 câu | 40 câu | 20 bài | Tích hợp vào 5 chương | Teal - Coral 🧠 |
| **Tổng cộng** | | | **28 chương** | **841 câu** | **224 câu** | **112 bài** | **Toàn diện 100%** | **Chuẩn hóa Modern Bento** |

---

## 5. Kiểm Định Chất Lượng & Tính Toàn Vẹn (Integrity Verification)

Hệ thống tích hợp bộ script kiểm thử tự động toàn diện:
```bash
python scripts/verify_lms_integrity.py
```
Bộ script tự động kiểm tra:
1. Đăng ký và hợp lệ của Agent Skills trong `.antigravity/skills_registry.json`.
2. Toàn bộ 28 chương học: Đủ tối thiểu 30 câu trắc nghiệm (chuẩn 4 đáp án A/B/C/D), 8 câu trả lời ngắn, 4 bài tự luận và file lý thuyết có nội dung.
3. Khởi tạo Static HTTP Server kiểm tra HTTP 200 cho `index.html`, `style.css`, `app.js`, `courses_manifest.json` và các file bài tập.
4. Tối ưu repository và loại trừ file dung lượng lớn khỏi git.

---

## 6. Cài Đặt Môi Trường & Triển Khai (Setup & Deployment)

1. **Cài đặt thư viện Python:**
```bash
pip install -r requirements.txt
```

2. **Chạy kiểm định toàn vẹn:**
```bash
python scripts/verify_lms_integrity.py
```

3. **Chạy máy chủ tĩnh cục bộ để xem giao diện:**
```bash
cd docs
python -m http.server 8000
# Mở trình duyệt tại: http://localhost:8000
```

4. **Triển khai GitHub Pages:**
Toàn bộ mã nguồn giao diện nằm trong thư mục `docs/`. Khi kích hoạt GitHub Pages với nguồn thư mục `/docs` trên nhánh `main`, hệ thống sẽ sẵn sàng phục vụ sinh viên trực tiếp trên internet mà không cần bất kỳ máy chủ backend nào.
