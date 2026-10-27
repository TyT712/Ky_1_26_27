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
│   └── skills_registry.json      # Định nghĩa các Agent Skills (Schema & Capabilities)
├── data/
│   ├── raw_pdfs/                 # Chứa file PDF giáo trình gốc (phân theo thư mục từng môn)
│   ├── notebook_exports/         # Chứa các file .md xuất ra từ Google NotebookLM của người dùng
│   └── parsed_markdown/          # Chứa nội dung giáo trình đã được bóc tách từ PDF sang Markdown
├── src/
│   ├── skills/                   # Mã nguồn thực thi của các Agent Skills
│   │   ├── __init__.py
│   │   ├── pdf_ingestor.py       # Skill bóc tách PDF sang Markdown giữ nguyên cấu trúc đề mục
│   │   ├── knowledge_retriever.py# Skill tìm kiếm ngữ nghĩa / từ khóa trong kho giáo trình
│   │   └── study_assistant.py    # Skill tổng hợp kiến thức, tạo câu hỏi ôn tập, giải bài tập
│   └── utils/                    # Các hàm bổ trợ
│       ├── __init__.py
│       ├── text_processing.py    # Chuẩn hóa văn bản, trích xuất đề mục & chunking
│       └── gemini_client.py      # Kết nối Gemini API (xử lý text & PDF multimodal)
├── docs/
│   └── architecture.md           # Tài liệu kiến trúc hệ thống và luồng dữ liệu (Mermaid.js)
├── requirements.txt              # Thư viện phụ thuộc
└── README.md
```

---

## 2. Các Kỹ Năng Cốt Lõi (Core Agent Skills)

### 2.1. `pdf_ingestor`
Bóc tách các file PDF giáo trình trong `data/raw_pdfs/` sang tài liệu Markdown chuẩn hóa trong `data/parsed_markdown/`:
- Giữ nguyên cấu trúc cây phân cấp đề mục (`#`, `##`, `###`).
- Giữ nguyên công thức toán/lý dạng LaTeX (`$...$` và `$$...$$`).
- Đánh dấu số trang `<!-- PAGE X -->` để phục vụ trích dẫn chính xác.
- Hỗ trợ chế độ AI Multimodal (sử dụng Gemini API để nhận diện bảng biểu & sơ đồ phức tạp) và chế độ cục bộ (dùng thư viện `pypdf`).

**Cách sử dụng:**
```bash
# Xử lý 1 file PDF cụ thể
python src/skills/pdf_ingestor.py --file data/raw_pdfs/giai_tich_1/giao_trinh.pdf --subject giai_tich_1

# Xử lý tự động toàn bộ thư mục PDF
python src/skills/pdf_ingestor.py --batch
```

### 2.2. `knowledge_retriever`
Truy xuất thông tin đối chiếu 2 tầng (Dual-Layer Retrieval):
- **Tầng 1:** Đọc hiểu nhanh bản đồ ý niệm từ tóm tắt của NotebookLM (`data/notebook_exports/`).
- **Tầng 2:** Tra cứu chuyên sâu chi tiết định lý, công thức, số trang trong giáo trình gốc (`data/parsed_markdown/`).

**Cách sử dụng:**
```bash
python src/skills/knowledge_retriever.py "Định lý giá trị trung bình Lagrange" --subject giai_tich_1
```

### 2.3. `study_assistant`
Trợ lý học thuật giúp ôn thi và làm bài tập bám sát 100% đề cương:
- **Giải bài tập (`solve`):** Giải từng bước chuẩn mực 4 bước, trích dẫn định lý giáo trình.
- **Tạo câu hỏi trắc nghiệm (`quiz`):** Sinh đề ôn tập có đáp án và giải thích chi tiết.
- **Giải thích khái niệm (`explain`):** Giảng giải trực quan lý thuyết khó.

**Cách sử dụng:**
```bash
# Giải bài tập
python src/skills/study_assistant.py solve "Tính đạo hàm hàm số f(x) = x^2 * sin(x)" --subject giai_tich_1

# Sinh bộ câu hỏi ôn tập
python src/skills/study_assistant.py quiz "Đạo hàm và Vi phân" --subject giai_tich_1 -n 5

# Giải thích khái niệm
python src/skills/study_assistant.py explain "Danh sách liên kết đơn vs mảng động" --subject cau_truc_du_lieu
```

---

## 3. Cài Đặt Môi Trường (Installation & Setup)

1. **Cài đặt thư viện Python:**
```bash
pip install -r requirements.txt
```

2. **Cấu hình biến môi trường (Tùy chọn cho tính năng LLM nâng cao):**
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your_gemini_api_key_here"

# Linux / macOS
export GEMINI_API_KEY="your_gemini_api_key_here"
```

---

## 4. Quy Tắc Hoạt Động Của Agent (Strict Grounding)
Mọi phản hồi học thuật từ Agent tuân thủ nghiêm ngặt quy tắc trong [.antigravity/context.md](file:///.antigravity/context.md):
1. **Không bịa đặt (Zero Hallucination):** Chỉ giải thích dựa trên nội dung có trong giáo trình đã nạp.
2. **Minh bạch trích dẫn:** Mọi câu trả lời đều có nhãn `[Môn học | Tài liệu | Mục | Trang]`.
3. **Phân tách tri thức:** Nếu giáo trình chưa đề cập, Agent sẽ thông báo rõ ràng trước khi gợi ý kiến thức tham khảo bên ngoài.

---

## 5. Các Môn Học Đã Đưa Lên Semester Hub LMS (Active Courses)

| STT | Mã môn | Tên môn học | Số chương | Trắc nghiệm | Trả lời ngắn | Tự luận | Chuyên đề NotebookLM |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | **HQTCSDL** | Hệ Quản Trị Cơ Sở Dữ Liệu | 11 chương | 331 câu | 88 câu | 44 bài | 10 chuyên đề |
| 2 | **CNXHKH** | Chủ Nghĩa Xã Hội Khoa Học | 7 chương | 210 câu | 56 câu | 28 bài | 7 chuyên đề |
| 3 | **CNPM** | Công Nghệ Phần Mềm | 5 chương | 150 câu | 40 câu | 20 bài | 5 chuyên đề |
| 4 | **TLH2** | Tâm Lý Học 2 (Lứa Tuổi & Sư Phạm) | 5 chương | 150 câu | 40 câu | 20 bài | 5 chuyên đề |
| **Tổng cộng** | | | **28 chương** | **841 câu** | **224 câu** | **112 bài** | **27 chuyên đề** |

LMS web portal được triển khai sẵn sàng tại thư mục [docs/](file:///c:/Users/dtht0/OneDrive/Desktop/semester-hub/docs) và hỗ trợ chạy static GitHub Pages.
