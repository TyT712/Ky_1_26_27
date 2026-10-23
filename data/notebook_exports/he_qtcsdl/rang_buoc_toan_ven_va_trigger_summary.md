# Tóm tắt Học thuật: Ràng buộc Toàn vẹn & Xử lý Vi phạm bằng Trigger (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Ràng buộc toàn vẹn (RBTV):** Điều kiện bất biến mà mọi trạng thái CSDL hợp lệ đều phải thỏa mãn ở bất kỳ thời điểm nào.
- **4 yếu tố xác định một RBTV:**
  1. *Điều kiện (Condition):* Biểu thức logic mô tả quy tắc ngữ nghĩa.
  2. *Bối cảnh (Context):* Tập các quan hệ mà RBTV tác động tới.
  3. *Tầm ảnh hưởng (Scope):* Thao tác Thêm, Xóa, Sửa trên từng quan hệ có nguy cơ vi phạm.
  4. *Hành động (Action):* Phản ứng của DBMS khi phát hiện vi phạm (từ chối `ROLLBACK` hoặc lan truyền `CASCADE`).

## 2. Phân Loại Ràng Buộc Toàn Vẹn
- **Trên 1 quan hệ:**
  * Miền giá trị: $\forall t \in KETQUA (0 \le t.DiemThi \le 10)$.
  * Liên thuộc tính: $\forall t \in PHIEUNHAP (t.NgayGiaoHang \ge t.NgayNhap)$.
  * Khóa chính (Toàn vẹn thực thể): Không trùng khóa chính, không chứa giá trị `NULL`.
- **Trên nhiều quan hệ:**
  * Khóa ngoại (Toàn vẹn tham chiếu): $\pi_{FK}(R_1) \subseteq \pi_{PK}(R_2)$. Thao tác Thêm trên bảng con ($R_1$) và Xóa trên bảng cha ($R_2$) có nguy cơ vi phạm.
  * Liên thuộc tính liên quan hệ.

## 3. Bảng Tầm Ảnh Hưởng & Trigger (SQL Server / T-SQL)
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
