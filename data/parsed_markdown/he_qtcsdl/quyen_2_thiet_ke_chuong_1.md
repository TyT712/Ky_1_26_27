# CHƯƠNG 1. RÀNG BUỘC TOÀN VẸN TRÊN CƠ SỞ DỮ LIỆU

<!-- PAGE 15 -->

## 1. MỞ ĐẦU VÀ MỤC TIÊU
Ràng buộc toàn vẹn (RBTV - Integrity Constraints) và kiểm tra sự vi phạm ràng buộc toàn vẹn là hai trong số những vấn đề rất quan trọng trong quá trình phân tích, thiết kế và khai thác cơ sở dữ liệu (CSDL). Trong quá trình phân tích thiết kế CSDL, nếu không quan tâm đúng mức đến những vấn đề trên, thì có thể dẫn đến những hậu quả rất nghiêm trọng về tính an toàn và toàn vẹn dữ liệu, đặc biệt trong những CSDL quy mô lớn.

### Mục tiêu chương:
- Trình bày các kiểu ràng buộc toàn vẹn trong hệ quản trị CSDL quan hệ.
- Phân tích rõ các ràng buộc toàn vẹn trên yêu cầu quản lý dữ liệu thực tế, giảm thiểu rủi ro dị thường và sai lệch dữ liệu.
- Thiết kế bảng tầm ảnh hưởng đối với các thao tác cập nhật (Thêm, Xóa, Sửa).
- Cài đặt cơ chế kiểm tra và xử lý vi phạm ràng buộc toàn vẹn thông qua việc xây dựng các Trigger (T-SQL / SQL Server).

---

## 2. ĐỊNH NGHĨA VÀ CÁC YẾU TỐ CỦA RÀNG BUỘC TOÀN VẸN
### 2.1. Định nghĩa Ràng buộc toàn vẹn
Trong một CSDL, luôn luôn tồn tại rất nhiều mối liên hệ và sự ràng buộc qua lại giữa các thuộc tính, giữa các bộ với nhau. Ràng buộc toàn vẹn là một **điều kiện bất biến** mà tất cả các thể hiện (instance) của các quan hệ có liên quan trong CSDL đều phải thỏa mãn ở bất kỳ thời điểm nào.

> **Định nghĩa:** Một ràng buộc toàn vẹn $R$ là một vị từ logic (quy tắc nghiệp vụ) áp đặt lên một tập các quan hệ trong CSDL sao cho một trạng thái CSDL được xem là hợp lệ (consistent/valid state) khi và chỉ khi $R$ nhận giá trị Chân lý (TRUE).

<!-- PAGE 16 -->

### 2.2. Các yếu tố cấu thành một Ràng buộc toàn vẹn
Mỗi ràng buộc toàn vẹn khi được phát biểu và thiết kế cần phải xác định đầy đủ 4 yếu tố:

1. **Điều kiện (Condition):** Là biểu thức logic hoặc quy tắc mô tả ngữ nghĩa ràng buộc cần thỏa mãn (thường được biểu diễn bằng ngôn ngữ tự nhiên, đại số quan hệ, hoặc logic vị từ bậc nhất).
2. **Bối cảnh (Context):** Là tập hợp các quan hệ mà ràng buộc đó tác động trực tiếp đến.
3. **Tầm ảnh hưởng (Scope of Impact):** Xác định các thao tác cập nhật (Thêm - Insert, Xóa - Delete, Sửa - Update) trên từng quan hệ trong bối cảnh có thể dẫn đến khả năng vi phạm ràng buộc hay không.
4. **Hành động khi vi phạm (Action on Violation):** Phản ứng của hệ thống khi phát hiện thao tác cập nhật làm vi phạm ràng buộc (từ chối thao tác và hủy giao dịch - `ROLLBACK`, hoặc kích hoạt các thao tác phụ thuộc dây chuyền - `CASCADE`).

<!-- PAGE 18 -->

### 2.3. Thiết kế Bảng tầm ảnh hưởng (Impact Matrix)
Bảng tầm ảnh hưởng là công cụ hình thức hóa quan trọng trong thiết kế CSDL nhằm xác định chính xác thao tác nào trên quan hệ nào cần phải kiểm tra tính toàn vẹn:

- Ký hiệu:
  - `+` : Cần kiểm tra ràng buộc khi thao tác diễn ra (vì có nguy cơ vi phạm).
  - `-` : Không cần kiểm tra ràng buộc (vì thao tác không bao giờ làm vi phạm ràng buộc này).
  - `*` : Chỉ cần kiểm tra khi thuộc tính được sửa nằm trong danh sách các thuộc tính tham gia ràng buộc.

| Quan hệ | Thêm (Insert) | Xóa (Delete) | Sửa (Update) |
| :--- | :---: | :---: | :---: |
| $R_1$ | $+$ / $-$ | $+$ / $-$ | $*$ |
| $R_2$ | $+$ / $-$ | $+$ / $-$ | $*$ |

<!-- PAGE 20 -->

---

## 3. PHÂN LOẠI RÀNG BUỘC TOÀN VẸN

### 3.1. Ràng buộc toàn vẹn có bối cảnh là một quan hệ
1. **Ràng buộc miền giá trị (Domain Constraints):**
   - Áp đặt lên từng thuộc tính đơn lẻ của quan hệ.
   - Ví dụ: `DiemThi >= 0 AND DiemThi <= 10`, `Phai IN ('Nam', 'Nu')`.
   - Biểu diễn logic: $\forall t \in KETQUA (0 \le t.DiemThi \le 10)$.

2. **Ràng buộc liên thuộc tính trong cùng một quan hệ (Intra-relation Attribute Constraints):**
   - Mối quan hệ logic giữa hai hay nhiều thuộc tính trong cùng một bộ dữ liệu.
   - Ví dụ: Trong quan hệ `PHIEUNHAP(MaPN, NgayNhap, NgayGiaoHang)`, ngày giao hàng phải lớn hơn hoặc bằng ngày lập phiếu nhập:
     $$\forall t \in PHIEUNHAP (t.NgayGiaoHang \ge t.NgayNhap)$$

3. **Ràng buộc liên bộ trong cùng một quan hệ (Intra-relation Tuple Constraints):**
   - Quy định mối quan hệ giữa các bộ khác nhau trong cùng một quan hệ.
   - **Ràng buộc khóa chính (Primary Key / Entity Integrity):** Không tồn tại hai bộ khác nhau có cùng giá trị khóa chính và khóa chính không được nhận giá trị `NULL`:
     $$\forall t_1, t_2 \in R ((t_1 \ne t_2) \implies (t_1[K] \ne t_2[K]))$$

<!-- PAGE 21 -->

### 3.2. Ràng buộc toàn vẹn có bối cảnh gồm nhiều quan hệ
1. **Ràng buộc khóa ngoại / Toàn vẹn tham chiếu (Foreign Key / Referential Integrity):**
   - Nếu thuộc tính $FK$ của quan hệ $R_1$ tham chiếu đến khóa chính $PK$ của quan hệ $R_2$, thì mọi giá trị của $t_1[FK]$ phải xuất hiện trong $R_2[PK]$ hoặc mang giá trị `NULL`.
   - Biểu diễn logic:
     $$\pi_{FK}(R_1) \subseteq \pi_{PK}(R_2)$$
   - **Bảng tầm ảnh hưởng của Ràng buộc khóa ngoại:**

| Quan hệ | Thêm (Insert) | Xóa (Delete) | Sửa (Update) |
| :--- | :---: | :---: | :---: |
| **$R_1$ (Quan hệ tham chiếu)** | $+$ | $-$ | $* (FK)$ |
| **$R_2$ (Quan hệ được tham chiếu)** | $-$ | $+$ | $* (PK)$ |

2. **Ràng buộc liên thuộc tính liên quan hệ:**
   - Điều kiện liên kết dữ liệu giữa các thuộc tính thuộc các quan hệ khác nhau.
   - Ví dụ: Trong CSDL Bán hàng gồm `HOADON(SoHD, NgayLap, MaKH)` và `CHITIET_HD(SoHD, MaSP, SoLuong, NgayGiao)`:
     $$\forall t_1 \in HOADON, \forall t_2 \in CHITIET\_HD ((t_1.SoHD = t_2.SoHD) \implies (t_2.NgayGiao \ge t_1.NgayLap))$$

<!-- PAGE 25 -->

---

## 4. BIỂU DIỄN RÀNG BUỘC TOÀN VẸN BẰNG PHỤ THUỘC HÀM
Một lớp lớn các ràng buộc toàn vẹn ngữ nghĩa có thể được biểu diễn hình thức dưới dạng các Phụ thuộc hàm (Functional Dependencies - FD):
- Nếu hai bộ bằng nhau trên tập thuộc tính $X$ thì chúng bắt buộc phải bằng nhau trên tập thuộc tính $Y$:
  $$X \to Y \iff (\forall t_1, t_2 \in R) (t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y])$$
- Các ràng buộc về khóa chính, khóa duy nhất (UNIQUE) là trường hợp đặc biệt của phụ thuộc hàm: $K \to U$ (với $U$ là toàn thể tập thuộc tính của lược đồ quan hệ).

<!-- PAGE 26 -->

---

## 5. XỬ LÝ VI PHẠM RÀNG BUỘC TOÀN VẸN BẰNG TRIGGER
Trigger là một đoạn chương trình thủ tục được lưu trữ trong CSDL (Stored Procedure đặc biệt) tự động thực thi (kích hoạt) khi có một biến cố cập nhật dữ liệu (`INSERT`, `UPDATE`, `DELETE`) tác động lên bảng dữ liệu tương ứng.

### 5.1. Hai bảng ảo logic trong Trigger (SQL Server / T-SQL)
Hệ quản trị CSDL SQL Server duy trì hai bảng ảo tạm thời trong suốt quá trình thực thi Trigger:
1. **Bảng `INSERTED`:** Chứa bản sao của các dòng mới được thêm vào (thao tác `INSERT`) hoặc các dòng sau khi đã được cập nhật giá trị mới (thao tác `UPDATE`).
2. **Bảng `DELETED`:** Chứa bản sao của các dòng vừa bị xóa bỏ (thao tác `DELETE`) hoặc các dòng mang giá trị cũ trước khi bị cập nhật (thao tác `UPDATE`).

<!-- PAGE 27 -->

### 5.2. Cú pháp và kỹ thuật cài đặt Trigger kiểm tra RBTV
```sql
CREATE TRIGGER trg_KiemTraRBTV
ON TenBang
FOR INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Kiểm tra điều kiện vi phạm
    IF EXISTS (
        SELECT 1 
        FROM INSERTED i
        WHERE [DieuKienViPham]
    )
    BEGIN
        RAISERROR (N'Lỗi vi phạm ràng buộc toàn vẹn!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END
END;
```

<!-- PAGE 29 -->

### 5.3. Ví dụ mẫu: Ràng buộc Ngày sinh và Ngày vào làm
Xét quan hệ `NHANVIEN(MaNV, HoTen, NgaySinh, NgayVaoLam)`. Ràng buộc: *Nhân viên khi vào làm phải từ đủ 18 tuổi trở lên (`DATEDIFF(year, NgaySinh, NgayVaoLam) >= 18`)*.

```sql
CREATE TRIGGER trg_NhanVien_DoTuoi
ON NHANVIEN
FOR INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1 
        FROM INSERTED 
        WHERE DATEDIFF(year, NgaySinh, NgayVaoLam) < 18
    )
    BEGIN
        RAISERROR (N'Lỗi: Nhân viên phải đủ từ 18 tuổi trở lên khi vào làm việc!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END
END;
```

<!-- PAGE 31 -->

---

## 6. BÀI TẬP CÓ HƯỚNG DẪN VÀ LỜI GIẢI

### Bài tập 1:
Cho CSDL Quản lý bán hàng gồm:
- `KHACHHANG(MaKH, TenKH, DiaChi, LoaiKH)`
- `DONHANG(SoDH, NgayDat, MaKH, TongTien)`

**Ràng buộc:** Chỉ khách hàng thuộc diện VIP (`LoaiKH = 'VIP'`) mới được phép đặt đơn hàng có `TongTien > 50,000,000 VNĐ`.

#### Lời giải chi tiết:
1. **Bối cảnh:** `KHACHHANG`, `DONHANG`.
2. **Biểu thức logic:**
   $$\forall d \in DONHANG, \forall k \in KHACHHANG ((d.MaKH = k.MaKH \land d.TongTien > 50000000) \implies k.LoaiKH = \text{'VIP'})$$
3. **Bảng tầm ảnh hưởng:**

| Quan hệ | Thêm (Insert) | Xóa (Delete) | Sửa (Update) |
| :--- | :---: | :---: | :---: |
| `DONHANG` | $+$ | $-$ | $* (MaKH, TongTien)$ |
| `KHACHHANG` | $-$ | $-$ | $* (LoaiKH)$ |

4. **Cài đặt Trigger trên bảng `DONHANG`:**
```sql
CREATE TRIGGER trg_KiemTra_DonHang_VIP
ON DONHANG
FOR INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1 
        FROM INSERTED d
        JOIN KHACHHANG k ON d.MaKH = k.MaKH
        WHERE d.TongTien > 50000000 AND k.LoaiKH <> 'VIP'
    )
    BEGIN
        RAISERROR (N'Chỉ khách hàng VIP mới được phép đặt đơn hàng trên 50 triệu!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END
END;
```

<!-- PAGE 40 -->
