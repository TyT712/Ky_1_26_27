# Tóm tắt Học thuật: Phụ thuộc Hàm, Bao đóng & Thuật toán Tìm Khóa (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Phụ thuộc hàm (FD):** $X \to Y \iff (\forall t_1, t_2 \in r)(t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y])$.
- **Hệ tiên đề Armstrong:**
  1. *Phản xạ:* $Y \subseteq X \implies X \to Y$.
  2. *Tăng trưởng:* $X \to Y \implies XZ \to YZ$.
  3. *Bắc cầu:* $X \to Y \land Y \to Z \implies X \to Z$.
  *Quy tắc dẫn xuất:* Hợp ($X \to Y, X \to Z \implies X \to YZ$), Phân rã ($X \to YZ \implies X \to Y, X \to Z$), Tựa bắc cầu.

## 2. Bao Đóng Của Tập Thuộc Tính ($X^+$) & Bài Toán Thành Viên
- **Bao đóng $X^+$:** Tập các thuộc tính $A$ sao cho $X \to A \in F^+$.
- **Bài toán thành viên:** Kiểm tra $X \to Y \in F^+ \iff Y \subseteq X^+$.

## 3. Thuật Toán Tìm Tất Cả Các Khóa (Lucchenssi - Osborn)
Phân loại tập thuộc tính toàn thể $U$ thành 4 nhóm:
- **Nhóm $L$ (Chỉ xuất hiện vế trái):** Bắt buộc có mặt trong mọi khóa.
- **Nhóm $R$ (Chỉ xuất hiện vế phải):** Không bao giờ xuất hiện trong bất kỳ khóa tối thiểu nào.
- **Nhóm $D$ (Độc lập, không xuất hiện trong $F$):** Bắt buộc có mặt trong mọi khóa.
- **Nhóm $M$ (Trung gian, xuất hiện cả hai vế):** Cần kết hợp thử nghiệm với tập nguồn $X_0 = L \cup D$.

**Quy trình tìm khóa:**
1. Đặt $X_0 = L \cup D$. Nếu $X_0^+ = U \implies X_0$ là khóa duy nhất.
2. Nếu $X_0^+ \ne U$, lần lượt thử kết hợp $X_0$ với các tập con $Y \subseteq M$ theo kích thước tăng dần. Nếu $(X_0 \cup Y)^+ = U$ và không chứa khóa đã tìm thấy trước đó, thì $(X_0 \cup Y)$ là khóa.

## 4. Phủ Tối Thiểu (Minimal Cover - $F_{min}$)
Tập $F_{min}$ tương đương $F$ đạt 3 điều kiện:
1. Vế phải đơn thuộc tính ($|Y| = 1$).
2. Không có thuộc tính dư thừa vế trái (loại bỏ $B \in X$ nếu $A \in (X \setminus \{B\})_F^+$).
3. Không có phụ thuộc hàm dư thừa (loại bỏ $f: X \to A$ nếu $A \in X_{F \setminus \{f\}}^+$).
