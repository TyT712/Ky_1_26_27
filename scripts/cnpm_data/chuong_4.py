# -*- coding: utf-8 -*-
"""Data definition for Chương 4: Phát triển, Tích hợp và Đảm bảo Chất lượng."""

CHAPTER_ID = "chuong_4"
CHAPTER_NUMBER = 4
CHAPTER_TITLE = "Chương 4: Phát triển, Tích hợp và Đảm bảo Chất lượng"
CHAPTER_SUMMARY = "Kế hoạch Sprint & phân rã công việc, kiến trúc phân tầng (Layered Architecture), nguyên lý Clean Code & tái cấu trúc, quy trình Code Review, kim tự tháp kiểm thử (Testing Pyramid), phương pháp phát triển hướng kiểm thử (TDD: Red-Green-Refactor) và kết thúc Sprint (Review & Retrospective)."

THEORY_MD = """# CHƯƠNG 4: PHÁT TRIỂN, TÍCH HỢP VÀ ĐẢM BẢO CHẤT LƯỢNG

## 1. Thiết Kế Kiến Trúc Đúng Lúc (Just-in-Time Design)
Trong phát triển phần mềm hiện đại, đội ngũ tránh bẫy **Big Design Up Front (BDUF)** (thiết kế quá chi tiết từ đầu khi chưa hiểu hết yêu cầu), thay vào đó áp dụng tư duy thiết kế kiến trúc tiến hóa (Evolutionary Architecture) có khả năng thích nghi:
- **Kiến trúc phân tầng chuẩn mực (Layered / N-Tier Architecture):**
  - **Controller / Presentation Layer:** Tiếp nhận HTTP Requests, xác thực tham số đầu vào và trả về JSON/View.
  - **Service / Business Logic Layer:** Xử lý toàn bộ logic nghiệp vụ cốt lõi, giao dịch (Transactions) và tính toán.
  - **Repository / Data Access Layer:** Tương tác trực tiếp với cơ sở dữ liệu (ORM, SQL queries, Redis cache).
  - **Database:** Lưu trữ dữ liệu bền vững (PostgreSQL, MySQL, MongoDB).

```mermaid
graph TD
    Client["Client (Browser / Mobile App)"] -->|HTTP / REST API| Controller["Controller Layer (API Gate)"]
    Controller -->|DTOs| Service["Service Layer (Business Logic)"]
    Service -->|Entities| Repository["Repository Layer (Data Access)"]
    Repository -->|SQL Queries| Database[("Cơ sở dữ liệu (Database)")]
```

## 2. Chuẩn Mực Clean Code & Nguyên Lý Thiết Kế
- **Nguyên lý đặt tên rõ nghĩa:** Tên biến/hàm phải bộc lộ rõ ý đồ (Intention-revealing). Ví dụ: Dùng `daysSinceLastLogin` thay vì `d` hoặc `val`.
- **Hàm ngắn và chỉ làm một việc duy nhất:** Hàm chỉ nên dài dưới 20-30 dòng và tuân thủ nguyên lý Single Responsibility Principle (SRP).
- **Tránh trùng lặp (DRY - Don't Repeat Yourself):** Mỗi tri thức hay logic nghiệp vụ chỉ nên có một biểu diễn duy nhất trong hệ thống.
- **Giữ cho code đơn giản (KISS - Keep It Simple, Stupid):** Không lạm dụng Design Patterns phức tạp khi bài toán chưa thực sự đòi hỏi.
- **Quy tắc hướng đạo sinh (Boy Scout Rule):** *"Luôn để lại khu cắm trại sạch sẽ hơn lúc bạn đến"* — luôn tối ưu lại một đoạn code nhỏ mỗi khi bạn chỉnh sửa file.

## 3. Chiến Lược Kiểm Thử & Kim Tự Tháp Kiểm Thử (Testing Pyramid)
Kim tự tháp kiểm thử do Mike Cohn đề xuất mô tả tỷ lệ lý tưởng giữa các cấp độ kiểm thử trong dự án phần mềm:

```mermaid
graph TD
    subgraph Pyramid["Kim Tự Tháp Kiểm Thử (Testing Pyramid)"]
        E2E["Đỉnh tháp: End-to-End / UI Tests (Số lượng ít, Chậm, Chi phí đắt)"]
        INT["Thân tháp: Integration Tests (Kiểm thử tích hợp API, Database)"]
        UNIT["Đáy tháp: Unit Tests (Số lượng nhiều nhất, Nhanh nhất, Rẻ nhất)"]
    end
    UNIT --> INT --> E2E
```

1. **Unit Testing (Kiểm thử đơn vị - Chiếm 70%):**
   - Kiểm tra các hàm, class nhỏ nhất một cách độc lập.
   - Sử dụng các kỹ thuật giả lập (Mocking / Stubbing) để cô lập các phụ thuộc bên ngoài (DB, Network).
   - Mô hình viết test chuẩn **AAA (Arrange - Act - Assert)**:
     - *Arrange:* Chuẩn bị dữ liệu và môi trường giả lập.
     - *Act:* Kích hoạt hàm cần kiểm thử.
     - *Assert:* Xác minh kết quả trả về có đúng kỳ vọng hay không.
2. **Integration Testing (Kiểm thử tích hợp - Chiếm 20%):**
   - Kiểm tra sự phối hợp kết nối giữa nhiều module, ví dụ: Service gọi Repository truy vấn DB thực tế, hoặc kiểm tra kết nối API bên thứ ba.
3. **End-to-End Testing (Kiểm thử đầu-cuối - Chiếm 10%):**
   - Mô phỏng toàn bộ hành trình người dùng từ giao diện (Cypress, Playwright, Selenium) xuyên suốt tới cơ sở dữ liệu.

## 4. Phát Triển Hướng Kiểm Thử (TDD - Test-Driven Development)
TDD là phương pháp kỹ nghệ đảo ngược: **Viết kiểm thử tự động trước khi viết mã nguồn thực tế**, tuân thủ nghiêm ngặt chu trình 3 bước **Red - Green - Refactor**:

```mermaid
graph LR
    RED["1. RED: Viết một ca kiểm thử lỗi (Failed Test)"] --> GREEN["2. GREEN: Viết mã nguồn tối thiểu để test vượt qua (Pass)"]
    GREEN --> REFACTOR["3. REFACTOR: Tối ưu hóa cấu trúc mã nguồn sạch sẽ (Clean Code)"]
    REFACTOR --> RED
```

- **Lợi ích của TDD:** Mã nguồn luôn có 100% test coverage tự nhiên; kiến trúc module hóa lỏng (vì code phải dễ test); lập trình viên tự tin tái cấu trúc mà không sợ sinh lỗi mới (No regression bugs).

## 5. Quy Trình Thẩm Duyệt Mã Nguồn (Code Review)
- Mỗi tính năng khi hoàn thành phải tạo Pull Request (PR).
- Tiêu chí đánh giá của Reviewer:
  - *Tính đúng đắn (Correctness):* Thuật toán có đúng nghiệp vụ không? Có lỗi ngoại lệ (NullPointerException, Division by zero) không?
  - *Bảo mật (Security):* Có nguy cơ SQL Injection, XSS, lộ thông tin mật không?
  - *Khả năng bảo trì (Maintainability):* Code có dễ hiểu không? Có bị lặp code không?
  - *Kiểm thử (Tests):* Có viết đủ unit tests cho các trường hợp biên không?
"""

TOPIC_SUMMARY = """# Chuyên Đề: Clean Code, Chiến Lược Kiểm Thử & TDD Trong Kỹ Nghệ Phần Mềm

## 1. Triết Lý Clean Code và Nợ Kỹ Thuật
- Mã nguồn được đọc nhiều gấp 10 lần so với thời gian viết ra nó. Viết code sạch là sự tôn trọng dành cho chính bạn và đồng nghiệp trong tương lai.
- Refactoring không phải là viết lại từ đầu mà là cải tiến cấu trúc bên trong của mã nguồn mà không làm thay đổi hành vi bên ngoài của hệ thống.

## 2. Cốt Lõi Kim Tự Tháp Kiểm Thử Hiện Đại
- Phá vỡ mô hình 'Cây kem ốc quế đảo ngược' (Anti-pattern: quá nhiều E2E test thủ công, quá ít unit test) giúp pipeline CI chạy nhanh từ vài chục phút xuống vài chục giây.
- Mocking và Stubbing là kỹ thuật sống còn để unit test đạt tốc độ mili-giây và chạy hoàn toàn độc lập với môi trường ngoài.

## 3. Sức Mạnh của Chu Trình TDD
- Viết test trước buộc lập trình viên phải đóng vai người sử dụng API trước khi lập trình cài đặt; từ đó thiết kế ra các hàm có giao diện trong sáng, dễ gọi và ít khớp nối.
"""

PARSED_MARKDOWN = f"""# Giáo trình Công nghệ Phần mềm - Chương 4: Phát triển, Tích hợp và Đảm bảo Chất lượng
<!-- Nguồn: TS. Trần Văn Long - Khoa Tin học, Đại học Sư phạm, Đại học Huế -->

<!-- PAGE 1 -->
## A. Mục tiêu Bài học
1. Tham gia hiệu quả vào các sự kiện Scrum: Sprint Planning, Sprint Review, Sprint Retrospective.
2. Vận dụng nguyên lý thiết kế kiến trúc phân tầng (Layered Architecture) và xây dựng RESTful API cho User Story.
3. Thành thạo quy trình quản lý mã nguồn với Git (Feature Branch, Pull Request, Resolving Conflicts).
4. Thực hiện Code Review chuyên nghiệp để đảm bảo chất lượng kỹ thuật mã nguồn.
5. Hiểu sâu các cấp độ kiểm thử trong Kim tự tháp kiểm thử và áp dụng thành thạo TDD (Test-Driven Development) bằng Unit Tests.

<!-- PAGE 3 -->
## B. Nội dung Chi tiết

### I. Sprint Planning & Phân rã Công việc (Task Breakdown)
- Xác định Mục tiêu Sprint (Sprint Goal).
- Phân rã User Story thành các nhiệm vụ kỹ thuật cụ thể (Technical Tasks có kích thước từ 2 đến 8 giờ làm việc).
- Ước lượng năng lực nhóm (Team Capacity).

### II. Thiết kế Kiến trúc Đúng lúc (Just-in-Time Design)
- Phân tầng Controller - Service - Repository.
- Thiết kế Data Transfer Object (DTO) và Entities.
- Chuẩn hóa RESTful API (HTTP Verbs: GET, POST, PUT, DELETE, PATCH; Status Codes: 200, 201, 400, 401, 403, 404, 500).

### III. Chuẩn mực Lập trình Clean Code & Tái cấu trúc (Refactoring)
- Nguyên tắc đặt tên biến, hàm, lớp.
- Tránh Code Smells: Long Method, Large Class, Feature Envy, Primitive Obsession, Dead Code.
- Nguyên lý DRY, KISS và Boy Scout Rule.

### IV. Chiến lược Kiểm thử Phần mềm & TDD
- Kim tự tháp kiểm thử: Unit Test, Integration Test, E2E Test.
- Quy chuẩn viết Unit Test theo cấu trúc AAA (Arrange, Act, Assert).
- Chu trình TDD Red - Green - Refactor.
- Sử dụng Test Doubles: Mock, Stub, Fake.

### V. Thẩm duyệt Mã nguồn & Kết thúc Sprint
- Quy trình mở và phê duyệt Pull Request (PR) trên GitHub.
- Các tiêu chí kiểm tra trong Code Review Checklist.
- Tổ chức Sprint Review (Demo sản phẩm đạt DoD) và Sprint Retrospective (Kế hoạch hành động cải tiến).
"""

MULTIPLE_CHOICE = [
    {
        "id": 1,
        "difficulty": "easy",
        "question": "Trong kiến trúc phần mềm phân tầng (Layered Architecture), tầng nào chịu trách nhiệm tiếp nhận HTTP Request từ client và trả về dữ liệu cho người dùng?",
        "options": {
            "A": "Database Layer",
            "B": "Controller / Presentation Layer",
            "C": "Repository Layer",
            "D": "Infrastructure Layer"
        },
        "correct_answer": "B",
        "explanation": "Controller Layer đóng vai trò cổng vào của ứng dụng, tiếp nhận các HTTP requests, xác thực sơ bộ tham số và điều phối gọi xuống tầng nghiệp vụ (Service)."
    },
    {
        "id": 2,
        "difficulty": "easy",
        "question": "Theo nguyên lý Clean Code của Robert C. Martin (Uncle Bob), một hàm (function/method) tốt nên có độ dài như thế nào?",
        "options": {
            "A": "Càng dài càng tốt, tối thiểu từ 500 dòng code trở lên để gộp chung logic",
            "B": "Ngắn gọn, lý tưởng dưới 20-30 dòng và chỉ thực hiện duy nhất một nhiệm vụ (Single Responsibility)",
            "C": "Phải chứa ít nhất 10 vòng lặp lồng nhau",
            "D": "Không được sử dụng bất kỳ tham số đầu vào nào"
        },
        "correct_answer": "B",
        "explanation": "Quy tắc vàng của Clean Code: Một hàm phải ngắn gọn, chỉ làm một việc duy nhất và làm việc đó thật tốt (Do one thing, do it well)."
    },
    {
        "id": 3,
        "difficulty": "easy",
        "question": "Nguyên lý 'DRY' trong phát triển phần mềm là viết tắt của cụm từ tiếng Anh nào?",
        "options": {
            "A": "Do Right Yourself",
            "B": "Don't Repeat Yourself",
            "C": "Design Ready Yesterday",
            "D": "Data Redundancy Yield"
        },
        "correct_answer": "B",
        "explanation": "DRY (Don't Repeat Yourself) nhắc nhở lập trình viên không được sao chép dán (copy-paste) code trùng lặp mà phải trừu tượng hóa và tái sử dụng logic chung."
    },
    {
        "id": 4,
        "difficulty": "easy",
        "question": "Trong Kim tự tháp kiểm thử (Testing Pyramid), cấp độ kiểm thử nào nằm ở ĐÁY THÁP (chiếm số lượng nhiều nhất, chạy nhanh nhất và chi phí thấp nhất)?",
        "options": {
            "A": "Kiểm thử giao diện người dùng thủ công (Manual UI Testing)",
            "B": "Kiểm thử đơn vị (Unit Testing)",
            "C": "Kiểm thử đầu-cuối (End-to-End Testing)",
            "D": "Kiểm thử tải trọng (Load Testing)"
        },
        "correct_answer": "B",
        "explanation": "Đáy tháp là Unit Tests (Kiểm thử đơn vị), chạy cực nhanh ở cấp độ hàm/lớp, giúp phát hiện lỗi sai logic ngay lập tức khi gõ code."
    },
    {
        "id": 5,
        "difficulty": "easy",
        "question": "Ba bước cơ bản trong chu trình phát triển hướng kiểm thử (TDD - Test-Driven Development) theo thứ tự chuẩn là gì?",
        "options": {
            "A": "Build - Deploy - Test",
            "B": "Red (Viết test lỗi) $\\to$ Green (Viết code tối thiểu để pass) $\\to$ Refactor (Tái cấu trúc mã sạch)",
            "C": "Plan - Code - Debug",
            "D": "Analyze - Design - Test"
        },
        "correct_answer": "B",
        "explanation": "Chu trình TDD kinh điển: Bắt đầu bằng Red (test fail vì chưa có code), Green (viết code nhanh để test pass) và Refactor (tối ưu hóa code mà test vẫn xanh)."
    },
    {
        "id": 6,
        "difficulty": "easy",
        "question": "Mô hình cấu trúc chuẩn gồm 3 phần khi viết một ca kiểm thử đơn vị (Unit Test) là gì?",
        "options": {
            "A": "Start - Middle - End",
            "B": "Arrange (Chuẩn bị dữ liệu) - Act (Thực thi hành động) - Assert (Kiểm chứng kết quả)",
            "C": "Input - Process - Output",
            "D": "Create - Read - Delete"
        },
        "correct_answer": "B",
        "explanation": "Khuôn mẫu AAA (Arrange - Act - Assert) là chuẩn mực giúp unit test rõ ràng, dễ đọc hiểu và dễ bảo trì."
    },
    {
        "id": 7,
        "difficulty": "easy",
        "question": "Mã trạng thái HTTP (Status Code) nào được coi là chuẩn RESTful khi một tài nguyên mới được tạo thành công trên máy chủ (ví dụ sau lệnh POST)?",
        "options": {
            "A": "200 OK",
            "B": "201 Created",
            "C": "204 No Content",
            "D": "400 Bad Request"
        },
        "correct_answer": "B",
        "explanation": "HTTP 201 Created là mã chuẩn xác thông báo tài nguyên mới (resource) đã được tạo thành công trên hệ thống."
    },
    {
        "id": 8,
        "difficulty": "easy",
        "question": "Quy tắc 'Boy Scout Rule' trong bảo trì phần mềm được phát biểu như thế nào?",
        "options": {
            "A": "Lập trình viên phải mặc đồng phục hướng đạo sinh khi đi làm",
            "B": "Luôn để lại khu cắm trại sạch sẽ hơn lúc bạn đến (Mỗi khi sửa một đoạn code, hãy luôn dọn dẹp và cải tiến nó sạch hơn một chút)",
            "C": "Chỉ những lập trình viên nam mới được phép commit mã nguồn",
            "D": "Không được phép sử dụng thư viện nguồn mở"
        },
        "correct_answer": "B",
        "explanation": "Boy Scout Rule khuyên các kỹ sư thực hiện refactor liên tục từng bước nhỏ mỗi ngày để ngăn ngừa sự tích tụ của nợ kỹ thuật."
    },
    {
        "id": 9,
        "difficulty": "easy",
        "question": "Khái niệm 'Refactoring' (Tái cấu trúc mã nguồn) được định nghĩa chính xác là gì?",
        "options": {
            "A": "Viết thêm các tính năng mới mà khách hàng chưa yêu cầu",
            "B": "Quá trình cải tiến cấu trúc nội bộ của mã nguồn nhằm làm code sạch hơn, dễ bảo trì hơn mà KHÔNG LÀM THAY ĐỔI hành vi bên ngoài của hệ thống",
            "C": "Xóa toàn bộ cơ sở dữ liệu để tạo lại từ đầu",
            "D": "Đổi ngôn ngữ lập trình của dự án"
        },
        "correct_answer": "B",
        "explanation": "Refactoring giữ nguyên hành vi bên ngoài (được đảm bảo bằng hệ thống unit test tự động) trong khi tối ưu cấu trúc bên trong của code."
    },
    {
        "id": 10,
        "difficulty": "easy",
        "question": "Trong quy trình kiểm thử, đối tượng 'Mock' (hoặc Test Double) được dùng để làm gì?",
        "options": {
            "A": "Giễu cợt các đoạn code bị lỗi của đồng nghiệp",
            "B": "Đối tượng giả lập hành vi của các phụ thuộc bên ngoài (như Cơ sở dữ liệu, Cổng thanh toán, Mạng) để cô lập đơn vị cần kiểm thử",
            "C": "Một con virus máy tính dùng để tấn công hệ thống",
            "D": "Trình duyệt web ảo để chạy quảng cáo"
        },
        "correct_answer": "B",
        "explanation": "Mock giả lập phản hồi của các thành phần phụ thuộc, giúp unit test chạy nhanh, độc lập và không phụ thuộc vào trạng thái cơ sở dữ liệu thật."
    },
    {
        "id": 11,
        "difficulty": "medium",
        "question": "Tại sao trong kiến trúc phần mềm hiện đại, việc tránh 'Big Design Up Front' (BDUF) lại giúp giảm thiểu rủi ro cho dự án?",
        "options": {
            "A": "Vì không cần phải tốn tiền mua máy tính cấu hình cao để vẽ biểu đồ",
            "B": "Vì các chi tiết thiết kế ban đầu khi chưa viết code thực tế thường dựa trên giả định mơ hồ; thiết kế kiến trúc tiến hóa từng bước (Evolutionary Architecture) giúp hệ thống uyển chuyển thích ứng khi hiểu sâu hơn về bài toán",
            "C": "Vì các kiến trúc sư phần mềm không thích vẽ sơ đồ",
            "D": "Vì mô hình BDUF đã bị pháp luật cấm sử dụng"
        },
        "correct_answer": "B",
        "explanation": "BDUF thường dẫn đến việc thiết kế thừa thãi (Over-engineering) cho những tình huống giả định không bao giờ xảy ra. Thiết kế linh hoạt (Just-in-Time) chỉ tập trung giải quyết bài toán hiện tại một cách sạch sẽ."
    },
    {
        "id": 12,
        "difficulty": "medium",
        "question": "Một đoạn mã nguồn kiểm tra dữ liệu đầu vào có 5 tầng câu lệnh `if-else` lồng nhau sâu hoắm. 'Mùi hôi của code' (Code Smell) này thường được gọi là gì và cách xử lý tốt nhất là gì?",
        "options": {
            "A": "Code Smell: Arrow Anti-pattern (Mã hình mũi tên); cách xử lý tốt nhất là áp dụng kỹ thuật 'Guard Clauses' (Thoát sớm - Early Return) để làm phẳng cấu trúc code",
            "B": "Code Smell: Large Class; cách xử lý là nhân đôi số dòng code",
            "C": "Code Smell: Dead Code; cách xử lý là xóa toàn bộ file",
            "D": "Không có vấn đề gì, lồng nhau càng sâu chứng tỏ thuật toán càng phức tạp"
        },
        "correct_answer": "A",
        "explanation": "Guard Clauses kiểm tra các điều kiện lỗi trước và return ngay lập tức, giúp loại bỏ các khối `else` lồng nhau, đưa mã nguồn trở lại cấu trúc tuyến tính dễ đọc."
    },
    {
        "id": 13,
        "difficulty": "medium",
        "question": "Hiện tượng 'Anti-pattern: Cây kem ốc quế' (Ice-cream Cone / Inverted Pyramid) trong kiểm thử phần mềm xảy ra khi nào?",
        "options": {
            "A": "Khi dự án tiêu tốn quá nhiều tiền để mua kem cho lập trình viên",
            "B": "Khi dự án có quá nhiều ca kiểm thử giao diện thủ công và E2E chậm chạp ở trên đỉnh, nhưng lại có quá ít hoặc hoàn toàn thiếu vắng các bài kiểm thử đơn vị (Unit Tests) tự động ở đáy tháp",
            "C": "Khi hệ thống không có giao diện đồ họa",
            "D": "Khi phần mềm bị đóng băng không hoạt động được"
        },
        "correct_answer": "B",
        "explanation": "Cây kem ốc quế đảo ngược khiến chi phí kiểm thử cực kỳ đắt đỏ, chạy test mất hàng giờ và khó định vị vị trí chính xác của dòng code sinh lỗi."
    },
    {
        "id": 14,
        "difficulty": "medium",
        "question": "Nguyên lý Single Responsibility Principle (SRP) trong bộ nguyên lý SOLID yêu cầu điều gì đối với một lớp (Class) hoặc mô-đun?",
        "options": {
            "A": "Một lớp phải chứa toàn bộ mã nguồn của toàn bộ dự án",
            "B": "Một lớp chỉ nên có một và chỉ một lý do duy nhất để thay đổi (chỉ đảm nhận một trách nhiệm chức năng duy nhất)",
            "C": "Mỗi lập trình viên chỉ được viết một class duy nhất trong dự án",
            "D": "Một lớp không được phép kế thừa từ lớp cha nào"
        },
        "correct_answer": "B",
        "explanation": "SRP quy định: 'A class should have one, and only one, reason to change'. Tách biệt các mối quan tâm (Separation of Concerns) giúp giảm thiểu ảnh hưởng lan truyền khi sửa code."
    },
    {
        "id": 15,
        "difficulty": "medium",
        "question": "Trong phương pháp TDD, tại sao bước đầu tiên BẮT BUỘC phải là viết một bài test BỊ LỖI (Red) trước khi được phép viết mã nguồn xử lý?",
        "options": {
            "A": "Để làm cho màn hình terminal đổi sang màu đỏ cho đẹp mắt",
            "B": "Để chứng minh rằng bài kiểm thử thực sự có khả năng phát hiện lỗi (không phải là một bài test luôn pass bất kể code sai) và giúp xác định chính xác mục tiêu thiết kế của hàm cần viết",
            "C": "Để chứng tỏ lập trình viên chưa làm việc",
            "D": "Vì đây là quy định bắt buộc của ngôn ngữ Java"
        },
        "correct_answer": "B",
        "explanation": "Nếu viết test sau khi có code hoặc test luôn xanh, ta không thể biết test có thực sự kiểm tra đúng logic nghiệp vụ hay không. Bước Red xác nhận bài test đang hoạt động chuẩn xác."
    },
    {
        "id": 16,
        "difficulty": "medium",
        "question": "Một API RESTful chuẩn mực để xóa một bài viết có ID là 42 nên sử dụng phương thức HTTP và đường dẫn nào sau đây?",
        "options": {
            "A": "GET /api/posts/delete/42",
            "B": "POST /api/deletePost?id=42",
            "C": "DELETE /api/posts/42",
            "D": "PUT /api/remove/42"
        },
        "correct_answer": "C",
        "explanation": "Chuẩn RESTful sử dụng danh từ số nhiều cho tài nguyên (`/posts/42`) và dùng đúng động từ HTTP (`DELETE`) để chỉ định hành động, không đặt động từ trong URL."
    },
    {
        "id": 17,
        "difficulty": "medium",
        "question": "Khi thực hiện Code Review một Pull Request, hành động nào sau đây bị coi là PHI NGUYÊN TẮC và thiếu tính xây dựng?",
        "options": {
            "A": "Chỉ trích gay gắt cá nhân lập trình viên bằng lời lẽ thô lỗ thay vì nhận xét khách quan về chất lượng của đoạn code",
            "B": "Đề xuất một giải pháp thuật toán tối ưu hơn kèm theo liên kết tài liệu tham khảo",
            "C": "Khen ngợi một đoạn xử lý logic thông minh và sạch sẽ",
            "D": "Yêu cầu bổ sung thêm ca kiểm thử cho trường hợp dữ liệu rỗng (Null input)"
        },
        "correct_answer": "A",
        "explanation": "Code Review là hoạt động rà soát kỹ thuật trên tinh thần đồng đội tôn trọng; tập trung vào 'Đoạn code này có thể cải tiến thế nào' thay vì công kích người viết."
    },
    {
        "id": 18,
        "difficulty": "medium",
        "question": "Khái niệm 'Code Coverage' (Độ bao phủ kiểm thử) đo lường điều gì và một con số 100% Code Coverage có đồng nghĩa với việc phần mềm hoàn toàn không còn lỗi (Bug-free) hay không?",
        "options": {
            "A": "Đo lường số lượng màn hình giao diện; 100% đồng nghĩa phần mềm không còn lỗi",
            "B": "Đo lường tỷ lệ phần trăm dòng lệnh hoặc nhánh mã nguồn được thực thi trong quá trình chạy test; 100% KHÔNG ĐỒNG NGHĨA phần mềm không có lỗi vì nó không phát hiện được các yêu cầu bị bỏ quên hoặc lỗi logic nghiệp vụ",
            "C": "Đo lường số giờ chạy máy tính của kiểm thử viên",
            "D": "Đo lường dung lượng RAM mà ứng dụng tiêu tốn"
        },
        "correct_answer": "B",
        "explanation": "Code coverage chỉ phản ánh code đã được chạy qua, không đảm bảo rằng các kịch bản biên hoặc hiểu sai yêu cầu người dùng đã được kiểm tra hết."
    },
    {
        "id": 19,
        "difficulty": "medium",
        "question": "Trong kiến trúc phân tầng, tại sao Controller TUYỆT ĐỐI KHÔNG NÊN gọi trực tiếp xuống Database hoặc viết câu lệnh SQL bên trong nó?",
        "options": {
            "A": "Vì Controller không có quyền truy cập vào mạng internet",
            "B": "Vì vi phạm nguyên lý tách biệt trách nhiệm (Separation of Concerns); làm cho logic nghiệp vụ bị trói chặt vào tầng giao diện, không thể tái sử dụng và cực kỳ khó khăn khi viết unit test",
            "C": "Vì các câu lệnh SQL chỉ chạy được trên hệ điều hành Linux",
            "D": "Vì SQL sẽ làm hỏng giao diện HTML của trang web"
        },
        "correct_answer": "B",
        "explanation": "Controller chỉ điều hướng yêu cầu. Việc giấu nghiệp vụ vào Service và giấu truy vấn vào Repository giúp dễ dàng thay đổi công nghệ cơ sở dữ liệu và mock dữ liệu khi test."
    },
    {
        "id": 20,
        "difficulty": "medium",
        "question": "Khái niệm 'Regression Testing' (Kiểm thử hồi quy) được hiểu chính xác là gì?",
        "options": {
            "A": "Kiểm thử phần mềm chạy trên các máy tính cổ đời cũ",
            "B": "Việc chạy lại toàn bộ hoặc một tập hợp các ca kiểm thử đã có để đảm bảo rằng các thay đổi mã nguồn mới (sửa bug hoặc thêm tính năng) không làm gãy hoặc phát sinh lỗi ở các tính năng cũ đang hoạt động ổn định",
            "C": "Kiểm thử tốc độ gõ phím của lập trình viên",
            "D": "Kiểm thử độ tương thích với trình duyệt Internet Explorer"
        },
        "correct_answer": "B",
        "explanation": "Kiểm thử hồi quy là tấm khiên bảo vệ hệ thống: mỗi lần thêm mã mới, hệ thống test tự động chạy lại để khẳng định những gì đã chạy hôm qua vẫn chạy tốt hôm nay."
    },
    {
        "id": 21,
        "difficulty": "medium",
        "question": "Chỉ số 'Độ phức tạp lặp vòng' (Cyclomatic Complexity) của Thomas McCabe đo lường điều gì trong một hàm mã nguồn?",
        "options": {
            "A": "Số lượng ký tự có trong file mã nguồn",
            "B": "Số lượng đường đi độc lập tuyến tính qua đồ thị dòng điều khiển của chương trình (dựa trên số lượng câu lệnh rẽ nhánh `if`, `while`, `for`, `switch`)",
            "C": "Tốc độ xử lý của vi xử lý khi chạy hàm đó",
            "D": "Số lượng biến toàn cục được khai báo trong chương trình"
        },
        "correct_answer": "B",
        "explanation": "Cyclomatic Complexity đo lường độ phân nhánh logic ($V(G) = E - N + 2P$). Điểm số càng cao ($> 10$) đồng nghĩa hàm càng phức tạp, càng nhiều nhánh rẽ và càng khó kiểm thử trọn vẹn."
    },
    {
        "id": 22,
        "difficulty": "medium",
        "question": "Trong giao thức HTTP, sự khác biệt căn bản giữa phương thức `PUT` và `PATCH` khi cập nhật tài nguyên qua REST API là gì?",
        "options": {
            "A": "`PUT` dùng cho máy tính để bàn, `PATCH` dùng cho điện thoại",
            "B": "`PUT` mang tính thay thế toàn bộ (Full replacement) tài nguyên bằng đối tượng mới gửi lên; còn `PATCH` chỉ áp dụng cập nhật cục bộ một phần (Partial update) các thuộc tính được chỉ định",
            "C": "`PUT` xóa tài nguyên, còn `PATCH` tạo tài nguyên mới",
            "D": "Hai phương thức này hoàn toàn giống hệt nhau về mặt đặc tả kỹ thuật"
        },
        "correct_answer": "B",
        "explanation": "Theo chuẩn RFC: `PUT` gửi toàn bộ entity để ghi đè hoàn toàn; `PATCH` chỉ gửi những trường thông tin cần thay đổi (ví dụ: chỉ sửa mỗi `status`)."
    },
    {
        "id": 23,
        "difficulty": "hard",
        "question": "Trong nguyên lý TDD, tại sao bước 'Refactor' lại được coi là bước KHÔNG THỂ THIẾU sau khi test đã chuyển sang màu xanh (Green)?",
        "options": {
            "A": "Vì trình biên dịch sẽ từ chối chạy code nếu không có refactor",
            "B": "Vì ở bước Green, lập trình viên thường viết mã nhanh nhất có thể (kể cả dùng code tạm, hardcode giá trị) chỉ để test pass; bước Refactor là cơ hội bắt buộc để dọn dẹp cấu trúc, khử trùng lặp, tối ưu thuật toán khi đã có bài test xanh bảo hộ an toàn",
            "C": "Vì khách hàng yêu cầu phải có commit mang tên Refactor",
            "D": "Vì Refactor giúp xóa bỏ các ca kiểm thử đã viết"
        },
        "correct_answer": "B",
        "explanation": "Nếu dừng lại ở Green, nợ kỹ thuật sẽ tích lũy ngay lập tức. Bước Refactor là chiếc then cài giúp nâng cao chất lượng mã nguồn mà không sợ làm hỏng logic nhờ có hệ thống test xanh bảo chứng."
    },
    {
        "id": 24,
        "difficulty": "hard",
        "question": "Giả sử một hàm xử lý chuyển tiền ngân hàng cần kiểm thử: `transferMoney(fromAcc, toAcc, amount)`. Để viết Unit Test độc lập và không làm biến đổi số dư tài khoản thật trong CSDL, kỹ sư nên áp dụng kỹ thuật nào?",
        "options": {
            "A": "Chuyển tiền thật bằng thẻ tín dụng cá nhân của tester",
            "B": "Áp dụng Dependency Injection (DI) để truyền vào một đối tượng giả lập `AccountRepositoryMock`, thiết lập hành vi giả lập (stubbing) và xác minh (verifying) các hàm được gọi",
            "C": "Tắt toàn bộ hệ thống kiểm thử tự động",
            "D": "Chỉ kiểm tra giao diện bằng mắt thường"
        },
        "correct_answer": "B",
        "explanation": "Sử dụng Dependency Injection kết hợp Mockito/Jest giúp thay thế repository thật bằng mock object, kiểm tra chính xác logic trừ/cộng tiền mà không chạm vào CSDL thật."
    },
    {
        "id": 25,
        "difficulty": "hard",
        "question": "Một đoạn mã nguồn vi phạm nguyên lý Open/Closed Principle (OCP) trong SOLID khi nào?",
        "options": {
            "A": "Khi file mã nguồn bị mở và đóng liên tục trong trình soạn thảo",
            "B": "Khi mỗi lần muốn bổ sung một loại hình thanh toán mới (ví dụ thêm Apple Pay), lập trình viên bắt buộc phải vào sửa đổi trực tiếp mã nguồn của lớp xử lý hiện tại bằng cách thêm nhánh `case` trong câu lệnh `switch` khổng lồ, thay vì mở rộng thông qua kế thừa hoặc interface",
            "C": "Khi phần mềm không hỗ trợ chuẩn mã nguồn mở",
            "D": "Khi hệ thống không có tính năng khóa tài khoản"
        },
        "correct_answer": "B",
        "explanation": "OCP quy định: 'Mở cho việc mở rộng, nhưng Đóng cho việc sửa đổi' (Open for extension, closed for modification). Thêm tính năng mới bằng cách tạo class mới cài đặt interface, không đụng vào code cũ đang chạy ổn định."
    },
    {
        "id": 26,
        "difficulty": "hard",
        "question": "Tại sao một ca kiểm thử đơn vị (Unit Test) phụ thuộc vào thời gian hệ thống thực tế (ví dụ: `new Date()`) hoặc độ trễ mạng thường bị coi là 'Flaky Test' (Kiểm thử chập chờn) và gây nguy hiểm cho pipeline CI?",
        "options": {
            "A": "Vì Flaky Test làm đồng hồ máy tính chạy nhanh hơn",
            "B": "Vì nó lúc Pass lúc Fail ngẫu nhiên dù mã nguồn không thay đổi, làm mất niềm tin của đội ngũ vào hệ thống kiểm thử tự động và khiến lập trình viên có thói quen phớt lờ cảnh báo lỗi đỏ trên CI",
            "C": "Vì nó làm tốn dung lượng lưu trữ trên GitHub",
            "D": "Vì Git không hỗ trợ kiểu dữ liệu thời gian"
        },
        "correct_answer": "B",
        "explanation": "Flaky test là kẻ thù số một của văn hóa tự động hóa: khi một test chập chờn thất bại không xác định, nhóm sẽ mất phản xạ cảnh giác và có xu hướng nhấn 'Run again' thay vì tìm lỗi thực sự."
    },
    {
        "id": 27,
        "difficulty": "hard",
        "question": "Trong kiến trúc REST, tính chất 'Idempotent' (Lũy thừa / Bất biến sau nhiều lần gọi) của một phương thức HTTP có nghĩa là gì? Phương thức nào sau đây KHÔNG mang tính Idempotent?",
        "options": {
            "A": "Lũy thừa nghĩa là thực hiện 1 lần hay n lần liên tiếp với cùng tham số đều cho cùng một trạng thái kết quả trên hệ thống; phương thức `POST` là phương thức KHÔNG mang tính Idempotent",
            "B": "Lũy thừa nghĩa là tốc độ thực thi tăng gấp đôi sau mỗi lần gọi; phương thức `GET` không lũy thừa",
            "C": "Lũy thừa nghĩa là mã hóa mật khẩu; phương thức `DELETE` không lũy thừa",
            "D": "Mọi phương thức HTTP đều mang tính Idempotent"
        },
        "correct_answer": "A",
        "explanation": "`GET`, `PUT`, `DELETE` mang tính Idempotent (xóa 1 lần hay 10 lần tài nguyên đó thì tài nguyên vẫn ở trạng thái biến mất). Trong khi đó, gọi `POST` 10 lần sẽ tạo ra 10 đơn hàng/bài viết khác nhau trong CSDL."
    },
    {
        "id": 28,
        "difficulty": "hard",
        "question": "Khái niệm 'Technical Spike' được nhóm áp dụng trong giai đoạn Sprint Planning khi nào?",
        "options": {
            "A": "Khi nhóm muốn tăng điểm số Story Points lên mức kỷ lục",
            "B": "Khi một User Story chứa đựng giải pháp công nghệ quá mới lạ hoặc kiến trúc chưa từng làm, nhóm quyết định phân bổ một khung thời gian ngắn để xây dựng một bản thử nghiệm chứng minh khái niệm (PoC - Proof of Concept) nhằm triệt tiêu rủi ro",
            "C": "Khi nhóm muốn tổ chức tiệc liên hoan",
            "D": "Khi cơ sở dữ liệu bị hỏng cần cài lại"
        },
        "correct_answer": "B",
        "explanation": "Spike giúp giảm thiểu sự bất định kỹ thuật: nhóm viết một đoạn code thử nghiệm ngắn để đo lường tính khả thi trước khi đưa ra cam kết chính thức."
    },
    {
        "id": 29,
        "difficulty": "hard",
        "question": "Kỹ thuật 'Mutation Testing' trong đánh giá chất lượng kiểm thử tự động có nguyên lý hoạt động là gì?",
        "options": {
            "A": "Cố tình biến đổi ngẫu nhiên cấu trúc mã nguồn (đổi `+` thành `-`, đổi `>` thành `<=`, đảo ngược điều kiện boolean) và chạy lại bộ test suite để kiểm tra xem hệ thống kiểm thử có phát hiện và 'tiêu diệt' (kill) được các lỗi nhân tạo này không",
            "B": "Sử dụng trí tuệ nhân tạo để tự động viết code thay cho lập trình viên",
            "C": "Thay đổi giao diện người dùng theo phong cách hoạt hình",
            "D": "Nén file mã nguồn để giảm dung lượng đĩa"
        },
        "correct_answer": "A",
        "explanation": "Mutation Testing đo lường chất lượng thực chất của bộ test: nếu code bị sửa sai mà bộ test vẫn báo xanh (mutant survived), chứng tỏ bài test đó viết hời hợt và thiếu các câu lệnh assert chuẩn xác."
    },
    {
        "id": 30,
        "difficulty": "hard",
        "question": "Trong buổi Sprint Review, khi nhóm trình diễn một tính năng nhưng khách hàng nhận xét: 'Giao diện và nghiệp vụ này chạy đúng như User Story nhưng không đúng với kỳ vọng kinh doanh thực tế của chúng tôi', phản ứng ĐÚNG ĐẮN NHẤT của Scrum Team là gì?",
        "options": {
            "A": "Cãi nhau với khách hàng và ép khách hàng phải ký biên bản nghiệm thu vì đã làm đúng từng câu chữ",
            "B": "Lắng nghe cởi mở, cảm ơn phản hồi quý báu của khách hàng; Product Owner ghi nhận sự khác biệt này thành các User Stories cải tiến mới trong Product Backlog để ưu tiên ở các Sprint sau theo đúng tinh thần Agile",
            "C": "Bắt lập trình viên phải thức trắng đêm làm lại ngay lập tức",
            "D": "Tuyên bố hủy hợp đồng dự án"
        },
        "correct_answer": "B",
        "explanation": "Mục đích tối thượng của Sprint Review là thu thập phản hồi sớm để thích nghi (Inspect & Adapt). Sự lệch pha giữa văn bản và kỳ vọng thực tế là điều bình thường và là cơ hội để sản phẩm tiến hóa hoàn thiện."
    }
]

SHORT_ANSWERS = [
    {
        "id": 1,
        "question": "Trình bày vai trò và trách nhiệm của 3 tầng cơ bản trong Kiến trúc Phân tầng (Layered Architecture): Controller, Service, Repository.",
        "expected_answer": "1. **Controller Layer:** Tiếp nhận yêu cầu HTTP từ client, kiểm tra hợp lệ sơ bộ tham số đầu vào (DTO validation) và định dạng dữ liệu trả về cho client.\n2. **Service Layer:** Chứa toàn bộ logic nghiệp vụ cốt lõi, điều phối các quy tắc tính toán và quản lý các giao dịch dữ liệu (Transactions).\n3. **Repository Layer:** Trực tiếp giao tiếp với cơ sở dữ liệu (thực thi câu lệnh SQL/ORM), trừu tượng hóa việc truy vấn và lưu trữ dữ liệu.",
        "explanation": "Kiến trúc này đảm bảo nguyên lý Tách biệt các mối quan tâm (Separation of Concerns)."
    },
    {
        "id": 2,
        "question": "Giải thích 3 bước trong chu trình phát triển hướng kiểm thử (TDD): Red - Green - Refactor.",
        "expected_answer": "1. **Red (Đỏ):** Viết một ca kiểm thử tự động (Unit Test) cho một hành vi tính năng mới và chạy kiểm thử để xác nhận bài test bị lỗi (Failed vì chưa có mã nguồn xử lý).\n2. **Green (Xanh):** Viết lượng mã nguồn tối thiểu cần thiết để bài kiểm thử vừa viết vượt qua thành công (Passed).\n3. **Refactor (Tái cấu trúc):** Tối ưu hóa, dọn dẹp cấu trúc mã nguồn, loại bỏ trùng lặp và áp dụng Clean Code trong khi vẫn đảm bảo bài kiểm thử tiếp tục xanh.",
        "explanation": "Đây là nhịp thở cốt lõi của TDD giúp tạo ra phần mềm có độ tin cậy cực cao."
    },
    {
        "id": 3,
        "question": "Mô tả 3 cấp độ chính trong Kim tự tháp kiểm thử (Testing Pyramid) và nêu tỷ lệ phân bổ khuyến nghị giữa các cấp độ.",
        "expected_answer": "1. **Unit Testing (Đáy tháp - ~70%):** Kiểm thử đơn vị các hàm, phương thức nhỏ; chạy cực nhanh, chi phí thấp, định vị lỗi chính xác.\n2. **Integration Testing (Thân tháp - ~20%):** Kiểm thử tích hợp giữa các module, kiểm tra giao tiếp giữa Service, Repository và Database thật.\n3. **End-to-End Testing (Đỉnh tháp - ~10%):** Kiểm thử đầu-cuối toàn bộ luồng nghiệp vụ qua giao diện người dùng; chạy chậm, tốn tài nguyên và dễ chập chờn.",
        "explanation": "Testing Pyramid đảm bảo phản hồi nhanh cho lập trình viên với chi phí vận hành tối ưu."
    },
    {
        "id": 4,
        "question": "Cấu trúc AAA (Arrange - Act - Assert) trong viết Unit Test gồm những bước cụ thể nào?",
        "expected_answer": "- **Arrange:** Chuẩn bị môi trường, khởi tạo các đối tượng, thiết lập dữ liệu mẫu đầu vào và cấu hình các đối tượng giả lập (Mocks/Stubs).\n- **Act:** Gọi phương thức hoặc hàm nghiệp vụ cần kiểm thử với tham số đã chuẩn bị.\n- **Assert:** Kiểm chứng kết quả trả về hoặc trạng thái mới của hệ thống có khớp chính xác với kỳ vọng đặt ra hay không.",
        "explanation": "Cấu trúc 3 chữ A giúp bài test tường minh, tách bạch rõ ràng giữa chuẩn bị, thực thi và kiểm tra."
    },
    {
        "id": 5,
        "question": "Nêu 4 tiêu chí cốt lõi cần kiểm tra khi thẩm duyệt mã nguồn (Code Review) một Pull Request của đồng nghiệp.",
        "expected_answer": "1. **Tính đúng đắn về nghiệp vụ:** Mã nguồn có giải quyết chính xác yêu cầu của User Story không? Thuật toán có đúng không?\n2. **Chất lượng mã nguồn (Clean Code):** Đặt tên có rõ nghĩa không? Hàm có ngắn gọn không? Có vi phạm nguyên lý DRY/KISS không?\n3. **Bảo mật & Hiệu năng:** Có nguy cơ SQL Injection/XSS không? Có vòng lặp vô hạn hay rò rỉ bộ nhớ không?\n4. **Độ bao phủ kiểm thử (Testing):** Đã có đủ unit test cho các trường hợp biên (Edge cases) và kịch bản lỗi chưa?",
        "explanation": "Code Review là tuyến phòng thủ chất lượng toàn diện của đội ngũ kỹ thuật."
    },
    {
        "id": 6,
        "question": "Kể tên 4 'Mùi hôi của code' (Code Smells) phổ biến trong lập trình và cách xử lý tương ứng cho một mùi hôi.",
        "expected_answer": "- 4 Code Smells: Long Method (Hàm quá dài), Large Class (Lớp quá đồ sộ), Duplicated Code (Code trùng lặp), Primitive Obsession (Lạm dụng kiểu dữ liệu nguyên thủy).\n-*Cách xử lý Long Method:* Áp dụng kỹ thuật tái cấu trúc 'Extract Method' (Tách hàm) để chia nhỏ hàm dài thành các hàm con có tên gọi rõ nghĩa, mỗi hàm chỉ đảm nhận một nhiệm vụ duy nhất.",
        "explanation": "Nhận diện Code Smells là bước đầu tiên để tiến hành Refactoring hiệu quả."
    },
    {
        "id": 7,
        "question": "Giải thích sự khác biệt giữa Test Stub và Test Mock trong kỹ thuật giả lập (Test Doubles).",
        "expected_answer": "- **Test Stub:** Cung cấp dữ liệu trả về cố định được định sẵn cho các lời gọi hàm trong quá trình test (State Verification - chỉ quan tâm dữ liệu trả về).\n- **Test Mock:** Đối tượng ghi nhận và kiểm chứng hành vi (Behavior Verification - kiểm tra xem hàm đó có được gọi đúng số lần, đúng thứ tự và đúng tham số kỳ vọng hay không).",
        "explanation": "Cả hai đều dùng để cô lập đơn vị kiểm thử nhưng khác nhau ở cơ chế kiểm chứng trạng thái hay hành vi."
    },
    {
        "id": 8,
        "question": "Tính toán Độ phức tạp lặp vòng (Cyclomatic Complexity) cho đoạn mã sau:\n```java\nif (a > 0 && b > 0) {\n    doSomething();\n} else if (c > 0) {\n    doOther();\n}\n```",
        "expected_answer": "Độ phức tạp $V(G) = 4$.\n*Giải thích:* Bắt đầu với điểm cơ sở là 1. Mỗi toán tử điều kiện rẽ nhánh cộng thêm 1 điểm:\n- Điều kiện `a > 0`: +1\n- Toán tử logic `&&` (nhánh rẽ thứ hai `b > 0`): +1\n- Điều kiện `else if (c > 0)`: +1\n$\\implies V(G) = 1 + 1 + 1 + 1 = 4$. Cần tối thiểu 4 ca kiểm thử để phủ hết mọi nhánh logic.",
        "explanation": "Toán tử logic `&&` và `||` tạo thêm một nhánh quyết định ngầm trong luồng điều khiển."
    }
]

ESSAYS = [
    {
        "id": 1,
        "title": "Thiết Kế Kiến Trúc Phân Tầng & Xây Dựng Ca Kiểm Thử TDD Cho Nghiệp Vụ Chuyển Tiền",
        "problem": "Bạn được giao nhiệm vụ phát triển module Chuyển tiền nội bộ cho một ứng dụng Ngân hàng số:\n1. Hãy thiết kế cấu trúc phân tầng (Controller, Service, Repository, Entity, DTO) và giải thích luồng dữ liệu khi Client gửi yêu cầu chuyển tiền.\n2. Phân tích các trường hợp kiểm thử biên (Edge cases) và rủi ro tương tranh (Concurrency) trong nghiệp vụ này.\n3. Áp dụng quy trình TDD (Red - Green - Refactor) và cấu trúc AAA để viết mã giả (Pseudocode) cho ca kiểm thử: 'Chuyển tiền thất bại khi số dư tài khoản nguồn không đủ'.",
        "solution_steps": [
            "Bước 1: Thiết kế kiến trúc phân tầng chuẩn mực\n- *TransferRequestDTO:* Chứa `fromAccountId`, `toAccountId`, `amount`, `message`.\n- *TransferController:* Nhận POST `/api/transfers`, validate DTO (số tiền $> 0$), gọi `transferService.executeTransfer(dto)`.\n- *TransferService:* Xử lý nghiệp vụ chính trong một Transaction Database:\n  1. Lấy thông tin tài khoản nguồn và đích qua `accountRepository`.\n  2. Kiểm tra số dư tài khoản nguồn $\\ge amount + fee$.\n  3. Trừ tiền tài khoản nguồn, cộng tiền tài khoản đích.\n  4. Tạo bản ghi giao dịch `TransactionHistory`.\n- *AccountRepository:* Cung cấp phương thức `findByIdWithLock(id)` (khóa bi quan Pessimistic Lock để chống race condition) và `save(account)`.",
            "Bước 2: Phân tích các trường hợp biên và rủi ro tương tranh\n- *Trường hợp biên (Edge cases):*\n  - Số tiền chuyển $\\le 0$ hoặc quá hạn mức một lần/ngày.\n  - Tài khoản nguồn trùng với tài khoản đích (`fromAccountId == toAccountId`).\n  - Tài khoản nguồn hoặc đích bị khóa, đóng hoặc không tồn tại.\n  - Số dư tài khoản nguồn bằng đúng số tiền cần chuyển (hết sạch số dư tối thiểu).\n- *Rủi ro tương tranh (Race Condition):* Hai yêu cầu chuyển tiền 5 triệu diễn ra đồng thời trong khi tài khoản chỉ có 6 triệu. Nếu không dùng cơ chế khóa cơ sở dữ liệu (`SELECT ... FOR UPDATE`), cả hai giao dịch đều đọc thấy còn 6 triệu và cùng thực hiện trừ tiền, dẫn đến tài khoản bị âm.",
            "Bước 3: Thực hành TDD và cấu trúc AAA cho ca kiểm thử số dư không đủ\n```java\n// Bước 1: RED - Viết ca kiểm thử trước khi viết mã xử lý\n@Test\nvoid transferMoney_InsufficientBalance_ShouldThrowException() {\n    // 1. ARRANGE (Chuẩn bị)\n    Account fromAcc = new Account(\"ACC01\", 1000.0); // Chỉ có 1,000\n    Account toAcc = new Account(\"ACC02\", 500.0);\n    TransferRequestDTO request = new TransferRequestDTO(\"ACC01\", \"ACC02\", 2000.0); // Chuyển 2,000\n    \n    // Giả lập Repository trả về đối tượng fromAcc khi tìm ID ACC01\n    when(accountRepository.findById(\"ACC01\")).thenReturn(Optional.of(fromAcc));\n    when(accountRepository.findById(\"ACC02\")).thenReturn(Optional.of(toAcc));\n\n    // 2. ACT & 3. ASSERT (Kích hoạt và Kiểm chứng)\n    assertThrows(InsufficientBalanceException.class, () -> {\n        transferService.executeTransfer(request);\n    });\n    \n    // Xác minh không có lệnh lưu (save) nào được thực hiện\n    verify(accountRepository, never()).save(any());\n}\n```\n- *Bước 2: GREEN:* Viết logic `if (fromAcc.getBalance() < amount) throw new InsufficientBalanceException();` trong `TransferService` để test chuyển sang màu xanh.\n- *Bước 3: REFACTOR:* Tách logic kiểm tra số dư thành hàm `fromAcc.hasSufficientBalance(amount)` nằm ngay trong Entity `Account` để tuân thủ nguyên lý Đóng gói (Encapsulation) và Domain-Driven Design."
        ]
    },
    {
        "id": 2,
        "title": "Tái Cấu Trúc Mã Nguồn (Refactoring) & Khử Các 'Mùi Hôi Của Code' (Code Smells)",
        "problem": "Cho một đoạn mã nguồn Java tính toán chiết khấu đơn hàng thực tế của một dự án cũ:\n```java\npublic class OrderService {\n    public double calc(Order o, String t, boolean vip) {\n        double d = 0;\n        if (t.equals(\"BOOK\")) {\n            if (o.total > 500000) {\n                if (vip) { d = o.total * 0.2; }\n                else { d = o.total * 0.1; }\n            } else { d = o.total * 0.05; }\n        } else if (t.equals(\"ELECTRONIC\")) {\n            if (o.total > 2000000) {\n                if (vip) { d = o.total * 0.15; }\n                else { d = o.total * 0.08; }\n            }\n        }\n        return d;\n    }\n}\n```\n1. Hãy chỉ ra ít nhất 4 Code Smells nghiêm trọng trong đoạn mã trên.\n2. Phân tích sự vi phạm các nguyên lý thiết kế SOLID (đặc biệt là Single Responsibility và Open/Closed Principle).\n3. Tiến hành tái cấu trúc lại đoạn mã trên áp dụng Clean Code, Guard Clauses hoặc Strategy Pattern kèm mã nguồn mới rõ ràng.",
        "solution_steps": [
            "Bước 1: Chỉ ra 4 Code Smells nghiêm trọng\n1. *Poor Naming (Đặt tên cẩu thả):* Tên hàm `calc`, biến `o`, `t`, `d` không bộc lộ bất kỳ ý nghĩa nghiệp vụ nào.\n2. *Arrow Anti-pattern / Deep Nesting:* Ba tầng `if-else` lồng nhau sâu hoắm, cực kỳ khó đọc và dễ phát sinh lỗi logic.\n3. *Primitive Obsession & Magic Strings:* Sử dụng chuỗi thô `\"BOOK\"`, `\"ELECTRONIC\"` thay vì dùng Enum hoặc Class đa hình, rất dễ bị lỗi chính tả khi chạy.\n4. *Hardcoded Magic Numbers:* Các con số tỷ lệ chiết khấu (`0.2`, `0.1`, `0.05`) và ngưỡng tiền (`500000`, `2000000`) bị gắn cứng rải rác khắp code.",
            "Bước 2: Phân tích vi phạm nguyên lý SOLID\n- *Vi phạm Single Responsibility Principle (SRP):* Lớp `OrderService` phải gánh vác việc kiểm tra điều kiện chiết khấu cho mọi loại hàng hóa khác nhau.\n- *Vi phạm Open/Closed Principle (OCP):* Mỗi khi doanh nghiệp bán thêm ngành hàng mới (ví dụ: `\"CLOTHES\"`), lập trình viên bắt buộc phải sửa đổi trực tiếp vào thân hàm `calc`, thêm nhánh `else if` mới, tiềm ẩn nguy cơ làm hỏng logic của sách và đồ điện tử đang chạy ổn định.",
            "Bước 3: Tái cấu trúc áp dụng Strategy Pattern và Clean Code\n```java\n// 1. Định nghĩa Interface Strategy\npublic interface DiscountStrategy {\n    boolean isApplicable(ProductCategory category);\n    double calculateDiscount(double orderTotal, boolean isVipCustomer);\n}\n\n// 2. Cài đặt Strategy cho Sách\npublic class BookDiscountStrategy implements DiscountStrategy {\n    private static final double HIGH_TIER_THRESHOLD = 500_000.0;\n    \n    @Override\n    public boolean isApplicable(ProductCategory category) {\n        return category == ProductCategory.BOOK;\n    }\n\n    @Override\n    public double calculateDiscount(double total, boolean isVip) {\n        if (total <= HIGH_TIER_THRESHOLD) return total * 0.05;\n        return isVip ? total * 0.20 : total * 0.10;\n    }\n}\n\n// 3. Service sạch sẽ tuân thủ OCP\npublic class OrderService {\n    private final List<DiscountStrategy> discountStrategies;\n\n    public OrderService(List<DiscountStrategy> strategies) {\n        this.discountStrategies = strategies;\n    }\n\n    public double calculateDiscount(Order order, ProductCategory category, boolean isVip) {\n        return discountStrategies.stream()\n            .filter(strategy -> strategy.isApplicable(category))\n            .findFirst()\n            .map(strategy -> strategy.calculateDiscount(order.getTotalAmount(), isVip))\n            .orElse(0.0);\n    }\n}\n```\n- *Kết quả:* Mã nguồn sạch sẽ, tên rõ nghĩa, không còn `if-else` lồng nhau, khi có ngành hàng mới chỉ cần tạo class mới mà không cần chạm vào `OrderService`."
        ]
    },
    {
        "id": 3,
        "title": "Thiết Kế Chiến Lược Kiểm Thử Kim Tự Tháp Cho Hệ Thống Đặt Vé Xem Phim",
        "problem": "Một công ty phát triển Cổng Đặt Vé Xem Phim Trực Tuyến đang gặp khủng hoảng: Đội QA mất 3 ngày chạy kiểm thử thủ công trước mỗi đợt release nhưng vẫn bỏ sót lỗi ghế bị đặt trùng trên Production.\nHãy đóng vai trò là QA Lead / Software Architect:\n1. Phân tích nguyên nhân thất bại của chiến lược kiểm thử hiện tại.\n2. Thiết kế lại chiến lược kiểm thử tự động toàn diện theo mô hình Kim tự tháp kiểm thử (Testing Pyramid).\n3. Phác thảo danh sách các ca kiểm thử cụ thể cho tính năng 'Chọn ghế và Giữ chỗ trong 5 phút' ở cả 3 tầng: Unit Test, Integration Test và End-to-End Test.",
        "solution_steps": [
            "Bước 1: Phân tích nguyên nhân thất bại hiện tại\n- Đội ngũ rơi vào bẫy 'Cây kem ốc quế' (Ice-cream cone): Phụ thuộc 100% vào kiểm thử thủ công qua màn hình UI, tốn quá nhiều thời gian nhưng không thể bao quát hết các kịch bản tương tranh.\n- Lỗi đặt trùng ghế (Double Booking) là lỗi tương tranh dữ liệu (Race Condition) ở tầng backend; kiểm thử thủ công bằng mắt người với 1-2 tài khoản không thể mô phỏng được hành vi của hàng trăm người cùng bấm chọn một chiếc ghế ở cùng một phần nghìn giây.",
            "Bước 2: Thiết kế lại chiến lược theo Kim tự tháp kiểm thử\n- *Tầng 1 - Unit Test (~70% số lượng test):* Kiểm tra logic nghiệp vụ độc lập: Kiểm tra trạng thái ghế (Trống $\\to$ Đang giữ $\\to$ Đã bán), thuật toán tính giá vé theo suất chiếu và độ tuổi, thuật toán đếm ngược 5 phút hết hạn giữ chỗ. Chạy trên máy dev trong vài giây.\n- *Tầng 2 - Integration Test (~20% số lượng test):* Kiểm tra tích hợp cơ sở dữ liệu và khóa giao dịch: Kiểm tra transaction DB, cơ chế khóa chỗ bằng Redis hoặc Optimistic Locking, đảm bảo 2 transaction đồng thời chọn cùng 1 ghế thì transaction thứ 2 sẽ bị từ chối.\n- *Tầng 3 - E2E Test (~10% số lượng test):* Sử dụng Cypress/Playwright chạy tự động trên trình duyệt: Mô phỏng hành trình từ lúc khách xem danh sách phim $\\to$ chọn rạp $\\to$ chọn ghế $\\to$ thanh toán thành công và nhận vé điện tử.",
            "Bước 3: Phác thảo ca kiểm thử cụ thể cho tính năng 'Giữ ghế 5 phút'\n- **Unit Test:**\n  - Test 1: Ghế đang ở trạng thái `AVAILABLE`, gọi `holdSeat(userId, 5_MINUTES)` thì trạng thái chuyển thành `HELD` và `holdExpiresAt` được gán chính xác bằng thời điểm hiện tại + 5 phút.\n  - Test 2: Ghế đang ở trạng thái `HELD` nhưng `holdExpiresAt` đã quá hạn, gọi `isAvailable()` phải trả về `true` (tự động giải phóng ghế).\n- **Integration Test:**\n  - Test 3: Tạo 10 threads song song cùng gửi yêu cầu giữ ghế số `D8` của suất chiếu `S100`. Kiểm chứng: Chỉ duy nhất 1 thread trả về mã HTTP 200 Created, 9 threads còn lại phải nhận mã HTTP 409 Conflict.\n- **E2E Test:**\n  - Test 4: Trình duyệt mở sơ đồ rạp $\\to$ Click chọn ghế `E5` $\\to$ Ghế chuyển sang màu vàng (đang giữ) $\\to$ Đồng hồ đếm ngược 5:00 bắt đầu chạy $\\to$ Hết 5 phút không thanh toán, ghế tự đổi lại màu trắng (trống) và hiển thị thông báo phiên giữ chỗ hết hạn."
        ]
    },
    {
        "id": 4,
        "title": "Thiết Kế Quy Trình Thẩm Duyệt Mã Nguồn (Code Review) Chuyên Nghiệp Trong Nhóm Kỹ Thuật",
        "problem": "Một doanh nghiệp công nghệ phát triển nhanh từ 5 lên 30 kỹ sư phần mềm. Tốc độ merge code tăng vọt nhưng kéo theo chất lượng đi xuống: Nhiều đoạn code cẩu thả, không có unit test và chứa lỗ hổng bảo mật nghiêm trọng vẫn được merge vào nhánh chính vì các đồng nghiệp review hời hợt theo kiểu 'LGTM' (Looks Good To Me).\nHãy xây dựng Bộ Quy Chuẩn Thẩm Duyệt Mã Nguồn (Code Review Framework) cho công ty:\n1. Xây dựng bộ tiêu chí kiểm tra bắt buộc (Code Review Checklist) gồm 4 khía cạnh: Tính đúng đắn, Kiến trúc, Bảo mật và Kiểm thử.\n2. Thiết lập quy định về quy mô và thời gian thẩm duyệt một Pull Request để tránh quá tải nhận thức (Cognitive Overload) cho Reviewer.\n3. Đề xuất giải pháp tự động hóa tích hợp vào GitHub Actions để giảm bớt gánh nặng kiểm tra thủ công cho con người.",
        "solution_steps": [
            "Bước 1: Xây dựng Code Review Checklist toàn diện\n- *1. Tính đúng đắn & Logic:* Code có thỏa mãn đúng Acceptance Criteria của User Story không? Các điều kiện rẽ nhánh có bao phủ hết trường hợp biên (Null, rỗng, số âm) không? Có bẫy rò rỉ tài nguyên (chưa đóng kết nối file/DB) không?\n- *2. Kiến trúc & Clean Code:* Có tuân thủ kiến trúc phân tầng không? Tên biến/hàm có trong sáng không? Có lặp code (vi phạm DRY) không? Có tuân thủ Single Responsibility không?\n- *3. An toàn & Bảo mật:* Có nguy cơ tấn công SQL Injection (dùng Parameterized Query chưa)? Dữ liệu nhạy cảm có bị log ra console không? Có kiểm tra quyền truy cập (Authorization) ở API endpoint không?\n- *4. Kiểm thử (Testing):* Có viết đủ unit tests không? Các ca kiểm thử có thực sự kiểm chứng logic (có đủ câu lệnh Assert rõ ràng) hay chỉ chạy cho có code coverage?",
            "Bước 2: Quy định về quy mô và thời lượng Pull Request\n- *Quy mô giới hạn:* Một Pull Request lý tưởng không nên vượt quá **200 - 400 dòng thay đổi (Lines of Code)** và chỉ tập trung vào một User Story duy nhất. Nghiên cứu của Cisco chỉ ra rằng khi review một PR dài trên 500 dòng, khả năng phát hiện lỗi của con người giảm đi hơn 70% do quá tải nhận thức.\n- *Thời gian phản hồi (SLA):* Mọi PR phải được phản hồi lần đầu trong vòng **24 giờ làm việc**. Tác giả PR có trách nhiệm tự review lại mã nguồn của chính mình trước khi gửi lời mời cho đồng nghiệp.\n- *Nguyên tắc phê duyệt:* Bắt buộc phải có tối thiểu 2 sự phê duyệt (Approve) từ 2 kỹ sư khác nhau trước khi được phép merge.",
            "Bước 3: Tự động hóa kiểm tra trước khi đến tay con người (Automated CI Gates)\nCấu hình GitHub Actions tự động chặn các lỗi cơ bản để Reviewer chỉ cần tập trung vào tư duy logic cao cấp:\n1. *Tự động Linter & Code Formatter:* Chạy SonarQube hoặc ESLint/Checkstyle để tự động bắt lỗi cú pháp, khoảng trắng, quy ước đặt tên và các lỗi tiềm ẩn.\n2. *Tự động Chạy Kiểm thử:* Chạy toàn bộ Unit Tests và Integration Tests tự động; nếu có dù chỉ 1 test bị Fail thì tự động khóa nút Merge.\n3. *Tự động Đo lường Code Coverage:* Sử dụng Codecov/JaCoCo kiểm tra độ bao phủ mã nguồn mới; nếu PR có tỷ lệ coverage dưới 80% thì tự động cảnh báo từ chối.\n4. *Tự động Quét Lỗ hổng Bảo mật:* Sử dụng GitHub Dependabot và Snyk quét các thư viện phụ thuộc để phát hiện ngay các phiên bản chứa mã độc hoặc lỗ hổng CVE đã công bố."
        ]
    }
]
