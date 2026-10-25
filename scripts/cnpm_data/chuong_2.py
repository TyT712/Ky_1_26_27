# -*- coding: utf-8 -*-
"""Data definition for Chương 2: Quy trình phát triển phần mềm."""

CHAPTER_ID = "chuong_2"
CHAPTER_NUMBER = 2
CHAPTER_TITLE = "Chương 2: Quy trình phát triển phần mềm"
CHAPTER_SUMMARY = "Các mô hình truyền thống (Thác nước, Chữ V), triết lý linh hoạt Agile (4 giá trị, 12 nguyên tắc), khung quy trình Scrum toàn diện (vai trò, sự kiện, tạo tác), và thực hành cộng tác với Git/GitHub."

THEORY_MD = """# CHƯƠNG 2: QUY TRÌNH PHÁT TRIỂN PHẦN MỀM

## 1. Khái niệm Mô hình Quy trình Phần mềm (Software Process Model)
- Một biểu diễn trừu tượng của một quy trình phát triển phần mềm, quy định các giai đoạn, hoạt động, sản phẩm bàn giao (Deliverables) và vai trò của các thành viên.

## 2. Các Mô hình Truyền thống (Traditional Heavyweight Models)
### A. Mô hình Thác nước (Waterfall Model)
- **Đặc trưng:** Tuần tự, tuyến tính. Giai đoạn sau chỉ được phép bắt đầu khi giai đoạn trước đã hoàn thành 100% và được phê duyệt (Sign-off).
- **Ưu điểm:** Cấu trúc chặt chẽ, dễ quản lý tiến độ và chi phí theo các mốc cột mốc (Milestones).
- **Nhược điểm cốt tử:** Rất khó thay đổi yêu cầu; khách hàng chỉ nhìn thấy sản phẩm chạy được ở giai đoạn cuối cùng; rủi ro thất bại tích tụ dồn về cuối dự án.
- **Trường hợp áp dụng:** Các dự án có yêu cầu rõ ràng từ đầu, ít biến động (ví dụ: phần mềm nhúng hàng không, y tế theo tiêu chuẩn pháp lý cứng).

### B. Mô hình Chữ V (V-Model)
- **Đặc trưng:** Mở rộng từ Thác nước, nhấn mạnh mối quan hệ đối ứng 1-1 giữa mỗi giai đoạn phát triển bên nhánh trái và một cấp độ kiểm thử tương ứng bên nhánh phải.
- **Các cặp tương ứng:**
  - *Đặc tả Yêu cầu (Requirements)* $\longleftrightarrow$ *Kiểm thử Chấp nhận (Acceptance Testing)*
  - *Thiết kế Hệ thống (System Design)* $\longleftrightarrow$ *Kiểm thử Hệ thống (System Testing)*
  - *Thiết kế Kiến trúc (Architecture)* $\longleftrightarrow$ *Kiểm thử Tích hợp (Integration Testing)*
  - *Thiết kế Module/Chi tiết* $\longleftrightarrow$ *Kiểm thử Đơn vị (Unit Testing)*

```mermaid
graph TD
    subgraph Phát_triển["Nhánh Phát Triển (Verification)"]
        A["1. Yêu cầu (Requirements)"]
        B["2. Thiết kế Hệ thống"]
        C["3. Thiết kế Kiến trúc"]
        D["4. Thiết kế Module"]
        E["5. LẬP TRÌNH (CODING)"]
    end
    subgraph Kiểm_thử["Nhánh Kiểm Thử (Validation)"]
        UT["Unit Testing (Đơn vị)"]
        IT["Integration Testing (Tích hợp)"]
        ST["System Testing (Hệ thống)"]
        AT["Acceptance Testing (Chấp nhận)"]
    end
    A --> B --> C --> D --> E
    E --> UT --> IT --> ST --> AT
    A -.Đối ứng.- AT
    B -.Đối ứng.- ST
    C -.Đối ứng.- IT
    D -.Đối ứng.- UT
```

## 3. Triết lý Linh hoạt Agile (Agile Philosophy)
Ra đời năm 2001 với **Tuyên ngôn Agile (Agile Manifesto)**, tập trung vào tính thích ứng và phản hồi nhanh trước sự thay đổi.

### 4 Giá trị Cốt lõi của Agile:
1. **Cá nhân và sự tương tác** hơn là quy trình và công cụ.
2. **Phần mềm chạy tốt** hơn là tài liệu đầy đủ, đồ sộ.
3. **Cộng tác với khách hàng** hơn là đàm phán hợp đồng.
4. **Phản hồi với sự thay đổi** hơn là bám sát một kế hoạch định sẵn.

## 4. Khung Quy trình Scrum (Scrum Framework)
Scrum là khung làm việc linh hoạt phổ biến nhất hiện nay, hoạt động theo các chu kỳ lặp gọi là **Sprint** (thường kéo dài từ 1 đến 4 tuần).

```mermaid
graph LR
    PB["Product Backlog (PO quản lý)"] -->|Sprint Planning| SB["Sprint Backlog"]
    SB --> S["SPRINT (1 - 4 tuần)"]
    S --> DS["Daily Scrum (15 phút mỗi ngày)"]
    DS --> S
    S -->|Kết thúc Sprint| INC["Potentially Releasable Increment (DoD)"]
    INC --> SR["Sprint Review (Demo sản phẩm)"]
    SR --> SRetro["Sprint Retrospective (Cải tiến quy trình)"]
    SRetro -.->|Đúc kết vào Sprint kế tiếp| SB
```

### A. Ba Vai trò trong Scrum (Scrum Roles):
1. **Product Owner (PO):** Đại diện cho tiếng nói khách hàng/thị trường, chịu trách nhiệm quản lý Product Backlog, tối đa hóa giá trị sản phẩm.
2. **Scrum Master (SM):** Người phục vụ - lãnh đạo (Servant Leader), loại bỏ các trở ngại (Blockers/Impediments) cho đội ngũ, hướng dẫn áp dụng Scrum chuẩn mực.
3. **Developers (Nhóm phát triển):** Đội ngũ liên chức năng (Cross-functional), tự tổ chức (Self-organizing), trực tiếp chuyển hóa các mục tiêu thành sản phẩm tăng tiến (Increment).

### B. Bốn Sự kiện Chính trong Scrum (Scrum Events):
1. **Sprint Planning (Lập kế hoạch Sprint):** Xác định Mục tiêu Sprint (Sprint Goal) và chọn các hạng mục từ Product Backlog đưa vào Sprint Backlog.
2. **Daily Scrum (Họp Scrum hàng ngày):** Cuộc họp 15 phút của Developers để đồng bộ tiến độ: *Hôm qua tôi đã làm gì? Hôm nay tôi sẽ làm gì? Tôi đang gặp trở ngại gì?*
3. **Sprint Review (Đánh giá Sprint):** Buổi demo sản phẩm tăng tiến thực tế cho các bên liên quan (Stakeholders) để lấy phản hồi nghiệm thu.
4. **Sprint Retrospective (Cải tiến Sprint):** Đội ngũ tự nhìn nhận lại quy trình làm việc, tìm ra điểm tốt, điểm chưa tốt và hành động cải tiến cho Sprint sau.

### C. Ba Tạo tác trong Scrum (Scrum Artifacts):
1. **Product Backlog:** Danh sách các yêu cầu/tính năng mong muốn của sản phẩm, được sắp xếp theo thứ tự ưu tiên giảm dần.
2. **Sprint Backlog:** Tập hợp các User Stories được chọn cho Sprint hiện tại kèm kế hoạch phân rã công việc kỹ thuật chi tiết.
3. **Increment (Sản phẩm Tăng tiến):** Phần mềm chạy được, thỏa mãn **Định nghĩa Hoàn thành (Definition of Done - DoD)**, sẵn sàng đưa vào vận hành nếu PO muốn phát hành.

## 5. Quy trình Làm việc Cộng tác với Git/GitHub (Feature Branch Workflow)
1. **Tạo nhánh tính năng:** `git checkout -b feature/user-profile` từ nhánh `develop`.
2. **Phát triển & commit mã nguồn:** Viết code, unit tests, commit đều đặn với thông điệp rõ nghĩa.
3. **Đẩy nhánh lên GitHub:** `git push origin feature/user-profile`.
4. **Mở Pull Request (PR):** Đề xuất gộp mã vào nhánh `develop`, gắn link tới User Story/Issue, gán người thẩm duyệt (Reviewers).
5. **Code Review & Thảo luận:** Reviewers đọc code, phản hồi các điểm chưa sạch hoặc tiềm ẩn lỗi.
6. **Merge PR & Xóa nhánh:** Khi đủ phê duyệt (Approve) và vượt qua kiểm tra CI tự động, thực hiện merge vào `develop`.
"""

TOPIC_SUMMARY = """# Chuyên Đề: Các Mô Hình Quy Trình & Khung Làm Việc Scrum

## 1. Sự Dịch Chuyển từ Quy Trình Cứng Nhắc Sang Linh Hoạt
- Mô hình Thác nước (Waterfall) và Chữ V (V-Model) hoạt động dựa trên giả định rằng mọi yêu cầu có thể đóng băng từ đầu. Giả định này không còn thực tế trong thời đại số.
- Agile không phải là sự tùy tiện mà là kỷ luật cao độ trong việc chia nhỏ rủi ro thành các vòng lặp ngắn hạn có thể kiểm chứng bằng sản phẩm chạy thực tế.

## 2. Cốt Lõi Khung Quy Trình Scrum
- Tính minh bạch (Transparency), Thanh tra (Inspection), và Thích nghi (Adaptation) là 3 trụ cột của lý thuyết thực nghiệm (Empiricism) trong Scrum.
- Một Sprint thất bại nếu đội ngũ không tạo ra được Increment đạt chuẩn Definition of Done (DoD).

## 3. Thực Hành Kỹ Thuật Cộng Tác Hiện Đại
- Luồng Pull Request và Code Review trên GitHub là lá chắn chất lượng quan trọng nhất ngăn ngừa lỗi lọt vào nhánh phát triển chung.
"""

PARSED_MARKDOWN = f"""# Giáo trình Công nghệ Phần mềm - Chương 2: Quy trình phát triển phần mềm
<!-- Nguồn: TS. Trần Văn Long - Khoa Tin học, Đại học Sư phạm, Đại học Huế -->

<!-- PAGE 1 -->
## A. Mục tiêu Bài học
1. Phân biệt được ưu và nhược điểm của các mô hình phát triển phần mềm truyền thống (Thác nước, Chữ V).
2. Trình bày và giải thích được 4 giá trị cốt lõi và 12 nguyên tắc của triết lý Agile.
3. Mô tả được các vai trò, sự kiện và tạo tác (artifacts) chính trong quy trình Scrum.
4. Áp dụng được luồng làm việc cộng tác trên GitHub (`Branch` -> `Commit` -> `Push` -> `Pull Request` -> `Merge`) để phát triển tính năng trong đồ án nhóm.

<!-- PAGE 4 -->
## B. Nội dung Chi tiết

### I. Các Mô hình Quy trình Truyền thống
- **Mô hình Thác nước (Waterfall Model):**
  - Tuần tự từ Yêu cầu $\to$ Thiết kế $\to$ Lập trình $\to$ Kiểm thử $\to$ Triển khai $\to$ Bảo trì.
  - Hạn chế: Khó phản ứng khi yêu cầu thay đổi, chi phí sửa lỗi muộn cực cao, khách hàng không thấy được sản phẩm sớm.
- **Mô hình Chữ V (V-Model):**
  - Nhánh trái: Phân rã và thiết kế; Nhánh phải: Tích hợp và kiểm định.
  - Nguyên lý song hành: Mỗi pha thiết kế đều có một pha kiểm thử đối ứng tương ứng.

### II. Triết lý Phát triển Phần mềm Linh hoạt (Agile)
- Bối cảnh ra đời của Tuyên ngôn Agile (2001).
- 4 Giá trị căn bản: Cá nhân & tương tác > Quy trình & công cụ; Phần mềm chạy tốt > Tài liệu đồ sộ; Cộng tác khách hàng > Đàm phán hợp đồng; Thích ứng thay đổi > Bám sát kế hoạch.
- Khái niệm bước lặp (Iteration) và phân phối tăng tiến (Incremental Delivery).

### III. Khung Làm việc Scrum Chi tiết
- **3 Vai trò:** Product Owner (chịu trách nhiệm về giá trị sản phẩm), Scrum Master (bảo vệ quy trình và loại bỏ rào cản), Development Team (trực tiếp tạo ra sản phẩm).
- **4 Sự kiện:** Sprint Planning, Daily Scrum (15 phút), Sprint Review, Sprint Retrospective.
- **3 Tạo tác:** Product Backlog, Sprint Backlog, Increment kèm Definition of Done (DoD).
- Công cụ trực quan hóa: Bảng Kanban/Scrum Board (To Do, In Progress, In Review, Done) và Biểu đồ Burndown Chart.

### IV. Quy trình Làm việc Nhóm với GitHub
- Luồng rẽ nhánh Feature Branch.
- Thao tác tạo và thẩm định Pull Request (PR).
- Quy chuẩn xử lý xung đột gộp (Merge Conflict).
"""

MULTIPLE_CHOICE = [
    {
        "id": 1,
        "difficulty": "easy",
        "question": "Mô hình phát triển phần mềm Thác nước (Waterfall Model) mang đặc trưng cơ bản nào sau đây?",
        "options": {
            "A": "Cho phép khách hàng thay đổi yêu cầu liên tục mỗi tuần",
            "B": "Thực hiện tuần tự, tuyến tính; giai đoạn sau chỉ bắt đầu khi giai đoạn trước đã hoàn thành và được nghiệm thu",
            "C": "Không cần giai đoạn phân tích yêu cầu mà đi thẳng vào viết code",
            "D": "Không cần kiểm thử phần mềm trước khi triển khai"
        },
        "correct_answer": "B",
        "explanation": "Mô hình Thác nước là mô hình tuần tự tuyến tính kinh điển, mỗi giai đoạn kết thúc bằng một bộ tài liệu bàn giao trước khi chuyển giao sang giai đoạn tiếp theo."
    },
    {
        "id": 2,
        "difficulty": "easy",
        "question": "Trong mô hình Chữ V (V-Model), giai đoạn 'Đặc tả Yêu cầu' (Requirements Specification) tương ứng trực tiếp với cấp độ kiểm thử nào?",
        "options": {
            "A": "Kiểm thử đơn vị (Unit Testing)",
            "B": "Kiểm thử tích hợp (Integration Testing)",
            "C": "Kiểm thử chấp nhận / nghiệm thu (Acceptance Testing)",
            "D": "Kiểm thử hiệu năng (Stress Testing)"
        },
        "correct_answer": "C",
        "explanation": "Kiểm thử chấp nhận (Acceptance Testing) kiểm chứng xem hệ thống có thỏa mãn đúng các yêu cầu nghiệp vụ ban đầu của khách hàng đã đặc tả hay không."
    },
    {
        "id": 3,
        "difficulty": "easy",
        "question": "Tuyên ngôn Agile (Agile Manifesto) năm 2001 khẳng định giá trị nào được ưu tiên hơn?",
        "options": {
            "A": "Quy trình và công cụ hơn là cá nhân và sự tương tác",
            "B": "Tài liệu đầy đủ hơn là phần mềm chạy tốt",
            "C": "Phần mềm chạy tốt hơn là tài liệu toàn diện đồ sộ",
            "D": "Đàm phán hợp đồng hơn là cộng tác với khách hàng"
        },
        "correct_answer": "C",
        "explanation": "Agile coi trọng 'Phần mềm chạy tốt hơn là tài liệu toàn diện' (Working software over comprehensive documentation), ưu tiên mang lại giá trị thực tế cho người dùng."
    },
    {
        "id": 4,
        "difficulty": "easy",
        "question": "Trong khung làm việc Scrum, ai là người chịu trách nhiệm tối đa hóa giá trị của sản phẩm và quản lý Product Backlog?",
        "options": {
            "A": "Scrum Master",
            "B": "Product Owner (PO)",
            "C": "Trưởng nhóm lập trình (Lead Developer)",
            "D": "Giám đốc kỹ thuật (CTO)"
        },
        "correct_answer": "B",
        "explanation": "Product Owner là người duy nhất sở hữu và chịu trách nhiệm sắp xếp thứ tự ưu tiên của các hạng mục trong Product Backlog nhằm tối ưu hóa giá trị sản phẩm."
    },
    {
        "id": 5,
        "difficulty": "easy",
        "question": "Độ dài tiêu chuẩn của một chu kỳ Sprint trong quy trình Scrum thường kéo dài bao lâu?",
        "options": {
            "A": "Từ 1 đến 4 tuần",
            "B": "Từ 6 đến 12 tháng",
            "C": "Chỉ đúng 24 giờ",
            "D": "Tùy ý không giới hạn thời gian"
        },
        "correct_answer": "A",
        "explanation": "Một Sprint trong Scrum là một khoảng thời gian đóng khung (Time-boxed) từ 1 đến tối đa 4 tuần nhằm duy trì tính nhịp nhàng và kiểm soát rủi ro."
    },
    {
        "id": 6,
        "difficulty": "easy",
        "question": "Sự kiện Daily Scrum (Họp Scrum hàng ngày) có thời lượng tối đa quy định là bao nhiêu phút?",
        "options": {
            "A": "60 phút",
            "B": "15 phút",
            "C": "30 phút",
            "D": "Không giới hạn thời lượng"
        },
        "correct_answer": "B",
        "explanation": "Daily Scrum là cuộc họp ngắn gọn đúng 15 phút dành cho Developers để đồng bộ công việc và nhận diện các trở ngại phát sinh."
    },
    {
        "id": 7,
        "difficulty": "easy",
        "question": "Tạo tác nào trong Scrum đại diện cho danh sách các công việc cụ thể mà nhóm phát triển cam kết hoàn thành trong Sprint hiện tại?",
        "options": {
            "A": "Product Backlog",
            "B": "Sprint Backlog",
            "C": "Release Roadmap",
            "D": "Vision Document"
        },
        "correct_answer": "B",
        "explanation": "Sprint Backlog bao gồm Mục tiêu Sprint (Sprint Goal), các User Story được chọn từ Product Backlog và các công việc kỹ thuật cần làm để hoàn thành chúng."
    },
    {
        "id": 8,
        "difficulty": "easy",
        "question": "Mục đích chính của sự kiện 'Sprint Retrospective' (Cải tiến Sprint) là gì?",
        "options": {
            "A": "Trình chiếu tính năng cho khách hàng xem và thu tiền",
            "B": "Đội ngũ tự nhìn nhận, đánh giá lại quy trình làm việc, mối quan hệ và công cụ để đề ra kế hoạch cải tiến cho Sprint kế tiếp",
            "C": "Phạt các thành viên làm việc chậm tiến độ",
            "D": "Phỏng vấn tuyển dụng thêm lập trình viên mới"
        },
        "correct_answer": "B",
        "explanation": "Sprint Retrospective là cơ hội để Scrum Team tự thanh tra và thích nghi quy trình nội bộ nhằm nâng cao hiệu suất và chất lượng làm việc trong tương lai."
    },
    {
        "id": 9,
        "difficulty": "easy",
        "question": "Khái niệm 'Definition of Done' (DoD) trong Scrum được định nghĩa là gì?",
        "options": {
            "A": "Khi lập trình viên đã viết xong code trên máy cá nhân",
            "B": "Bản tiêu chí thống nhất khẳng định một hạng mục công việc đã đạt chuẩn chất lượng và sẵn sàng để tích hợp vào Increment",
            "C": "Thời điểm kết thúc hợp đồng dự án",
            "D": "Khi khách hàng thanh toán hết tiền dự án"
        },
        "correct_answer": "B",
        "explanation": "DoD là bản thỏa thuận chung của nhóm về các tiêu chuẩn chất lượng (viết code, unit test pass, code review, kiểm thử tích hợp, tài liệu hóa) để một tính năng được coi là hoàn tất."
    },
    {
        "id": 10,
        "difficulty": "easy",
        "question": "Lệnh Git nào được dùng để tạo một nhánh mới có tên `feature/login` và chuyển ngay sang nhánh đó?",
        "options": {
            "A": "git branch feature/login",
            "B": "git checkout -b feature/login (hoặc git switch -c feature/login)",
            "C": "git merge feature/login",
            "D": "git push -u feature/login"
        },
        "correct_answer": "B",
        "explanation": "Lệnh `git checkout -b <tên_nhánh>` hoặc cú pháp mới `git switch -c <tên_nhánh>` kết hợp tạo mới và chuyển vùng làm việc sang nhánh vừa tạo."
    },
    {
        "id": 11,
        "difficulty": "medium",
        "question": "Nhược điểm LỚN NHẤT của mô hình Thác nước khi áp dụng cho các dự án khởi nghiệp công nghệ (Tech Startups) là gì?",
        "options": {
            "A": "Chi phí mua phần mềm quản lý dự án quá đắt",
            "B": "Thời gian đưa sản phẩm ra thị trường (Time-to-Market) quá chậm; không có cơ chế thu thập phản hồi sớm từ người dùng thực tế trước khi cạn kiệt vốn",
            "C": "Không cho phép sử dụng công nghệ điện toán đám mây",
            "D": "Bắt buộc phải thuê hàng trăm kỹ sư tham gia"
        },
        "correct_answer": "B",
        "explanation": "Startups hoạt động trong môi trường cực kỳ bất định; mô hình Thác nước mất hàng tháng/năm mới ra được sản phẩm cuối cùng, nếu sai thị trường thì toàn bộ chi phí và công sức sẽ mất trắng."
    },
    {
        "id": 12,
        "difficulty": "medium",
        "question": "Trong mô hình Chữ V, giai đoạn 'Thiết kế Kiến trúc' (Architectural Design) tương ứng với cấp độ kiểm thử nào ở nhánh bên phải?",
        "options": {
            "A": "Kiểm thử đơn vị (Unit Testing)",
            "B": "Kiểm thử tích hợp (Integration Testing)",
            "C": "Kiểm thử chấp nhận (Acceptance Testing)",
            "D": "Kiểm thử hồi quy (Regression Testing)"
        },
        "correct_answer": "B",
        "explanation": "Kiểm thử tích hợp (Integration Testing) kiểm tra sự tương tác, kết nối và giao tiếp dữ liệu giữa các module hoặc hệ thống con đã được quy định trong thiết kế kiến trúc."
    },
    {
        "id": 13,
        "difficulty": "medium",
        "question": "Ai là người có quyền đưa ra quyết định HỦY BỎ (Cancel) một Sprint đang diễn ra trước khi hết thời gian quy định?",
        "options": {
            "A": "Scrum Master",
            "B": "Duy nhất Product Owner (PO), khi Mục tiêu Sprint (Sprint Goal) trở nên lỗi thời hoặc vô nghĩa",
            "C": "Đội ngũ Developers bỏ phiếu kín",
            "D": "Khách hàng gửi khiếu nại"
        },
        "correct_answer": "B",
        "explanation": "Theo Scrum Guide, chỉ duy nhất Product Owner mới có thẩm quyền hủy bỏ Sprint nếu mục tiêu của Sprint không còn phù hợp với chiến lược kinh doanh của công ty."
    },
    {
        "id": 14,
        "difficulty": "medium",
        "question": "Tại sao trong Scrum, Scrum Master KHÔNG ĐƯỢC đóng vai trò là 'Người quản lý trực tiếp' (Project Manager hay Boss) của nhóm phát triển?",
        "options": {
            "A": "Vì Scrum Master không được công ty trả lương",
            "B": "Vì Scrum Master là người phục vụ - lãnh đạo (Servant Leader), có trách nhiệm loại bỏ rào cản và trao quyền tự chủ (Self-organization) cho nhóm thay vì giao việc kiểu chỉ huy",
            "C": "Vì Scrum Master chỉ được phép làm việc bán thời gian",
            "D": "Vì vai trò quản lý đã do Product Owner kiêm nhiệm hoàn toàn"
        },
        "correct_answer": "B",
        "explanation": "Scrum Master không quản lý con người hay áp đặt công việc. Họ là Servant Leader giúp nhóm tự tổ chức, tự quản lý và tối ưu hóa năng suất theo các giá trị Scrum."
    },
    {
        "id": 15,
        "difficulty": "medium",
        "question": "Biểu đồ Burndown Chart trong quản lý dự án Scrum dùng để theo dõi chỉ số nào?",
        "options": {
            "A": "Lượng điện năng tiêu thụ của phòng máy chủ",
            "B": "Lượng công việc còn lại (Remaining Effort) theo thời gian trong suốt thời gian diễn ra Sprint",
            "C": "Số dòng mã lệnh (Lines of Code) mà mỗi lập trình viên viết được mỗi ngày",
            "D": "Tỷ lệ tăng trưởng doanh thu hàng quý của công ty"
        },
        "correct_answer": "B",
        "explanation": "Burndown Chart trực quan hóa số lượng Story Points hoặc số giờ làm việc còn lại mỗi ngày so với đường lý tưởng (Ideal line) để dự đoán nhóm có kịp về đích đúng hạn hay không."
    },
    {
        "id": 16,
        "difficulty": "medium",
        "question": "Trong quy trình GitHub Flow, thao tác 'Pull Request' (PR) mang ý nghĩa bản chất là gì?",
        "options": {
            "A": "Yêu cầu máy chủ GitHub khởi động lại hệ thống",
            "B": "Một đề xuất chính thức xin gộp các commit từ một nhánh tính năng vào nhánh chính, tạo không gian để các thành viên khác thẩm duyệt mã nguồn (Code Review) trước khi merge",
            "C": "Lệnh kéo toàn bộ mã nguồn về máy tính cá nhân để xóa",
            "D": "Tải một file nén zip của dự án về máy"
        },
        "correct_answer": "B",
        "explanation": "Pull Request là cơ chế cộng tác trên Git/GitHub cho phép thông báo, thảo luận và review mã nguồn trước khi chính thức hợp nhất vào nhánh chính của dự án."
    },
    {
        "id": 17,
        "difficulty": "medium",
        "question": "Điều gì xảy ra nếu vào cuối Sprint, có một User Story chưa hoàn thành đầy đủ theo Definition of Done (DoD)?",
        "options": {
            "A": "Đội ngũ vẫn tính điểm Story Points cho phần đã làm được",
            "B": "User Story đó không được tính điểm, không đưa vào demo trong Sprint Review và được chuyển trở lại Product Backlog để PO tái ước lượng và ưu tiên",
            "C": "Sprint phải được kéo dài thêm vài ngày để làm cho xong",
            "D": "Scrum Master phải tự tay hoàn thành phần còn thiếu"
        },
        "correct_answer": "B",
        "explanation": "Trong Scrum, không có khái niệm 'hoàn thành 80%'. Nếu một hạng mục chưa thỏa mãn 100% DoD, nó không được tính vào Increment và phải quay về Product Backlog."
    },
    {
        "id": 18,
        "difficulty": "medium",
        "question": "Sự khác biệt chính giữa Sprint Review và Sprint Retrospective là gì?",
        "options": {
            "A": "Review bàn về con người, Retrospective bàn về sản phẩm",
            "B": "Sprint Review tập trung vào SẢN PHẨM (những gì đã làm được và phản hồi của khách hàng), còn Sprint Retrospective tập trung vào QUY TRÌNH & CON NGƯỜI (cách thức làm việc và giải pháp cải tiến nội bộ)",
            "C": "Sprint Review họp hàng ngày, còn Sprint Retrospective họp hàng tháng",
            "D": "Sprint Review do Scrum Master chủ trì, còn Retrospective do giám đốc chủ trì"
        },
        "correct_answer": "B",
        "explanation": "Sprint Review là sự kiện hướng ngoại đánh giá sản phẩm phần mềm chạy được; Sprint Retrospective là sự kiện hướng nội đúc kết kinh nghiệm làm việc của toàn đội."
    },
    {
        "id": 19,
        "difficulty": "medium",
        "question": "Một nhóm Scrum có 7 lập trình viên. Trong buổi Sprint Planning, Product Owner yêu cầu đội ngũ phải cam kết làm 100 Story Points dù tốc độ (Velocity) trung bình của nhóm các Sprint trước chỉ là 60 Points. Nhóm nên xử lý như thế nào theo chuẩn Scrum?",
        "options": {
            "A": "Bắt buộc chấp nhận vì PO là người có quyền ra lệnh",
            "B": "Developers là người duy nhất có quyền quyết định lượng công việc đưa vào Sprint dựa trên năng lực và Velocity thực tế; nhóm cần giải thích và chỉ cam kết khối lượng vừa sức",
            "C": "Đồng ý nhận nhưng sẽ không viết kiểm thử để kịp tiến độ",
            "D": "Yêu cầu Scrum Master sa thải Product Owner"
        },
        "correct_answer": "B",
        "explanation": "Trong Scrum, nhóm phát triển là đội ngũ tự tổ chức. Chỉ có Developers mới có quyền quyết định số lượng công việc họ có thể hoàn thành trong một Sprint."
    },
    {
        "id": 20,
        "difficulty": "medium",
        "question": "Khi làm việc nhóm với Git, câu lệnh nào được dùng để cập nhật những thay đổi mới nhất từ nhánh `develop` trên GitHub về nhánh cục bộ của bạn?",
        "options": {
            "A": "git push origin develop",
            "B": "git pull origin develop",
            "C": "git commit -a",
            "D": "git branch -d develop"
        },
        "correct_answer": "B",
        "explanation": "`git pull origin develop` tải về (fetch) các commit mới nhất từ máy chủ từ xa và tự động gộp (merge) vào nhánh hiện tại trên máy cá nhân."
    },
    {
        "id": 21,
        "difficulty": "medium",
        "question": "Tại sao trong mô hình Thác nước, chi phí rủi ro thường đạt mức cao nhất vào giai đoạn cuối của dự án?",
        "options": {
            "A": "Vì lúc này các lập trình viên đã mệt mỏi và xin nghỉ việc",
            "B": "Vì đây là thời điểm đầu tiên các thành phần được tích hợp lại với nhau và người dùng cuối mới được chạm vào sản phẩm thực tế để kiểm tra",
            "C": "Vì chi phí thuê địa điểm văn phòng tăng lên",
            "D": "Vì các bản quyền phần mềm hết hạn sử dụng"
        },
        "correct_answer": "B",
        "explanation": "Sự chậm trễ trong việc tích hợp và nghiệm thu của mô hình Thác nước khiến cho các sai lệch kiến trúc hoặc hiểu lầm yêu cầu từ đầu chỉ phát lộ ở giai đoạn cuối cùng."
    },
    {
        "id": 22,
        "difficulty": "medium",
        "question": "Nguyên tắc số 1 trong 12 nguyên tắc của Tuyên ngôn Agile nhấn mạnh điều gì?",
        "options": {
            "A": "Ưu tiên cao nhất của chúng tôi là thỏa mãn khách hàng thông qua việc chuyển giao sớm và liên tục phần mềm có giá trị",
            "B": "Viết tài liệu thiết kế càng dài càng tốt",
            "C": "Không cho phép khách hàng thay đổi yêu cầu sau tuần đầu tiên",
            "D": "Thuê các chuyên gia nước ngoài kiểm thử sản phẩm"
        },
        "correct_answer": "A",
        "explanation": "Nguyên tắc số 1: 'Our highest priority is to satisfy the customer through early and continuous delivery of valuable software'."
    },
    {
        "id": 23,
        "difficulty": "hard",
        "question": "Trong Scrum, khái niệm 'Time-box' (Đóng khung thời gian) mang lại lợi ích kỹ thuật quan trọng nhất nào?",
        "options": {
            "A": "Ép buộc nhân viên phải làm việc tăng ca vào ban đêm",
            "B": "Ngăn ngừa việc tối ưu hóa quá mức không cần thiết (Over-engineering), tập trung vào mục tiêu quan trọng nhất và tạo ra nhịp điệu sinh hoạt ổn định (Cadence) để kiểm soát biến số",
            "C": "Giúp công ty tiết kiệm tiền điện văn phòng",
            "D": "Đảm bảo mã nguồn không bị tấn công mạng"
        },
        "correct_answer": "B",
        "explanation": "Time-box đặt ra giới hạn cứng về thời gian giúp nhóm tập trung hoàn thành các mục tiêu có giá trị cao nhất, tránh bẫy trì hoãn và thiết lập chu kỳ phản hồi định kỳ."
    },
    {
        "id": 24,
        "difficulty": "hard",
        "question": "Giả sử bạn đang ở nhánh `feature/cart`. Trước khi tạo Pull Request vào `develop`, bạn nên thực hiện thao tác nào để đảm bảo code của bạn không xung đột với các commit mới nhất mà đồng nghiệp vừa đẩy lên `develop`?",
        "options": {
            "A": "Xóa nhánh `develop` trên máy tính",
            "B": "Chuyển sang nhánh `develop`, kéo mã mới nhất về (`git pull origin develop`), sau đó quay lại nhánh `feature/cart` và thực hiện gộp hoặc rebase nhánh `develop` vào (`git merge develop`) để giải quyết xung đột trước",
            "C": "Đẩy thẳng code lên nhánh `main` mà không cần PR",
            "D": "Tắt tính năng kiểm tra xung đột của GitHub"
        },
        "correct_answer": "B",
        "explanation": "Luôn đồng bộ và resolve conflict cục bộ trước khi mở hoặc merge PR giúp nhánh chính luôn xanh và giảm thiểu rủi ro làm gãy luồng tích hợp chung."
    },
    {
        "id": 25,
        "difficulty": "hard",
        "question": "Một nhóm dự án xây dựng phần mềm tự hành cho tàu điện ngầm đô thị. Khách hàng yêu cầu tài liệu hóa tỉ mỉ mọi giao diện phần cứng và tuân thủ các quy chuẩn an toàn IEC 62279 cố định. Mô hình nào sau đây là phù hợp nhất?",
        "options": {
            "A": "Mô hình Chữ V nghiêm ngặt kết hợp phương pháp đặc tả hình thức (Formal Methods)",
            "B": "Mô hình Agile tự do không cần tài liệu",
            "C": "Mô hình Lập trình cực đoan (XP) không cần kiểm thử hệ thống",
            "D": "Mô hình phát triển tự phát"
        },
        "correct_answer": "A",
        "explanation": "Đối với các hệ thống quan trọng an toàn (Safety-critical), yêu cầu pháp lý cố định và rủi ro sinh mạng, mô hình Chữ V với kiểm thử đối ứng từng tầng là sự lựa chọn bắt buộc."
    },
    {
        "id": 26,
        "difficulty": "hard",
        "question": "Hiện tượng 'Scope Creep' (Phình phạm vi) thường xuyên xảy ra trong mô hình Thác nước dẫn đến hậu quả gì?",
        "options": {
            "A": "Phần mềm chạy nhanh hơn dự kiến",
            "B": "Các yêu cầu mới liên tục được bổ sung không chính thức vào giữa chừng mà không điều chỉnh thời gian và ngân sách, dẫn đến vỡ kế hoạch dự án",
            "C": "Dung lượng đĩa cứng của máy tính bị đầy",
            "D": "Không có ảnh hưởng gì đáng kể"
        },
        "correct_answer": "B",
        "explanation": "Scope Creep là hiện tượng phạm vi dự án bị nở rộng ngoài tầm kiểm soát do không có quy trình quản lý thay đổi (Change Control) nghiêm ngặt trong mô hình truyền thống."
    },
    {
        "id": 27,
        "difficulty": "hard",
        "question": "Trong một buổi Daily Scrum, một lập trình viên báo cáo: 'Tôi đang bị kẹt 2 ngày nay ở lỗi tích hợp cổng thanh toán vì chưa có API Key từ đối tác'. Trách nhiệm trực tiếp của Scrum Master lúc này là gì?",
        "options": {
            "A": "Ngồi viết code thay cho lập trình viên đó",
            "B": "Ghi nhận trở ngại (Impediment/Blocker) này và chủ động liên hệ với PO hoặc đối tác để lấy API Key, giúp giải tỏa bế tắc cho lập trình viên tập trung công việc",
            "C": "Trừ lương của lập trình viên vì không tự liên hệ đối tác",
            "D": "Yêu cầu hủy bỏ tính năng thanh toán khỏi dự án"
        },
        "correct_answer": "B",
        "explanation": "Nhiệm vụ cốt lõi của Scrum Master là loại bỏ các rào cản (Remove Impediments) ngoài tầm kiểm soát của nhóm để đảm bảo dòng chảy công việc được thông suốt."
    },
    {
        "id": 28,
        "difficulty": "hard",
        "question": "Sự khác biệt căn bản giữa `git merge` và `git rebase` khi tích hợp nhánh tính năng vào nhánh chính là gì?",
        "options": {
            "A": "`git merge` xóa toàn bộ code cũ, còn `git rebase` giữ lại",
            "B": "`git merge` tạo ra một commit gộp (Merge Commit) lưu giữ lịch sử phân nhánh chân thực; trong khi `git rebase` viết lại lịch sử commit thành một đường thẳng tuyến tính sạch sẽ",
            "C": "`git rebase` chỉ hoạt động được khi có mạng internet",
            "D": "Hai lệnh này hoàn toàn giống nhau về mặt lịch sử commit"
        },
        "correct_answer": "B",
        "explanation": "Merge bảo toàn đúng thời gian và cấu trúc rẽ nhánh thực tế (kèm merge commit); Rebase chuyển gốc của nhánh tính năng lên đầu nhánh chính, tạo lịch sử thẳng hàng."
    },
    {
        "id": 29,
        "difficulty": "hard",
        "question": "Một tổ chức chuyển đổi từ mô hình truyền thống sang Scrum nhưng vẫn giữ việc ban giám đốc áp đặt phạm vi công việc cứng và thời hạn cố định cho từng Sprint mà không cho phép nhóm thương lượng. Hiện tượng này thường được gọi là gì trong thực tế ngành CNPM?",
        "options": {
            "A": "Pure Agile",
            "B": "ScrumBut (hoặc 'Zombie Scrum' / 'Water-Scrum-Fall')",
            "C": "Extreme Programming",
            "D": "DevOps Transformation"
        },
        "correct_answer": "B",
        "explanation": "'Water-Scrum-Fall' hoặc 'ScrumBut' là hiện tượng áp dụng hình thức bên ngoài của Scrum (họp Daily, chia Sprint) nhưng bản chất bên trong vẫn là tư duy quản lý áp đặt cứng nhắc kiểu Thác nước."
    },
    {
        "id": 30,
        "difficulty": "hard",
        "question": "Trong Scrum, tính 'Liên chức năng' (Cross-functional) của Development Team có nghĩa là gì?",
        "options": {
            "A": "Tất cả các thành viên đều phải thành thạo mọi ngôn ngữ lập trình trên thế giới",
            "B": "Nhóm sở hữu đầy đủ tất cả các kỹ năng cần thiết (phân tích, thiết kế, lập trình, kiểm thử, tích hợp) để hoàn thành một Increment có thể bàn giao được mà không phải phụ thuộc vào nhóm bên ngoài",
            "C": "Các thành viên thay phiên nhau làm giám đốc công ty",
            "D": "Nhóm phải kiêm nhiệm luôn việc bán hàng và chăm sóc khách hàng"
        },
        "correct_answer": "B",
        "explanation": "Cross-functional team nghĩa là đội ngũ có đủ mọi chuyên môn trong nội bộ để tự mình đưa một tính năng từ ý tưởng thành sản phẩm hoàn chỉnh đạt Definition of Done."
    }
]

SHORT_ANSWERS = [
    {
        "id": 1,
        "question": "Nêu 4 giá trị cốt lõi của Tuyên ngôn Agile (Agile Manifesto 2001).",
        "expected_answer": "1. Cá nhân và sự tương tác hơn là quy trình và công cụ.\n2. Phần mềm chạy tốt hơn là tài liệu toàn diện.\n3. Cộng tác với khách hàng hơn là đàm phán hợp đồng.\n4. Phản hồi với sự thay đổi hơn là bám sát kế hoạch.",
        "explanation": "Bốn giá trị này định hướng tư duy ưu tiên hiệu quả thực tế và khả năng thích ứng linh hoạt."
    },
    {
        "id": 2,
        "question": "Liệt kê 3 vai trò (Roles) chính thức trong khung làm việc Scrum và trách nhiệm chính của từng vai trò.",
        "expected_answer": "1. **Product Owner (PO):** Quản lý Product Backlog, tối đa hóa giá trị sản phẩm và đại diện cho khách hàng.\n2. **Scrum Master (SM):** Người lãnh đạo phục vụ, đảm bảo thực thi đúng quy trình Scrum và loại bỏ các trở ngại cho nhóm.\n3. **Developers (Nhóm phát triển):** Nhóm chuyên gia liên chức năng trực tiếp xây dựng sản phẩm tăng tiến (Increment) đạt chuẩn Definition of Done.",
        "explanation": "Scrum không có chức danh phân cấp truyền thống như Trưởng dự án hay Đội trưởng kỹ thuật."
    },
    {
        "id": 3,
        "question": "Trình bày 4 sự kiện chính (Events) diễn ra trong một chu kỳ Sprint của Scrum.",
        "expected_answer": "1. **Sprint Planning:** Lập kế hoạch công việc cho Sprint.\n2. **Daily Scrum:** Cuộc họp đồng bộ 15 phút hàng ngày.\n3. **Sprint Review:** Trình diễn sản phẩm hoàn thành cho các bên liên quan để nhận phản hồi.\n4. **Sprint Retrospective:** Đội ngũ tự đúc kết kinh nghiệm và cải tiến quy trình nội bộ.",
        "explanation": "Bản thân Sprint là sự kiện chứa đựng (Container event) tất cả 4 sự kiện trên."
    },
    {
        "id": 4,
        "question": "Nêu 3 tạo tác (Artifacts) chính thức trong Scrum và cam kết (Commitment) đi kèm với mỗi tạo tác.",
        "expected_answer": "1. **Product Backlog** $\\longleftrightarrow$ Cam kết: **Mục tiêu Sản phẩm (Product Goal)**.\n2. **Sprint Backlog** $\\longleftrightarrow$ Cam kết: **Mục tiêu Sprint (Sprint Goal)**.\n3. **Increment** $\\longleftrightarrow$ Cam kết: **Định nghĩa Hoàn thành (Definition of Done - DoD)**.",
        "explanation": "Mỗi tạo tác trong Scrum Guide đều gắn liền với một cam kết minh bạch để đo lường tiến độ."
    },
    {
        "id": 5,
        "question": "Trong mô hình Chữ V, hãy liệt kê 4 cấp độ kiểm thử tương ứng với 4 cấp độ thiết kế từ trên xuống dưới.",
        "expected_answer": "1. Đặc tả yêu cầu (Requirements) $\\longleftrightarrow$ Kiểm thử chấp nhận (Acceptance Testing)\n2. Thiết kế hệ thống (System Design) $\\longleftrightarrow$ Kiểm thử hệ thống (System Testing)\n3. Thiết kế kiến trúc (Architecture Design) $\\longleftrightarrow$ Kiểm thử tích hợp (Integration Testing)\n4. Thiết kế module chi tiết (Detailed Design) $\\longleftrightarrow$ Kiểm thử đơn vị (Unit Testing)",
        "explanation": "Mô hình Chữ V thể hiện sự đối ứng chặt chẽ giữa thiết kế và kiểm thử."
    },
    {
        "id": 6,
        "question": "Viết chuỗi 4 lệnh Git cơ bản để đưa một nhánh tính năng mới `feature/cart` từ máy cục bộ lên kho chứa GitHub và thiết lập theo dõi (tracking).",
        "expected_answer": "```bash\ngit checkout -b feature/cart\ngit add .\ngit commit -m \"feat(cart): add shopping cart functionality\"\ngit push -u origin feature/cart\n```",
        "explanation": "Cờ `-u` (hoặc `--set-upstream`) giúp liên kết nhánh cục bộ với nhánh từ xa trên GitHub."
    },
    {
        "id": 7,
        "question": "Thế nào là một 'Increment' đạt chuẩn trong Scrum? Nếu một tính năng chưa đạt Definition of Done thì xử lý như thế nào?",
        "expected_answer": "Một Increment đạt chuẩn là một phần mềm chạy được, đã được kiểm thử toàn diện và thỏa mãn 100% các tiêu chí trong Definition of Done (DoD). Nếu một tính năng chưa đạt chuẩn DoD vào cuối Sprint, tính năng đó tuyệt đối không được đưa vào demo trong Sprint Review và phải được chuyển trở lại Product Backlog để PO tái đánh giá ở Sprint sau.",
        "explanation": "Quy tắc không nhân nhượng về chất lượng là cốt lõi để giữ hệ thống không bị nợ kỹ thuật."
    },
    {
        "id": 8,
        "question": "Trình bày 3 câu hỏi kinh điển mà mỗi thành viên trả lời trong cuộc họp Daily Scrum 15 phút.",
        "expected_answer": "1. Hôm qua tôi đã hoàn thành công việc gì để giúp nhóm đạt được Mục tiêu Sprint?\n2. Hôm nay tôi sẽ thực hiện công việc gì để giúp nhóm tiến gần hơn đến Mục tiêu Sprint?\n3. Tôi có đang gặp trở ngại hay rào cản nào cản trở tiến độ của tôi hoặc nhóm hay không?",
        "explanation": "Các câu hỏi này tập trung vào tính tương trợ và hướng tới Mục tiêu Sprint chung."
    }
]

ESSAYS = [
    {
        "id": 1,
        "title": "So Sánh Toàn Diện Mô Hình Thác Nước (Waterfall) và Phương Pháp Luận Linh Hoạt (Agile/Scrum)",
        "problem": "Một doanh nghiệp phần mềm đang đứng trước quyết định lựa chọn quy trình phát triển cho 2 dự án:\n- Dự án A: Xây dựng hệ thống điều khiển phanh chống bó cứng (ABS) cho ô tô điện theo hợp đồng trọn gói với các tiêu chuẩn an toàn kỹ thuật cố định.\n- Dự án B: Xây dựng ứng dụng mạng xã hội chia sẻ video ngắn trên thiết bị di động hướng đến người dùng trẻ, chưa rõ các tính năng nào sẽ tạo 'trend'.\n\nHãy phân tích và tư vấn:\n1. Lập bảng so sánh chi tiết giữa Mô hình Thác nước và Agile/Scrum theo các tiêu chí: Quản lý yêu cầu, Thời điểm bàn giao sản phẩm, Mức độ tham gia của khách hàng, Quản trị rủi ro và Khả năng thích ứng.\n2. Đưa ra khuyến nghị lựa chọn mô hình phù hợp cho từng Dự án A và B kèm theo luận giải kỹ thuật xác đáng.",
        "solution_steps": [
            "Bước 1: Lập bảng so sánh chi tiết\n| Tiêu chí | Mô hình Thác nước (Waterfall) | Phương pháp Agile/Scrum |\n| :--- | :--- | :--- |\n| Quản lý Yêu cầu | Yêu cầu được cố định và phê duyệt chi tiết ngay từ đầu; hạn chế tối đa thay đổi | Yêu cầu mở, tiến hóa liên tục qua từng Sprint qua Product Backlog |\n| Thời điểm bàn giao | Sản phẩm chỉ được bàn giao một lần duy nhất vào cuối dự án | Bàn giao từng phần mềm chạy được (Increment) liên tục sau mỗi 1-4 tuần |\n| Sự tham gia khách hàng | Khách hàng chỉ tham gia nhiều ở đầu (đưa yêu cầu) và cuối (nghiệm thu) | Khách hàng/PO tham gia liên tục hàng ngày và nghiệm thu trong mỗi Sprint Review |\n| Quản trị Rủi ro | Rủi ro tích tụ dồn về cuối; nếu sai thiết kế từ đầu thì hậu quả khôn lường | Rủi ro được chia nhỏ và phát hiện sớm ngay trong từng Sprint |\n| Khả năng Thích ứng | Rất thấp, quy trình thay đổi hợp đồng phức tạp | Cực kỳ cao, biến sự thay đổi thành lợi thế cạnh tranh |",
            "Bước 2: Phân tích và lựa chọn cho Dự án A (Hệ thống ABS ô tô điện)\n- *Khuyến nghị:* Chọn **Mô hình Chữ V hoặc Thác nước cải tiến**.\n- *Luận giải:* Hệ thống điều khiển ABS là hệ thống quan trọng an toàn (Safety-critical system). Các yêu cầu kỹ thuật, giao thức phần cứng và tiêu chuẩn an toàn (ISO 26262) được định nghĩa rất rõ ràng, chuẩn xác và không được phép tùy tiện thay đổi giữa chừng. Việc tài liệu hóa nghiêm ngặt và kiểm thử đối ứng từng tầng của V-Model là bắt buộc để đáp ứng quy định pháp lý.",
            "Bước 3: Phân tích và lựa chọn cho Dự án B (Ứng dụng mạng xã hội video ngắn)\n- *Khuyến nghị:* Chọn **Khung quy trình Agile/Scrum**.\n- *Luận giải:* Thị hiếu người dùng và xu hướng công nghệ trên thị trường mạng xã hội biến đổi tính bằng tuần. Nhóm phát triển cần nhanh chóng tung ra phiên bản thử nghiệm khả dụng tối thiểu (MVP - Minimum Viable Product) sau vài Sprint để đo lường phản ứng người dùng, sau đó liên tục lặp (Iterate) và bổ sung tính năng phù hợp dựa trên dữ liệu phân tích thực tế."
        ]
    },
    {
        "id": 2,
        "title": "Thiết Kế Luồng Làm Việc Scrum Chuẩn Cho Dự Án Phần Mềm 3 Tháng",
        "problem": "Nhóm của bạn gồm 1 Product Owner, 1 Scrum Master và 5 Developers được giao nhiệm vụ phát triển Hệ thống Đăng ký Tín chỉ Trực tuyến trong thời gian 3 tháng (12 tuần):\n1. Hãy hoạch định độ dài Sprint, số lượng Sprint và lịch trình các sự kiện Scrum trong một Sprint điển hình.\n2. Định nghĩa chi tiết bộ tiêu chí 'Definition of Done' (DoD) chuẩn mực cho nhóm để đảm bảo chất lượng kỹ thuật.\n3. Trình bày quy trình xử lý khi nhóm phát hiện một lỗi bảo mật nghiêm trọng (Critical Security Bug) trên môi trường thử nghiệm giữa chừng Sprint.",
        "solution_steps": [
            "Bước 1: Hoạch định cấu trúc Sprint và lịch trình sự kiện\n- Độ dài Sprint: Chọn **2 tuần/Sprint** $\\implies$ Tổng cộng dự án gồm 6 Sprints.\n- Lịch trình các sự kiện trong 1 Sprint (10 ngày làm việc):\n  - *Ngày 1 (Thứ Hai tuần 1):* Sprint Planning (4 giờ: 2 giờ đầu làm việc với PO để chốt mục tiêu và User Stories; 2 giờ sau nhóm kỹ thuật phân rã Tasks).\n  - *Hàng ngày (từ Thứ Hai đến Thứ Sáu):* Daily Scrum (15 phút vào 9:00 sáng).\n  - *Giữa Sprint (Thứ Tư tuần 2):* Backlog Refinement/Grooming (1-2 giờ để làm mịn các User Story cho Sprint sau).\n  - *Ngày cuối (Thứ Sáu tuần 2):* Sprint Review (1.5 giờ demo cho Stakeholders) $\\to$ Sprint Retrospective (1.5 giờ họp nội bộ đúc kết cải tiến quy trình).",
            "Bước 2: Xây dựng tiêu chí Definition of Done (DoD) chuẩn mực\nMột User Story chỉ được coi là 'Hoàn thành' (Done) khi thỏa mãn toàn bộ checklist sau:\n1. Mã nguồn tuân thủ coding conventions của dự án và không có cảnh báo nghiêm trọng từ Linter.\n2. Đạt độ bao phủ kiểm thử đơn vị (Unit Test Coverage) $\\ge 80%$ cho các nghiệp vụ chính.\n3. Vượt qua 100% các ca kiểm thử tự động trên pipeline CI.\n4. Đã vượt qua Code Review và được chấp thuận (Approved) bởi ít nhất 1 Senior Developer.\n5. Đã được triển khai thành công lên môi trường Staging/Testing.\n6. Kiểm thử chấp nhận (Acceptance Criteria) được kiểm chứng và ký duyệt bởi Product Owner.\n7. Tài liệu API (Swagger/Postman) đã được cập nhật.",
            "Bước 3: Quy trình xử lý lỗi bảo mật đột xuất giữa Sprint\n1. Đội ngũ thông báo khẩn cấp cho PO và Scrum Master.\n2. PO đánh giá mức độ khẩn cấp: Nếu đây là lỗi rủi ro an ninh nghiêm trọng cần vá gấp, PO và Developers thống nhất đưa một việc sửa lỗi (Bug/Hotfix Task) vào Sprint Backlog hiện tại.\n3. Do dung lượng làm việc của Sprint là cố định, PO cùng nhóm thống nhất chuyển bớt một User Story có mức ưu tiên thấp nhất tương đương ra khỏi Sprint Backlog để bảo vệ tính khả thi của Sprint Goal mà không gây kiệt sức cho đội ngũ."
        ]
    },
    {
        "id": 3,
        "title": "Phân Tích Cơ Chế Thẩm Duyệt Mã Nguồn (Code Review) & Xây Dựng Git Workflow Nhóm",
        "problem": "Một dự án nhóm gồm 4 thành viên thường xuyên gặp tình trạng: Một thành viên đẩy trực tiếp code lỗi lên nhánh `main`, làm hỏng toàn bộ môi trường chung và các thành viên khác không thể làm việc tiếp.\nHãy tái cấu trúc lại toàn bộ quy trình làm việc trên GitHub:\n1. Thiết lập quy tắc bảo vệ nhánh (Branch Protection Rules) cho nhánh `main` và `develop`.\n2. Thiết kế mẫu biểu thẩm duyệt Pull Request (PR Template) chuẩn mực.\n3. Xây dựng bộ quy tắc ứng xử và tiêu chí kỹ thuật khi thực hiện Code Review giữa các thành viên.",
        "solution_steps": [
            "Bước 1: Thiết lập Branch Protection Rules trên GitHub\n- Khóa quyền đẩy code trực tiếp (Disallow direct push) lên cả 2 nhánh `main` và `develop`.\n- Bắt buộc mọi thay đổi phải đi qua Pull Request (Require a pull request before merging).\n- Yêu cầu ít nhất 1 sự phê duyệt chấp thuận (Require at least 1 approving review) từ thành viên khác.\n- Bắt buộc các kiểm tra tự động phải vượt qua (Require status checks to pass before merging: Build test, Unit test, Linting).\n- Yêu cầu giải quyết toàn bộ các bình luận thảo luận (Require conversation resolution) trước khi bấm Merge.",
            "Bước 2: Thiết kế Pull Request Template (`.github/pull_request_template.md`)\n```markdown\n## Mô tả tóm tắt\n- Nêu tính năng hoặc bug được giải quyết (gắn link Issue/User Story).\n\n## Những thay đổi chính\n- [ ] Đã thêm API / Entity / Component nào?\n- [ ] Đã cập nhật cấu trúc DB hoặc file môi trường chưa?\n\n## Checklist tự kiểm tra của tác giả\n- [ ] Đã chạy unit test cục bộ PASS 100%?\n- [ ] Đã tự review code của chính mình trước khi mở PR?\n- [ ] Không chứa thông tin nhạy cảm (passwords, tokens)?\n```",
            "Bước 3: Tiêu chuẩn kỹ thuật và văn hóa Code Review\n- *Tiêu chuẩn kỹ thuật:* Kiểm tra tính đúng đắn logic nghiệp vụ, lỗ hổng bảo mật tiềm ẩn (SQL Injection, XSS), hiệu năng thuật toán, khả năng xử lý ngoại lệ, và việc tuân thủ nguyên lý Clean Code (đặt tên rõ nghĩa, hàm ngắn).\n- *Văn hóa giao tiếp:* Nhận xét trên tinh thần xây dựng, tập trung vào đoạn code chứ không công kích cá nhân; giải thích rõ *tại sao* nên sửa và đề xuất giải pháp thay thế; công nhận những đoạn code hay và giải thuật thông minh của đồng nghiệp."
        ]
    },
    {
        "id": 4,
        "title": "Ứng Phó với Sự Cố 'Zombie Scrum' và Sự Suy Thoái Quy Trình trong Doanh Nghiệp",
        "problem": "Một công ty công nghệ tuyên bố đã áp dụng Scrum được 1 năm. Tuy nhiên, qua khảo sát thực tế:\n- Cuộc họp Daily Scrum biến thành buổi báo cáo điểm danh kéo dài 45 phút, mọi người ngồi nghe thụ động.\n- Product Owner không bao giờ tham gia Sprint Review, chỉ xuất hiện vào cuối dự án để phê bình.\n- Định nghĩa Definition of Done bị bỏ qua để 'chạy kịp tiến độ', nợ kỹ thuật chồng chất, tỷ lệ lỗi ở Production tăng 200%.\n\nHãy đóng vai trò là Chuyên gia Tư vấn Agile (Agile Coach):\n1. Hãy chỉ ra các 'Mùi hôi quy trình' (Process Smells) và bản chất của hiện tượng 'Zombie Scrum' trong trường hợp này.\n2. Phân tích nguyên nhân gốc rễ (Root Causes) từ cấp độ lãnh đạo đến cấp độ kỹ thuật.\n3. Đề xuất lộ trình 4 bước cụ thể để tái thiết lập văn hóa Agile thực thụ cho tổ chức.",
        "solution_steps": [
            "Bước 1: Nhận diện các Process Smells và Zombie Scrum\n- Hiện tượng 'Zombie Scrum': Đội ngũ chỉ thực hiện các nghi thức hình thức bề ngoài của Scrum nhưng thiếu vắng hoàn toàn linh hồn của Agile (không có sự cộng tác thực chất, không có giá trị phần mềm chạy được sau mỗi Sprint, và không có sự tự chủ của đội ngũ).\n- Biểu hiện cụ thể: Daily Scrum biến thành buổi báo cáo vi mô (Micromanagement) với sếp thay vì đối thoại ngang hàng; PO vắng mặt khiến nhóm đi trong bóng tối; phá vỡ DoD để lấy thành tích ảo dẫn đến nợ kỹ thuật bùng nổ.",
            "Bước 2: Phân tích nguyên nhân gốc rễ\n- *Cấp lãnh đạo:* Tư duy quản lý truyền thống (Command & Control) áp đặt, không tin tưởng đội ngũ, coi Agile chỉ là công cụ để ép nhân viên làm nhanh hơn.\n- *Cấp Product Owner:* Không được trao quyền thực sự hoặc thiếu năng lực và cam kết thời gian cho sản phẩm.\n- *Cấp Kỹ thuật:* Thiếu kỷ luật kỹ thuật (Engineering Discipline), xem nhẹ kiểm thử tự động, thiếu kỹ năng viết Clean Code và tái cấu trúc.",
            "Bước 3: Lộ trình 4 bước tái thiết lập văn hóa Agile\n1. *Đào tạo lại tư duy (Mindset Reset):* Tổ chức workshop cho ban lãnh đạo và PO về bản chất của Empiricism và giá trị cốt lõi của Scrum.\n2. *Khôi phục kỷ luật sự kiện:* Giới hạn nghiêm ngặt Daily Scrum đúng 15 phút, đứng họp và chỉ tập trung vào 3 câu hỏi hướng tới Sprint Goal; bắt buộc PO phải tham dự Sprint Review để thẩm định Increment.\n3. *Tái thiết lập và bảo vệ Definition of Done:* Thống nhất lại DoD với các tiêu chí chất lượng tối thiểu không được thỏa hiệp; kiên quyết không tính điểm cho các Story chưa đạt DoD.\n4. *Đầu tư vào Kỹ nghệ Thực nghiệm:* Đào tạo nhóm về TDD, Clean Code, thiết lập pipeline CI/CD tự động kiểm tra chất lượng mã nguồn mỗi khi tạo PR."
        ]
    }
]
