# -*- coding: utf-8 -*-
"""Data definition for Chương 1: Tổng quan về Công nghệ Phần mềm."""

CHAPTER_ID = "chuong_1"
CHAPTER_NUMBER = 1
CHAPTER_TITLE = "Chương 1: Tổng quan về Công nghệ phần mềm"
CHAPTER_SUMMARY = "Khái niệm phần mềm, khủng hoảng phần mềm, định nghĩa CNPM, vòng đời phát triển phần mềm (SDLC), thuộc tính chất lượng phần mềm, vai trò dự án & kỹ năng chữ T, quản lý mã nguồn cơ bản với Git."

THEORY_MD = """# CHƯƠNG 1: TỔNG QUAN VỀ CÔNG NGHỆ PHẦN MỀM

## 1. Khái niệm và Bản chất của Phần mềm
- **Phần mềm (Software):** Tập hợp các chỉ dẫn lập trình (chương trình máy tính), cấu trúc dữ liệu và tài liệu hướng dẫn nhằm thực hiện các nhiệm vụ cụ thể trên máy tính hoặc thiết bị điện tử.
- **Đặc tính cơ bản của phần mềm:**
  - Là sản phẩm **vô hình, phi vật lý**: Được phát triển hoặc kỹ nghệ hóa (engineered), không phải được chế tạo theo nghĩa công nghiệp truyền thống.
  - **Không bị hao mòn vật lý (Wear out):** Phần mềm không bị mòn cơ học theo thời gian như phần cứng; tuy nhiên nó bị **thoái hóa (Deterioration)** do các thay đổi môi trường hệ điều hành, thư viện phụ thuộc và lỗi tích tụ qua các lần vá chắp vá.
  - Phần lớn phần mềm vẫn được tùy biến theo yêu cầu riêng, mặc dù xu hướng tái sử dụng thành phần (Component-based reuse) ngày càng phát triển.

## 2. Khủng hoảng Phần mềm (Software Crisis) & Sự ra đời của CNPM
- **Khủng hoảng phần mềm (thập niên 1960 - 1970):** Xuất hiện khi phần cứng máy tính phát triển vượt bậc về năng lực tính toán, trong khi phương pháp phát triển phần mềm mang tính cá nhân, tự phát (ad-hoc), dẫn đến:
  - Chi phí dự án vượt xa dự toán ban đầu (Cost overrun).
  - Trễ hạn bàn giao nghiêm trọng (Schedule delay).
  - Chất lượng kém, chứa nhiều lỗi nghiêm trọng khi vận hành thực tế.
  - Chi phí bảo trì khổng lồ, khó nâng cấp và mở rộng.
- **Định nghĩa Công nghệ Phần mềm (IEEE Standard 610.12):**
  > *"Công nghệ phần mềm là việc áp dụng một cách tiếp cận có hệ thống, có kỷ luật và định lượng được vào việc phát triển, vận hành và bảo trì phần mềm; nghĩa là áp dụng kỹ nghệ (engineering) vào phần mềm."*

## 3. Vòng đời Phát triển Phần mềm (SDLC - Software Development Life Cycle)
Vòng đời phát triển phần mềm bao gồm các giai đoạn cốt lõi:
1. **Phân tích yêu cầu (Requirements Analysis):** Thu thập, làm rõ và tài liệu hóa những gì hệ thống cần thực hiện.
2. **Thiết kế hệ thống & kiến trúc (Architecture & System Design):** Xác định cấu trúc tổng thể, mô hình dữ liệu, giao diện API và công nghệ sử dụng.
3. **Cài đặt & Lập trình (Implementation / Coding):** Chuyển hóa thiết kế thành mã nguồn chạy được bằng ngôn ngữ lập trình.
4. **Kiểm thử phần mềm (Testing):** Xác minh (Verification) và thẩm định (Validation) để phát hiện và khắc phục lỗi trước khi bàn giao.
5. **Triển khai (Deployment):** Đưa phần mềm vào môi trường vận hành thực tế (Production).
6. **Vận hành & Bảo trì (Maintenance):** Khắc phục lỗi phát sinh, thích ứng môi trường mới và mở rộng tính năng.

```mermaid
graph LR
    A["1. Phân tích Yêu cầu"] --> B["2. Thiết kế Kiến trúc"]
    B --> C["3. Cài đặt Mã nguồn"]
    C --> D["4. Kiểm thử Chất lượng"]
    D --> E["5. Triển khai Hệ thống"]
    E --> F["6. Vận hành & Bảo trì"]
    F -.->|Cải tiến & Phản hồi| A
```

## 4. Các Thuộc tính Chất lượng Phần mềm (Software Quality Attributes)
Theo chuẩn ISO/IEC 25010, chất lượng phần mềm được đánh giá qua các trục cốt lõi:
- **Tính tin cậy (Reliability):** Khả năng duy trì mức độ hoạt động ổn định trong các điều kiện xác định qua một khoảng thời gian (MTBF - Mean Time Between Failures).
- **Tính hiệu năng (Performance Efficiency):** Thời gian đáp ứng nhanh, thông lượng cao và sử dụng tối ưu tài nguyên (CPU, RAM, Network).
- **Tính bảo mật (Security):** Bảo vệ dữ liệu và thông tin người dùng trước sự truy cập trái phép, tính toàn vẹn và chống chối bỏ.
- **Tính khả dụng (Usability):** Giao diện trực quan, dễ học, dễ sử dụng và hạn chế thao tác nhầm lẫn của người dùng.
- **Tính dễ bảo trì (Maintainability):** Mã nguồn rõ ràng, kiến trúc module hóa giúp dễ phân tích lỗi, dễ sửa đổi và kiểm thử hồi quy.
- **Tính tương thích & Di động (Portability):** Khả năng chuyển dịch và hoạt động mượt mà trên nhiều nền tảng, hệ điều hành khác nhau.

## 5. Vai trò Dự án & Mô hình Kỹ năng Chữ T (T-Shaped Skills)
- **Các vai trò chủ chốt:**
  - **Project Manager (PM):** Quản lý tiến độ, ngân sách, nhân sự và quản trị rủi ro.
  - **Product Owner (PO):** Đại diện cho khách hàng/người dùng, chịu trách nhiệm về tầm nhìn sản phẩm và giá trị của Product Backlog.
  - **Business Analyst (BA):** Cầu nối giữa khách hàng và đội ngũ kỹ thuật, làm rõ yêu cầu nghiệp vụ.
  - **Software Architect:** Quyết định kiến trúc hệ thống, khung công nghệ và chuẩn mực thiết kế.
  - **Software Developer (Dev):** Xây dựng tính năng, viết clean code và unit tests.
  - **QA/QC Engineer (Tester):** Thiết kế kịch bản kiểm thử, kiểm tra chất lượng và đảm bảo sản phẩm đáp ứng tiêu chí nghiệm thu.
  - **DevOps Engineer:** Tự động hóa quy trình CI/CD, giám sát hạ tầng và môi trường triển khai.
- **Mô hình Kỹ năng Chữ T (T-shaped Skills):**
  - **Thanh ngang:** Bề rộng kiến thức liên ngành (hiểu về quy trình Agile, Git, UI/UX, kiểm thử cơ bản, kỹ năng giao tiếp).
  - **Thanh dọc:** Chuyên môn kỹ thuật sâu sắc ở một lĩnh vực mũi nhọn (ví dụ: Chuyên sâu về Backend Node.js/Java, hoặc Database Optimization).

## 6. Quản lý Mã nguồn Cơ bản với Git
- **Ba trạng thái (Three States) của tập tin trong Git:**
  1. **Working Directory:** Thư mục làm việc thực tế chứa mã nguồn đang được chỉnh sửa.
  2. **Staging Area (Index):** Khu vực tạm lưu giữ các thay đổi được chọn lọc để đưa vào bản commit kế tiếp.
  3. **Repository (.git directory):** Cơ sở dữ liệu lịch sử lưu trữ vĩnh viễn các commit snapshots.
- **Các lệnh Git cơ bản:**
  - `git init`: Khởi tạo kho lưu trữ Git cục bộ mới.
  - `git status`: Kiểm tra trạng thái các tập tin (untracked, modified, staged).
  - `git add <file>` / `git add .`: Đưa thay đổi vào Staging Area.
  - `git commit -m "Thông điệp"`: Tạo bản lưu snapshot vĩnh viễn với thông điệp rõ nghĩa.
  - `git log --oneline`: Xem lịch sử các commit đã thực hiện.
  - `git diff`: So sánh sự khác biệt giữa Working Directory và Staging Area.
"""

TOPIC_SUMMARY = """# Chuyên Đề: Tổng quan SDLC & Quản Lý Mã Nguồn với Git

## 1. Khủng hoảng Phần mềm và Sự cần thiết của Quy trình Kỹ nghệ
- Khủng hoảng phần mềm bắt nguồn từ sự phức tạp ngày càng tăng của hệ thống trong khi phương pháp phát triển mang tính thủ công, thiếu kiểm soát.
- Kỹ nghệ phần mềm (Software Engineering) ra đời nhằm chuyển đổi việc viết phần mềm từ "nghệ thuật cá nhân" thành một "ngành kỹ thuật có quy chuẩn", có khả năng dự đoán chi phí, thời gian và chất lượng.

## 2. Vòng đời SDLC & Trục Đánh giá Chất lượng
- SDLC định hình đường đi của một phần mềm từ lúc khởi tạo ý tưởng đến khi ngừng hoạt động.
- Trục chất lượng phần mềm không chỉ nằm ở "chạy đúng chức năng" mà phải thỏa mãn đồng thời:
  - Chất lượng bên ngoài: Độ tin cậy, thời gian phản hồi, tính bảo mật, trải nghiệm người dùng.
  - Chất lượng bên trong: Dễ đọc (Readability), Dễ bảo trì (Maintainability), Dễ mở rộng (Extensibility) và Khả năng kiểm thử (Testability).

## 3. Kiến trúc Không gian Làm việc của Git
- Git theo mô hình phân tán (Distributed Version Control System - DVCS), mỗi lập trình viên sở hữu toàn bộ lịch sử commit tại máy cục bộ.
- Chu trình làm việc chuẩn: Chỉnh sửa tại Working Directory $\to$ `git add` vào Staging Area $\to$ `git commit` lưu vào Local Repo $\to$ `git push` đồng bộ lên Remote Repo (GitHub/GitLab).
"""

PARSED_MARKDOWN = f"""# Giáo trình Công nghệ Phần mềm - Chương 1: Tổng quan về Công nghệ Phần mềm
<!-- Nguồn: TS. Trần Văn Long - Khoa Tin học, Đại học Sư phạm, Đại học Huế -->

<!-- PAGE 1 -->
## A. Mục tiêu Bài học
1. Trình bày được bối cảnh lịch sử, định nghĩa và tầm quan trọng của ngành Công nghệ Phần mềm (CNPM).
2. Mô tả các hoạt động cốt lõi trong Vòng đời Phát triển Phần mềm (SDLC) và các thuộc tính chất lượng của sản phẩm phần mềm.
3. Hiểu rõ các vai trò nghề nghiệp trong dự án phần mềm và ý nghĩa của mô hình kỹ năng chữ T (T-shaped skills).
4. Cài đặt, cấu hình và sử dụng thành thạo các lệnh Git cơ bản (`init`, `status`, `add`, `commit`, `log`, `diff`) để quản lý phiên bản mã nguồn cục bộ.
5. Nhận thức rõ sự khác biệt mang tính sống còn giữa phát triển kỹ thuật có quy chuẩn và làm việc tự phát.

<!-- PAGE 3 -->
## B. Nội dung Chi tiết

### I. Các khái niệm Cơ bản về Phần mềm & CNPM
- **Phần mềm là gì?** Phần mềm không đơn thuần là các dòng mã nguồn (source code) mà là một tập hợp hoàn chỉnh gồm: Chương trình máy tính thực thi, cấu trúc dữ liệu lưu trữ và tài liệu kỹ thuật/hướng dẫn sử dụng.
- **Đặc trưng phân biệt phần mềm với phần cứng:**
  - Phần mềm được kỹ nghệ hóa (software is engineered), không chế tạo theo dây chuyền vật lý.
  - Phần mềm không bị mòn cơ học theo thời gian mà suy thoái (deteriorates) do sự biến đổi của môi trường và các lần sửa lỗi chắp vá thiếu kiểm soát.
  - Khó đo lường độ phức tạp và tiến độ bằng trực quan thông thường.

### II. Khủng hoảng Phần mềm (Software Crisis)
- Nguyên nhân sâu xa: Độ phức tạp của phần mềm tăng theo hàm mũ, sự phụ thuộc quá mức vào các cá nhân "ngôi sao", thiếu quy trình kiểm thử và quản lý yêu cầu.
- Hậu quả: Nhiều dự án thất bại hoàn toàn, chi phí bảo trì chiếm hơn 70-80% tổng chi phí vòng đời của một hệ thống phần mềm.
- Giải pháp: Định hình ngành Công nghệ Phần mềm (NATO Science Committee, Garmisch, 1968) áp dụng nguyên lý công nghệ vào phần mềm.

### III. Vòng đời Phát triển Phần mềm (SDLC)
- Các công đoạn cốt lõi: Phân tích yêu cầu $\to$ Thiết kế hệ thống $\to$ Lập trình $\to$ Kiểm thử $\to$ Triển khai $\to$ Vận hành & Bảo trì.
- Các thuộc tính chất lượng: Độ tin cậy (Reliability), Hiệu năng (Efficiency), Bảo mật (Security), Khả dụng (Usability), Dễ bảo trì (Maintainability), Tương thích (Portability).

### IV. Vai trò và Kỹ năng Lập trình viên
- Đội ngũ dự án: Project Manager, Product Owner, Business Analyst, Software Architect, Software Engineer, QA/QC Tester, DevOps Engineer.
- Tư duy kỹ năng chữ T (T-shaped): Kết hợp sự am hiểu rộng rãi về quy trình, giao tiếp, kiểm thử và năng lực chuyên sâu vào một công nghệ mũi nhọn.

### V. Quản lý Phiên bản Mã nguồn với Git
- Khái niệm hệ thống quản lý phiên bản phân tán (DVCS).
- Ba khu vực làm việc: Working Tree, Staging Area, Local Repository.
- Thao tác thực hành cơ bản: Cấu hình danh tính, khởi tạo repo, theo dõi trạng thái, ghi nhận snapshot.
"""

MULTIPLE_CHOICE = [
    {
        "id": 1,
        "difficulty": "easy",
        "question": "Thuộc tính nào sau đây thể hiện ĐẶC TRƯNG CỐT LÕI của phần mềm so với sản phẩm phần cứng truyền thống?",
        "options": {
            "A": "Phần mềm bị hao mòn vật lý theo thời gian sử dụng",
            "B": "Phần mềm là sản phẩm vô hình và được kỹ nghệ hóa (engineered) chứ không sản xuất theo dây chuyền cơ học",
            "C": "Phần mềm không bao giờ bị lỗi sau khi đã triển khai",
            "D": "Phần mềm có chi phí sản xuất tăng đều theo số lượng bản sao chép đĩa"
        },
        "correct_answer": "B",
        "explanation": "Phần mềm là sản phẩm vô hình, phi vật lý. Nó không bị hao mòn cơ học (wear out) như máy móc phần cứng mà thoái hóa (deteriorate) do sự thay đổi của môi trường và quá trình sửa đổi mã nguồn."
    },
    {
        "id": 2,
        "difficulty": "easy",
        "question": "Hiện tượng 'Khủng hoảng phần mềm' (Software Crisis) bùng nổ vào cuối thập niên 1960 chủ yếu do nguyên nhân nào?",
        "options": {
            "A": "Phần cứng máy tính quá yếu không thể chạy được các hệ điều hành",
            "B": "Sự phát triển vượt bậc của năng lực phần cứng khiến độ phức tạp của bài toán tăng vọt, trong khi phương pháp viết phần mềm tự phát, thiếu quy trình có hệ thống",
            "C": "Các ngôn ngữ lập trình bậc cao chưa xuất hiện",
            "D": "Chi phí mua máy tính cá nhân quá đắt đỏ"
        },
        "correct_answer": "B",
        "explanation": "Khủng hoảng phần mềm xảy ra khi bài toán trở nên phức tạp và phần cứng mạnh mẽ hơn, nhưng kỹ thuật lập trình tự phát (ad-hoc) không thể kiểm soát được tiến độ, chi phí và chất lượng của các hệ thống quy mô lớn."
    },
    {
        "id": 3,
        "difficulty": "easy",
        "question": "Theo tiêu chuẩn IEEE 610.12, Công nghệ Phần mềm (Software Engineering) được định nghĩa là gì?",
        "options": {
            "A": "Kỹ năng lập trình nhanh nhất bằng một ngôn ngữ lập trình cụ thể",
            "B": "Việc áp dụng một cách tiếp cận có hệ thống, có kỷ luật và định lượng được vào việc phát triển, vận hành và bảo trì phần mềm",
            "C": "Nghệ thuật cài đặt hệ điều hành và tối ưu hóa phần cứng máy chủ",
            "D": "Quy trình thiết kế giao diện đồ họa đẹp mắt cho các ứng dụng web"
        },
        "correct_answer": "B",
        "explanation": "IEEE 610.12 định nghĩa CNPM là việc áp dụng phương pháp tiếp cận có hệ thống, kỷ luật và có thể định lượng được (systematic, disciplined, quantifiable approach) vào toàn bộ vòng đời phát triển, vận hành và bảo trì phần mềm."
    },
    {
        "id": 4,
        "difficulty": "easy",
        "question": "Trong vòng đời phát triển phần mềm (SDLC), hoạt động nào nhằm xác định chính xác 'Hệ thống cần làm gì' từ phía khách hàng và người dùng?",
        "options": {
            "A": "Thiết kế kiến trúc (Architecture Design)",
            "B": "Phân tích và kỹ thuật yêu cầu (Requirements Analysis)",
            "C": "Kiểm thử chấp nhận (Acceptance Testing)",
            "D": "Triển khai phần mềm (Deployment)"
        },
        "correct_answer": "B",
        "explanation": "Giai đoạn phân tích yêu cầu (Requirements Analysis) có mục tiêu làm rõ, phân tích và thống nhất các chức năng, nghiệp vụ và ràng buộc mà hệ thống phần mềm phải thực hiện."
    },
    {
        "id": 5,
        "difficulty": "easy",
        "question": "Trong hệ thống quản lý phiên bản Git, vùng 'Staging Area' (hoặc Index) đóng vai trò gì?",
        "options": {
            "A": "Nơi lưu trữ lịch sử commit vĩnh viễn đã được đẩy lên GitHub",
            "B": "Khu vực tạm lưu trữ các thay đổi được chọn lọc trước khi chính thức ghi nhận vào một bản commit",
            "C": "Thư mục chứa các file nhị phân của trình biên dịch",
            "D": "Nhánh chính (main branch) trên máy chủ từ xa"
        },
        "correct_answer": "B",
        "explanation": "Staging Area là vùng đệm nơi lập trình viên chọn lọc các thay đổi cụ thể bằng lệnh `git add` trước khi gom chúng thành một snapshot bằng lệnh `git commit`."
    },
    {
        "id": 6,
        "difficulty": "easy",
        "question": "Lệnh Git nào được dùng để kiểm tra trạng thái hiện tại của các file (chưa theo dõi, đã sửa đổi, đã đưa vào vùng chờ)?",
        "options": {
            "A": "git log",
            "B": "git status",
            "C": "git branch",
            "D": "git checkout"
        },
        "correct_answer": "B",
        "explanation": "Lệnh `git status` hiển thị trạng thái của thư mục làm việc (Working Tree) và vùng chờ (Staging Area), chỉ rõ file nào đã sửa, file nào untracked và file nào đã staged."
    },
    {
        "id": 7,
        "difficulty": "easy",
        "question": "Thuộc tính chất lượng nào thể hiện khả năng hệ thống phần mềm bảo vệ dữ liệu, ngăn chặn truy cập trái phép và bảo đảm tính toàn vẹn thông tin?",
        "options": {
            "A": "Tính khả dụng (Usability)",
            "B": "Tính bảo mật (Security)",
            "C": "Tính tương thích (Portability)",
            "D": "Tính dễ bảo trì (Maintainability)"
        },
        "correct_answer": "B",
        "explanation": "Tính bảo mật (Security) đảm bảo dữ liệu được mã hóa, xác thực người dùng đúng thẩm quyền, ngăn ngừa truy cập trái phép và bảo toàn tính toàn vẹn của hệ thống."
    },
    {
        "id": 8,
        "difficulty": "easy",
        "question": "Trong một dự án phần mềm, vai trò của Business Analyst (BA) là gì?",
        "options": {
            "A": "Trực tiếp lập trình các API backend và cấu hình cơ sở dữ liệu",
            "B": "Cầu nối phân tích yêu cầu nghiệp vụ của khách hàng và chuyển hóa thành tài liệu đặc tả kỹ thuật cho đội ngũ phát triển",
            "C": "Chịu trách nhiệm bảo trì hệ thống mạng máy chủ nội bộ",
            "D": "Thiết kế logo và đồ họa thương hiệu cho sản phẩm"
        },
        "correct_answer": "B",
        "explanation": "BA là người lắng nghe khách hàng, thấu hiểu quy trình nghiệp vụ và dịch các nhu cầu đó thành các đặc tả kỹ thuật, User Story rõ ràng cho Developer và Tester thực thi."
    },
    {
        "id": 9,
        "difficulty": "easy",
        "question": "Lệnh Git nào dùng để cấu hình tên người dùng toàn cục trên máy tính cá nhân?",
        "options": {
            "A": "git set user.name \"Tên\"",
            "B": "git config --global user.name \"Tên\"",
            "C": "git user --create \"Tên\"",
            "D": "git init --username \"Tên\""
        },
        "correct_answer": "B",
        "explanation": "Cú pháp chuẩn để cấu hình thông tin định danh tác giả commit trong Git là `git config --global user.name \"Họ và Tên\"`."
    },
    {
        "id": 10,
        "difficulty": "easy",
        "question": "Khái niệm 'Kỹ năng chữ T' (T-shaped skills) trong ngành kỹ thuật phần mềm đề cập đến điều gì?",
        "options": {
            "A": "Chỉ tập trung học một ngôn ngữ lập trình duy nhất từ đầu đến cuối",
            "B": "Sự kết hợp giữa kiến thức bề rộng (thanh ngang: quy trình, kỹ năng mềm, kiến thức tổng quát) và năng lực chuyên sâu (thanh dọc: một chuyên môn mũi nhọn)",
            "C": "Khả năng gõ bàn phím tốc độ cao theo hình chữ T",
            "D": "Kỹ năng kiểm thử phần mềm tự động bằng công cụ TestNG"
        },
        "correct_answer": "B",
        "explanation": "Mô hình chữ T mô tả một kỹ sư có kiến thức nền tảng rộng rãi để phối hợp làm việc nhóm hiệu quả (thanh ngang) và có ít nhất một kỹ năng chuyên môn sâu sắc (thanh dọc)."
    },
    {
        "id": 11,
        "difficulty": "medium",
        "question": "Tại sao việc sửa lỗi (Bug fixing) ở giai đoạn Vận hành & Bảo trì lại tốn kém chi phí gấp hàng chục đến hàng trăm lần so với việc phát hiện và sửa ở giai đoạn Yêu cầu?",
        "options": {
            "A": "Vì lúc này chi phí trả lương cho lập trình viên cao hơn",
            "B": "Vì một lỗi sai ở tầng yêu cầu khi đã qua thiết kế, lập trình và triển khai sẽ kéo theo việc phải đập bỏ và làm lại toàn bộ kiến trúc, mã nguồn, ca kiểm thử và dữ liệu thực tế",
            "C": "Vì các công cụ kiểm thử ở giai đoạn vận hành tính phí bản quyền rất cao",
            "D": "Vì khách hàng không còn hợp tác với doanh nghiệp phần mềm"
        },
        "correct_answer": "B",
        "explanation": "Hiệu ứng khuếch đại chi phí lỗi (Cost of defect): một sai sót trong đặc tả yêu cầu nếu không phát hiện sớm sẽ dẫn đến thiết kế sai, viết mã sai, kiểm thử sai và ảnh hưởng trực tiếp đến dữ liệu người dùng khi đã online, gây tốn kém khủng khiếp để khắc phục."
    },
    {
        "id": 12,
        "difficulty": "medium",
        "question": "Điểm khác biệt căn bản giữa Hệ thống quản lý phiên bản tập trung (CVCS như SVN) và Hệ thống quản lý phiên bản phân tán (DVCS như Git) là gì?",
        "options": {
            "A": "CVCS lưu trữ mã nguồn trên đám mây, còn Git không cho phép đẩy mã lên mạng",
            "B": "Trong Git, mỗi máy trạm của lập trình viên đều chứa toàn bộ bản sao đầy đủ của kho lưu trữ (lịch sử commit), cho phép commit và kiểm tra lịch sử offline",
            "C": "Git chỉ hỗ trợ ngôn ngữ lập trình C, còn SVN hỗ trợ mọi ngôn ngữ",
            "D": "SVN có khả năng tự động giải quyết xung đột tốt hơn Git"
        },
        "correct_answer": "B",
        "explanation": "Trong mô hình DVCS của Git, mỗi clone là một bản sao đầy đủ (full clone) của toàn bộ repository bao gồm mọi nhánh và lịch sử, giúp lập trình viên commit, rẽ nhánh và tra cứu log ngay cả khi không có kết nối internet."
    },
    {
        "id": 13,
        "difficulty": "medium",
        "question": "Khi thực hiện lệnh `git commit -m \"Update login logic\"`, điều gì thực sự diễn ra bên trong Git?",
        "options": {
            "A": "Git sao chép toàn bộ thư mục dự án sang một ổ cứng khác",
            "B": "Git tạo một snapshot (ảnh chụp trạng thái) của tất cả các file đang nằm trong Staging Area và ghi nhận metadata (tác giả, thời gian, commit cha, mã băm SHA-1/SHA-256)",
            "C": "Git tự động đẩy mã nguồn lên kho lưu trữ GitHub từ xa",
            "D": "Git biên dịch các file mã nguồn sang file nhị phân .exe"
        },
        "correct_answer": "B",
        "explanation": "Một commit trong Git là một đối tượng chứa snapshot của cây thư mục (tree object) từ Staging Area kèm thông tin tác giả, timestamp, thông điệp commit và con trỏ trỏ tới commit cha."
    },
    {
        "id": 14,
        "difficulty": "medium",
        "question": "Một hệ thống ngân hàng yêu cầu thời gian ngừng hoạt động (Downtime) tối đa không quá 5 phút mỗi năm (tương đương độ sẵn sàng 99.999%). Đây là ví dụ về loại yêu cầu nào?",
        "options": {
            "A": "Yêu cầu Chức năng (Functional Requirement)",
            "B": "Yêu cầu Phi chức năng về Độ tin cậy và Sẵn sàng (Non-functional: Reliability & Availability)",
            "C": "Yêu cầu Nghiệp vụ kế toán (Accounting Requirement)",
            "D": "Yêu cầu Ràng buộc Giao diện người dùng (UI Constraint)"
        },
        "correct_answer": "B",
        "explanation": "Chỉ số độ sẵn sàng (Availability) và tỷ lệ thời gian hoạt động ổn định là thuộc tính chất lượng kỹ thuật phi chức năng (Non-functional Requirement), không phải là tính năng người dùng thao tác trực tiếp."
    },
    {
        "id": 15,
        "difficulty": "medium",
        "question": "Lệnh nào sau đây cho phép lập trình viên hủy bỏ thao tác đưa một file `app.js` vào Staging Area mà KHÔNG làm mất các thay đổi trong file mã nguồn?",
        "options": {
            "A": "git rm app.js",
            "B": "git restore --staged app.js (hoặc git reset HEAD app.js)",
            "C": "git checkout --force",
            "D": "git clean -df"
        },
        "correct_answer": "B",
        "explanation": "`git restore --staged <file>` loại bỏ file khỏi Staging Area và đưa trở lại trạng thái Modified trong Working Directory, giữ nguyên nội dung mã nguồn vừa chỉnh sửa."
    },
    {
        "id": 16,
        "difficulty": "medium",
        "question": "Thuộc tính 'Tính dễ bảo trì' (Maintainability) của phần mềm phụ thuộc trực tiếp nhất vào yếu tố nào sau đây?",
        "options": {
            "A": "Số lượng máy chủ đám mây mà hệ thống đang thuê",
            "B": "Kiến trúc module hóa rõ ràng, tính gắn kết cao (High Cohesion), độ phụ thuộc thấp (Low Coupling) và mã nguồn tuân thủ Clean Code",
            "C": "Việc sử dụng ngôn ngữ lập trình mới nhất vừa ra mắt trên thị trường",
            "D": "Tốc độ xử lý của chip CPU trên thiết bị người dùng cuối"
        },
        "correct_answer": "B",
        "explanation": "Một phần mềm dễ bảo trì đòi hỏi thiết kế kiến trúc chuẩn mực: các module độc lập cao (Low Coupling), thực hiện chức năng tập trung (High Cohesion) và mã nguồn trong sáng, dễ đọc hiểu."
    },
    {
        "id": 17,
        "difficulty": "medium",
        "question": "File `.gitignore` trong một dự án Git có tác dụng chính là gì?",
        "options": {
            "A": "Liệt kê danh sách các thành viên bị cấm commit vào dự án",
            "B": "Khai báo các mẫu đường dẫn tập tin và thư mục mà Git cần bỏ qua, không theo dõi và không đưa vào Staging Area",
            "C": "Lưu mật khẩu và token truy cập của tài khoản GitHub",
            "D": "Chứa nội dung tài liệu hướng dẫn cài đặt phần mềm"
        },
        "correct_answer": "B",
        "explanation": "File `.gitignore` ngăn chặn việc vô tình commit các file rác, file sinh tự động (`node_modules/`, `build/`, `.env`, file nhị phân) vào kho lưu trữ mã nguồn."
    },
    {
        "id": 18,
        "difficulty": "medium",
        "question": "Trong vòng đời SDLC, hoạt động 'Xác minh' (Verification) và 'Thẩm định' (Validation) khác nhau căn bản như thế nào?",
        "options": {
            "A": "Verification kiểm tra phần cứng, Validation kiểm tra phần mềm",
            "B": "Verification trả lời câu hỏi 'Chúng ta có xây dựng sản phẩm đúng quy chuẩn thiết kế không?', còn Validation trả lời 'Chúng ta có xây dựng đúng sản phẩm khách hàng thực sự cần không?'",
            "C": "Verification do khách hàng làm, còn Validation do lập trình viên làm",
            "D": "Hai khái niệm này hoàn toàn đồng nghĩa và có thể thay thế cho nhau"
        },
        "correct_answer": "B",
        "explanation": "Verification (Xác minh): kiểm tra sản phẩm có đáp ứng các tiêu chuẩn và tài liệu kỹ thuật đã quy định ('Are we building the product right?'). Validation (Thẩm định): kiểm tra sản phẩm có đáp ứng đúng nhu cầu thực tế của khách hàng ('Are we building the right product?')."
    },
    {
        "id": 19,
        "difficulty": "medium",
        "question": "Khi chạy lệnh `git log --oneline --graph --all`, thông tin nào được hiển thị trực quan nhất?",
        "options": {
            "A": "Mức tiêu thụ dung lượng RAM của kho chứa Git",
            "B": "Cây phân nhánh lịch sử commit, vị trí các nhánh và các điểm gộp (merge points) dưới dạng sơ đồ ASCII cô đọng",
            "C": "Danh sách tất cả các mật khẩu đã từng sử dụng",
            "D": "Thời gian chi tiết từng giây của quá trình tải mã nguồn"
        },
        "correct_answer": "B",
        "explanation": "Cờ `--graph` kết hợp `--oneline` giúp vẽ sơ đồ hình cây trực quan các nhánh rẽ và điểm gộp commit trong toàn bộ lịch sử repository."
    },
    {
        "id": 20,
        "difficulty": "medium",
        "question": "Một kỹ sư QA phát hiện phần mềm bị crash khi người dùng nhập chuỗi ký tự dài 1000 chữ cái vào ô 'Họ tên'. Lỗi này thuộc về sự vi phạm thuộc tính chất lượng nào?",
        "options": {
            "A": "Tính bền vững và kiểm soát ngoại lệ (Robustness & Error Tolerance thuộc nhóm Reliability)",
            "B": "Tính di động (Portability)",
            "C": "Tính dễ tái sử dụng (Reusability)",
            "D": "Tính thân thiện môi trường"
        },
        "correct_answer": "A",
        "explanation": "Khả năng xử lý dữ liệu đầu vào bất thường mà không làm sập ứng dụng thuộc về tính bền vững (Robustness) và khả năng dung lỗi (Fault Tolerance) của nhóm độ tin cậy (Reliability)."
    },
    {
        "id": 21,
        "difficulty": "medium",
        "question": "Lệnh `git diff --staged` (hoặc `git diff --cached`) được sử dụng để làm gì?",
        "options": {
            "A": "So sánh sự khác biệt giữa Working Directory và Staging Area",
            "B": "So sánh sự khác biệt giữa các thay đổi đã đưa vào Staging Area với commit gần nhất (HEAD)",
            "C": "So sánh hai nhánh trên máy chủ từ xa",
            "D": "Xóa toàn bộ các thay đổi trong Staging Area"
        },
        "correct_answer": "B",
        "explanation": "`git diff` mặc định so sánh Working Directory với Staging Area. Thêm cờ `--staged` sẽ so sánh nội dung đang nằm trong Staging Area với commit mới nhất ở HEAD."
    },
    {
        "id": 22,
        "difficulty": "medium",
        "question": "Tại sao trong quy trình chuyên nghiệp, lập trình viên tuyệt đối KHÔNG NÊN đưa các file chứa thông tin nhạy cảm như `.env` (chứa API Keys, Database Password) lên GitHub?",
        "options": {
            "A": "Vì file `.env` sẽ làm tăng kích thước commit lên quá nhiều megabyte",
            "B": "Vì một khi đã commit và đẩy lên Git, thông tin nhạy cảm sẽ nằm vĩnh viễn trong lịch sử commit và có nguy cơ bị lộ cho bất kỳ ai có quyền truy cập repo hoặc bị hacker quét tự động",
            "C": "Vì Git không hỗ trợ đọc định dạng file không có đuôi mở rộng",
            "D": "Vì GitHub sẽ tự động khóa tài khoản lập trình viên nếu thấy file `.env`"
        },
        "correct_answer": "B",
        "explanation": "Lịch sử commit trong Git là bất biến; việc lộ credentials trên Git rất dễ bị bot quét khai thác và đòi hỏi phải xóa triệt để lịch sử Git (sử dụng git-filter-repo hoặc BFG Repo-Cleaner) rất phức tạp."
    },
    {
        "id": 23,
        "difficulty": "hard",
        "question": "Giả sử một lập trình viên lỡ tay thực hiện lệnh `git commit` với thông điệp sai chính tả và chưa thực hiện `git push`. Lệnh nào giúp sửa lại thông điệp của commit gần nhất đó mà không tạo thêm commit mới?",
        "options": {
            "A": "git commit --revert",
            "B": "git commit --amend -m \"Thông điệp mới chính xác\"",
            "C": "git reset --hard HEAD~1",
            "D": "git checkout -b fix-message"
        },
        "correct_answer": "B",
        "explanation": "Cờ `--amend` cho phép kết hợp các thay đổi mới hoặc cập nhật lại thông điệp của commit gần nhất, thay thế commit cũ bằng một commit mới có mã hash mới."
    },
    {
        "id": 24,
        "difficulty": "hard",
        "question": "Tại sao 'Phần mềm không thể bị mòn đi theo nghĩa vật lý, nhưng chi phí bảo trì vẫn luôn chiếm phần lớn chi phí toàn bộ vòng đời'?",
        "options": {
            "A": "Do linh kiện bán dẫn bên trong chip máy tính nóng lên làm giảm tốc độ thực thi của code",
            "B": "Do phần mềm liên tục phải thích ứng với sự thay đổi của yêu cầu kinh doanh, quy định pháp lý, hệ điều hành mới, bản vá bảo mật và sự gia tăng của 'Nợ kỹ thuật' (Technical Debt) tích tụ qua các lần sửa đổi",
            "C": "Do các nhà sản xuất hệ điều hành cố tình làm chậm phần mềm cũ để bán phần mềm mới",
            "D": "Do lập trình viên tính tiền công bảo trì cao hơn tiền viết code mới"
        },
        "correct_answer": "B",
        "explanation": "Định luật bảo trì phần mềm (Lehman's Laws of Software Evolution) chỉ ra rằng một hệ thống phần mềm muốn tiếp tục hữu dụng bắt buộc phải liên tục biến đổi để thích nghi với môi trường xung quanh, dẫn đến nợ kỹ thuật và chi phí bảo trì tích lũy."
    },
    {
        "id": 25,
        "difficulty": "hard",
        "question": "Trong kiến trúc lưu trữ đối tượng của Git, 4 loại đối tượng (Git Objects) cơ bản lưu trong thư mục `.git/objects` là gì?",
        "options": {
            "A": "File, Folder, Link, Metadata",
            "B": "Blob (chứa nội dung file), Tree (đại diện thư mục), Commit (thông tin snapshot), Tag (nhãn đánh dấu)",
            "C": "Branch, Remote, Head, Config",
            "D": "Text, Binary, Image, Code"
        },
        "correct_answer": "B",
        "explanation": "Git quản lý dữ liệu thông qua 4 kiểu đối tượng bất biến định danh bằng mã băm SHA: Blob (dữ liệu thô của file), Tree (danh sách các blob/tree con kèm tên file), Commit (con trỏ tới cây thư mục gốc và commit cha) và Tag (con trỏ gắn thẻ phiên bản)."
    },
    {
        "id": 26,
        "difficulty": "hard",
        "question": "Một dự án phát triển phần mềm y tế kiểm soát máy xạ trị ung thư đòi hỏi mức độ sai số bằng 0. Theo phân loại chất lượng phần mềm, nhóm thuộc tính nào cần được ưu tiên tuyệt đối?",
        "options": {
            "A": "Tính hấp dẫn của giao diện (Aesthetics Usability)",
            "B": "Tính an toàn sinh mạng (Safety) và Độ tin cậy cực hạn (Fault Tolerance & High Reliability)",
            "C": "Khả năng đổi mới giao diện liên tục mỗi tuần",
            "D": "Tối thiểu hóa chi phí phát triển bằng cách bỏ qua giai đoạn kiểm thử"
        },
        "correct_answer": "B",
        "explanation": "Các hệ thống quan trọng tính mạng (Safety-critical systems) như y tế, hàng không bắt buộc phải đặt tiêu chí Safety, Fault Tolerance và Reliability lên hàng đầu với quy trình xác thực và kiểm thử hình thức cực kỳ nghiêm ngặt."
    },
    {
        "id": 27,
        "difficulty": "hard",
        "question": "Nếu một thành viên trong nhóm vô tình xóa mất một file mã nguồn quan trọng trong Working Directory nhưng file đó ĐÃ ĐƯỢC COMMIT vào Git trước đó, lệnh nào giúp phục hồi lại file ngay lập tức?",
        "options": {
            "A": "git restore <tên_file> (hoặc git checkout HEAD -- <tên_file>)",
            "B": "git init --recover",
            "C": "git rm --cached <tên_file>",
            "D": "git clean -f"
        },
        "correct_answer": "A",
        "explanation": "`git restore <file>` sao chép trạng thái của file từ commit gần nhất (HEAD) về lại Working Directory, khôi phục lại file đã bị xóa cục bộ."
    },
    {
        "id": 28,
        "difficulty": "hard",
        "question": "Khái niệm 'Nợ kỹ thuật' (Technical Debt) trong kỹ nghệ phần mềm được hiểu chính xác nhất là gì?",
        "options": {
            "A": "Khoản tiền công ty phần mềm vay ngân hàng để mua máy chủ",
            "B": "Hệ quả tích lũy của việc lựa chọn giải pháp viết mã nhanh, cẩu thả, đốt cháy quy trình thay vì áp dụng kiến trúc chuẩn mực, khiến cho việc sửa chữa và mở rộng trong tương lai ngày càng đắt đỏ",
            "C": "Tiền bồi thường hợp đồng khi giao sản phẩm trễ hạn",
            "D": "Số tiền phải trả cho bản quyền phần mềm mã nguồn mở"
        },
        "correct_answer": "B",
        "explanation": "Ward Cunningham định nghĩa Technical Debt là chi phí trả thêm trong tương lai do việc chọn giải pháp tạm thời, cắt xén quy trình và thiết kế cẩu thả ở hiện tại; nếu không 'trả nợ' bằng Refactoring thì hệ thống sẽ ngày càng đình trệ."
    },
    {
        "id": 29,
        "difficulty": "hard",
        "question": "Khi hai thành viên cùng sửa đổi một dòng code trên cùng một file ở hai commit khác nhau và thực hiện gộp (merge), trạng thái nào sẽ xảy ra trong Git?",
        "options": {
            "A": "Git tự động xóa mã của người commit trước",
            "B": "Xảy ra Xung đột Gộp (Merge Conflict); Git đánh dấu vị trí xung đột trong file và tạm dừng quá trình merge để con người xử lý thủ công",
            "C": "Git làm sập kho lưu trữ và yêu cầu khởi tạo lại từ đầu",
            "D": "Git gửi email cảnh báo tới ban quản trị GitHub"
        },
        "correct_answer": "B",
        "explanation": "Khi có xung đột nội dung trên cùng một dòng, Git không thể tự phán đoán ý đồ nghiệp vụ nên sẽ chèn các điểm đánh dấu xung đột (`<<<<<<<`, `=======`, `>>>>>>>`) và yêu cầu lập trình viên đối chiếu quyết định."
    },
    {
        "id": 30,
        "difficulty": "hard",
        "question": "Mô hình quy trình phát triển phần mềm nào được coi là phương thuốc giải quyết bế tắc lớn nhất của mô hình Thác nước truyền thống trong môi trường kinh doanh biến động?",
        "options": {
            "A": "Mô hình Thác nước mở rộng (Waterfall 2.0)",
            "B": "Phương pháp luận Linh hoạt (Agile Methodology) với chu kỳ phát triển lặp ngắn và phản hồi liên tục từ khách hàng",
            "C": "Mô hình viết mã tự do không cần kế hoạch (Cowboy Coding)",
            "D": "Mô hình đóng gói phần mềm một lần duy nhất không bao giờ cập nhật"
        },
        "correct_answer": "B",
        "explanation": "Agile giải quyết nhược điểm cứng nhắc, bàn giao muộn của Waterfall bằng cách chia nhỏ dự án thành các vòng lặp (Sprint/Iteration) 1-4 tuần, tạo ra sản phẩm chạy được liên tục và sẵn sàng đón nhận thay đổi."
    }
]

SHORT_ANSWERS = [
    {
        "id": 1,
        "question": "Nêu định nghĩa Công nghệ Phần mềm (Software Engineering) theo tiêu chuẩn IEEE 610.12.",
        "expected_answer": "Công nghệ phần mềm là việc áp dụng một cách tiếp cận có hệ thống, có kỷ luật và định lượng được vào việc phát triển, vận hành và bảo trì phần mềm; nghĩa là áp dụng kỹ nghệ (engineering) vào phần mềm.",
        "explanation": "Định nghĩa này nhấn mạnh 3 yếu tố cốt lõi: Tiếp cận có hệ thống (Systematic), Kỷ luật (Disciplined), và Có thể định lượng (Quantifiable)."
    },
    {
        "id": 2,
        "question": "Trình bày 4 triệu chứng chính của hiện tượng 'Khủng hoảng phần mềm' (Software Crisis) vào cuối thập niên 1960.",
        "expected_answer": "1. Dự án vượt quá dự toán ngân sách (Cost overrun).\n2. Dự án trễ hạn bàn giao so với kế hoạch (Schedule delay).\n3. Chất lượng phần mềm kém, phát sinh nhiều lỗi nghiêm trọng khi vận hành.\n4. Mã nguồn khó bảo trì, chi phí sửa đổi và bảo dưỡng tốn kém vượt bậc.",
        "explanation": "Khủng hoảng phần mềm đã thúc đẩy sự ra đời của ngành Kỹ nghệ phần mềm tại hội nghị NATO năm 1968."
    },
    {
        "id": 3,
        "question": "Liệt kê 6 giai đoạn cơ bản trong Vòng đời Phát triển Phần mềm (SDLC) theo thứ tự tuần tự chuẩn.",
        "expected_answer": "1. Phân tích yêu cầu (Requirements Analysis)\n2. Thiết kế kiến trúc & hệ thống (System Design)\n3. Cài đặt & Lập trình (Implementation / Coding)\n4. Kiểm thử phần mềm (Testing)\n5. Triển khai (Deployment)\n6. Vận hành & Bảo trì (Maintenance)",
        "explanation": "Đây là khung sườn căn bản áp dụng trong mọi mô hình quy trình từ truyền thống đến Agile."
    },
    {
        "id": 4,
        "question": "Phân biệt sự khác nhau giữa 'Hao mòn cơ học' (Wear out) của phần cứng và 'Thoái hóa' (Deterioration) của phần mềm.",
        "expected_answer": "Phần cứng bị hao mòn cơ học theo thời gian do ma sát, nhiệt độ và tác động vật lý của môi trường (tỷ lệ lỗi tăng vọt ở cuối vòng đời theo đường cong bồn tắm Bath-tub curve). Ngược lại, phần mềm là sản phẩm logic, không bị mòn cơ học nhưng bị thoái hóa do các thay đổi liên tục, các bản vá chắp vá gây ra lỗi tiềm ẩn và sự biến đổi của môi trường vận hành (hệ điều hành, thư viện bên thứ ba).",
        "explanation": "Đây là luận điểm kinh điển trong giáo trình Pressman và Sommerville về bản chất của phần mềm."
    },
    {
        "id": 5,
        "question": "Nêu 3 trạng thái (Three States) cơ bản của một tập tin trong hệ thống quản lý phiên bản Git.",
        "expected_answer": "1. **Modified (Đã sửa đổi):** Tập tin đã có sự thay đổi nội dung ở Working Directory nhưng chưa được đánh dấu đưa vào commit.\n2. **Staged (Đã đưa vào vùng chờ):** Tập tin đã được đánh dấu đưa vào Staging Area (bằng lệnh `git add`) để chuẩn bị cho snapshot tiếp theo.\n3. **Committed (Đã ghi nhận):** Dữ liệu đã được lưu trữ an toàn và vĩnh viễn trong cơ sở dữ liệu cục bộ (`.git` repository).",
        "explanation": "Ba trạng thái này tương ứng với ba vùng: Working Directory, Staging Area, và Local Git Repository."
    },
    {
        "id": 6,
        "question": "Mô hình Kỹ năng Chữ T (T-shaped skills) có ý nghĩa như thế nào đối với một kỹ sư phần mềm làm việc trong môi trường hiện đại?",
        "expected_answer": "Thanh ngang đại diện cho bề rộng kiến thức (hiểu biết về quy trình Agile, Git, kiểm thử, UI/UX, giao tiếp, tư duy giải quyết vấn đề) giúp kỹ sư dễ dàng cộng tác liên chức năng. Thanh dọc đại diện cho năng lực chuyên môn sâu sắc ở một lĩnh vực mũi nhọn (ví dụ: tối ưu cơ sở dữ liệu, an ninh mạng, hoặc kiến trúc backend), đảm bảo kỹ sư có thể giải quyết dứt điểm các bài toán kỹ thuật phức tạp.",
        "explanation": "Mô hình chữ T giúp kỹ sư linh hoạt (adaptable) nhưng vẫn giữ được thế mạnh cạnh tranh vượt trội (specialized)."
    },
    {
        "id": 7,
        "question": "Kể tên 4 thuộc tính chất lượng phần mềm quan trọng theo tiêu chuẩn ISO/IEC 25010 và giải thích ngắn gọn một thuộc tính.",
        "expected_answer": "Bốn thuộc tính: Độ tin cậy (Reliability), Hiệu năng (Performance Efficiency), Khả năng bảo trì (Maintainability), Tính bảo mật (Security).\n*Giải thích tính Dễ bảo trì (Maintainability):* Là mức độ hiệu quả và dễ dàng mà phần mềm có thể được các kỹ sư phân tích, sửa lỗi, cải tiến hoặc thích ứng với môi trường mới mà không làm phát sinh lỗi hồi quy (regression bugs).",
        "explanation": "ISO/IEC 25010 là tiêu chuẩn quốc tế định hình các tiêu chí nghiệm thu phần mềm."
    },
    {
        "id": 8,
        "question": "Viết chuỗi câu lệnh Git trên terminal để: Khởi tạo một repo mới, tạo file `index.html`, đưa file vào vùng chờ và tạo commit đầu tiên.",
        "expected_answer": "```bash\ngit init\necho \"<h1>Hello Semester Hub</h1>\" > index.html\ngit add index.html\ngit commit -m \"Initial commit: add index.html\"\n```",
        "explanation": "Chuỗi thao tác khởi tạo căn bản bắt buộc mọi lập trình viên đều phải thành thạo."
    }
]

ESSAYS = [
    {
        "id": 1,
        "title": "Phân Tích Nguyên Nhân Khủng Hoảng Phần Mềm và Vai Trò của Kỹ Nghệ Phần Mềm",
        "problem": "Hãy phân tích bối cảnh ra đời của ngành Công nghệ Phần mềm:\n1. Nêu rõ nguyên nhân khách quan và chủ quan dẫn đến hiện tượng Khủng hoảng phần mềm vào những năm 1960.\n2. Lấy ví dụ minh họa về thiệt hại điển hình (về chi phí, thời gian, sự cố thực tế) khi phát triển phần mềm theo lối tự phát.\n3. Phân tích tại sao áp dụng phương pháp tiếp cận có hệ thống (Systematic, Disciplined, Quantifiable) lại là chìa khóa giải quyết cuộc khủng hoảng này.",
        "solution_steps": [
            "Bước 1: Bối cảnh và nguyên nhân khủng hoảng phần mềm\n- *Nguyên nhân khách quan:* Năng lực phần cứng bùng nổ (định luật Moore), máy tính mạnh hơn, bộ nhớ lớn hơn cho phép con người đặt ra những bài toán nghiệp vụ đồ sộ và phức tạp hơn rất nhiều.\n- *Nguyên nhân chủ quan:* Lối tiếp cận thủ công, 'lập trình kiểu nghệ sĩ' (Cowboy coding), phụ thuộc vào tài năng cá nhân, không có tài liệu thiết kế, bỏ qua kiểm thử bài bản và không có phương pháp quản lý phiên bản.",
            "Bước 2: Hậu quả và ví dụ thực tiễn\n- Chi phí phát triển thực tế thường đội lên gấp 2-5 lần dự toán; thời gian trễ hạn hàng tháng hoặc hàng năm.\n- Sự cố tiêu biểu trong lịch sử: Thảm họa tàu vũ trụ Mariner 1 (1962) bị phá hủy sau khi phóng 293 giây chỉ vì một dấu gạch ngang (dấu phủ định) bị thiếu trong công thức tính toán trên code; sự cố máy xạ trị Therac-25 làm bệnh nhân nhiễm độc xạ do lỗi tương tranh (race condition) phần mềm.\n- Chi phí bảo trì chiếm tới 70-80% ngân sách vòng đời vì mã nguồn như 'đống mì ý' (Spaghetti code) không ai dám chạm vào.",
            "Bước 3: Vai trò quyết định của Kỹ nghệ Phần mềm\n- *Tiếp cận có hệ thống (Systematic):* Chia nhỏ quy trình thành các giai đoạn rõ ràng trong SDLC, mỗi giai đoạn có tiêu chí đầu vào (Entry Criteria) và đầu ra (Exit Criteria) chuẩn xác.\n- *Kỷ luật (Disciplined):* Áp dụng các chuẩn mực viết mã (Coding Standards), quy ước kiểm thử (Testing Conventions), thẩm duyệt mã nguồn (Code Review) và quản lý phiên bản (Version Control).\n- *Định lượng được (Quantifiable):* Đo lường tiến độ bằng số liệu thực tế (Story Points, Defect Density, Velocity, Code Coverage) thay vì phỏng đoán cảm tính."
        ]
    },
    {
        "id": 2,
        "title": "So Sánh Bản Chất Phần Mềm & Phần Cứng: Đường Cong Thất Bại (Failure Curve)",
        "problem": "Một nhà quản lý nhà máy cơ khí chuyển sang quản lý một công ty phần mềm và thắc mắc: 'Tại sao máy móc cơ khí càng dùng càng mòn phải thay phụ tùng, còn phần mềm viết một lần chạy mãi mà các kỹ sư lại liên tục xin ngân sách bảo trì?'.\nHãy viết bài phân tích kỹ thuật giải thích:\n1. Phân tích sự khác biệt giữa đường cong thất bại của phần cứng (Bath-tub curve) và đường cong thực tế của phần mềm.\n2. Giải thích cơ chế 'thoái hóa' (Deterioration) của phần mềm dù không bị hao mòn vật lý.\n3. Đề xuất các biện pháp kỹ thuật giúp làm chậm quá trình thoái hóa của hệ thống phần mềm.",
        "solution_steps": [
            "Bước 1: So sánh đường cong thất bại (Failure Curves)\n- *Phần cứng (Đường cong bồn tắm - Bathtub Curve):* Tỷ lệ lỗi ban đầu cao (do lỗi chế tạo / lắp ráp - 'Burn-in phase'), sau đó duy trì ở mức thấp ổn định trong suốt vòng đời hữu ích, và cuối cùng tăng vọt do hiện tượng hao mòn cơ học, mỏi kim loại, oxy hóa (Wear-out phase).\n- *Phần mềm lý tưởng:* Tỷ lệ lỗi cao ban đầu, sau đó giảm dần khi tìm và sửa hết bug, duy trì đường nằm ngang lý tưởng mãi mãi.\n- *Phần mềm thực tế:* Mỗi khi phát sinh yêu cầu thay đổi từ khách hàng, một bản vá chắp vá được đưa vào. Mỗi bản vá lại gây ra các hiệu ứng phụ (Side-effects), làm xuất hiện các đỉnh nhọn tỷ lệ lỗi mới. Sau nhiều lần thay đổi, mức lỗi nền của phần mềm bị nâng cao dần cho đến khi hệ thống trở nên không thể bảo trì nổi.",
            "Bước 2: Cơ chế thoái hóa của phần mềm (Software Deterioration)\n- Sự thay đổi môi trường: Hệ điều hành nâng cấp, phiên bản cơ sở dữ liệu thay đổi, trình duyệt cập nhật chính sách bảo mật, các thư viện mã nguồn mở (dependencies) bị lỗi thời hoặc xuất hiện lỗ hổng CVE.\n- Nợ kỹ thuật (Technical Debt): Lập trình viên chọn giải pháp chắp vá tạm thời để kịp tiến độ bàn giao (Hardcode, copy-paste code), phá vỡ tính toàn vẹn của kiến trúc ban đầu.",
            "Bước 3: Biện pháp kỹ thuật làm chậm quá trình thoái hóa\n- Áp dụng kiến trúc module hóa lỏng (Loose Coupling) và nguyên lý SOLID.\n- Xây dựng hệ thống kiểm thử tự động toàn diện (Automated Regression Testing) để phát hiện ngay các lỗi phát sinh khi sửa đổi.\n- Định kỳ thực hiện Tái cấu trúc mã nguồn (Refactoring) để dọn dẹp nợ kỹ thuật.\n- Quản lý chặt chẽ dependencies và thường xuyên cập nhật bản vá bảo mật."
        ]
    },
    {
        "id": 3,
        "title": "Hoạch Định Thuộc Tính Chất Lượng Phần Mềm cho Hệ Thống Thương Mại Điện Tử",
        "problem": "Bạn là Kiến trúc sư phần mềm (Software Architect) được giao nhiệm vụ thiết kế một nền tảng Thương mại điện tử (E-Commerce) phục vụ ngày hội mua sắm Mega Sale (Black Friday):\n1. Hãy xác định 4 thuộc tính chất lượng cốt lõi nhất cần ưu tiên cho hệ thống này theo chuẩn ISO/IEC 25010.\n2. Với mỗi thuộc tính, hãy nêu một kịch bản chất lượng cụ thể (chỉ số đo lường định lượng được).\n3. Phân tích sự đánh đổi (Trade-off) tất yếu giữa Tính năng Hiệu năng (Performance) và Tính Bảo mật (Security) trong hệ thống này.",
        "solution_steps": [
            "Bước 1: Xác định 4 thuộc tính chất lượng cốt lõi\n1. *Hiệu năng & Khả năng mở rộng (Performance Efficiency & Scalability):* Chịu tải hàng chục nghìn lượt truy cập đồng thời tại thời điểm mở bán Flash Sale.\n2. *Tính sẵn sàng & Độ tin cậy (Availability & Reliability):* Hệ thống không được sập, thời gian hoạt động đạt 99.99% trong toàn bộ chiến dịch.\n3. *Tính bảo mật & Toàn vẹn (Security & Data Integrity):* Bảo vệ dữ liệu thẻ thanh toán, ngăn ngừa gian lận mã giảm giá và tấn công tấn công từ chối dịch vụ (DDoS).\n4. *Tính dễ bảo trì & Khả năng quan sát (Maintainability & Observability):* Ghi log và giám sát thời gian thực để đội ngũ trực chiến (On-call) phát hiện và cô lập lỗi trong vài phút.",
            "Bước 2: Xây dựng kịch bản chất lượng định lượng\n- *Hiệu năng:* Khi lưu lượng truy cập đạt 50,000 requests/giây, thời gian phản hồi cho tác vụ 'Tìm kiếm sản phẩm' và 'Thêm vào giỏ hàng' phải $\\le 500$ ms đối với 95% số người dùng (P95 latency $\\le 500$ ms).\n- *Sẵn sàng:* Hệ thống tự động co giãn tài nguyên (Auto-scaling) từ 10 pods lên 100 pods trong vòng 90 giây khi CPU vượt ngưỡng 75% mà không làm rớt bất kỳ phiên thanh toán nào.\n- *Bảo mật:* 100% giao dịch thanh toán tuân thủ chuẩn PCI-DSS, mã hóa TLS 1.3 và ngăn chặn thành công các đợt brute-force OTP.",
            "Bước 3: Phân tích đánh đổi (Trade-off) giữa Hiệu năng và Bảo mật\n- Để tăng cường Bảo mật: Cần kiểm tra quyền (Authorization), giải mã token JWT, lọc request qua tường lửa WAF, mã hóa dữ liệu cơ sở dữ liệu ở trạng thái nghỉ (At-rest) và truyền tải (In-transit), kiểm tra gian lận nhiều lớp. Những thao tác này tiêu tốn tài nguyên tính toán và làm tăng độ trễ (Latency).\n- Giải pháp cân bằng kiến trúc: Áp dụng cơ chế phân tầng bảo vệ (Layered Security), sử dụng Hardware Acceleration cho mã hóa TLS, lưu trữ cache các quyền truy cập tĩnh ở Redis và kiểm tra bất đồng bộ các hành vi gian lận (Async Fraud Detection)."
        ]
    },
    {
        "id": 4,
        "title": "Thiết Kế Quy Trình Quản Lý Phiên Bản với Git cho Đội Ngũ Phát Triển Phần Mềm",
        "problem": "Một nhóm phát triển gồm 5 lập trình viên thường xuyên gặp tình trạng đè code của nhau, mất code và không biết ai là người gây ra lỗi trên môi trường kiểm thử.\nHãy thiết kế một quy trình làm việc chuẩn mực với Git:\n1. Giải thích chi tiết vòng đời của một thay đổi từ Working Directory đến khi vào kho lưu trữ an toàn.\n2. Xây dựng quy chuẩn đặt tên nhánh (Branching Strategy) và quy chuẩn thông điệp commit (Conventional Commits).\n3. Đưa ra hướng dẫn xử lý từng bước khi xảy ra Xung đột Gộp (Merge Conflict).",
        "solution_steps": [
            "Bước 1: Vòng đời kiểm soát thay đổi trong Git\n- Lập trình viên chỉnh sửa file trên Working Directory $\\to$ Chạy `git status` để kiểm tra các file modified/untracked $\\to$ Chạy `git diff` để rà soát dòng lệnh vừa sửa $\\to$ Chạy `git add <file>` đưa các thay đổi hoàn chỉnh vào Staging Area $\\to$ Chạy `git commit -m \"...\"` để lưu trữ vĩnh viễn vào Local Repository với mã băm hash duy nhất.",
            "Bước 2: Quy chuẩn rẽ nhánh và thông điệp commit\n- *Chiến lược rẽ nhánh (Git Feature Branch Workflow):*\n  - Nhánh `main`: Ổn định, chỉ chứa mã nguồn đã qua kiểm thử sẵn sàng triển khai.\n  - Nhánh `develop`: Nhánh tích hợp chung của toàn đội.\n  - Nhánh tính năng: `feature/<tên_tính_năng>` (ví dụ: `feature/user-auth`, `feature/payment-vnpay`).\n  - Nhánh sửa lỗi nóng: `hotfix/<tên_lỗi>` (ví dụ: `hotfix/fix-discount-calc`).\n- *Chuẩn thông điệp commit (Conventional Commits):* `type(scope): subject`\n  - Ví dụ: `feat(auth): add JWT login authentication`, `fix(cart): prevent negative quantity of items`, `docs(readme): update installation guide`.",
            "Bước 3: Quy trình giải quyết xung đột (Merge Conflict Resolution)\n- Khi merge nhánh `feature` vào `develop` và gặp thông báo 'Automatic merge failed; fix conflicts and then commit the result':\n  1. Chạy `git status` để xác định danh sách các file bị xung đột (Unmerged paths).\n  2. Mở file xung đột, xác định khối `<<<<<<< HEAD` (mã của nhánh hiện tại), `=======` (vạch phân cách), và `>>>>>>> feature/...` (mã của nhánh cần gộp).\n  3. Thảo luận trực tiếp với đồng nghiệp phụ trách nhánh liên quan để thống nhất giữ lại logic đúng đắn nhất, xóa bỏ các ký hiệu đánh dấu của Git.\n  4. Chạy kiểm thử cục bộ đảm bảo code biên dịch và chạy đúng.\n  5. Chạy `git add <tên_file>` để đánh dấu đã xử lý xong xung đột.\n  6. Chạy `git commit` để hoàn tất merge commit."
        ]
    }
]
