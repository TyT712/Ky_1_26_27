# CHƯƠNG 3. LÝ THUYẾT PHÂN TÁCH LƯỢC ĐỒ QUAN HỆ

<!-- PAGE 78 -->

## 1. GIỚI THIỆU VÀ ĐỊNH NGHĨA PHÉP PHÂN TÁCH

### 1.1. Mục đích của phép phân tách
Trong thiết kế cơ sở dữ liệu quan hệ, việc gom quá nhiều thuộc tính vào một lược đồ quan hệ lớn thường dẫn đến các hiện tượng dị thường dữ liệu (dư thừa thông tin, bất thường khi chèn, xóa và cập nhật). Để giải quyết vấn đề này, người ta áp dụng kỹ thuật **phân tách (Decomposition)** để chia một lược đồ quan hệ lớn thành nhiều lược đồ quan hệ nhỏ hơn, chuẩn hóa hơn.

Tuy nhiên, một phép phân tách chỉ được xem là tốt và có thể áp dụng trong thực tế nếu thỏa mãn hai tính chất cơ bản:
1. **Bảo toàn thông tin (Lossless Join):** Khi thực hiện phép kết tự nhiên ($\bowtie$) các quan hệ con lại với nhau, ta phải thu hồi lại chính xác quan hệ ban đầu, không làm sinh ra các bộ dữ liệu giả (Spurious Tuples) hay mất mát dữ liệu.
2. **Bảo toàn phụ thuộc hàm (Dependency Preservation):** Tất cả các ràng buộc phụ thuộc hàm trên quan hệ ban đầu đều có thể kiểm tra trực tiếp trên các quan hệ con mà không cần phải thực hiện phép kết nối các quan hệ con đó.

<!-- PAGE 79 -->

### 1.2. Định nghĩa Phép phân tách
Cho lược đồ quan hệ $R(U, F)$ với tập thuộc tính $U$.
Một **phép phân tách** của $R$ là một họ các tập con của $U$:
$$\rho = \{R_1, R_2, \dots, R_k\}$$
sao cho:
$$\bigcup_{i=1}^k R_i = R_1 \cup R_2 \cup \dots \cup R_k = U$$

---

## 2. PHÉP PHÂN TÁCH BẢO TOÀN THÔNG TIN (LOSSLESS-JOIN DECOMPOSITION)

### 2.1. Định nghĩa hình thức
Phép phân tách $\rho = \{R_1, R_2, \dots, R_k\}$ của lược đồ quan hệ $R(U, F)$ được gọi là **bảo toàn thông tin** (hay **kết nối không mất mát thông tin**) đối với tập phụ thuộc hàm $F$ nếu với mọi thể hiện quan hệ $r$ hợp lệ trên $R$ (nghĩa là $r$ thỏa $F$):
$$r = \pi_{R_1}(r) \bowtie \pi_{R_2}(r) \bowtie \dots \bowtie \pi_{R_k}(r)$$

Tổng quát luôn có $r \subseteq \pi_{R_1}(r) \bowtie \dots \bowtie \pi_{R_k}(r)$. Do đó, tính bảo toàn thông tin đồng nghĩa với việc không sinh ra bộ giả mạo khi kết nối.

<!-- PAGE 80 -->

### 2.2. Trường hợp phân tách thành 2 lược đồ con: Định lý Decobel
Khi phân tách $R$ thành hai lược đồ con $\rho = \{R_1, R_2\}$ (với $R_1 \cup R_2 = U$), Định lý Decobel đưa ra điều kiện cần và đủ rất nhanh gọn:

> **Định lý Decobel:** Phép phân tách $\rho = \{R_1, R_2\}$ là bảo toàn thông tin đối với tập phụ thuộc hàm $F$ khi và chỉ khi:
> $$(R_1 \cap R_2) \to (R_1 \setminus R_2) \in F^+ \quad \text{HOẶC} \quad (R_1 \cap R_2) \to (R_2 \setminus R_1) \in F^+$$

*Ý nghĩa trực giác:* Giao của hai lược đồ con ($R_1 \cap R_2$) phải tạo thành một **siêu khóa** của ít nhất một trong hai lược đồ con đó.

### 2.3. Thuật toán bảng kiểm tra bảo toàn thông tin tổng quát (Chase Algorithm)
Đối với phép phân tách tổng quát thành $k \ge 2$ lược đồ con $\rho = \{R_1, R_2, \dots, R_k\}$, ta sử dụng thuật toán Bảng kiểm định (Chase Matrix):

- **Khởi tạo:**
  Lập bảng gồm $k$ dòng (tương ứng với các lược đồ con $R_1, R_2, \dots, R_k$) và $n$ cột (tương ứng với các thuộc tính $A_1, A_2, \dots, A_n \in U$).
  Ô $(i, j)$ được điền giá trị:
  - $a_j$: Nếu thuộc tính $A_j \in R_i$.
  - $b_{ij}$: Nếu thuộc tính $A_j \notin R_i$.

- **Lặp biến đổi bảng:**
  Lặp duyệt qua từng phụ thuộc hàm $X \to Y \in F$:
  - Tìm tất cả các dòng có các giá trị giống hệt nhau trên các cột thuộc tập $X$.
  - Đồng nhất hóa các giá trị trên các cột thuộc tập $Y$ của các dòng đó theo quy tắc ưu tiên:
    - Nếu trong số các giá trị có ký hiệu $a_j$, hãy chuyển tất cả các giá trị khác trên cột $j$ của các dòng đó thành $a_j$.
    - Nếu chưa có $a_j$, hãy chọn một ký hiệu $b_{kj}$ làm đại diện và thay thế tất cả các giá trị $b_{ij}$ kia bằng ký hiệu đó.

- **Điều kiện dừng và kết luận:**
  - Nếu trong bảng xuất hiện **ít nhất một dòng chứa toàn ký hiệu $a$** ($a_1, a_2, \dots, a_n$), thuật toán dừng lại và kết luận: **Phép phân tách $\rho$ là bảo toàn thông tin.**
  - Nếu bảng không còn thay đổi được nữa mà không có dòng nào chứa toàn ký hiệu $a$, kết luận: **Phép phân tách $\rho$ làm mất mát thông tin.**

<!-- PAGE 81 -->

---

## 3. PHÉP PHÂN TÁCH BẢO TOÀN TẬP PHỤ THUỘC HÀM (DEPENDENCY PRESERVATION)

### 3.1. Hình chiếu của tập phụ thuộc hàm
Cho lược đồ quan hệ $R(U, F)$ và tập con các thuộc tính $R_i \subseteq U$.
**Hình chiếu của $F$ lên $R_i$**, ký hiệu là $\pi_{R_i}(F)$ (hoặc $F_{R_i}$), là tập hợp tất cả các phụ thuộc hàm thuộc $F^+$ mà cả vế trái lẫn vế phải đều chỉ chứa các thuộc tính thuộc $R_i$:
$$\pi_{R_i}(F) = \{X \to Y \in F^+ \mid XY \subseteq R_i\}$$

### 3.2. Định nghĩa bảo toàn phụ thuộc hàm
Phép phân tách $\rho = \{R_1, R_2, \dots, R_k\}$ được gọi là **bảo toàn tập phụ thuộc hàm** đối với $F$ nếu:
$$\left( \bigcup_{i=1}^k \pi_{R_i}(F) \right)^+ = F^+$$

### 3.3. Thuật toán kiểm tra bảo toàn phụ thuộc hàm
Để kiểm tra xem một phụ thuộc hàm $X \to Y \in F$ có được bảo toàn qua phép phân tách $\rho = \{R_1, \dots, R_k\}$ hay không, ta thực hiện tính bao đóng $X$ qua họ $\rho$:

```text
Thuật toán Kiem_Tra_Bao_Toan_FD(X -> Y, rho, F):
1.  Z := X;
2.  Lặp lại:
3.      Old_Z := Z;
4.      Với mỗi R_i trong rho:
5.          Z := Z hợp ((Z giao R_i)+ giao R_i);
6.  Cho đến khi (Z == Old_Z);
7.  Nếu Y là tập con của Z:
8.      Trả về TRUE (Phụ thuộc hàm được bảo toàn);
9.  Ngược lại:
10.     Trả về FALSE (Không được bảo toàn);
```

Nếu mọi phụ thuộc hàm $f \in F$ đều được bảo toàn, thì phép phân tách $\rho$ bảo toàn phụ thuộc hàm.

<!-- PAGE 83 -->

---

## 4. BÀI TẬP CÓ HƯỚNG DẪN VÀ LỜI GIẢI

### Bài tập 1:
Cho lược đồ quan hệ $R(A, B, C, D, E)$ và tập phụ thuộc hàm:
$$F = \{A \to B, BC \to D, E \to C\}$$
Xét phép phân tách $\rho = \{R_1(A, B, E), R_2(B, C, D, E)\}$.
Hỏi phép phân tách $\rho$ có bảo toàn thông tin hay không?

#### Lời giải chi tiết (Áp dụng Định lý Decobel):
- Ta có $\rho$ gồm 2 quan hệ con $R_1$ và $R_2$:
  - $R_1 \cup R_2 = \{A, B, E\} \cup \{B, C, D, E\} = \{A, B, C, D, E\} = U$.
  - Giao hai lược đồ: $R_1 \cap R_2 = \{A, B, E\} \cap \{B, C, D, E\} = \{B, E\}$.
  - $R_1 \setminus R_2 = \{A, B, E\} \setminus \{B, C, D, E\} = \{A\}$.
  - $R_2 \setminus R_1 = \{B, C, D, E\} \setminus \{A, B, E\} = \{C, D\}$.
- Tính bao đóng của phần giao $(R_1 \cap R_2)^+ = (BE)^+$ đối với $F$:
  - $X^{(0)} = BE$.
  - Xét $E \to C$: Vì $E \subseteq BE \implies X^{(1)} = BCE$.
  - Xét $BC \to D$: Vì $BC \subseteq BCE \implies X^{(2)} = BCDE$.
  - Xét $A \to B$: Vế trái $A \not\subseteq BCDE$.
  - Vậy $(BE)^+ = BCDE$.
- Kiểm tra điều kiện:
  - $(R_1 \cap R_2) \to (R_2 \setminus R_1) \iff BE \to CD$.
  - Vì $CD \subseteq (BE)^+ = BCDE$, nên $BE \to CD \in F^+$.
- **Kết luận:** Theo Định lý Decobel, phép phân tách $\rho = \{R_1, R_2\}$ **hoàn toàn bảo toàn thông tin (Lossless Join)**.

<!-- PAGE 90 -->
