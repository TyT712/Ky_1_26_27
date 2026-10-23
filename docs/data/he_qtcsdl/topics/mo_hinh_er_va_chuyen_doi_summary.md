# Tóm tắt Học thuật: Mô hình E-R & Quy tắc Chuyển đổi sang Lược đồ Quan hệ (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Mô hình Thực thể - Quan hệ (E-R):** Công cụ thiết kế CSDL mức khái niệm độc lập với phần mềm DBMS và hệ điều hành.
- **Thực thể & Thuộc tính:**
  * Thuộc tính đơn vs Thuộc tính kết hợp (Họ tên $\to$ Họ, Tên).
  * Thuộc tính đơn trị vs Thuộc tính đa trị (Số điện thoại, elip nét đôi).
  * Thuộc tính suy dẫn (Tuổi suy dẫn từ Ngày sinh, elip nét đứt).
- **Khóa:** Siêu khóa $\to$ Khóa dự tuyển (siêu khóa tối tiểu) $\to$ Khóa chính (Primary Key).

## 2. Bản Số & Phân Loại Mối Quan Hệ
- **1 - 1 (Một - Một):** Mỗi cá thể bên này liên kết tối đa 1 cá thể bên kia.
- **1 - N (Một - Nhiều):** Bên Một liên kết nhiều bên Nhiều; bên Nhiều liên kết duy nhất 1 bên Một.
- **N - N (Nhiều - Nhiều):** Cả hai bên đều liên kết nhiều cá thể của nhau. Thường mang thuộc tính riêng của mối quan hệ.

## 3. Bảng Quy Tắc Chuyển Đổi Sang Lược Đồ Quan Hệ (Mapping Rules)
1. **Tập thực thể mạnh:** $\to$ Tạo 1 bảng riêng, khóa chính giữ nguyên.
2. **Quan hệ 1 - N:** $\to$ Lấy khóa chính của bên **"Một"** đưa sang bên **"Nhiều"** làm **khóa ngoại**.
3. **Quan hệ N - N:** $\to$ Bắt buộc tạo **1 bảng mới** với khóa chính là tổ hợp khóa của hai thực thể tham gia:
   $$\text{PK} = (\text{PK}_A, \text{PK}_B)$$
4. **Thuộc tính đa trị:** $\to$ Tạo bảng riêng gồm `(Khóa thực thể, Thuộc tính đa trị)`.
5. **Thực thể yếu:** $\to$ Tạo bảng có khóa chính gồm `(Khóa thực thể chủ, Khóa bộ phận)`.
