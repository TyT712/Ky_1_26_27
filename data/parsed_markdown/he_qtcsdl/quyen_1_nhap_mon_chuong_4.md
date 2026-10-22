# Giáo trình Thực hành Cơ sở Dữ liệu (Phần I - Nhập môn) - Chương 4: Ngôn ngữ Khai thác Cơ sở Dữ liệu (SQL)

<!-- PAGE 108 -->
## 1. Giới Thiệu Ngôn Ngữ SQL (Structured Query Language)

SQL là ngôn ngữ tiêu chuẩn hóa được sử dụng phổ biến nhất trong các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS). SQL có tính phi thủ tục (Non-procedural/Declarative): người dùng chỉ cần chỉ rõ **dữ liệu nào cần lấy**, không cần chỉ dẫn **cách thức lấy như thế nào**.

### 1.1. Các kiểu dữ liệu cơ bản trong SQL
- `CHAR(n)`: Chuỗi ký tự độ dài cố định $n$.
- `VARCHAR(n)`: Chuỗi ký tự độ dài thay đổi tối đa $n$.
- `INT` / `INTEGER`: Số nguyên 4 bytes.
- `FLOAT` / `REAL`: Số thực dấu phẩy động.
- `DECIMAL(p, s)` / `NUMERIC(p, s)`: Số thập phân chính xác với $p$ chữ số tổng cộng và $s$ chữ số phần thập phân.
- `DATE`, `TIME`, `DATETIME`: Kiểu ngày tháng và thời gian.
- `BOOLEAN` / `BIT`: Giá trị logic (`TRUE`, `FALSE`).

<!-- PAGE 114 -->
## 2. Ngôn Ngữ Định Nghĩa Dữ Liệu (DDL - Data Definition Language)

### 2.1. Lệnh tạo bảng (`CREATE TABLE`)
Cú pháp cơ bản kèm các ràng buộc toàn vẹn:

```sql
CREATE TABLE KHOA (
    MaKhoa VARCHAR(10) PRIMARY KEY,
    TenKhoa NVARCHAR(100) NOT NULL,
    NamThanhLap INT CHECK (NamThanhLap >= 1950)
);

CREATE TABLE SINH_VIEN (
    MaSV VARCHAR(10) PRIMARY KEY,
    HoTen NVARCHAR(100) NOT NULL,
    NgaySinh DATE,
    GioiTinh NVARCHAR(5) CHECK (GioiTinh IN (N'Nam', N'Nữ')),
    QueQuan NVARCHAR(100),
    MaKhoa VARCHAR(10),
    CONSTRAINT FK_SinhVien_Khoa FOREIGN KEY (MaKhoa) 
        REFERENCES KHOA(MaKhoa)
        ON UPDATE CASCADE 
        ON DELETE SET NULL
);
```

### 2.2. Lệnh sửa đổi cấu trúc bảng (`ALTER TABLE`)
- Thêm cột mới:
```sql
ALTER TABLE SINH_VIEN ADD Email VARCHAR(100);
```
- Sửa đổi kiểu dữ liệu cột:
```sql
ALTER TABLE SINH_VIEN ALTER COLUMN QueQuan NVARCHAR(150);
```
- Xóa cột:
```sql
ALTER TABLE SINH_VIEN DROP COLUMN Email;
```

### 2.3. Lệnh xóa bảng (`DROP TABLE`)
```sql
DROP TABLE SINH_VIEN;
```

<!-- PAGE 120 -->
### 2.4. Khung nhìn (View)
Khung nhìn là một bảng ảo dựa trên kết quả của một câu lệnh truy vấn `SELECT`:
```sql
CREATE VIEW VW_SINHVIEN_CNTT AS
SELECT MaSV, HoTen, NgaySinh, QueQuan
FROM SINH_VIEN
WHERE MaKhoa = 'CNTT';
```

<!-- PAGE 122 -->
## 3. Ngôn Ngữ Cập Nhật Dữ Liệu (DML - Data Manipulation Language)

### 3.1. Thêm dữ liệu (`INSERT INTO`)
```sql
INSERT INTO KHOA (MaKhoa, TenKhoa, NamThanhLap)
VALUES ('CNTT', N'Công nghệ Thông tin', 1995);

INSERT INTO SINH_VIEN (MaSV, HoTen, NgaySinh, GioiTinh, QueQuan, MaKhoa)
VALUES ('SV001', N'Nguyễn Văn An', '2004-05-15', N'Nam', N'Thừa Thiên Huế', 'CNTT');
```

### 3.2. Sửa đổi dữ liệu (`UPDATE`)
```sql
UPDATE SINH_VIEN
SET QueQuan = N'Đà Nẵng'
WHERE MaSV = 'SV001';
```

### 3.3. Xóa dữ liệu (`DELETE FROM`)
```sql
DELETE FROM SINH_VIEN
WHERE MaSV = 'SV001';
```

<!-- PAGE 124 -->
## 4. Lệnh Truy Vấn Dữ Liệu (`SELECT`)

### 4.1. Cú pháp tổng quát
```sql
SELECT [DISTINCT] Danh_Sach_Cot
FROM Danh_Sach_Bang
[WHERE Dieu_Kien_Loc]
[GROUP BY Cot_Gom_Nhom]
[HAVING Dieu_Kien_Gom_Nhom]
[ORDER BY Cot_Sap_Xep [ASC | DESC]];
```

### 4.2. Thứ tự thực thi logic của câu truy vấn
1. `FROM` và `JOIN`: Xác định các bảng nguồn và thực hiện kết nối.
2. `WHERE`: Lọc các hàng thô không thỏa mãn điều kiện.
3. `GROUP BY`: Gom nhóm các hàng có cùng giá trị trên các cột gom nhóm.
4. `HAVING`: Lọc các nhóm dựa trên các hàm tổng hợp (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).
5. `SELECT`: Tính toán các biểu thức và trích xuất danh sách cột đầu ra.
6. `DISTINCT`: Loại bỏ các hàng kết quả trùng lặp.
7. `ORDER BY`: Sắp xếp các hàng theo thứ tự chỉ định.

<!-- PAGE 132 -->
### 4.3. Các phép kết nối bảng (JOIN Operations)
- **INNER JOIN:** Chỉ trả về các hàng có sự khớp nhau ở cả hai bảng.
```sql
SELECT SV.MaSV, SV.HoTen, K.TenKhoa
FROM SINH_VIEN SV
INNER JOIN KHOA K ON SV.MaKhoa = K.MaKhoa;
```
- **LEFT (OUTER) JOIN:** Trả về tất cả các hàng từ bảng bên trái, các cột bảng bên phải mang giá trị `NULL` nếu không tìm thấy cặp khớp:
```sql
SELECT SV.MaSV, SV.HoTen, KQ.Diem
FROM SINH_VIEN SV
LEFT JOIN KET_QUA KQ ON SV.MaSV = KQ.MaSV;
```

### 4.4. Truy vấn con (Subquery)
- **Truy vấn con với toán tử `IN` / `NOT IN`:**
```sql
SELECT HoTen, QueQuan
FROM SINH_VIEN
WHERE MaSV IN (
    SELECT MaSV FROM KET_QUA WHERE Diem >= 8.5
);
```
- **Truy vấn con tương quan với `EXISTS`:**
```sql
SELECT K.TenKhoa
FROM KHOA K
WHERE EXISTS (
    SELECT 1 FROM SINH_VIEN SV WHERE SV.MaKhoa = K.MaKhoa
);
```

<!-- PAGE 136 -->
## 5. Các Lệnh Về Bảo Mật & Phân Quyền (Data Control Language - DCL)

- Cấp quyền đọc và chèn cho người dùng:
```sql
GRANT SELECT, INSERT ON SINH_VIEN TO User_SinhVien;
```
- Thu hồi quyền:
```sql
REVOKE INSERT ON SINH_VIEN FROM User_SinhVien;
```

<!-- PAGE 142 -->
## 6. Bài Tập Thực Hành Chương 4 Có Lời Giải

**Đề bài:** Cho cơ sở dữ liệu gồm 3 bảng `SINH_VIEN(MaSV, HoTen, MaLop)`, `MON_HOC(MaMH, TenMH, SoTinChi)`, `KET_QUA(MaSV, MaMH, Diem)`.
Viết câu truy vấn SQL tìm danh sách sinh viên (Mã SV, Họ tên) có điểm trung bình chung tích lũy $\ge 8.0$.

**Lời giải SQL:**
```sql
SELECT SV.MaSV, SV.HoTen, ROUND(AVG(KQ.Diem), 2) AS DiemTrungBinh
FROM SINH_VIEN SV
INNER JOIN KET_QUA KQ ON SV.MaSV = KQ.MaSV
GROUP BY SV.MaSV, SV.HoTen
HAVING AVG(KQ.Diem) >= 8.0
ORDER BY DiemTrungBinh DESC;
```
