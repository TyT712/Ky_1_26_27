# PROJECT CONTEXT & AGENT OPERATING PRINCIPLES
## Academic Knowledge & Study System (Hệ thống Quản lý Học tập & Trợ lý Học thuật)

---

## 1. TỔNG QUAN HỆ THỐNG (SYSTEM OVERVIEW)
Hệ thống Quản lý Học tập & Trợ lý Học thuật Thông minh là nền tảng quản trị tri thức và hỗ trợ học tập cá nhân hóa được hỗ trợ bởi Antigravity Agent.
Hệ thống giải quyết bài toán cốt lõi của sinh viên/học viên:
- Khối lượng giáo trình PDF đồ sộ, khó tra cứu nhanh ngữ nghĩa và công thức.
- Tản mát tài liệu giữa giáo trình gốc chính thức và các bản ghi chú/tóm tắt học tập cá nhân (được kết xuất từ Google NotebookLM).
- Nhu cầu ôn luyện thi cử, giải bài tập bám sát 100% đề cương và chuẩn mực học thuật của nhà trường, tránh hiện tượng ảo giác (hallucination) thường gặp của các LLM thông thường.

---

## 2. NGUỒN DỮ LIỆU CỐT LÕI (CORE DATA SOURCES)
Hệ thống tổ chức dữ liệu theo kiến trúc hai tầng tri thức (Dual-Layer Knowledge Store):

1. **Lớp Giáo trình Gốc (Primary Academic Source - `data/raw_pdfs/` & `data/parsed_markdown/`):**
   - Tập hợp giáo trình PDF định dạng chuẩn của từng môn học (được tổ chức theo thư mục môn học, ví dụ `data/raw_pdfs/cs101_cau_truc_du_lieu/`).
   - Được tiền xử lý bởi `pdf_ingestor` thành Markdown chuẩn, bảo tồn nguyên vẹn cấu trúc mục lục (H1, H2, H3), bảng biểu, block code và công thức toán dạng LaTeX (`$...$` hoặc `$$...$$`).

2. **Lớp Tóm tắt & Ghi chú Học tập (Synthesized Knowledge - `data/notebook_exports/`):**
   - Các bản xuất Markdown trực tiếp từ Google NotebookLM.
   - Chứa các ý niệm tóm tắt cốt lõi (key takeaways), mindmaps, câu hỏi trọng tâm của từng chủ đề.
   - Đóng vai trò là chỉ mục ngữ nghĩa mức cao (high-level semantic index) giúp định vị nhanh chương mục cần tra cứu sâu.

---

## 3. QUY TẮC HOẠT ĐỘNG CỦA AGENT (AGENT OPERATING RULES)

### 3.1. Nguyên tắc Khách quan & Căn cứ Học thuật (Strict Grounding & Zero Hallucination)
- **Bắt buộc trích dẫn nguồn:** Mọi câu trả lời, lời giải bài tập hay giải thích lý thuyết đều phải chỉ rõ căn cứ: `[Tên môn học] > [Tên giáo trình / File] > [Chương / Mục]` và kèm số trang (nếu có metadata trang).
- **Phân định rõ ranh giới tri thức:** Nếu tài liệu trong kho giáo trình không cung cấp đủ thông tin để trả lời hoặc giải quyết câu hỏi, Agent **bắt buộc phải thông báo minh bạch**: *"Tài liệu giáo trình hiện có chưa đề cập đến nội dung này"* trước khi đề xuất kiến thức bổ trợ bên ngoài (và phải gắn nhãn rõ `[Kiến thức tham khảo bổ sung]`).
- **Không tự suy diễn công thức/định nghĩa:** Sử dụng chính xác định nghĩa, ký hiệu và quy ước toán học/khoa học được ghi trong giáo trình đã nạp.

### 3.2. Chuẩn hóa Định dạng Markdown & Công thức
- **Toán học & Khoa học:** Dùng chuẩn LaTeX `$inline$` và `$$block$$`.
- **Mã nguồn:** Luôn chỉ định ngôn ngữ trong code block (ví dụ ```python, ```cpp, ```sql).
- **Hệ thống đề mục:** Tuân thủ phân cấp logic nghiêm ngặt (không nhảy cóc từ H1 xuống H3).

### 3.3. Quy trình Xử lý Chuỗi Tác vụ (Task Pipeline Flow)
1. **Ingest:** Tiếp nhận PDF mới -> Bóc tách Markdown giữ nguyên tiêu đề và đoạn văn -> Lưu vào `data/parsed_markdown/`.
2. **Retrieve:** Khi nhận câu hỏi ôn tập / bài tập -> Tìm kiếm trên cả 2 nguồn (tóm tắt NotebookLM trước để nắm định hướng khái niệm, sau đó truy vấn sâu vào Markdown giáo trình gốc).
3. **Assist:** Tổng hợp lời giải, tạo flashcard, câu hỏi trắc nghiệm hoặc đề thi thử có đáp án chi tiết và chỉ dẫn học lại phần lý thuyết liên quan.

---

## 4. BỘ KỸ NĂNG CỐT LÕI (CORE AGENT SKILLS)
1. **`pdf_ingestor`:** Bóc tách PDF sang Markdown cấu trúc cao, nhận diện tiêu đề, trích xuất text rõ ràng.
2. **`knowledge_retriever`:** Truy xuất đa tầng (Hybrid Search: Full-text & Semantic Context) đối chiếu chéo giữa giáo trình và ghi chú NotebookLM.
3. **`study_assistant`:** Sinh bài tập tự luyện, flashcards, giải bài tập từng bước (step-by-step) bám sát tài liệu.
4. **`chapter_study_pack_generator`:** *(đã được thay thế)* Đóng gói chương thành một file Markdown đơn khối cho Docsify.
5. **`lms_chapter_pack_generator`:** Biến chương giáo trình thành gói dữ liệu tách biệt `{chapter_id}_theory.md` + `{chapter_id}_exercises.json` (30 trắc nghiệm Easy/Medium/Hard, 8 trả lời ngắn, 4 tự luận) cho Static SPA LMS; đặc tả tại `.antigravity/skills/lms_chapter_pack_generator.md`.

---

## 5. KIẾN TRÚC LMS TĨNH (STATIC SPA LMS) - GitHub Pages
- **Frontend:** `docs/index.html`, `docs/assets/css/style.css`, `docs/assets/js/app.js` (HTML5 + TailwindCSS CDN + Vanilla JS + Marked.js + KaTeX + Highlight.js + Mermaid), điều hướng bằng URL hash.
- **Luồng:** `#/` Cổng môn học -> `#/course/{id}` Trang môn học -> `#/course/{id}/chapter/{chapter_id}` Không gian chương (4 tab: Lý thuyết, Trắc nghiệm 30 câu, Trả lời ngắn, Tự luận) -> Kết quả & Xem lại.
- **Quy tắc chấm điểm theo lô:** không hiển thị đúng/sai khi chọn đáp án; chỉ chấm và giải thích sau khi người học bấm "Nộp bài & Chấm điểm".
- **Dữ liệu:** `docs/data/courses_manifest.json` và `docs/data/{subject}/{chapter_id}_{theory.md|exercises.json}`; chuyên đề tổng hợp tại `docs/data/{subject}/topics/`.
- **Pipeline sinh dữ liệu:** `scripts/extract_legacy_packs.py` -> `scripts/chapter_data/*.py` -> `scripts/build_lms_data.py` -> `scripts/verify_lms_integrity.py` (phải PASS 100%).
- **Tiến độ người học:** lưu trong `localStorage` (khóa `semesterhub.progress.v1`).

