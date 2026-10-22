# Giáo trình Thực hành Cơ sở Dữ liệu (Phần I - Nhập môn) - Chương 2: Mô hình Thực thể - Quan hệ (Entity - Relationship Model)

<!-- PAGE 40 -->
## 1. Quá Trình Thiết Kế Cơ Sở Dữ Liệu

Thiết kế cơ sở dữ liệu là quá trình chuyển đổi các yêu cầu thông tin trong thế giới thực thành một mô hình dữ liệu có cấu trúc có thể cài đặt trên hệ quản trị CSDL cụ thể. Quá trình này gồm 4 giai đoạn chính:

1. **Giai đoạn phân tích yêu cầu (Requirements Analysis):** Khảo sát hiện trạng, thu thập và lập tài liệu các yêu cầu dữ liệu và yêu cầu xử lý của người dùng.
2. **Giai đoạn thiết kế khái niệm (Conceptual Design):** Xây dựng sơ đồ thực thể - quan hệ (E-R Diagram) độc lập với hệ quản trị CSDL và phần cứng.
3. **Giai đoạn thiết kế logic (Logical Design):** Chuyển đổi mô hình E-R thành lược đồ cơ sở dữ liệu quan hệ (Relational Schema) và thực hiện chuẩn hóa dữ liệu.
4. **Giai đoạn thiết kế vật lý (Physical Design):** Chọn cấu trúc tệp, phương pháp đánh chỉ mục và phân vùng lưu trữ cho hệ quản trị CSDL đã chọn.

<!-- PAGE 42 -->
## 2. Các Khái Niệm Cơ Bản Của Mô Hình Thực Thể - Quan Hệ (E-R)

### 2.1. Thực thể và Tập thực thể (Entity & Entity Set)
- **Thực thể (Entity):** Là một đối tượng cụ thể hoặc trừu tượng trong thế giới thực, có thể phân biệt được với các đối tượng khác (Ví dụ: sinh viên Nguyễn Văn A, môn học Hệ CSDL).
- **Tập thực thể (Entity Set):** Tập hợp các thực thể cùng loại, có chung tập các thuộc tính (Ví dụ: tập thực thể `SINH_VIEN`, tập thực thể `MON_HOC`).

### 2.2. Thuộc tính (Attribute)
Thuộc tính mô tả các đặc trưng của tập thực thể. Phân loại thuộc tính:
- **Thuộc tính đơn (Simple Attribute):** Thuộc tính mang giá trị nguyên tử, không thể phân chia nhỏ hơn (Ví dụ: `DiemSo`, `Tuoi`).
- **Thuộc tính kết hợp (Composite Attribute):** Thuộc tính có thể phân tích thành các thành phần nhỏ hơn (Ví dụ: `HoTen` gồm `Ho`, `TenDem`, `Ten`; `DiaChi` gồm `SoNha`, `Duong`, `Quan`, `ThanhPho`).
- **Thuộc tính đơn trị (Single-valued Attribute):** Mỗi thực thể chỉ có một giá trị duy nhất (Ví dụ: `NgaySinh`).
- **Thuộc tính đa trị (Multi-valued Attribute):** Một thực thể có thể có nhiều giá trị (Ví dụ: `SoDienThoai`, `Email`). Ký hiệu hình elip nét đôi.
- **Thuộc tính suy dẫn (Derived Attribute):** Giá trị được tính toán từ các thuộc tính khác (Ví dụ: `Tuoi` suy dẫn từ `NgaySinh` và ngày hiện tại). Ký hiệu nét đứt.

### 2.3. Khóa của tập thực thể (Keys)
- **Siêu khóa (Superkey):** Tập hợp một hoặc nhiều thuộc tính cho phép xác định duy nhất từng thực thể trong tập thực thể.
- **Khóa dự tuyển (Candidate Key):** Siêu khóa tối tiểu (không chứa bất kỳ tập con thực sự nào cũng là siêu khóa).
- **Khóa chính (Primary Key):** Là khóa dự tuyển được người thiết kế lựa chọn để định danh duy nhất các thực thể trong tập thực thể. Thuộc tính khóa chính được gạch chân trong sơ đồ E-R.

<!-- PAGE 44 -->
## 3. Mối Quan Hệ và Phân Loại Mối Quan Hệ (Relationship Types)

### 3.1. Bản số của mối quan hệ (Cardinality Ratio)
Đối với mối quan hệ nhị nguyên giữa hai tập thực thể $A$ và $B$, bản số quy định số lượng thực thể của $B$ có thể liên kết với một thực thể của $A$:

1. **Quan hệ Một - Một (1 - 1):**
   - Một thực thể thuộc $A$ liên kết với tối đa một thực thể thuộc $B$, và ngược lại.
   - *Ví dụ:* Khoa - Trưởng khoa (`KHOA` và `GIANG_VIEN`), mỗi khoa có một trưởng khoa duy nhất và mỗi giảng viên làm trưởng khoa tối đa một khoa.

2. **Quan hệ Một - Nhiều (1 - N):**
   - Một thực thể thuộc $A$ liên kết với nhiều thực thể thuộc $B$, nhưng mỗi thực thể thuộc $B$ chỉ liên kết với tối đa một thực thể thuộc $A$.
   - *Ví dụ:* Khoa - Lớp học (`KHOA` và `LOP`), một khoa quản lý nhiều lớp, nhưng mỗi lớp thuộc về một khoa duy nhất.

3. **Quan hệ Nhiều - Nhiều (N - N):**
   - Một thực thể thuộc $A$ liên kết với nhiều thực thể thuộc $B$, và ngược lại.
   - *Ví dụ:* Sinh viên - Môn học (`SINH_VIEN` và `MON_HOC`), một sinh viên có thể đăng ký nhiều môn học và một môn học có nhiều sinh viên theo học. Mối quan hệ này có thể chứa thuộc tính bổ sung như `DiemThi`.

<!-- PAGE 49 -->
### 3.2. Mối quan hệ phản xạ (Recursive Relationship)
Một tập thực thể có thể tham gia vào mối quan hệ với chính nó dưới các vai trò khác nhau.
- *Ví dụ:* Mối quan hệ `QUAN_LY` trong tập thực thể `NHAN_VIEN`: Một nhân viên có thể là người quản lý các nhân viên khác, và mỗi nhân viên chịu sự quản lý của một nhân viên cấp trên.

<!-- PAGE 51 -->
## 4. Ký Hiệu Chuẩn Trên Sơ Đồ Thực Thể - Quan Hệ (E-R Diagram)

| Ký hiệu hình học | Ý nghĩa trong sơ đồ E-R |
| :--- | :--- |
| **Hình chữ nhật** | Tập thực thể (Entity Set) |
| **Hình chữ nhật nét đôi** | Tập thực thể yếu (Weak Entity Set) - phụ thuộc tồn tại vào thực thể chủ |
| **Hình thoi** | Mối quan hệ (Relationship Set) |
| **Hình thoi nét đôi** | Mối quan hệ xác định (Identifying Relationship) cho tập thực thể yếu |
| **Hình elip** | Thuộc tính (Attribute) |
| **Hình elip có gạch chân** | Thuộc tính khóa chính (Primary Key Attribute) |
| **Hình elip nét đôi** | Thuộc tính đa trị (Multivalued Attribute) |
| **Hình elip nét đứt** | Thuộc tính suy dẫn (Derived Attribute) |

<!-- PAGE 54 -->
## 5. Tóm Tắt & Bài Tập Chương 2

### 5.1. Bài tập có hướng dẫn
**Đề bài:** Hãy thiết kế sơ đồ E-R cho hệ thống quản lý thư viện trường đại học với các yêu cầu sau:
- Mỗi độc giả có mã độc giả (khóa), họ tên, lớp, ngày sinh.
- Mỗi cuốn sách có mã sách (khóa), tên sách, tên tác giả, năm xuất bản.
- Độc giả có thể mượn nhiều cuốn sách, và mỗi cuốn sách có thể được mượn bởi nhiều độc giả vào các thời điểm khác nhau. Cần ghi nhận ngày mượn, ngày hẹn trả và ngày trả thực tế.

**Lời giải phân tích:**
1. *Các tập thực thể:*
   - `DOC_GIA`(`MaDG`, `HoTen`, `Lop`, `NgaySinh`) với `MaDG` là khóa chính.
   - `SACH`(`MaSach`, `TenSach`, `TacGia`, `NamXB`) với `MaSach` là khóa chính.
2. *Mối quan hệ:*
   - Mối quan hệ `MUON` kết nối giữa `DOC_GIA` và `SACH`.
   - Bản số quan hệ: Nhiều - Nhiều (N - N).
   - Thuộc tính của mối quan hệ: `NgayMuon`, `NgayHenTra`, `NgayTraThucTe`.
