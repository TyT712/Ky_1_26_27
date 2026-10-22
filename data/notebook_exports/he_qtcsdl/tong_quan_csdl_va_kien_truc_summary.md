# Tóm tắt Học thuật: Tổng quan Cơ sở Dữ liệu & Kiến trúc Hệ QTCSDL (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Cơ sở dữ liệu (Database):** Tập hợp dữ liệu có cấu trúc, lưu trữ trên bộ nhớ ngoài, có mối quan hệ logic, phục vụ nhiều người dùng và nhiều chương trình đồng thời.
- **Hệ quản trị CSDL (DBMS):** Phần mềm trung gian cung cấp các dịch vụ định nghĩa (DDL), thao tác (DML), kiểm soát an toàn và điều khiển tương tranh.
- **Giảm thiểu dư thừa & Không nhất quán:** Ưu điểm vượt trội của DBMS so với hệ thống quản lý tệp tin (File-based System).

## 2. Kiến Trúc 3 Mức ANSI/SPARC & Tính Độc Lập Dữ Liệu
1. **Mức ngoài (View / External Level):** Cách nhìn dữ liệu của từng đối tượng người dùng cụ thể thông qua khung nhìn (View).
2. **Mức khái niệm (Conceptual Level):** Mô tả toàn thể cấu trúc logic của toàn bộ CSDL (các thực thể, mối liên kết, kiểu dữ liệu và ràng buộc toàn vẹn).
3. **Mức trong (Internal / Physical Level):** Chi tiết cấu trúc lưu trữ vật lý trên đĩa (cấu trúc tệp, khối nhớ block, chỉ mục Index, băm Hash).

### Hai cấp độ độc lập dữ liệu:
- **Độc lập dữ liệu logic:** Thay đổi mức khái niệm mà không ảnh hưởng đến mức ngoài và mã nguồn ứng dụng.
- **Độc lập dữ liệu vật lý:** Thay đổi cấu trúc lưu trữ và phương pháp truy xuất ở mức trong mà không ảnh hưởng đến mức khái niệm và mức ngoài.

## 3. Phân Phẩm Ngôn Ngữ CSDL
- **DDL (Data Definition Language):** `CREATE`, `ALTER`, `DROP`.
- **DML (Data Manipulation Language):** `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- **DCL (Data Control Language):** `GRANT`, `REVOKE`.
