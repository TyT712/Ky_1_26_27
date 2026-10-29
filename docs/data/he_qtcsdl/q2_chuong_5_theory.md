# CHƯƠNG 5 (QUYỂN 2): PHỤ THUỘC ĐA TRỊ (MVD) & DẠNG CHUẨN 4 (4NF)

### 1. Sơ Đồ Tiến Hóa Chuẩn Hóa: Từ BCNF Đến Dạng Chuẩn 4 (4NF)
```mermaid
graph TD
    BCNF["Dạng chuẩn BCNF<br>(Đã khử toàn bộ dư thừa từ Phụ thuộc hàm FD)"] --> Anomaly["Dư thừa phát sinh do các mối liên kết 1-nhiều độc lập<br>(Ví dụ: Môn học ➔➔ Giảng viên, Môn học ➔➔ Giáo trình)"]
    Anomaly --> MVD["Lý thuyết Phụ thuộc Đa trị (MVD)<br>X ↠ Y (Giá trị Y độc lập với các thuộc tính còn lại)"]
    MVD --> Fagin["Định lý Fagin: Bảo toàn thông tin với MVD<br>(R_1 ∩ R_2) ↠ (R_1 \\ R_2) HOẶC (R_1 ∩ R_2) ↠ (R_2 \\ R_1)"]
    Fagin --> Norm4NF["Dạng chuẩn 4 (4NF)<br>Mọi MVD không tầm thường đều có vế trái là Siêu khóa"]
```

### 2. Định Nghĩa Phụ Thuộc Đa Trị (Multivalued Dependency - MVD)
Cho lược đồ quan hệ $R(U)$ và $X, Y \subseteq U$, đặt $Z = U \setminus (X \cup Y)$.
Ta nói rằng **$X$ xác định đa trị $Y$** (hay **$Y$ phụ thuộc đa trị vào $X$**), ký hiệu là:
$$X \twoheadrightarrow Y$$
nếu với mọi thể hiện quan hệ $r$ trên $R$ và với bất kỳ hai bộ dữ liệu $t_1, t_2 \in r$ thỏa mãn $t_1[X] = t_2[X]$, luôn luôn tồn tại hai bộ $t_3, t_4 \in r$ sao cho:
1. $t_3[X] = t_1[X], \quad t_3[Y] = t_1[Y], \quad t_3[Z] = t_2[Z]$
2. $t_4[X] = t_1[X], \quad t_4[Y] = t_2[Y], \quad t_4[Z] = t_1[Z]$

- **MVD tầm thường (Trivial MVD):** $X \twoheadrightarrow Y$ là tầm thường nếu $Y \subseteq X$ hoặc $X \cup Y = U$.
- **Mối quan hệ giữa FD và MVD (Luật sao chép):**
  $$X \to Y \implies X \twoheadrightarrow Y$$
  *(Mọi phụ thuộc hàm đều là một trường hợp đặc biệt của phụ thuộc đa trị).*

### 3. Định Lý Fagin (Lossless Join Với MVD)
> **Định lý Fagin:** Phép phân tách lược đồ quan hệ $R$ thành hai lược đồ con $\rho = \{R_1, R_2\}$ (với $R_1 \cup R_2 = U$) là **bảo toàn thông tin (Lossless Join)** khi và chỉ khi:
> $$(R_1 \cap R_2) \twoheadrightarrow (R_1 \setminus R_2) \quad \text{HOẶC} \quad (R_1 \cap R_2) \twoheadrightarrow (R_2 \setminus R_1)$$

### 4. Dạng Chuẩn 4 (4NF - Fourth Normal Form)
- **Định nghĩa:** Lược đồ quan hệ $R(U, D)$ đạt Dạng chuẩn 4 (4NF) nếu với mọi phụ thuộc đa trị không tầm thường $X \twoheadrightarrow Y \in D^+$ (nghĩa là $Y \not\subseteq X$ và $XY \subset U$):
  $$X \text{ bắt buộc phải là một siêu khóa của } R$$
- **Quan hệ thứ bậc hoàn chỉnh:**
  $$\text{4NF} \subset \text{BCNF} \subset \text{3NF} \subset \text{2NF} \subset \text{1NF}$$

---

## Tinh Hoa Kiến Thức & Tóm Tắt Chuyên Sâu (Key Takeaways)
> **Chuyên đề mở rộng:** Ràng buộc Toàn vẹn & Xử lý Vi phạm bằng Trigger

### 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Ràng buộc toàn vẹn (RBTV):** Điều kiện bất biến mà mọi trạng thái CSDL hợp lệ đều phải thỏa mãn ở bất kỳ thời điểm nào.
- **4 yếu tố xác định một RBTV:**
  1. *Điều kiện (Condition):* Biểu thức logic mô tả quy tắc ngữ nghĩa.
  2. *Bối cảnh (Context):* Tập các quan hệ mà RBTV tác động tới.
  3. *Tầm ảnh hưởng (Scope):* Thao tác Thêm, Xóa, Sửa trên từng quan hệ có nguy cơ vi phạm.
  4. *Hành động (Action):* Phản ứng của DBMS khi phát hiện vi phạm (từ chối `ROLLBACK` hoặc lan truyền `CASCADE`).

### 2. Phân Loại Ràng Buộc Toàn Vẹn
- **Trên 1 quan hệ:**
  * Miền giá trị: $\forall t \in KETQUA (0 \le t.DiemThi \le 10)$.
  * Liên thuộc tính: $\forall t \in PHIEUNHAP (t.NgayGiaoHang \ge t.NgayNhap)$.
  * Khóa chính (Toàn vẹn thực thể): Không trùng khóa chính, không chứa giá trị `NULL`.
- **Trên nhiều quan hệ:**
  * Khóa ngoại (Toàn vẹn tham chiếu): $\pi_{FK}(R_1) \subseteq \pi_{PK}(R_2)$. Thao tác Thêm trên bảng con ($R_1$) và Xóa trên bảng cha ($R_2$) có nguy cơ vi phạm.
  * Liên thuộc tính liên quan hệ.

### 3. Bảng Tầm Ảnh Hưởng & Trigger (SQL Server / T-SQL)
- **Bảng ảo `INSERTED` và `DELETED`:**
  * Thao tác `INSERT`: Dữ liệu mới nằm trong `INSERTED`, bảng `DELETED` rỗng.
  * Thao tác `DELETE`: Dữ liệu bị xóa nằm trong `DELETED`, bảng `INSERTED` rỗng.
  * Thao tác `UPDATE`: Dữ liệu cũ nằm trong `DELETED`, dữ liệu mới sau sửa đổi nằm trong `INSERTED`.
- **Mẫu kiểm tra bằng Trigger:**
```sql
CREATE TRIGGER trg_KiemTraRBTV ON TenBang FOR INSERT, UPDATE AS
BEGIN
    SET NOCOUNT ON;
    IF EXISTS (SELECT 1 FROM INSERTED i WHERE [DieuKienViPham])
    BEGIN
        RAISERROR (N'Lỗi vi phạm ràng buộc toàn vẹn!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END
END;
```
