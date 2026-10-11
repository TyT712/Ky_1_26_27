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
      name: "Hệ quản trị cơ sở dữ liệu",
      chapters: [
        {
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
        },
        ]
        },
        {
          id: "database-chapter-2",
          title: "Chương 2: Mô hình Thực thể - Quan hệ (E-R)",
          content: "# Chương 2: Mô hình Thực thể - Quan hệ (E-R)",
          tasks: [
            {
              id: "task-db-ch2-01",
              title: "Bài 1: Quản lý hệ thống thư viện trung tâm của trường đại học (Phiên bản mở rộng)",
              note: `Nhằm hiện đại hóa quy trình mượn/trả sách và kiểm soát tài nguyên, thư viện trung tâm của một trường đại học cần xây dựng một CSDL chi tiết. Qua khảo sát, quy trình hoạt động thực tế được mô tả như sau:

**1. Quản lý Đầu sách và Bản sao (Cuốn sách vật lý):**

- Thư viện quản lý các **Đầu sách** thông qua các thông tin: *Mã ISBN, Tên sách, Năm xuất bản, Số trang, Ngôn ngữ*.
- Mỗi đầu sách được viết bởi một hoặc nhiều **Tác giả** (*Mã tác giả, Họ tên, Bút danh, Quốc tịch, Email*) và do một **Nhà xuất bản** (*Mã NXB, Tên NXB, Địa chỉ, Số điện thoại*) phát hành. Đồng thời, một đầu sách có thể thuộc về nhiều **Thể loại** (*Mã thể loại, Tên thể loại*) khác nhau.
- Do nhu cầu mượn cao, với mỗi đầu sách, thư viện sẽ mua nhiều **Bản sao** (cuốn sách vật lý thực tế). Mỗi bản sao được dán một *Mã cá biệt (Mã vạch/Barcode)* duy nhất, có ghi nhận *Tình trạng sách* (mới, cũ, rách trang, mất bìa...) và *Vị trí lưu trữ* cụ thể (Mã kệ, Tầng).

**2. Quản lý Độc giả:**

- Độc giả bao gồm sinh viên, học viên cao học và giảng viên. Mỗi người được cấp một **Thẻ thư viện** với các thông tin: *Mã thẻ (đóng vai trò là mã độc giả), Họ tên, Ngày sinh, Số điện thoại, Email cá nhân, Ngày cấp thẻ, Ngày hết hạn*.
- Mỗi độc giả thuộc một **Loại độc giả** (*Mã loại, Tên loại, Số sách mượn tối đa, Thời gian mượn tối đa*). Ví dụ: Giảng viên được mượn 10 cuốn trong 30 ngày, sinh viên được mượn 5 cuốn trong 14 ngày.

**3. Quản lý Nhân viên thư viện:**

- Thư viện có nhiều **Nhân viên thủ thư**. Cần lưu trữ: *Mã nhân viên, Họ tên, Số điện thoại, Cấp bậc, Ca làm việc*.

**4. Quá trình Mượn, Trả và Xử lý vi phạm:**

- Khi độc giả đến mượn sách, nhân viên sẽ lập một **Phiếu mượn**. Mỗi phiếu mượn có *Mã phiếu, Ngày giờ lập phiếu*, do một nhân viên phụ trách và chỉ dành cho một độc giả.
- Trong một phiếu mượn, độc giả có thể mượn nhiều bản sao sách (Mã cá biệt) khác nhau. Tại chi tiết của phiếu mượn, hệ thống cần ghi nhận *Ngày hạn trả* cho từng cuốn sách riêng biệt.
- **Trả sách:** Độc giả không nhất thiết phải trả tất cả sách cùng một lúc. Do đó, hệ thống cần ghi nhận *Ngày trả thực tế* và *Tình trạng sách lúc trả* cho từng bản sao sách trong phiếu mượn.
- **Phạt vi phạm:** Nếu độc giả trả sách trễ hạn, hoặc tình trạng sách lúc trả bị hỏng/mất so với lúc mượn, hệ thống sẽ phát sinh một **Phiếu phạt** gắn với cuốn sách vi phạm đó. Thông tin phạt gồm: *Mã phiếu phạt, Số tiền phạt, Lý do phạt (Trễ hạn/Làm hỏng/Làm mất), Trạng thái thanh toán (Đã đóng/Chưa đóng)*.

**Yêu cầu:**

Từ các mô tả nghiệp vụ thực tế trên, bạn hãy xác định các thực thể, thuộc tính, khóa chính/khóa ngoại và vẽ **Sơ đồ Thực thể - Quan hệ (E-R)** để biểu diễn cấu trúc CSDL cho hệ thống thư viện này.`,
              priority: "medium",
              status: "todo"
            },
            {
              id: "task-db-ch2-02",
              title: "Bài 2: Quản lý hệ thống đặt phòng và dịch vụ chuỗi khách sạn (Phiên bản mở rộng)",
              note: `Để nâng cao chất lượng quản lý và chăm sóc khách hàng, một chuỗi khách sạn cao cấp cần xây dựng một CSDL tập trung cho tất cả các chi nhánh. Qua khảo sát, quy trình hoạt động thực tế được mô tả chi tiết như sau:

**1. Quản lý Chi nhánh Khách sạn và Phòng lưu trú:**

- Hệ thống quản lý một chuỗi khách sạn với nhiều chi nhánh, mỗi chi nhánh lưu thông tin về mã khách sạn (MAKS), tên khách sạn (TENKS) và địa chỉ (DIACHI). Đồng thời, mỗi chi nhánh cần ghi nhận thêm số điện thoại hotline và hạng sao.
- Tại mỗi khách sạn sẽ có nhiều phòng, được quản lý thông qua số phòng (SOP) và gắn liền với mã khách sạn nơi nó trực thuộc.
- Mỗi phòng được phân loại theo loại phòng (LOAIP) và có đơn giá thuê (GIA) đi kèm. Để chi tiết hơn, mỗi loại phòng (như Standard, Deluxe, Suite) còn cần quản lý thông tin về số lượng giường, mô tả tiện nghi, sức chứa tối đa (số người) và tình trạng thực tế của phòng (trống, đang có khách, đang dọn dẹp, hoặc đang bảo trì).

**2. Quản lý Khách hàng:**

- Thông tin cơ bản của khách hàng cần được lưu trữ bao gồm mã khách (MAKHACH), họ tên (HOTEN) và địa chỉ (DIACHI).
- Để phục vụ các nghiệp vụ định danh và hậu mãi, khách hàng bắt buộc phải cung cấp thêm số CCCD/Passport, số điện thoại, Email. Mỗi khách hàng sẽ được xếp vào một hạng thẻ thành viên (Thành viên thường, Bạc, Vàng, Kim cương) dựa trên điểm tích lũy.

**3. Quản lý Đặt phòng (Booking) và Lưu trú:**

- Khách hàng có thể đặt phòng trước cho những khoảng thời gian nhất định; thông tin đặt phòng trên hệ thống sẽ ghi nhận mã khách sạn, mã khách hàng, ngày nhận dự kiến (NGAYNHAN), ngày trả dự kiến (NGAYTRA) và số phòng (SOP) đã chọn.
- Mỗi giao dịch đặt phòng (Booking) được cấp một Mã phiếu đặt, trong đó lưu trữ ngày lập phiếu, số tiền khách đã đặt cọc, trạng thái phiếu (chưa duyệt, đã xác nhận, đã hủy) và nhân viên lễ tân phụ trách. Một phiếu đặt phòng có thể đặt cùng lúc nhiều phòng khác nhau cho một đoàn khách.
- Quy trình thuê phòng thực tế (lúc Check-in) còn được theo dõi thông qua một sổ quản lý khách thuê phòng riêng, trong đó ghi chú rõ ngày đến, ngày đi, phòng số, số người lưu trú thực tế và tiền phí phát sinh.

**4. Quản lý Dịch vụ và Thanh toán Hóa đơn:**

- Bên cạnh việc lưu trú, khách sạn cung cấp một Danh mục dịch vụ (nhà hàng, giặt ủi, spa, xe đưa đón). Mỗi dịch vụ có các thông tin: Mã dịch vụ, Tên dịch vụ, Đơn vị tính và Đơn giá hiện hành.
- Trong thời gian ở tại khách sạn, khách thuê phòng có thể sử dụng các dịch vụ này nhiều lần. Hệ thống cần có phiếu ghi nhận chi tiết việc sử dụng dịch vụ gồm: số phòng gọi dịch vụ, mã dịch vụ, ngày giờ sử dụng, số lượng và thành tiền.
- **Thanh toán:** Khi khách làm thủ tục trả phòng (Check-out), hệ thống tự động tổng hợp một **Hóa đơn**. Hóa đơn bao gồm: Mã hóa đơn, Ngày giờ lập, Nhân viên thu ngân thực hiện, Tổng tiền phòng, Tổng tiền dịch vụ, Thuế VAT, các khoản phụ thu (nếu làm hỏng đồ/trễ giờ) và Số tiền thực tế khách phải thanh toán (sau khi đã trừ đi tiền cọc).

**Yêu cầu:**

Từ các mô tả nghiệp vụ thực tế trên, bạn hãy xác định các tập thực thể, thuộc tính, khóa chính/khóa ngoại và vẽ **Sơ đồ Thực thể - Quan hệ (E-R)** để biểu diễn cấu trúc CSDL cho hệ thống chuỗi khách sạn này.`,
              priority: "medium",
              status: "todo"
            },
            {
              id: "task-db-ch2-03",
              title: "Bài 3: Quản lý hệ thống vận chuyển và giao nhận hàng hóa (Logistics - Phiên bản mở rộng)",
              note: `Nhằm tối ưu hóa chuỗi cung ứng và cho phép khách hàng theo dõi lộ trình đơn hàng theo thời gian thực, một công ty giao nhận Logistics quy mô quốc gia cần xây dựng một CSDL toàn diện. Qua khảo sát, quy trình hoạt động thực tế được mô tả chi tiết như sau:

**1. Quản lý Khách hàng và Đối tác:**

- Hệ thống lưu trữ thông tin tập trung cho mọi **Khách hàng** (có thể đóng vai trò là người gửi hoặc người nhận trong các giao dịch khác nhau) bao gồm: *Mã khách hàng, Họ tên/Tên doanh nghiệp, Số điện thoại, Địa chỉ chi tiết, Loại khách (Cá nhân, Doanh nghiệp đối tác)*.
- Đối với khách hàng doanh nghiệp, hệ thống yêu cầu quản lý thêm *Mã số thuế* và *Mã hợp đồng nguyên tắc* để áp dụng các chính sách chiết khấu cước phí riêng.

**2. Quản lý Bưu cục và Nhân viên:**

- Công ty sở hữu một mạng lưới nhiều **Bưu cục** (Hub/Kho trạm). Mỗi bưu cục có *Mã bưu cục, Tên bưu cục, Cấp bưu cục (Tổng kho, Kho phân loại tỉnh, Trạm giao nhận)* và *Địa chỉ*.
- **Nhân viên** làm việc tại công ty được quản lý bởi *Mã nhân viên, Họ tên, Số điện thoại, Chức vụ (Quản lý kho, Điều phối, Shipper)*. Mỗi nhân viên trực thuộc sự quản lý cố định của một bưu cục.
- Riêng đối với đội ngũ giao hàng (Shipper), hệ thống cần lưu thêm thông tin định danh phương tiện gồm *Biển số xe* và *Loại phương tiện (Xe máy, Xe tải nhỏ, Xe tải lớn)*.

**3. Quản lý Đơn vận (Bưu kiện):**

- Mỗi bưu kiện khi được tiếp nhận sẽ được cấp một **Đơn vận** gắn với một *Mã vận đơn* duy nhất.
- Thông tin chi tiết của đơn vận bao gồm: *Ngày giờ tạo, Khối lượng thực tế (kg), Kích thước (Dài-Rộng-Cao), Mô tả nội dung hàng hóa, Giá trị khai báo, Loại dịch vụ (Hỏa tốc, Tiêu chuẩn, Tiết kiệm)*.
- Trên mỗi đơn vận phải xác định rõ một khách hàng là *Người gửi*, một khách hàng là *Người nhận*, số tiền *Thu hộ (COD)*, *Tổng cước phí vận chuyển*, và *Hình thức thanh toán* (Người gửi trả, Người nhận trả, hoặc Trả cuối tháng đối với doanh nghiệp).

**4. Theo dõi Hành trình (Tracking) và Trạng thái luân chuyển:**

- Sự di chuyển của đơn vận từ lúc nhận hàng đến lúc giao thành công phải qua nhiều khâu luân chuyển giữa các bưu cục. Hệ thống cần thiết kế cấu trúc để lưu lại **Nhật ký hành trình** chi tiết theo thời gian thực cho từng đơn vận.
- Mỗi bản ghi cập nhật hành trình gồm: *Mã nhật ký, Ngày giờ cập nhật, Trạng thái (Đã nhận hàng, Nhập kho, Đang luân chuyển, Xuất kho đi giao, Đã giao thành công, Khách hẹn lại, Chuyển hoàn), Ghi chú bổ sung*.
- Tại mỗi mốc chuyển trạng thái, hệ thống bắt buộc phải xác định được sự kiện đó diễn ra tại *Bưu cục* nào và do *Nhân viên* nào thao tác thực hiện (ví dụ: nhân viên kho xác nhận nhập kho, shipper cập nhật trạng thái đã giao hàng).

**Yêu cầu:**

Từ các mô tả nghiệp vụ thực tế trên, bạn hãy xác định các tập thực thể, thuộc tính, khóa chính/khóa ngoại và vẽ **Sơ đồ Thực thể - Quan hệ (E-R)** để biểu diễn cấu trúc CSDL cho hệ thống Logistics này.`,
              priority: "medium",
              status: "todo"
            },
            {
              id: "task-db-ch2-04",
              title: "Bài 4: Quản lý hệ thống đào tạo của trung tâm ngoại ngữ (Phiên bản mở rộng)",
              note: `Để tối ưu hóa quy trình tuyển sinh, sắp xếp lịch học và theo dõi chất lượng đào tạo, một trung tâm ngoại ngữ lớn cần xây dựng CSDL đồng bộ. Quy trình vận hành thực tế được quy định như sau:

**1. Quản lý Khóa học và Lớp học:**

- Trung tâm cung cấp nhiều **Khóa học** khác nhau, được quản lý bằng: *Mã khóa học, Tên khóa học, Ngôn ngữ đào tạo (Anh, Nhật, Hàn,...), Cấp độ (Cơ bản, Nâng cao, Luyện thi), Thời lượng (tổng số buổi)* và *Học phí tiêu chuẩn*.
- Mỗi khóa học sẽ được mở thành nhiều **Lớp học** tùy theo nhu cầu. Thông tin của lớp học gồm: *Mã lớp, Tên lớp, Ngày khai giảng dự kiến, Ngày kết thúc dự kiến, Sĩ số tối đa, Trạng thái (Sắp khai giảng, Đang học, Đã kết thúc)*.
- Mỗi lớp học cần được xếp **Thời khóa biểu** cụ thể bao gồm các thông tin: *Ngày học trong tuần (thứ 2-4-6 hoặc 3-5-7), Ca học (Sáng, Chiều, Tối - ghi rõ giờ bắt đầu và giờ kết thúc)* và được bố trí tại một *Phòng học* nhất định (Mã phòng, Sức chứa, Trang thiết bị).

**2. Quản lý Giáo viên và Phân công giảng dạy:**

- Hệ thống lưu trữ hồ sơ của **Giáo viên** gồm: *Mã giáo viên, Họ tên, Ngày sinh, Số điện thoại, Email, Loại giáo viên (Cơ hữu, Thỉnh giảng)*. Để phân công đúng người, hệ thống cần lưu lại chi tiết các *Văn bằng/Chứng chỉ chuyên môn* mà giáo viên đó đang sở hữu.
- Quá trình **Phân công giảng dạy**: Một lớp học có thể được phân công cho nhiều giáo viên cùng giảng dạy (ví dụ: một giáo viên dạy Ngữ pháp, một giáo viên nước ngoài dạy Giao tiếp). Trong bảng phân công, hệ thống cần ghi nhận rõ *Mã giáo viên, Mã lớp, Vai trò (Giáo viên chính, Trợ giảng)* và *Tổng số giờ dạy* của từng người trong lớp đó.

**3. Quản lý Học viên, Ghi danh và Học phí:**

- Thông tin **Học viên** được lưu trữ bao gồm: *Mã học viên, Họ tên, Ngày sinh, Địa chỉ, Số điện thoại, Email*.
- Khi học viên muốn tham gia học, nhân viên tư vấn sẽ lập một **Phiếu ghi danh (Đăng ký)**. Một phiếu ghi danh lưu trữ các thông tin: *Mã phiếu, Ngày lập phiếu, Nhân viên tư vấn phụ trách, Mã học viên, Mã lớp đăng ký*. Một học viên có thể lập nhiều phiếu ghi danh ở các thời điểm khác nhau để đăng ký nhiều lớp.
- Kèm theo việc ghi danh là quy trình **Thu học phí**. Biên lai thu tiền sẽ ghi nhận: *Số biên lai, Ngày đóng, Số tiền thực đóng, Hình thức thanh toán (Tiền mặt, Chuyển khoản), Mức chiết khấu/Khuyến mãi (nếu có)*. Một phiếu ghi danh có thể được đóng học phí chia làm nhiều đợt.

**4. Theo dõi Kết quả học tập và Điểm danh:**

- Trong quá trình học, hệ thống cần cho phép giáo viên/trợ giảng ghi nhận **Điểm danh** theo từng buổi học của lớp (Trạng thái: Có mặt, Vắng phép, Vắng không phép).
- Kết thúc khóa học, trung tâm tổ chức thi và ghi nhận **Bảng điểm** cho từng học viên trong lớp. Thông tin lưu trữ gồm: *Điểm giữa kỳ, Điểm cuối kỳ, Điểm trung bình, Đánh giá của giáo viên* và *Trạng thái (Đạt, Không đạt, Bảo lưu)*.

**Yêu cầu:**

Từ các mô tả nghiệp vụ thực tế trên, bạn hãy xác định các tập thực thể, thuộc tính, khóa chính/khóa ngoại và vẽ **Sơ đồ Thực thể - Quan hệ (E-R)** để biểu diễn cấu trúc CSDL cho hệ thống quản lý trung tâm ngoại ngữ này.`,
              priority: "medium",
              status: "todo"
            },
            {
              id: "task-db-ch2-05",
              title: "Bài 5: Quản lý hệ thống dự án của công ty sản xuất phần mềm (Phiên bản mở rộng)",
              note: `Để tối ưu hóa việc phân bổ nguồn lực và theo dõi tiến độ công việc, một công ty sản xuất phần mềm cần xây dựng một cơ sở dữ liệu chi tiết. Quy trình vận hành thực tế được quy định như sau:

**1. Quản lý Phòng ban và Nhân viên:**

- Công ty có một vài phòng ban, các phòng ban được định danh bởi số phòng ban, tên và địa điểm. Một người quản lý sẽ quản lý một phòng ban cụ thể.
- Các nhân viên được định danh bởi ID, tên, địa chỉ, ngày vào công ty. Mỗi lập trình viên gồm có các thông tin như email, số điện thoại, vị trí công việc (ví dụ như lập trình web, lập trình trên thiết bị di động, trưởng nhóm công nghệ, quản lý dự án).
- Mỗi nhân viên làm việc chỉ ở một phòng ban.

**2. Quản lý Dự án phát triển phần mềm:**

- Một công ty sản xuất phần mềm có thể phụ trách một hoặc nhiều dự án phát triển phần mềm. Mỗi dự án sẽ có mã dự án, tên dự án, ngày bắt đầu, hạn kết thúc.
- Mỗi phòng ban liên kết với một số dự án.
- Mỗi dự án phần mềm có một nhóm các lập trình viên tham gia. Mỗi nhân viên có thể tham gia nhiều dự án.

**3. Quản lý Gói công việc (Task) và Chấm công:**

- Một dự án bao gồm các gói công việc được kết nối theo một cấu trúc phân cấp: mỗi gói công việc có thể bao gồm nhiều gói công việc khác.
- Mỗi gói công việc có đúng một nhân viên chịu trách nhiệm chính. Nhân viên có thể chịu trách nhiệm cho một số gói công việc.
- Việc chấm công cho nhân viên sẽ được tính theo số giờ làm việc hàng tuần. Hệ thống cần lưu lại thông tin chấm công chi tiết cho mỗi dự án bao gồm mã nhân viên, mã dự án, tuần và số giờ.

**Yêu cầu:**

Từ các mô tả nghiệp vụ thực tế trên, bạn hãy xác định các tập thực thể, thuộc tính, khóa chính/khóa ngoại và vẽ **Sơ đồ Thực thể - Quan hệ (E-R)** để biểu diễn cấu trúc CSDL cho hệ thống quản lý dự án phần mềm này.`,
              priority: "medium",
              status: "todo"
            }
          ]
        }
      ]
    }
  ]
};