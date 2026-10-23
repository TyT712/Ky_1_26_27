# CHƯƠNG 5. PHỤ THUỘC ĐA TRỊ VÀ DẠNG CHUẨN 4 (4NF)

<!-- PAGE 125 -->

## 1. MỞ ĐẦU VÀ ĐỊNH NGHĨA PHỤ THUỘC ĐA TRỊ (MVD)

### 1.1. Bối cảnh và Hạn chế của BCNF
Mặc dù Dạng chuẩn Boyce-Codd (BCNF) đã loại bỏ toàn bộ sự dư thừa dữ liệu phát sinh từ các Phụ thuộc hàm (FD), nhưng trong thực tế vẫn tồn tại những dạng dư thừa dữ liệu nghiêm trọng xuất phát từ sự độc lập giữa hai hay nhiều mối liên kết 1-nhiều trong cùng một lược đồ quan hệ.

**Ví dụ điển hình:**
Xét quan hệ `KHOAHOC_GV_GIAOTRINH(MonHoc, GiangVien, GiaoTrinh)`:
- Một môn học có thể do nhiều giảng viên phụ trách giảng dạy độc lập.
- Một môn học có thể sử dụng nhiều cuốn giáo trình tham khảo độc lập.
- Giữa giảng viên và giáo trình hoàn toàn không có mối liên hệ ngữ nghĩa ràng buộc nào, nhưng khi biểu diễn trong một bảng, ta phải nhân tích Descartes: nếu môn CSDL có 3 giảng viên và 4 giáo trình, bảng phải lưu trữ $3 \times 4 = 12$ dòng dữ liệu lặp đi lặp lại.

Khóa của quan hệ trên là toàn bộ bộ ba thuộc tính `(MonHoc, GiangVien, GiaoTrinh)`, do đó quan hệ này đã đạt BCNF theo lý thuyết phụ thuộc hàm, nhưng vẫn chứa đựng sự dư thừa dữ liệu rất lớn. Để giải quyết triệt để loại dư thừa này, Ronald Fagin (1977) đã đề xuất khái niệm **Phụ thuộc đa trị (Multivalued Dependency - MVD)** và **Dạng chuẩn 4 (4NF)**.

<!-- PAGE 126 -->

### 1.2. Định nghĩa Phụ thuộc đa trị (Multivalued Dependency)
Cho lược đồ quan hệ $R(U)$ và các tập thuộc tính $X, Y \subseteq U$. Đặt $Z = U \setminus (X \cup Y)$.

> **Định nghĩa:** Ta nói rằng **$X$ xác định đa trị $Y$** (hay **$Y$ phụ thuộc đa trị vào $X$**), ký hiệu là:
> $$X \twoheadrightarrow Y$$
> nếu với mọi quan hệ $r$ trên $R$ và với bất kỳ hai bộ dữ liệu $t_1, t_2 \in r$ thỏa mãn $t_1[X] = t_2[X]$, luôn luôn tồn tại hai bộ dữ liệu $t_3, t_4 \in r$ sao cho:
> 1. $t_3[X] = t_1[X], \quad t_3[Y] = t_1[Y], \quad t_3[Z] = t_2[Z]$
> 2. $t_4[X] = t_1[X], \quad t_4[Y] = t_2[Y], \quad t_4[Z] = t_1[Z]$

*Ý nghĩa trực quan:* Giá trị của $Y$ liên kết với một giá trị của $X$ hoàn toàn độc lập với các giá trị của các thuộc tính còn lại $Z$.

<!-- PAGE 127 -->

### 1.3. Phụ thuộc đa trị tầm thường (Trivial MVD)
Một phụ thuộc đa trị $X \twoheadrightarrow Y$ trên lược đồ $R(U)$ được gọi là **tầm thường** nếu:
- $Y \subseteq X$, hoặc
- $X \cup Y = U$ (tức $Z = \emptyset$).

Ngược lại, nếu $Y \not\subseteq X$ và $X \cup Y \subset U$, thì $X \twoheadrightarrow Y$ được gọi là **phụ thuộc đa trị không tầm thường**.

---

## 2. HỆ TIÊN ĐỀ CHO PHỤ THUỘC ĐA TRỊ

Hệ tiên đề Armstrong mở rộng cho phụ thuộc đa trị bao gồm các luật cơ bản sau:

1. **Luật bù (Complementation Rule):**
   $$\text{Nếu } X \twoheadrightarrow Y \implies X \twoheadrightarrow U \setminus (X \cup Y)$$
   *(Phụ thuộc đa trị luôn đi theo cặp đối xứng bù trừ nhau)*
2. **Luật tăng trưởng (Augmentation Rule):**
   $$\text{Nếu } X \twoheadrightarrow Y \text{ và } W \subseteq V \implies X V \twoheadrightarrow Y W$$
3. **Luật bắc cầu (Transitivity Rule):**
   $$\text{Nếu } X \twoheadrightarrow Y \text{ và } Y \twoheadrightarrow Z \implies X \twoheadrightarrow Z \setminus Y$$
4. **Luật sao chép (Replication / FD to MVD):**
   $$\text{Nếu } X \to Y \implies X \twoheadrightarrow Y$$
   *(Mọi phụ thuộc hàm đều là một phụ thuộc đa trị đặc biệt)*
5. **Luật kết hợp (Coalescence Rule):**
   $$\text{Nếu } X \twoheadrightarrow Y \text{ và tồn tại } W \text{ sao cho } W \cap Y = \emptyset, \ Z \subseteq Y, \text{ và } W \to Z \implies X \to Z$$

<!-- PAGE 128 -->

---

## 3. CƠ SỞ PHỤ THUỘC VÀ ĐỊNH LÝ FAGIN

### 3.1. Cơ sở phụ thuộc (Dependency Basis)
Cho lược đồ quan hệ $R(U)$ và tập phụ thuộc đa trị và phụ thuộc hàm $D$.
Với một tập thuộc tính $X \subset U$, **Cơ sở phụ thuộc của $X$**, ký hiệu là $DepB(X)$, là một phân hoạch của tập thuộc tính $U \setminus X$ thành các tập con rời nhau $\{Y_1, Y_2, \dots, Y_m\}$ sao cho:
- Với mỗi $Y_i$, ta có $X \twoheadrightarrow Y_i \in D^+$.
- Bất kỳ phụ thuộc đa trị $X \twoheadrightarrow W$ nào cũng có $W$ là hợp của một số tập trong $\{Y_1, \dots, Y_m\}$.

<!-- PAGE 130 -->

### 3.2. Định lý Fagin (Kết nối không mất thông tin với MVD)
Định lý Fagin mở rộng Định lý Decobel cho trường hợp phụ thuộc đa trị:

> **Định lý Fagin:** Phép phân tách lược đồ quan hệ $R(U)$ thành hai lược đồ con $\rho = \{R_1, R_2\}$ (với $R_1 \cup R_2 = U$) là **bảo toàn thông tin (Lossless Join)** khi và chỉ khi:
> $$(R_1 \cap R_2) \twoheadrightarrow (R_1 \setminus R_2) \quad \text{HOẶC} \quad (R_1 \cap R_2) \twoheadrightarrow (R_2 \setminus R_1)$$

<!-- PAGE 131 -->

---

## 4. DẠNG CHUẨN 4 (4NF - FOURTH NORMAL FORM)

### 4.1. Định nghĩa Dạng chuẩn 4
> **Định nghĩa:** Lược đồ quan hệ $R(U, D)$ được gọi là ở **Dạng chuẩn 4 (4NF)** nếu với mọi phụ thuộc đa trị không tầm thường $X \twoheadrightarrow Y \in D^+$ (nghĩa là $Y \not\subseteq X$ và $X \cup Y \subset U$):
> $$X \text{ bắt buộc phải là một siêu khóa của } R$$

#### Quan hệ thứ bậc:
$$\text{4NF} \subset \text{BCNF} \subset \text{3NF} \subset \text{2NF} \subset \text{1NF}$$

Nếu một lược đồ quan hệ đạt 4NF thì nó **chắc chắn đạt BCNF** (bởi vì nếu có $X \to Y$ vi phạm BCNF thì theo luật sao chép, $X \twoheadrightarrow Y$ cũng sẽ vi phạm 4NF).

<!-- PAGE 133 -->

### 4.2. Thuật toán phân tách về Dạng chuẩn 4 (4NF)
Thuật toán phân tách đệ quy bảo đảm **kết nối không mất thông tin**:

```text
Thuật toán Chuan_Hoa_4NF(R, D):
1.  rho := { R };
2.  Khi vẫn tồn tại một lược đồ R_i trong rho CHƯA đạt 4NF:
3.      Tìm một phụ thuộc đa trị không tầm thường X ->> Y vi phạm 4NF trên R_i
        (tức Y không là con của X, X hợp Y c R_i, và X không là siêu khóa của R_i);
4.      Phân tách R_i thành hai lược đồ con:
            R_{i1} := X hợp Y;
            R_{i2} := R_i \ (Y \ X);
5.      Thay thế R_i trong rho bằng { R_{i1}, R_{i2} };
6.  Trả về rho;
```

---

## 5. BÀI TẬP CÓ HƯỚNG DẪN VÀ LỜI GIẢI

### Bài tập 1:
Cho lược đồ quan hệ $R(MonHoc, GiangVien, GiaoTrinh)$ biểu diễn thông tin môn học, giảng viên phụ trách và giáo trình tham khảo.
Biết rằng mỗi môn học có thể do nhiều giảng viên dạy độc lập, và có thể tham khảo nhiều giáo trình độc lập:
$$D = \{MonHoc \twoheadrightarrow GiangVien, \ MonHoc \twoheadrightarrow GiaoTrinh\}$$

1. Xác định khóa của $R$.
2. Lược đồ $R$ có đạt BCNF không? Có đạt 4NF không?
3. Chuẩn hóa $R$ về Dạng chuẩn 4 (4NF).

#### Lời giải chi tiết:
1. **Tìm khóa:**
   - Vì không có phụ thuộc hàm không tầm thường nào giữa các thuộc tính riêng lẻ, khóa duy nhất của $R$ là toàn thể bộ ba thuộc tính:
     $$K = \{MonHoc, GiangVien, GiaoTrinh\}$$

2. **Kiểm tra dạng chuẩn:**
   - **BCNF:** Vì tập phụ thuộc hàm $F = \emptyset$ (chỉ có các phụ thuộc hàm tầm thường), nên $R$ thỏa mãn định nghĩa BCNF một cách tầm thường.
   - **4NF:** Xét phụ thuộc đa trị $MonHoc \twoheadrightarrow GiangVien$:
     - Đây là phụ thuộc đa trị không tầm thường (vì $GiangVien \not\subseteq MonHoc$ và $\{MonHoc, GiangVien\} \ne U$).
     - Vế trái $MonHoc$ **không phải là siêu khóa** của $R$.
     - Do đó, $R$ **vi phạm 4NF**.

3. **Chuẩn hóa về 4NF:**
   - Áp dụng thuật toán phân tách theo phụ thuộc đa trị vi phạm $MonHoc \twoheadrightarrow GiangVien$:
     - $R_1 = \{MonHoc, GiangVien\}$
     - $R_2 = \{MonHoc, GiaoTrinh\}$
   - Kiểm tra hai lược đồ con:
     - Trong $R_1$: Phụ thuộc đa trị $MonHoc \twoheadrightarrow GiangVien$ trở thành tầm thường (vì $R_1 = \{MonHoc, GiangVien\}$). Do đó $R_1$ đạt 4NF.
     - Trong $R_2$: Phụ thuộc đa trị $MonHoc \twoheadrightarrow GiaoTrinh$ trở thành tầm thường. Do đó $R_2$ đạt 4NF.
   - Giao của 2 lược đồ: $R_1 \cap R_2 = \{MonHoc\}$. Theo Định lý Fagin, vì $MonHoc \twoheadrightarrow GiangVien$, nên phép tách này **hoàn toàn bảo toàn thông tin**.
   - **Kết quả phân tách:** $\rho = \{R_1(MonHoc, GiangVien), R_2(MonHoc, GiaoTrinh)\}$.

<!-- PAGE 138 -->
