# Tóm tắt Học thuật: Ngôn ngữ SQL & Kỹ thuật Truy vấn Nâng cao (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Bản chất SQL:** Ngôn ngữ khai báo (Declarative), chỉ định kết quả mong muốn thay vì thuật toán từng bước.
- **Thứ tự viết câu lệnh:** `SELECT` $\to$ `FROM` $\to$ `WHERE` $\to$ `GROUP BY` $\to$ `HAVING` $\to$ `ORDER BY`.
- **Thứ tự thực thi ngầm định trong DBMS:**
  $$\text{FROM} \longrightarrow \text{WHERE} \longrightarrow \text{GROUP BY} \longrightarrow \text{HAVING} \longrightarrow \text{SELECT} \longrightarrow \text{ORDER BY}$$

## 2. Kỹ Thuật Phân Biệt `WHERE` và `HAVING`
- `WHERE`: Lọc từng dòng dữ liệu **trước khi** gom nhóm. Không được dùng hàm kết hợp (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) trong mệnh đề `WHERE`.
- `HAVING`: Lọc các nhóm **sau khi** đã tính toán hàm kết hợp.

## 3. Các Phép Kết Nối Bảng (JOIN)
- **INNER JOIN:** Chỉ lấy dữ liệu khi có sự tương ứng khóa ở cả 2 bảng.
- **LEFT JOIN:** Lấy toàn bộ bảng bên trái, bảng bên phải nếu thiếu sẽ điền `NULL`. Rất hữu ích để tìm các đối tượng **chưa từng phát sinh giao dịch/hoạt động**:
```sql
-- Tìm sinh viên chưa đăng ký bất kỳ môn học nào:
SELECT SV.MaSV, SV.HoTen
FROM SINH_VIEN SV
LEFT JOIN DANG_KY DK ON SV.MaSV = DK.MaSV
WHERE DK.MaSV IS NULL;
```

## 4. Các Mẫu Truy Vấn Con (Subquery Patterns)
1. **Toán tử `IN` / `NOT IN`:** So sánh với tập danh sách kết quả từ truy vấn con.
2. **Toán tử `EXISTS` / `NOT EXISTS`:** Kiểm tra sự tồn tại của ít nhất một dòng thỏa mãn điều kiện liên kết (cho hiệu năng tối ưu với bảng lớn).
