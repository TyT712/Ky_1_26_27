# -*- coding: utf-8 -*-
"""Bổ sung Quyển 1 - Chương 4 (SQL toàn diện).
Lược đồ: KHOA(MaKhoa, TenKhoa), SINHVIEN(MaSV, HoTen, MaKhoa, DiemTB), MONHOC(MaMH, TenMH), KETQUA(MaSV, MaMH, Diem)."""

MCQ = [
    ("medium", r"Điều kiện `Diem BETWEEN 5 AND 8` tương đương với:",
     [r"`Diem > 5 AND Diem < 8`", r"`Diem >= 5 AND Diem <= 8`", r"`Diem >= 5 OR Diem <= 8`", r"`Diem > 5 AND Diem <= 8`"],
     "B", r"`BETWEEN` bao gồm cả hai đầu mút."),
    ("medium", r"Biểu thức nào đếm số khoa khác nhau có sinh viên trong bảng `SINHVIEN`?",
     [r"`COUNT(MaKhoa)`", r"`COUNT(*)`", r"`COUNT(DISTINCT MaKhoa)`", r"`SUM(DISTINCT MaKhoa)`"],
     "C", r"`COUNT(DISTINCT col)` đếm số giá trị khác nhau không `NULL`."),
    ("medium", r"Trong SQL Server, câu lệnh nào lấy 3 sinh viên có `DiemTB` cao nhất?",
     [r"`SELECT TOP 3 * FROM SINHVIEN ORDER BY DiemTB DESC`", r"`SELECT * FROM SINHVIEN ORDER BY DiemTB DESC WHERE ROWNUM <= 3`", r"`SELECT TOP 3 * FROM SINHVIEN ORDER BY DiemTB ASC`", r"`SELECT 3 * FROM SINHVIEN`"],
     "A", r"`TOP n` kết hợp `ORDER BY ... DESC`. Ý C lấy ba người thấp nhất; ý B sai cú pháp (`WHERE` đứng sau `ORDER BY`)."),
    ("medium", r"Để tìm sinh viên chưa có `DiemTB` (giá trị rỗng), ta viết:",
     [r"`WHERE DiemTB = NULL`", r"`WHERE DiemTB = ''`", r"`WHERE DiemTB = 0`", r"`WHERE DiemTB IS NULL`"],
     "D", r"`NULL` không so sánh được bằng `=`; so sánh với `NULL` cho kết quả UNKNOWN. Phải dùng `IS NULL`."),
    ("medium", r"Câu lệnh `SELECT MaKhoa, HoTen, COUNT(*) FROM SINHVIEN GROUP BY MaKhoa` bị lỗi vì:",
     [r"Thiếu mệnh đề `ORDER BY`", r"`HoTen` không nằm trong `GROUP BY` cũng không là hàm tổng hợp", r"Không được dùng `COUNT(*)`", r"`MaKhoa` là khóa chính"],
     "B", r"Các cột ở `SELECT` phải thuộc `GROUP BY` hoặc nằm trong hàm tổng hợp."),
    ("medium", r"Điểm khác nhau giữa `UNION` và `UNION ALL` là:",
     [r"`UNION` giữ dòng trùng, `UNION ALL` loại trùng", r"`UNION` loại trùng, `UNION ALL` giữ toàn bộ dòng", r"Cả hai giống hệt nhau", r"`UNION ALL` chỉ dùng cho cùng một bảng"],
     "B", r"`UNION` tương ứng phép hợp tập hợp (khử trùng, kèm bước sắp xếp/băm), `UNION ALL` giữ nguyên nên nhanh hơn."),
    ("medium", r"Lược đồ `KETQUA(MaSV)` có khóa ngoại tham chiếu `SINHVIEN(MaSV) ON DELETE CASCADE`. Khi xóa một sinh viên:",
     [r"Lệnh xóa bị từ chối nếu còn kết quả", r"Cột `MaSV` trong `KETQUA` được đặt `NULL`", r"Không có gì thay đổi trong `KETQUA`", r"Các dòng `KETQUA` của sinh viên đó bị xóa theo"],
     "D", r"`CASCADE` lan truyền thao tác xóa sang bảng con."),
    ("medium", r"Cột `Diem` của 3 dòng có giá trị `6`, `NULL`, `8`. Kết quả `SELECT AVG(Diem)` là:",
     [r"`7`", r"`4.67`", r"`NULL`", r"`14`"],
     "A", r"Hàm tổng hợp bỏ qua `NULL`: $(6+8)/2 = 7$."),
    ("medium", r"`INNER JOIN` giữa `SINHVIEN` và `KHOA` trên `MaKhoa` trả về:",
     [r"Mọi sinh viên, kể cả sinh viên chưa có khoa", r"Mọi khoa kể cả khoa chưa có sinh viên", r"Chỉ các cặp sinh viên - khoa thỏa điều kiện nối", r"Tích Descartes của hai bảng"],
     "C", r"`INNER JOIN` chỉ giữ các cặp khớp điều kiện."),
    ("medium", r"Câu lệnh `SELECT DiemTB*10 AS D FROM SINHVIEN WHERE D > 50` bị lỗi vì:",
     [r"`WHERE` được thực hiện trước `SELECT`, nên bí danh `D` chưa tồn tại", r"Không thể nhân cột số với hằng", r"Thiếu `GROUP BY`", r"`AS` chỉ dùng trong `ORDER BY`"],
     "A", r"Thứ tự logic: `FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY`. Bí danh chỉ dùng được từ `ORDER BY` trở đi."),
    ("medium", r"Từ khóa `DISTINCT` trong `SELECT DISTINCT MaKhoa FROM SINHVIEN` có tác dụng:",
     [r"Sắp xếp kết quả", r"Đếm số dòng", r"Chỉ lấy dòng đầu tiên", r"Loại bỏ các dòng kết quả trùng nhau"],
     "D", r"`DISTINCT` khử các dòng trùng ở kết quả chiếu."),
    ("medium", r"Toán tử nào kiểm tra một giá trị có nằm trong tập kết quả của truy vấn con không?",
     [r"`LIKE`", r"`IN`", r"`BETWEEN`", r"`IS`"],
     "B", r"`x IN (SELECT ...)` đúng khi `x` bằng ít nhất một giá trị của truy vấn con."),

    ("hard", r"Truy vấn nào cho sinh viên có `DiemTB` cao nhất (kể cả khi có nhiều người đồng hạng)?",
     [r"`SELECT TOP 1 * FROM SINHVIEN ORDER BY DiemTB DESC`", r"`SELECT * FROM SINHVIEN WHERE DiemTB = MAX(DiemTB)`", r"`SELECT * FROM SINHVIEN WHERE DiemTB = (SELECT MAX(DiemTB) FROM SINHVIEN)`", r"`SELECT MAX(DiemTB), HoTen FROM SINHVIEN`"],
     "C", r"Ý A chỉ lấy một người; ý B dùng hàm tổng hợp trong `WHERE` (sai); ý D thiếu `GROUP BY`. Ý C trả về mọi sinh viên đồng hạng."),
    ("hard", r"`KHACHHANG(MaKH)` và `HOADON(MaKH)`, trong đó `HOADON.MaKH` có chứa ít nhất một giá trị `NULL`. Kết quả `SELECT MaKH FROM KHACHHANG WHERE MaKH NOT IN (SELECT MaKH FROM HOADON)` là:",
     [r"Danh sách khách hàng chưa có hóa đơn", r"Toàn bộ khách hàng", r"Báo lỗi cú pháp", r"Tập rỗng"],
     "D", r"`x NOT IN (..., NULL)` cho UNKNOWN với mọi `x` không nằm trong tập nên không dòng nào thỏa. Nên dùng `NOT EXISTS` hoặc lọc `WHERE MaKH IS NOT NULL` trong truy vấn con."),
    ("hard", r"Câu lệnh nào đúng cú pháp để liệt kê các khoa có hơn 2 sinh viên?",
     [r"`SELECT MaKhoa FROM SINHVIEN WHERE COUNT(*) > 2 GROUP BY MaKhoa`", r"`SELECT MaKhoa FROM SINHVIEN GROUP BY MaKhoa HAVING COUNT(*) > 2`", r"`SELECT MaKhoa FROM SINHVIEN HAVING COUNT(*) > 2`", r"`SELECT MaKhoa, COUNT(*) > 2 FROM SINHVIEN`"],
     "B", r"Điều kiện trên hàm tổng hợp phải đặt trong `HAVING` sau `GROUP BY`."),
    ("hard", r"Truy vấn nào tìm sinh viên đã học TẤT CẢ các môn (giả sử `KETQUA` không có dòng trùng cặp `(MaSV,MaMH)`)?",
     [r"`SELECT MaSV FROM KETQUA GROUP BY MaSV HAVING COUNT(MaMH) > 0`", r"`SELECT MaSV FROM KETQUA GROUP BY MaSV HAVING COUNT(DISTINCT MaMH) = (SELECT COUNT(*) FROM MONHOC)`", r"`SELECT MaSV FROM KETQUA WHERE MaMH IN (SELECT MaMH FROM MONHOC)`", r"`SELECT MaSV FROM KETQUA INNER JOIN MONHOC ON 1 = 1`"],
     "B", r"Số môn khác nhau sinh viên đã học phải bằng tổng số môn: cài đặt phép chia bằng đếm. Có thể dùng `NOT EXISTS` lồng nhau."),
    ("hard", r"Bảng `A` có 3 dòng, `B` có 4 dòng. Trong phép `A LEFT JOIN B`, dòng `a1` khớp 2 dòng `B`, `a2` không khớp dòng nào, `a3` khớp 1 dòng `B`. Số dòng kết quả là:",
     [r"3", r"4", r"5", r"12"],
     "B", r"$a_1$ cho 2 dòng, $a_2$ cho 1 dòng (cột $B$ là `NULL`), $a_3$ cho 1 dòng. Tổng $2+1+1 = 4$."),
    ("hard", r"Mệnh đề nào sau đây CÓ THỂ dùng bí danh cột được định nghĩa ở `SELECT`?",
     [r"`WHERE`", r"`GROUP BY` (trong SQL chuẩn)", r"`HAVING` (trong SQL chuẩn)", r"`ORDER BY`"],
     "D", r"`ORDER BY` thực hiện sau `SELECT` nên dùng được bí danh."),
    ("hard", r"Truy vấn `SELECT * FROM SINHVIEN s1 WHERE DiemTB > (SELECT AVG(DiemTB) FROM SINHVIEN s2 WHERE s2.MaKhoa = s1.MaKhoa)` trả về:",
     [r"Sinh viên có điểm cao hơn trung bình toàn trường", r"Sinh viên có điểm cao hơn trung bình của chính khoa mình", r"Sinh viên có điểm thấp hơn trung bình khoa", r"Toàn bộ sinh viên"],
     "B", r"Truy vấn con tương quan (correlated) tính trung bình riêng theo khoa của từng dòng ngoài."),
    ("hard", r"Bảng lương `{10, 10, 8}`. Kết quả `SELECT MAX(Luong) FROM NV WHERE Luong < (SELECT MAX(Luong) FROM NV)` là:",
     [r"10", r"NULL", r"18", r"8"],
     "D", r"Truy vấn con trả `10`; sau đó chọn lương nhỏ hơn 10 là `{8}`, `MAX` là `8` (mức lương cao thứ nhì theo giá trị khác nhau)."),
]

SHORT = [
    (r"Viết SQL liệt kê tên khoa và số sinh viên, chỉ giữ khoa có từ 50 sinh viên trở lên, sắp giảm dần theo số sinh viên.",
     """```sql
SELECT K.TenKhoa, COUNT(*) AS SoSV
FROM KHOA K JOIN SINHVIEN S ON S.MaKhoa = K.MaKhoa
GROUP BY K.MaKhoa, K.TenKhoa
HAVING COUNT(*) >= 50
ORDER BY SoSV DESC;
```""",
     r"Điều kiện trên `COUNT(*)` phải ở `HAVING`; bí danh `SoSV` dùng được trong `ORDER BY`."),
    (r"Viết SQL tìm mã sinh viên đã học tất cả các môn học.",
     """```sql
SELECT MaSV
FROM KETQUA
GROUP BY MaSV
HAVING COUNT(DISTINCT MaMH) = (SELECT COUNT(*) FROM MONHOC);
```""",
     r"Cách khác: `NOT EXISTS (MonHoc ... NOT EXISTS (KetQua ...))`."),
    (r"Viết SQL tăng 0.5 điểm cho mọi kết quả của sinh viên khoa `'CNTT'` nhưng không vượt quá 10.",
     """```sql
UPDATE KETQUA
SET Diem = CASE WHEN Diem + 0.5 > 10 THEN 10 ELSE Diem + 0.5 END
WHERE MaSV IN (SELECT MaSV FROM SINHVIEN WHERE MaKhoa = 'CNTT');
```""",
     r"`CASE` chặn trần 10; truy vấn con lọc theo khoa."),
]

ESSAY = [
    (r"Viết các truy vấn thống kê nâng cao trên CSDL quản lý sinh viên",
     r"Với lược đồ `KHOA`, `SINHVIEN(MaSV, HoTen, MaKhoa, DiemTB)`, `MONHOC`, `KETQUA`. Viết SQL (T-SQL): a) 3 khoa có điểm trung bình sinh viên cao nhất; b) Sinh viên có `DiemTB` cao hơn trung bình khoa của mình; c) Sinh viên chưa đăng ký môn nào; d) Giải thích vì sao câu c) nên dùng `NOT EXISTS` thay vì `NOT IN`.",
     ["Bước 1 - Câu a:\n```sql\nSELECT TOP 3 K.TenKhoa, AVG(S.DiemTB) AS DTB\nFROM KHOA K JOIN SINHVIEN S ON S.MaKhoa = K.MaKhoa\nGROUP BY K.MaKhoa, K.TenKhoa\nORDER BY DTB DESC;\n```",
      "Bước 2 - Câu b (truy vấn tương quan):\n```sql\nSELECT S1.*\nFROM SINHVIEN S1\nWHERE S1.DiemTB > (SELECT AVG(S2.DiemTB) FROM SINHVIEN S2 WHERE S2.MaKhoa = S1.MaKhoa);\n```",
      "Bước 3 - Câu c:\n```sql\nSELECT S.*\nFROM SINHVIEN S\nWHERE NOT EXISTS (SELECT 1 FROM KETQUA K WHERE K.MaSV = S.MaSV);\n```",
      r"Bước 4 - Giải thích: `NOT IN` cho kết quả sai (rỗng) nếu truy vấn con chứa `NULL` do logic ba giá trị; `NOT EXISTS` chỉ kiểm tra sự tồn tại nên không bị ảnh hưởng và thường được tối ưu thành anti-join.",
      r"Kết luận: kết hợp `JOIN`, `GROUP BY`, truy vấn con tương quan và `NOT EXISTS` giải quyết các bài toán thống kê và phủ định phổ biến."]),
]
