# -*- coding: utf-8 -*-
"""Bổ sung Quyển 2 - Chương 1 (Ràng buộc toàn vẹn & Trigger)."""

MCQ = [
    ("medium", r"Ràng buộc 'Điểm thi `Diem` phải nằm trong khoảng $[0,10]$' thuộc loại ràng buộc toàn vẹn nào?",
     [r"Ràng buộc khóa chính", r"Ràng buộc miền giá trị", r"Ràng buộc tham chiếu", r"Ràng buộc liên bảng"],
     "B", r"Ràng buộc quy định tập giá trị hợp lệ của một thuộc tính là ràng buộc miền giá trị, cài bằng `CHECK`."),
    ("medium", r"Ràng buộc 'Ngày giao hàng $\ge$ ngày đặt hàng' trong cùng một bảng `DONHANG` là:",
     [r"Ràng buộc liên thuộc tính (trên cùng một bộ)", r"Ràng buộc liên quan hệ", r"Ràng buộc thuộc tính tổng hợp", r"Ràng buộc khóa ngoại"],
     "A", r"Điều kiện so sánh hai thuộc tính trong cùng một bộ, có thể khai báo bằng `CHECK (NgayGiao >= NgayDat)`."),
    ("medium", r"Ràng buộc 'Mọi `MaLop` trong `SINHVIEN` phải tồn tại trong `LOPHOC`' là:",
     [r"Ràng buộc miền", r"Ràng buộc duy nhất", r"Ràng buộc khóa chính", r"Ràng buộc toàn vẹn tham chiếu (khóa ngoại)"],
     "D", r"Giá trị khóa ngoại phải trùng một giá trị khóa chính của bảng cha hoặc là `NULL` (nếu cho phép)."),
    ("medium", r"Bảng tầm ảnh hưởng của ràng buộc khóa ngoại: thao tác nào trên BẢNG CHA (được tham chiếu) có thể làm vi phạm?",
     [r"Thêm", r"Xóa và sửa khóa chính", r"Chỉ sửa cột không phải khóa", r"Không thao tác nào"],
     "B", r"Xóa hoặc sửa khóa chính của cha có thể để lại bản ghi con mồ côi. Thêm cha không bao giờ vi phạm."),
    ("medium", r"Khi chạy trigger `AFTER INSERT` trong SQL Server, bảng ảo `INSERTED` và `DELETED` chứa:",
     [r"`INSERTED` chứa các dòng vừa thêm, `DELETED` rỗng", r"`INSERTED` rỗng, `DELETED` chứa dòng vừa thêm", r"Cả hai chứa dòng vừa thêm", r"Cả hai rỗng"],
     "A", r"`INSERT` chỉ có dữ liệu mới nên bảng `DELETED` không có dòng nào."),
    ("medium", r"Trong trigger `AFTER DELETE`, các dòng vừa bị xóa nằm ở:",
     [r"Bảng `INSERTED`", r"Bảng `DELETED`", r"Bảng gốc, chưa bị xóa", r"Nhật ký hệ thống, không truy cập được"],
     "B", r"`DELETED` giữ bản sao các dòng bị xóa; `INSERTED` rỗng."),
    ("medium", r"Trigger `AFTER` (hay `FOR`) được kích hoạt vào thời điểm nào?",
     [r"Trước khi lệnh DML bắt đầu", r"Sau khi lệnh DML đã thực hiện xong và trước khi giao dịch commit", r"Chỉ sau khi hệ thống khởi động lại", r"Thay thế hoàn toàn lệnh DML"],
     "B", r"`AFTER` chạy sau khi thay đổi đã được áp dụng; nếu phát hiện vi phạm, có thể `ROLLBACK TRANSACTION` để hủy cả lệnh gây trigger."),
    ("medium", r"Trong trigger phát hiện vi phạm, câu lệnh `ROLLBACK TRANSACTION` có tác dụng:",
     [r"Chỉ hủy dòng hiện tại", r"Hủy toàn bộ giao dịch, kể cả lệnh DML đã kích hoạt trigger", r"Xóa trigger", r"Khởi động lại máy chủ"],
     "B", r"Trigger chạy trong cùng giao dịch với lệnh DML; rollback hoàn tác tất cả thay đổi của giao dịch đó."),
    ("medium", r"Vì sao ràng buộc 'Sĩ số lớp = số sinh viên của lớp' cần trigger mà không dùng được `CHECK` thông thường?",
     [r"Vì `CHECK` không có kiểu số", r"Vì ràng buộc liên quan đến nhiều bảng và dữ liệu tổng hợp, `CHECK` chỉ kiểm tra trên một dòng", r"Vì trigger luôn nhanh hơn", r"Vì `CHECK` chỉ dùng cho khóa chính"],
     "B", r"`CHECK` đánh giá điều kiện trên dòng hiện tại; ràng buộc liên bảng/tổng hợp cần trigger (hoặc cơ chế khác)."),
    ("medium", r"Mẫu kiểm tra nào đúng trong trigger `AFTER INSERT, UPDATE` để từ chối điểm ngoài $[0,10]$?",
     [r"`IF EXISTS (SELECT * FROM inserted WHERE Diem < 0 OR Diem > 10) ROLLBACK TRANSACTION`", r"`IF Diem < 0 ROLLBACK`", r"`IF (SELECT Diem FROM inserted) < 0 ROLLBACK` (giả định một dòng)", r"`IF EXISTS (SELECT * FROM deleted)`"],
     "A", r"Dùng `EXISTS` trên bảng `inserted` xử lý được cả khi một câu lệnh thêm/sửa nhiều dòng; ý C chỉ đúng khi giả định một dòng."),
    ("medium", r"Trigger trong SQL Server được kích hoạt:",
     [r"Theo mỗi dòng bị tác động", r"Một lần cho mỗi câu lệnh DML, bất kể số dòng bị tác động", r"Chỉ khi người dùng gọi tên", r"Theo thời gian biểu"],
     "B", r"Trigger SQL Server là mức câu lệnh (statement-level): một lần cho mỗi câu lệnh, nên phải viết mã xử lý tập nhiều dòng."),
    ("medium", r"`ON DELETE CASCADE` trên khóa ngoại `KETQUA.MaSV` nghĩa là:",
     [r"Cấm xóa sinh viên còn kết quả", r"Đặt `MaSV` trong kết quả thành `NULL`", r"Xóa sinh viên thì tự động xóa các kết quả liên quan", r"Không có tác dụng"],
     "C", r"`CASCADE` lan truyền hành động xóa xuống bảng con."),

    ("hard", r"Trong trigger `AFTER UPDATE` trên `SINHVIEN`, cách đúng để chỉ xử lý khi cột `MaLop` thực sự có trong danh sách `SET` của lệnh `UPDATE` là:",
     [r"`IF NOT EXISTS (SELECT * FROM deleted)`", r"`IF UPDATE(MaLop)`", r"`IF COLUMNS(MaLop)`", r"`IF @@ROWCOUNT = 0 RETURN`"],
     "B", r"`UPDATE(col)` trả `TRUE` nếu cột được nêu trong mệnh đề `SET` (hoặc có trong lệnh `INSERT`). Nó không bảo đảm giá trị khác đi, cần so sánh `inserted` với `deleted` nếu muốn biết."),
    ("hard", r"Trigger `AFTER INSERT` trên `SINHVIEN` cần cập nhật `LOPHOC.SiSo` khi một lệnh `INSERT` thêm nhiều sinh viên cùng lớp cùng lúc. Cách nào đúng?",
     [r"`UPDATE L SET SiSo = SiSo + 1 FROM LOPHOC L JOIN inserted i ON L.MaLop = i.MaLop`", r"`UPDATE L SET SiSo = SiSo + x.n FROM LOPHOC L JOIN (SELECT MaLop, COUNT(*) AS n FROM inserted GROUP BY MaLop) x ON L.MaLop = x.MaLop`", r"`UPDATE LOPHOC SET SiSo = (SELECT TOP 1 MaLop FROM inserted)`", r"Chỉ cập nhật cho dòng đầu của `inserted`"],
     "B", r"Phải gom nhóm theo lớp và cộng đúng số dòng thêm vào. Ý A chỉ cộng 1 cho mỗi lớp dù thêm nhiều sinh viên (do join không nhân bản trong `UPDATE ... FROM`)."),
    ("hard", r"Ràng buộc 'SiSo của lớp bằng số sinh viên thực tế'. Bảng tầm ảnh hưởng đúng là:",
     [r"`SINHVIEN`: thêm `-`, xóa `-`, sửa MaLop `-`; `LOPHOC`: không", r"`SINHVIEN`: thêm `+`, xóa `+`, sửa MaLop `*`; `LOPHOC`: thêm `-`, xóa `-`, sửa SiSo `*`", r"Chỉ `LOPHOC` bị ảnh hưởng", r"Mọi thao tác đều `-`"],
     "B", r"Thêm/xóa sinh viên và đổi lớp làm lệch sĩ số; sửa `SiSo` trực tiếp cũng có thể gây lệch; thêm/xóa lớp mới (`SiSo = 0`) không làm sai khi chưa có sinh viên."),
    ("hard", r"Khi thực hiện `UPDATE` trong SQL Server, trigger nhìn thấy:",
     [r"`INSERTED` rỗng, `DELETED` chứa giá trị mới", r"`INSERTED` chứa giá trị mới và `DELETED` chứa giá trị cũ của các dòng bị sửa", r"Chỉ bảng gốc", r"Chỉ `DELETED` chứa giá trị mới"],
     "B", r"Một `UPDATE` được xem như xóa dòng cũ và chèn dòng mới. Có thể ghép `inserted` và `deleted` theo khóa để so sánh trước/sau."),
    ("hard", r"Trigger `INSTEAD OF` trên một VIEW cho phép:",
     [r"Chỉ đọc view", r"Chặn lệnh DML gốc và tự viết logic thay thế (ví dụ ghi vào nhiều bảng nền)", r"Xóa view", r"Tăng tốc truy vấn `SELECT`"],
     "B", r"`INSTEAD OF` thay thế lệnh DML; nếu muốn dữ liệu thay đổi, bản thân trigger phải thực hiện các lệnh tương ứng."),
    ("hard", r"Trigger trên `SANPHAM` cập nhật chính bảng `SANPHAM` có thể gây đệ quy. Phát biểu nào đúng?",
     [r"Luôn luôn bị cấm", r"Đệ quy trực tiếp chịu điều khiển bởi tùy chọn `RECURSIVE_TRIGGERS` của CSDL (mặc định tắt); cần thiết kế để tránh vòng lặp vô hạn", r"Đệ quy không bao giờ xảy ra", r"Đệ quy luôn bật mặc định"],
     "B", r"Cần thiết kế điều kiện dừng hoặc dùng `IF UPDATE(...)` để tránh trigger tự kích hoạt lặp."),
    ("hard", r"Ràng buộc 'Tồn kho không âm' khi xuất hàng bằng trigger `AFTER INSERT` trên `CHITIET_PHIEUXUAT`. Trình tự hợp lý là:",
     [r"Kiểm tra `inserted`, nếu vi phạm thì rollback; nếu hợp lệ thì trừ tồn", r"Trừ tồn kho theo `inserted`, sau đó kiểm tra còn dòng `SoLuongTon < 0` hay không, nếu có thì `ROLLBACK`", r"Chỉ trừ tồn mà không cần kiểm tra", r"Xóa chi tiết phiếu"],
     "B", r"Dòng đã được chèn rồi nên trigger tính lại tồn rồi kiểm tra; nếu âm, rollback sẽ hoàn tác cả lệnh chèn và việc trừ tồn."),
    ("hard", r"Khi nào nên ưu tiên ràng buộc khai báo (`PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `UNIQUE`) thay vì trigger?",
     [r"Khi ràng buộc phức tạp liên quan nhiều bảng", r"Khi ràng buộc có thể diễn đạt bằng khai báo, vì được DBMS tối ưu, ít lỗi và áp dụng cho mọi cách truy cập", r"Không bao giờ", r"Chỉ khi bảng rỗng"],
     "B", r"Ràng buộc khai báo rõ ràng, hiệu quả hơn; trigger dành cho các quy tắc nghiệp vụ không khai báo được."),
]

SHORT = [
    (r"Lập bảng tầm ảnh hưởng cho ràng buộc: 'Mỗi sinh viên phải thuộc một lớp tồn tại' giữa `SINHVIEN(MaLop)` và `LOPHOC(MaLop)`.",
     """| Bảng | Thêm | Xóa | Sửa |
| :--- | :---: | :---: | :---: |
| `SINHVIEN` | `+` | `-` | `+ (MaLop)` |
| `LOPHOC` | `-` | `+` | `+ (MaLop)` |""",
     r"Con: thêm/sửa khóa ngoại có thể vi phạm; cha: xóa/sửa khóa chính có thể vi phạm."),
    (r"Viết trigger `AFTER INSERT, UPDATE` trên `KETQUA` từ chối điểm không thuộc $[0,10]$.",
     """```sql
CREATE TRIGGER trg_KetQua_Diem ON KETQUA
AFTER INSERT, UPDATE
AS
BEGIN
  IF EXISTS (SELECT 1 FROM inserted WHERE Diem < 0 OR Diem > 10)
  BEGIN
    RAISERROR(N'Điểm phải nằm trong [0,10]', 16, 1);
    ROLLBACK TRANSACTION;
  END
END
```""",
     r"Nếu chỉ kiểm tra một dòng, `CHECK (Diem BETWEEN 0 AND 10)` là lựa chọn tốt hơn."),
    (r"Viết lệnh thêm ràng buộc `CHECK` bảo đảm `NgayGiao >= NgayDat` cho bảng `DONHANG`.",
     """```sql
ALTER TABLE DONHANG
ADD CONSTRAINT CK_DonHang_Ngay CHECK (NgayGiao >= NgayDat);
```""",
     r"Nếu `NgayGiao` là `NULL`, điều kiện `UNKNOWN` được chấp nhận."),
]

ESSAY = [
    (r"Cài đặt ràng buộc nghiệp vụ 'một giảng viên dạy tối đa 3 lớp trong một học kỳ'",
     r"Bảng `GIANGDAY(MaGV, MaLop, HocKy)` với khóa chính `(MaGV, MaLop, HocKy)`. Yêu cầu: a) phát biểu RBTV theo logic vị từ; b) xác định bối cảnh và bảng tầm ảnh hưởng; c) viết trigger T-SQL hoàn chỉnh xử lý cả trường hợp thêm/sửa nhiều dòng cùng lúc.",
     [r"Bước 1 - Phát biểu: $\forall gv, hk:\ |\{ lop \mid (gv, lop, hk) \in GIANGDAY \}| \le 3$.",
      r"Bước 2 - Bối cảnh: quan hệ `GIANGDAY`.",
      "Bước 3 - Bảng tầm ảnh hưởng:\n| Thao tác | Thêm | Xóa | Sửa |\n| :--- | :---: | :---: | :---: |\n| `GIANGDAY` | `+` | `-` | `+ (MaGV, HocKy)` |",
      "Bước 4 - Trigger:\n```sql\nCREATE TRIGGER trg_GiangDay_Max3 ON GIANGDAY\nAFTER INSERT, UPDATE\nAS\nBEGIN\n  IF EXISTS (\n    SELECT 1\n    FROM GIANGDAY g\n    JOIN (SELECT DISTINCT MaGV, HocKy FROM inserted) i\n      ON g.MaGV = i.MaGV AND g.HocKy = i.HocKy\n    GROUP BY g.MaGV, g.HocKy\n    HAVING COUNT(*) > 3\n  )\n  BEGIN\n    RAISERROR(N'Một giảng viên chỉ dạy tối đa 3 lớp mỗi học kỳ', 16, 1);\n    ROLLBACK TRANSACTION;\n  END\nEND\n```",
      r"Bước 5 - Giải thích: chỉ kiểm tra các cặp `(MaGV, HocKy)` vừa bị tác động (bảng `inserted`) để tránh quét toàn bảng; `GROUP BY ... HAVING COUNT(*) > 3` đếm số lớp thực tế sau khi lệnh đã áp dụng; `ROLLBACK` hoàn tác cả lệnh gây vi phạm.",
      r"Kết luận: xóa không bao giờ làm vi phạm nên không cần trigger `AFTER DELETE`."]),
]
