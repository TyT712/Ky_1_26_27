# Giáo trình Thực hành Cơ sở Dữ liệu (Phần I - Nhập môn) - Chương 3: Mô hình Dữ liệu Quan hệ & Đại số Quan hệ

<!-- PAGE 66 -->
## 1. Khái Niệm Cơ Bản Của Mô Hình Dữ Liệu Quan Hệ (Relational Model)

Mô hình dữ liệu quan hệ do E. F. Codd đề xuất năm 1970, biểu diễn toàn bộ dữ liệu dưới dạng các bảng hai chiều (gọi là các **quan hệ - relations**).

### 1.1. Các định nghĩa hình thức
- **Thuộc tính (Attribute):** Cột của bảng, đại diện cho một đặc trưng của đối tượng cần quản lý. Mỗi thuộc tính $A_i$ có một miền giá trị xác định $dom(A_i)$.
- **Lược đồ quan hệ (Relation Schema):** Ký hiệu $R(A_1, A_2, \dots, A_n)$ bao gồm tên quan hệ $R$ và danh sách các thuộc tính $A_1, A_2, \dots, A_n$. Bậc (Degree) của lược đồ quan hệ là số lượng thuộc tính $n$.
- **Bộ giá trị (Tuple):** Một hàng của bảng, ký hiệu $t = (v_1, v_2, \dots, v_n)$ với $v_i \in dom(A_i)$. Lực lượng (Cardinality) của quan hệ là số lượng bộ giá trị hiện có trong quan hệ.
- **Quan hệ (Relation):** Thể hiện cụ thể $r(R)$ của lược đồ quan hệ $R$ tại một thời điểm, là tập hợp con của tích Descartes các miền giá trị:
  $$r(R) \subseteq dom(A_1) \times dom(A_2) \times \dots \times dom(A_n)$$

<!-- PAGE 68 -->
### 1.2. Khóa và Ràng buộc Toàn vẹn (Keys & Integrity Constraints)
1. **Ràng buộc khóa (Key Constraint):**
   - Không được phép có hai bộ khác nhau trong cùng một quan hệ có cùng giá trị trên các thuộc tính khóa.
   - **Khóa ngoại (Foreign Key):** Tập thuộc tính $FK$ của quan hệ $R_1$ được gọi là khóa ngoại tham chiếu đến quan hệ $R_2$ nếu các giá trị của $FK$ trong $R_1$ phải xuất hiện trong tập khóa chính $PK$ của $R_2$ hoặc mang giá trị `NULL`.
2. **Ràng buộc thực thể (Entity Integrity):** Khóa chính của quan hệ không được phép mang giá trị `NULL`.
3. **Ràng buộc toàn vẹn tham chiếu (Referential Integrity):** Ngăn chặn việc một khóa ngoại trỏ tới một bản ghi không tồn tại trong bảng được tham chiếu.

<!-- PAGE 71 -->
## 2. Quy Tắc Chuyển Đổi Từ Sơ Đồ E-R Sang Lược Đồ Quan Hệ

| Loại cấu trúc trong E-R | Quy tắc chuyển đổi sang Lược đồ Quan hệ | Ví dụ minh họa |
| :--- | :--- | :--- |
| **Tập thực thể mạnh** | Tạo một quan hệ riêng biệt. Khóa chính của tập thực thể trở thành khóa chính của quan hệ. | `SINH_VIEN(MaSV, HoTen, NgaySinh, QueQuan)` |
| **Mối quan hệ Một - Nhiều (1 - N)** | Đưa khóa chính của bên "Một" vào bên "Nhiều" để làm **khóa ngoại**. Nếu mối quan hệ có thuộc tính riêng, đưa các thuộc tính đó vào bên "Nhiều". | Bảng `LOP(MaLop, TenLop, MaKhoa)` với `MaKhoa` là khóa ngoại tham chiếu đến `KHOA(MaKhoa)` |
| **Mối quan hệ Nhiều - Nhiều (N - N)** | Bắt buộc tạo một **quan hệ mới**. Khóa chính của quan hệ mới là sự kết hợp các khóa chính của hai tập thực thể tham gia, đồng thời chứa các thuộc tính riêng của mối quan hệ. | `DANG_KY(MaSV, MaMH, HocKy, DiemThi)` với khóa chính là `(MaSV, MaMH)` |
| **Mối quan hệ Một - Một (1 - 1)** | Có thể chọn khóa chính của một trong hai bên làm khóa ngoại của bên còn lại (ưu tiên đặt vào bên có sự tham gia toàn phần), hoặc gộp thành một bảng nếu cả hai bên tham gia toàn phần. | `KHOA(MaKhoa, TenKhoa, MaTruongKhoa)` tham chiếu đến `GIANG_VIEN(MaGV)` |
| **Thuộc tính đa trị** | Tạo một quan hệ riêng gồm khóa chính của thực thể gốc và thuộc tính đa trị. Khóa chính là tổ hợp của cả hai thuộc tính. | `SO_DIEN_THOAI(MaSV, SoDT)` |

<!-- PAGE 75 -->
## 3. Các Phép Toán Đại Số Quan Hệ (Relational Algebra)

Đại số quan hệ là một hệ thống hình thức bao gồm tập các phép toán nhận đầu vào là một hoặc hai quan hệ và cho kết quả là một quan hệ mới.

### 3.1. Nhóm các phép toán tập hợp kinh điển
Giả sử quan hệ $R$ và $S$ khả hợp (cùng bậc và tương thích miền giá trị thuộc tính):
1. **Phép hợp (Union - $\cup$):**
   $$R \cup S = \{ t \mid t \in R \text{ hoặc } t \in S \}$$
2. **Phép giao (Intersection - $\cap$):**
   $$R \cap S = \{ t \mid t \in R \text{ và } t \in S \}$$
3. **Phép trừ (Difference - $-$):**
   $$R - S = \{ t \mid t \in R \text{ và } t \notin S \}$$
4. **Phép tích Descartes (Cartesian Product - $\times$):**
   $$R \times S = \{ t_R \circ t_S \mid t_R \in R \text{ và } t_S \in S \}$$

<!-- PAGE 80 -->
### 3.2. Nhóm các phép toán quan hệ chuyên biệt

#### 1. Phép chọn (Selection - $\sigma$)
Trích xuất các bộ giá trị trong quan hệ $R$ thỏa mãn một biểu thức điều kiện logic $C$:
$$\sigma_{C}(R) = \{ t \in R \mid C(t) = \text{True} \}$$
- *Ví dụ:* Tìm sinh viên có điểm trung bình lớn hơn 8.0:
  $$\sigma_{DiemTB > 8.0}(SINH\_VIEN)$$

#### 2. Phép chiếu (Projection - $\pi$)
Trích xuất một tập con các thuộc tính $L = \{A_1, A_2, \dots, A_k\}$ từ quan hệ $R$ và tự động loại bỏ các bộ trùng lặp:
$$\pi_{L}(R) = \{ t[L] \mid t \in R \}$$
- *Ví dụ:* Lấy ra danh sách mã số và họ tên của tất cả sinh viên:
  $$\pi_{MaSV, HoTen}(SINH\_VIEN)$$

#### 3. Phép kết nối điều kiện ($\theta$-Join - $\bowtie_\theta$)
Kết hợp các bộ từ hai quan hệ $R$ và $S$ thỏa mãn điều kiện kết nối $\theta$:
$$R \bowtie_\theta S = \sigma_\theta(R \times S)$$

#### 4. Phép kết tự nhiên (Natural Join - $\bowtie$)
Trường hợp đặc biệt của phép kết bằng trên tất cả các thuộc tính có cùng tên của hai quan hệ, tự động loại bỏ cột trùng lặp:
$$R \bowtie S$$

#### 5. Phép chia (Division - $\div$)
Áp dụng cho bài toán tìm các đối tượng liên kết với **tất cả** các đối tượng trong tập khác.
- *Ví dụ:* Tìm mã sinh viên đã học tất cả các môn học có trong danh sách môn của ngành CNTT:
  $$\pi_{MaSV, MaMH}(HOC) \div \pi_{MaMH}(\sigma_{Nganh='CNTT'}(MON\_HOC))$$

<!-- PAGE 86 -->
## 4. Bảng Dữ Liệu Quan Hệ Mẫu & Minh Họa Truy Vấn

### Bảng `SINH_VIEN`:
| MaSV | HoTen | GioiTinh | QueQuan | MaLop |
| :--- | :--- | :--- | :--- | :--- |
| SV01 | Nguyễn Văn An | Nam | Hà Nội | L01 |
| SV02 | Trần Thị Bình | Nữ | Đà Nẵng | L01 |
| SV03 | Lê Văn Cường | Nam | Huế | L02 |

### Bảng `KET_QUA`:
| MaSV | MaMH | Diem |
| :--- | :--- | :--- |
| SV01 | CSDL | 8.5 |
| SV01 | CTDL | 9.0 |
| SV02 | CSDL | 7.0 |
| SV03 | CSDL | 9.5 |

**Truy vấn Đại số quan hệ:** Tìm họ tên của các sinh viên quê ở 'Huế' và có điểm môn 'CSDL' $\ge 8.0$:
$$\pi_{HoTen}(\sigma_{QueQuan='Hue' \land MaMH='CSDL' \land Diem \ge 8.0}(SINH\_VIEN \bowtie KET\_QUA))$$
Kết quả: `Lê Văn Cường`.
