# CHƯƠNG 2 (QUYỂN 2): PHỤ THUỘC HÀM, BAO ĐÓNG & THUẬT TOÁN TÌM KHÓA

### 1. Sơ Đồ Thuật Toán Phân Loại Thuộc Tính Tìm Tất Cả Các Khóa (Lucchenssi - Osborn)
```mermaid
graph TD
    U["Tập thuộc tính toàn thể U"] --> Classify["Phân loại theo vị trí xuất hiện trong tập F"]
    
    Classify --> L["Nhóm L (Left only)<br>Chỉ ở vế trái"]
    Classify --> R["Nhóm R (Right only)<br>Chỉ ở vế phải"]
    Classify --> D["Nhóm D (Disconnected)<br>Không xuất hiện ở cả 2 vế"]
    Classify --> M["Nhóm M (Middle)<br>Xuất hiện ở cả 2 vế"]
    
    L --> Core["Tập nguồn cốt lõi: X_0 = L ∪ D<br>(BẮT BUỘC có mặt trong mọi khóa)"]
    D --> Core
    R --> Drop["LOẠI KHỎI KHÓA<br>(Không bao giờ nằm trong khóa tối thiểu)"]
    
    Core --> Check{"(X_0)+ == U ?"}
    Check -- "Đúng" --> OneKey["X_0 là KHÓA DUY NHẤT của lược đồ"]
    Check -- "Sai" --> Comb["Tổ hợp X_0 với từng tập con Y ⊆ M<br>(Kích thước tăng dần từ 1, 2... |M|)"]
    Comb --> MultiKeys["Xác định toàn bộ các khóa tối thiểu"]
```

### 2. Các Khái Niệm & Định Nghĩa Toán Học Nền Tảng
- **Phụ thuộc hàm (Functional Dependency):**
  Cho lược đồ quan hệ $R(U)$ và $X, Y \subseteq U$. Ta nói $X \to Y$ nếu với mọi cặp bộ $t_1, t_2 \in r$:
  $$t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$$
- **Hệ tiên đề Armstrong:**
  1. *Tiên đề Phản xạ:* Nếu $Y \subseteq X \subseteq U \implies X \to Y$.
  2. *Tiên đề Tăng trưởng:* Nếu $X \to Y$ và $Z \subseteq U \implies XZ \to YZ$.
  3. *Tiên đề Bắc cầu:* Nếu $X \to Y$ và $Y \to Z \implies X \to Z$.
- **Các quy tắc suy dẫn thứ cấp:**
  - Quy tắc Hợp: $X \to Y \land X \to Z \implies X \to YZ$.
  - Quy tắc Phân rã: $X \to YZ \implies X \to Y \land X \to Z$.
  - Quy tắc Tựa bắc cầu: $X \to Y \land WY \to Z \implies WX \to Z$.
- **Bao đóng của tập thuộc tính ($X^+$):** Tập tất cả các thuộc tính $A \in U$ sao cho $X \to A \in F^+$.
- **Bài toán thành viên:** Kiểm tra $X \to Y \in F^+ \iff Y \subseteq X^+$.
- **Định nghĩa Khóa (Candidate Key):** $K \subseteq U$ là khóa của $R(U, F)$ nếu:
  1. $K^+ = U$ ($K$ là siêu khóa).
  2. $\forall K' \subset K \implies K'^+ \ne U$ (Tính tối thiểu, không rút gọn được nữa).

### 3. Thuật Toán 3 Bước Tìm Phủ Tối Thiểu (Minimal Cover - $F_{min}$)
1. **Bước 1 (Đơn thuộc tính hóa vế phải):** Tách các phụ thuộc hàm có vế phải nhiều thuộc tính thành các phụ thuộc hàm đơn ($X \to A_1 A_2 \implies X \to A_1, X \to A_2$).
2. **Bước 2 (Loại bỏ thuộc tính dư thừa vế trái):** Với mỗi $X \to A \in F$ và mỗi $B \in X$, đặt $Z = X \setminus \{B\}$. Nếu $A \in Z_F^+ \implies$ loại bỏ $B$ khỏi vế trái ($Z \to A$).
3. **Bước 3 (Loại bỏ phụ thuộc hàm dư thừa):** Với mỗi $f: X \to A \in F$, đặt $G = F \setminus \{f\}$. Nếu $A \in X_G^+ \implies$ loại bỏ hoàn toàn $f$ khỏi $F$.

---

## Tinh Hoa Kiến Thức & Tóm Tắt Chuyên Sâu (Key Takeaways)
> **Chuyên đề mở rộng:** Chuẩn hóa Dữ liệu (1NF, 2NF, 3NF, BCNF)

### 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Chuẩn hóa (Normalization):** Quá trình tái cấu trúc lược đồ để triệt tiêu dị thường thêm, xóa, sửa và loại bỏ dư thừa dữ liệu.
- **Thuộc tính nguyên tố vs không nguyên tố:** Thuộc tính nguyên tố nằm trong ít nhất 1 khóa của quan hệ; thuộc tính không nguyên tố không nằm trong bất kỳ khóa nào.

### 2. Tiêu Chuẩn Các Dạng Chuẩn
- **1NF (Dạng chuẩn 1):** Mọi thuộc tính đều mang giá trị nguyên tử (Atomic), không có thuộc tính đa trị hay quan hệ lồng ghép.
- **2NF (Dạng chuẩn 2):** Đạt 1NF và mọi thuộc tính không nguyên tố phải **phụ thuộc hàm đầy đủ** vào khóa chính (không phụ thuộc vào một phần của khóa chính ghép).
- **3NF (Dạng chuẩn 3):** Đạt 2NF và không có thuộc tính không nguyên tố nào **phụ thuộc bắc cầu** vào khóa chính.
  *Điều kiện tương đương:* Với mọi $X \to A \in F^+$ ($A \notin X$): hoặc $X$ là siêu khóa, hoặc $A$ là thuộc tính nguyên tố.
- **BCNF (Dạng chuẩn Boyce-Codd):** Với mọi $X \to A \in F^+$ ($A \notin X$), $X$ **bắt buộc phải là siêu khóa**.

$$\text{BCNF} \subset \text{3NF} \subset \text{2NF} \subset \text{1NF}$$

### 3. Thuật Toán Chuẩn Hóa
1. **Thuật toán chuẩn hóa về 3NF (Thuật toán tổng hợp Bernstein):**
   - Bước 1: Tìm phủ tối thiểu $F_{min}$.
   - Bước 2: Gom nhóm các PTH có cùng vế trái $X \to Y$. Tạo lược đồ con $R_i = X \cup Y$.
   - Bước 3: Nếu chưa có $R_i$ nào chứa khóa của quan hệ ban đầu, thêm một lược đồ con chứa khóa.
   - Bước 4: Loại bỏ các $R_i$ là tập con thực sự của $R_j$.
   - *Tính chất:* Luôn bảo đảm đồng thời **Bảo toàn thông tin** và **Bảo toàn phụ thuộc hàm**.
2. **Thuật toán chuẩn hóa về BCNF:**
   - Phân tách đệ quy theo các PTH $X \to Y$ vi phạm BCNF: $R_1 = X \cup Y$ và $R_2 = R \setminus (Y \setminus X)$.
   - *Tính chất:* Luôn **Bảo toàn thông tin**, nhưng **không bảo đảm bảo toàn phụ thuộc hàm**.
