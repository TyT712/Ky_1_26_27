window.SEMESTER_DATA = {
  semesterInfo: {
    title: "Học Kỳ 1 - Năm Học 2026 - 2027",
    studentName: "Sinh Viên Đại Học",
    studentId: "22020000",
    major: "Sư phạm Tin",
    academicYear: "2026-2027",
    targetGPA: "3.6 / 4.0",
    announcement: ""
  },
  courses: [
    {
      id: "software-engineering",
      name: "Công nghệ phần mềm",
      chapters: [{
        id: "software-engineering-chapter-1",
        title: "Chương 1: Tổng quan về Công nghệ phần mềm",
        content: `# Chương 1: Tổng quan về Công nghệ phần mềm

## 1. Tổng quan về Công nghệ phần mềm (Bài giảng / Lý thuyết)

### Khái niệm và đặc tính của phần mềm

- **Phần mềm (Software):** Tập hợp các chỉ dẫn (chương trình) và dữ liệu được lập trình để thực hiện những nhiệm vụ cụ thể trên máy tính hoặc thiết bị điện tử.
- **Đặc tính cơ bản:** Phần mềm là sản phẩm vô hình, phụ thuộc vào phần cứng, dễ sao chép và phân phối, có thể nâng cấp và mở rộng. Phần mềm không bị hao mòn vật lý nhưng có thể bị thoái hóa theo thời gian.
- **Phân loại:** Phần mềm hệ thống, phần mềm ứng dụng, phần mềm nhúng, phần mềm thời gian thực, phần mềm trên Web và phần mềm trí tuệ nhân tạo.

### Bối cảnh ra đời và cuộc khủng hoảng phần mềm

Thuật ngữ **Công nghệ phần mềm (Software Engineering)** được NATO đưa ra vào khoảng năm 1967–1968 nhằm giải quyết **cuộc khủng hoảng phần mềm**.

Sự phát triển nhanh chóng của phần cứng vượt xa năng lực phát triển phần mềm, khiến nhiều dự án thường xuyên trễ hẹn, vượt ngân sách, có chất lượng kém với nhiều lỗi và rất khó bảo trì.

### Lập trình và Công nghệ phần mềm

- **Lập trình (Programming):** Tập trung vào viết mã, giải thuật, cấu trúc dữ liệu và cú pháp ngôn ngữ; thường mang tính cá nhân và thủ công.
- **Công nghệ phần mềm (Software Engineering):** Áp dụng các nguyên tắc kỹ thuật một cách có hệ thống, có kỷ luật và có thể đo lường trong toàn bộ quá trình phát triển, vận hành và bảo trì phần mềm.

### Thuộc tính chất lượng phần mềm

Một phần mềm tốt không chỉ cần chạy được mà còn đáp ứng các thuộc tính chất lượng cốt lõi:

- **Tính đúng đắn (Correctness).**
- **Độ tin cậy (Reliability).**
- **Tính khả dụng (Usability).**
- **Hiệu năng (Efficiency).**
- **Tính bảo trì (Maintainability).**

### Vòng đời phát triển phần mềm và nghề nghiệp

Vòng đời phát triển phần mềm (SDLC) gồm các giai đoạn tổng quan: xác định yêu cầu, phân tích và đặc tả, thiết kế, cài đặt, tích hợp và bảo trì. Chương này cũng giới thiệu các con đường nghề nghiệp trong ngành Công nghệ phần mềm và tầm quan trọng của **mô hình kỹ năng chữ T**.

## 2. Chương 1 - Hướng dẫn thực hành (HDTH)

### Phần 1: Làm quen với Git, GitHub và Markdown

**Mục tiêu:** Hiểu vai trò của hệ thống quản lý phiên bản (VCS), cài đặt và cấu hình Git, tạo tài khoản GitHub và nắm vững cú pháp Markdown.

**Nội dung thực hành tại lớp:**

1. Tạo tài khoản GitHub và khởi tạo repository cá nhân, ví dụ gioi-thieu-ban-than.
2. Soạn thảo và định dạng file README.md bằng Markdown, gồm tiêu đề, danh sách, liên kết và trích dẫn.
3. Thực hiện chu trình Git cơ bản: git add, git commit với thông điệp rõ ràng và git push để đưa dữ liệu lên GitHub; sau đó nộp URL repository.

### Phần 2: Quản lý mã nguồn với Git và GitHub (Branching & Pull Request)

**Mục tiêu:** Nắm quy trình làm việc theo nhánh (Branching Workflow), phối hợp mã nguồn giữa máy cục bộ (Local) và kho lưu trữ (Remote), tạo và xử lý Pull Request (PR).

**Nội dung thực hành và bài tập:**

1. Thiết lập dự án, ví dụ ứng dụng danh sách công việc todo-list-app.
2. Tạo các nhánh tính năng (Feature branch) độc lập với nhánh chính main, ví dụ feature/add-task và feature/list-tasks.
3. Thực hiện thay đổi mã nguồn trên nhánh riêng, đẩy (push) nhánh lên GitHub và khởi tạo Pull Request (PR).
4. Tự review mã nguồn, kiểm tra các thay đổi và Merge (gộp) Pull Request vào nhánh main.
`,
        tasks: [
          {
            id: "task-se-ch1-01",
            title: "Task 1 (Lý thuyết): Tìm hiểu khái niệm CNPM và cuộc khủng hoảng phần mềm",
            note: "Mục tiêu: Phân biệt lập trình tự phát với Công nghệ phần mềm (CNPM), đồng thời giải thích bối cảnh lịch sử ra đời của ngành.\n\nYêu cầu:\n1. Trình bày định nghĩa phần mềm, các đặc tính phi vật lý (không hao mòn cơ học nhưng có thể thoái hóa theo thời gian) và phân loại các hệ thống phần mềm như hệ thống, ứng dụng, nhúng, AI.\n2. Phân tích nguyên nhân của cuộc khủng hoảng phần mềm trong thập niên 1960–1970, gồm vượt chi phí, trễ hạn, nhiều lỗi và khó bảo trì; giải thích lý do ngành CNPM ra đời.\n3. So sánh tư duy lập trình cá nhân với việc áp dụng quy trình kỹ thuật bài bản.",
            priority: "medium",
            status: "todo"
          },
          {
            id: "task-se-ch1-02",
            title: "Task 2 (Lý thuyết): Phân tích thuộc tính chất lượng và vòng đời phần mềm (SDLC)",
            note: "Mục tiêu: Nắm các tiêu chuẩn đánh giá phần mềm tốt và tổng quan các giai đoạn phát triển.\n\nYêu cầu:\n1. Nêu và giải thích 5 thuộc tính chất lượng: Tính đúng đắn (Correctness), Độ tin cậy (Reliability), Tính khả dụng (Usability), Hiệu năng (Efficiency) và Tính bảo trì (Maintainability).\n2. Tóm tắt các hoạt động SDLC: Thu thập yêu cầu, Phân tích/Đặc tả, Thiết kế, Cài đặt, Kiểm thử và Bảo trì.\n3. Tìm hiểu mô hình kỹ năng chữ T (T-shaped skills) và các vị trí công việc trong dự án phần mềm.",
            priority: "medium",
            status: "todo"
          },
          {
            id: "task-se-ch1-03",
            title: "Task 3 (Thực hành): Cài đặt Git, cấu hình môi trường và tạo repository GitHub",
            note: "Mục tiêu: Chuẩn bị công cụ làm việc và tạo repository cá nhân đầu tiên.\n\nYêu cầu:\n1. Cài đặt Git; cấu hình người dùng bằng các lệnh git config --global user.name và git config --global user.email.\n2. Đăng ký GitHub và thiết lập SSH Key để kết nối an toàn với máy tính.\n3. Tạo repository Public tên nhap-mon-cnpm-practice và khởi tạo cùng file README.md.",
            priority: "high",
            status: "todo"
          },
          {
            id: "task-se-ch1-04",
            title: "Task 4 (Thực hành): Markdown và chu trình Git Clone, Add, Commit, Push",
            note: "Mục tiêu: Thành thạo các lệnh Git cơ bản trên máy cục bộ và cú pháp Markdown.\n\nYêu cầu:\n1. Clone repository nhap-mon-cnpm-practice từ GitHub về máy bằng lệnh git clone.\n2. Dùng VS Code soạn README.md giới thiệu bản thân, sử dụng tiêu đề (#), chữ in đậm/nghiêng, danh sách, liên kết và trích dẫn (Blockquote).\n3. Thực hiện chu trình: git add README.md (hoặc git add .), git commit -m với thông điệp Cập nhật thông tin cá nhân, sau đó git push.\n4. Nộp URL repository sau khi xác nhận nội dung đã được đẩy lên GitHub.",
            priority: "high",
            status: "todo"
          },
          {
            id: "task-se-ch1-05",
            title: "Task 5 (Thực hành nâng cao): Feature Branch Workflow và Pull Request",
            note: "Mục tiêu: Làm việc độc lập trên nhánh riêng và tích hợp mã nguồn an toàn qua Pull Request.\n\nYêu cầu:\n1. Tạo repository cho ứng dụng cá nhân, ví dụ todo-list-app, rồi clone về máy.\n2. Tạo nhánh feature/add-task bằng git checkout -b feature/add-task để giữ nhánh main ổn định.\n3. Viết mã cho tính năng trên nhánh mới, thực hiện git add và git commit, sau đó đẩy nhánh bằng git push -u origin feature/add-task.\n4. Trên GitHub, tạo Pull Request từ feature/add-task vào main; tự review trong tab Files changed và Merge Pull Request.\n5. Trên máy cục bộ, chuyển về main bằng git checkout main và đồng bộ bằng git pull origin main.",
            priority: "high",
            status: "todo"
          }
        ]
      }]
    },
    {
      id: "data-structures-algorithms",
      name: "Cấu trúc dữ liệu và giải thuật",
      chapters: []
    },
    {
      id: "database-management",
      name: "Hệ quản trị dữ liệu",
      chapters: [{
        id: "database-chapter-1",
        title: "Chương 1: Tổng quan về Cơ sở dữ liệu",
        content: `

    ## 1. Các khái niệm cốt lõi

    - **Cơ sở dữ liệu (CSDL - Database):** Tập hợp các dữ liệu có liên quan với nhau, chứa thông tin về một tổ chức hoặc thực thể. Dữ liệu được lưu trên thiết bị nhớ thứ cấp như đĩa từ, băng từ để phục vụ nhu cầu khai thác thông tin của nhiều người dùng với nhiều mục đích khác nhau.
    - **Hệ quản trị CSDL (DBMS - Database Management System):** Hệ thống phần mềm chuyên dụng cho phép tạo lập CSDL và điều khiển mọi truy cập, khai thác trên CSDL đó. Ví dụ: Oracle, SQL Server, MS Access.
    - **Hệ CSDL (Database System):** Sự kết hợp tổng thể giữa CSDL, Hệ QTCSDL, con người và trang thiết bị lưu trữ/xử lý.

    ## 2. Ưu điểm của CSDL và các vấn đề kỹ thuật

    ### Ưu điểm nổi bật

    - Giảm trùng lặp thông tin, đảm bảo tính nhất quán và toàn vẹn dữ liệu.
    - Đảm bảo sự độc lập giữa dữ liệu và chương trình ứng dụng.
    - Trừu tượng hóa dữ liệu, che giấu chi tiết lưu trữ vật lý phức tạp.
    - Hỗ trợ nhiều khung nhìn (multi-view) cho từng đối tượng người dùng.
    - Cho phép nhiều người dùng (multi-user) chia sẻ dữ liệu đồng thời.

    ### Các vấn đề kỹ thuật cần giải quyết

    - **Tính chủ quyền dữ liệu:** Bảo vệ quyền kiểm soát thông tin khi dữ liệu được dùng chung.
    - **Bảo mật và phân quyền:** Kiểm soát quyền truy cập của từng người dùng.
    - **Tranh chấp dữ liệu:** Kiểm soát và giải quyết xung đột khi nhiều giao tác truy cập đồng thời.
    - **An toàn khi có sự cố:** Sao lưu (Backup) và phục hồi (Restore), sử dụng nhật ký thao tác khi xảy ra sự cố phần cứng hoặc phần mềm.

    ## 3. Kiến trúc 3 mức trừu tượng và độc lập dữ liệu

    Theo chuẩn ANSI-SPARC, kiến trúc CSDL có 3 mức nhằm tách biệt ứng dụng người dùng khỏi CSDL vật lý:

    1. **Mức vật lý (mức trong):** Mô tả chi tiết dữ liệu được lưu trữ như thế nào và ở đâu trên thiết bị lưu trữ, chẳng hạn tệp, đĩa từ và chỉ mục.
    2. **Mức khái niệm (mức logic):** Mô tả toàn bộ CSDL lưu trữ những loại dữ liệu nào, các thuộc tính và mối quan hệ giữa chúng.
    3. **Mức khung nhìn (mức ngoài):** Thể hiện góc nhìn hoặc mối quan tâm riêng của từng người dùng hay ứng dụng cụ thể.

    **Độc lập dữ liệu (Data Independence)** là khả năng thay đổi lược đồ ở một mức mà không cần thay đổi lược đồ ở mức cao hơn.

    - **Độc lập dữ liệu logic:** Thay đổi lược đồ khái niệm mà không cần sửa lược đồ ngoài hoặc chương trình ứng dụng.
    - **Độc lập dữ liệu vật lý:** Thay đổi lược đồ mức trong, như cách tổ chức lưu trữ hoặc chỉ mục, mà không làm thay đổi lược đồ khái niệm.

    ## 4. Lược đồ (Schema) và thể hiện (Instance)

    - **Lược đồ CSDL:** Thiết kế tổng thể, đóng vai trò bộ khung hoặc cấu trúc cố định của CSDL, bao gồm các loại dữ liệu và thuộc tính.
    - **Thể hiện của CSDL:** Tập hợp dữ liệu thực tế đang được lưu trong CSDL tại một thời điểm xác định; dữ liệu này thay đổi liên tục theo thời gian.

    ## 5. Mô hình dữ liệu và ngôn ngữ CSDL

    **Mô hình dữ liệu** gồm hệ thống ký hiệu mô tả dữ liệu và tập các phép toán thao tác trên dữ liệu. Các mô hình phổ biến gồm mô hình Thực thể - Quan hệ (E-R), mô hình Quan hệ, mô hình Phân cấp, mô hình Mạng và mô hình Hướng đối tượng.

    ### Các nhóm ngôn ngữ CSDL

    - **DDL (Data Definition Language):** Ngôn ngữ định nghĩa dữ liệu, dùng để tạo, sửa, xóa cấu trúc bảng và các ràng buộc.
    - **DML (Data Manipulation Language):** Ngôn ngữ thao tác dữ liệu, dùng để thêm, sửa, xóa bản ghi.
    - **SQL (Structured Query Language):** Ngôn ngữ truy vấn chuẩn để khai thác CSDL.
    - **Ngôn ngữ chủ (Host Language):** Ngôn ngữ lập trình tổng quát như C++, Java, Pascal; có thể nhúng lệnh SQL để xây dựng phần mềm ứng dụng.

    ## 6. Kiến trúc nội bộ của Hệ QTCSDL (DBMS)

    - **Bộ xử lý truy vấn (Query Processor):** Tối ưu hóa và điều khiển thực thi câu truy vấn.
    - **Bộ quản lý lưu trữ (Storage Manager), quản lý tệp và bộ đệm:** Tương tác với thiết bị lưu trữ vật lý.
    - **Bộ quản trị giao dịch (Transaction Manager):** Đảm bảo tính toàn vẹn và xử lý truy cập đồng thời.
    - **Bộ quản lý từ điển dữ liệu (Metadata Manager):** Quản lý thông tin mô tả cấu trúc CSDL (siêu dữ liệu - metadata).

    ## 7. Các đối tượng sử dụng CSDL

    - **Đối tượng trực tiếp:** Người quản trị CSDL (DBA), phụ trách phân quyền, bảo mật và sao lưu; người thiết kế CSDL; người sử dụng cuối (End-users); lập trình viên ứng dụng và nhà phân tích hệ thống.
    - **Đối tượng gián tiếp:** Nhà phát triển công cụ (Tool developers), nhà phát triển hệ thống DBMS, Tester và System maintainer.`.replace(/^ {4}/gm, ""),
        tasks: [
        {
          id: "task-db-ch1-01",
          title: "Task 1: Phân biệt CSDL, Hệ QTCSDL và Hệ CSDL qua ví dụ thực tế",
          note: "Nhiệm vụ: Định nghĩa và phân biệt Cơ sở dữ liệu (CSDL), Hệ quản trị CSDL (DBMS) và Hệ CSDL. Với bài toán quản lý bán hàng tại siêu thị, xác định dữ liệu được lưu ở đâu, phần mềm quản trị là gì và những ai tham gia vận hành.\n\nMục tiêu: Nắm vững ranh giới giữa tập hợp dữ liệu, phần mềm quản trị và toàn bộ môi trường hệ thống.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-02",
          title: "Task 2: Phân tích ưu điểm của CSDL và đề xuất giải pháp kỹ thuật",
          note: "Nhiệm vụ: Phân tích 5 ưu điểm của CSDL so với lưu trữ tệp truyền thống: giảm trùng lặp, độc lập chương trình - dữ liệu, trừu tượng hóa, nhiều khung nhìn và chia sẻ đa người dùng. Trình bày 4 vấn đề cần giải quyết: chủ quyền dữ liệu, bảo mật và phân quyền, tranh chấp truy cập đồng thời, an toàn khi có sự cố. Đề xuất cơ chế phù hợp cho từng vấn đề, chẳng hạn phân quyền, khóa giao tác, sao lưu/khôi phục và nhật ký thao tác.\n\nMục tiêu: Hiểu lý do ra đời của hệ CSDL và các cơ chế bảo vệ dữ liệu.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-03",
          title: "Task 3: Biểu diễn CSDL Quản lý Thư viện ở 3 mức trừu tượng",
          note: "Nhiệm vụ: Dựa trên kiến trúc 3 mức ANSI-SPARC, mô tả CSDL thư viện ở mức ngoài với khung nhìn cho độc giả tra cứu và thủ thư quản lý mượn/trả; mức khái niệm với các bảng SÁCH, ĐỘC GIẢ, MƯỢN SÁCH, thuộc tính và mối liên hệ; mức vật lý với cách lưu trữ trên tệp, đĩa từ và chỉ mục.\n\nMục tiêu: Tách biệt ứng dụng người dùng khỏi chi tiết lưu trữ vật lý.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-04",
          title: "Task 4: Phân tích độc lập dữ liệu logic và vật lý",
          note: "Nhiệm vụ: Phân biệt độc lập dữ liệu logic và độc lập dữ liệu vật lý. Phân tích tình huống A: chuyển tệp CSDL từ HDD sang RAID và tạo chỉ mục B-cây để tăng tốc truy vấn. Phân tích tình huống B: bổ sung trường Email và Số điện thoại vào lược đồ SINHVIEN. Với mỗi tình huống, nêu mức bị thay đổi và ảnh hưởng đến các mức cao hơn/chương trình ứng dụng.\n\nMục tiêu: Hiểu khả năng thay đổi lược đồ ở một mức mà không phải sửa ứng dụng ở mức cao hơn.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-05",
          title: "Task 5: Xây dựng lược đồ và thể hiện CSDL Quản lý Quán cà phê",
          note: "Nhiệm vụ: Phân biệt lược đồ CSDL (cấu trúc) và thể hiện CSDL (dữ liệu tại một thời điểm). Với các đối tượng THỨC UỐNG, BÀN, HÓA ĐƠN, khai báo tên bảng và thuộc tính ở mức khái niệm; lập một thể hiện minh họa tại thời điểm quán hoạt động với ít nhất 3 bản ghi cho mỗi bảng.\n\nMục tiêu: Phân biệt cấu trúc tĩnh với dữ liệu biến động theo thời gian.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-06",
          title: "Task 6: Khảo sát và so sánh các mô hình dữ liệu",
          note: "Nhiệm vụ: Nêu khái niệm mô hình dữ liệu, gồm hệ thống ký hiệu mô tả và tập phép toán. Liệt kê các mô hình E-R, quan hệ, phân cấp, mạng và hướng đối tượng. Phân tích ưu/nhược điểm chính cùng phạm vi ứng dụng của mô hình E-R và mô hình quan hệ trong thiết kế CSDL hiện đại.\n\nMục tiêu: Nắm tổng quan các phương pháp tiếp cận mô hình hóa dữ liệu.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-07",
          title: "Task 7: Phân tích điều kiện khôi phục CSDL về một thời điểm trong quá khứ",
          note: "Tình huống: CSDL bán hàng gặp lỗi lúc 14:30 khiến một số hóa đơn bị cập nhật nhầm. Yêu cầu khôi phục trạng thái dữ liệu về 14:25, ngay trước khi xảy ra lỗi.\n\nNhiệm vụ: Phân tích những điều kiện cần để thực hiện khôi phục đến đúng thời điểm (point-in-time recovery): phải có bản sao lưu đầy đủ phù hợp được tạo trước 14:25; các bản sao lưu gia tăng/khác biệt cần thiết (nếu dùng) phải còn đầy đủ; nhật ký giao dịch hoặc log lưu trữ phải bao phủ liên tục từ bản sao lưu đến 14:25 và không bị thiếu/hỏng; hệ quản trị CSDL phải hỗ trợ khôi phục theo thời điểm và xác định chính xác mốc thời gian, múi giờ. Mô tả thứ tự khôi phục bản sao lưu và phát lại log, đồng thời nêu cách kiểm tra dữ liệu sau khôi phục.\n\nPhân tích thêm: Nếu thiếu bản sao lưu phù hợp hoặc log bị đứt đoạn trước 14:25 thì có thể khôi phục đến đâu? Vì sao nên khôi phục thử trên một máy chủ/bản sao riêng trước khi thay thế CSDL đang hoạt động?\n\nMục tiêu: Hiểu rằng khôi phục đúng một thời điểm trong quá khứ cần cả bản sao lưu và chuỗi log liên tục, không chỉ cần một file backup.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-08",
          title: "Task 8: Sơ đồ hóa kiến trúc nội bộ của DBMS",
          note: "Nhiệm vụ: Vẽ sơ đồ khối các thành phần chính trong DBMS và trình bày chức năng của Bộ xử lý truy vấn (Query Processor), Bộ quản lý lưu trữ (Storage Manager), Bộ quản trị giao dịch (Transaction Manager), Bộ quản lý tệp và bộ đệm, Bộ quản lý từ điển dữ liệu (Metadata/Data Dictionary Manager). Mô tả đường đi của câu lệnh từ người dùng đến thiết bị lưu trữ vật lý.\n\nMục tiêu: Hiểu cách DBMS xử lý câu lệnh và quản lý dữ liệu.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-09",
          title: "Task 9: Phân tích vai trò của các đối tượng sử dụng CSDL",
          note: "Nhiệm vụ: Phân loại các đối tượng tương tác với CSDL thành trực tiếp và gián tiếp. Trình bày nhiệm vụ của DBA (ít nhất 4 chức năng: cài đặt, cấp quyền, sao lưu, duy trì hoạt động), nhà phân tích hệ thống, lập trình viên ứng dụng, người sử dụng cuối, nhóm phát triển công cụ/DBMS và kiểm thử viên.\n\nMục tiêu: Xác định vị trí, quyền hạn và trách nhiệm của từng nhóm trong vòng đời hệ CSDL.",
          priority: "medium",
          status: "todo"
        },
        {
          id: "task-db-ch1-10",
          title: "Task 10: Dự án mini - Thiết kế sơ bộ hệ thống Quản lý Đào tạo Đại học",
          note: "Nhiệm vụ: Liệt kê 5 loại dữ liệu cần lưu trữ, ví dụ SINHVIEN, KHOAHOC, THONGTIN_KHOAHOC, DIEM, DIEUKIEN_TIENQUYET, cùng các thuộc tính. Viết 3 câu truy vấn và 3 yêu cầu cập nhật bằng ngôn ngữ tự nhiên. Đề xuất phân quyền: sinh viên chỉ xem điểm của mình; giảng viên được nhập/sửa điểm môn mình dạy.\n\nMục tiêu: Tổng hợp kiến thức Chương 1 vào một bài toán thực tế hoàn chỉnh.",
          priority: "medium",
          status: "todo"
        }
        ]
      }]
    }
  ]
};