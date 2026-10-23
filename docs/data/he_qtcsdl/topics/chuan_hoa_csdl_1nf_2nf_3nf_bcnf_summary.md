# Tóm tắt Học thuật: Chuẩn hóa Dữ liệu (1NF, 2NF, 3NF, BCNF) (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Chuẩn hóa (Normalization):** Quá trình tái cấu trúc lược đồ để triệt tiêu dị thường thêm, xóa, sửa và loại bỏ dư thừa dữ liệu.
- **Thuộc tính nguyên tố vs không nguyên tố:** Thuộc tính nguyên tố nằm trong ít nhất 1 khóa của quan hệ; thuộc tính không nguyên tố không nằm trong bất kỳ khóa nào.

## 2. Tiêu Chuẩn Các Dạng Chuẩn
- **1NF (Dạng chuẩn 1):** Mọi thuộc tính đều mang giá trị nguyên tử (Atomic), không có thuộc tính đa trị hay quan hệ lồng ghép.
- **2NF (Dạng chuẩn 2):** Đạt 1NF và mọi thuộc tính không nguyên tố phải **phụ thuộc hàm đầy đủ** vào khóa chính (không phụ thuộc vào một phần của khóa chính ghép).
- **3NF (Dạng chuẩn 3):** Đạt 2NF và không có thuộc tính không nguyên tố nào **phụ thuộc bắc cầu** vào khóa chính.
  *Điều kiện tương đương:* Với mọi $X \to A \in F^+$ ($A \notin X$): hoặc $X$ là siêu khóa, hoặc $A$ là thuộc tính nguyên tố.
- **BCNF (Dạng chuẩn Boyce-Codd):** Với mọi $X \to A \in F^+$ ($A \notin X$), $X$ **bắt buộc phải là siêu khóa**.

$$\text{BCNF} \subset \text{3NF} \subset \text{2NF} \subset \text{1NF}$$

## 3. Thuật Toán Chuẩn Hóa
1. **Thuật toán chuẩn hóa về 3NF (Thuật toán tổng hợp Bernstein):**
   - Bước 1: Tìm phủ tối thiểu $F_{min}$.
   - Bước 2: Gom nhóm các PTH có cùng vế trái $X \to Y$. Tạo lược đồ con $R_i = X \cup Y$.
   - Bước 3: Nếu chưa có $R_i$ nào chứa khóa của quan hệ ban đầu, thêm một lược đồ con chứa khóa.
   - Bước 4: Loại bỏ các $R_i$ là tập con thực sự của $R_j$.
   - *Tính chất:* Luôn bảo đảm đồng thời **Bảo toàn thông tin** và **Bảo toàn phụ thuộc hàm**.
2. **Thuật toán chuẩn hóa về BCNF:**
   - Phân tách đệ quy theo các PTH $X \to Y$ vi phạm BCNF: $R_1 = X \cup Y$ và $R_2 = R \setminus (Y \setminus X)$.
   - *Tính chất:* Luôn **Bảo toàn thông tin**, nhưng **không bảo đảm bảo toàn phụ thuộc hàm**.
