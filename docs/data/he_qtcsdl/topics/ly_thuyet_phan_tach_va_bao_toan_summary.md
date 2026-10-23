# Tóm tắt Học thuật: Lý thuyết Phân tách Lược đồ Quan hệ (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Mục đích phân tách:** Chia nhỏ lược đồ quan hệ để loại bỏ dư thừa và dị thường cập nhật.
- **Hai tiêu chuẩn vàng của phép phân tách $\rho = \{R_1, R_2, \dots, R_k\}$:**
  1. *Bảo toàn thông tin (Lossless Join):* $r = \pi_{R_1}(r) \bowtie \pi_{R_2}(r) \bowtie \dots \bowtie \pi_{R_k}(r)$ (không sinh ra bộ giả).
  2. *Bảo toàn phụ thuộc hàm (Dependency Preservation):* $(\pi_{R_1}(F) \cup \dots \cup \pi_{R_k}(F))^+ = F^+$ (kiểm tra toàn vẹn nội bộ trên từng bảng con).

## 2. Kiểm Tra Bảo Toàn Thông Tin (Lossless Join)
- **Trường hợp 2 quan hệ con $\rho = \{R_1, R_2\}$ (Định lý Decobel):**
  $$(R_1 \cap R_2) \to (R_1 \setminus R_2) \in F^+ \quad \text{HOẶC} \quad (R_1 \cap R_2) \to (R_2 \setminus R_1) \in F^+$$
  *Điều kiện tương đương:* Phần giao $R_1 \cap R_2$ phải là siêu khóa của ít nhất một trong hai lược đồ con.
- **Trường hợp tổng quát $k \ge 2$ (Thuật toán bảng Chase):**
  * Lập bảng $k$ hàng và $n$ cột, điền $a_j$ nếu $A_j \in R_i$, ngược lại điền $b_{ij}$.
  * Dùng các phụ thuộc hàm $X \to Y \in F$ để đồng nhất các hàng giống nhau trên $X$ sang ký hiệu $a$ trên cột $Y$.
  * Phép phân tách bảo toàn thông tin khi và chỉ khi xuất hiện **ít nhất một dòng chứa toàn bộ ký hiệu $a$**.

## 3. Kiểm Tra Bảo Toàn Phụ Thuộc Hàm
- Hình chiếu phụ thuộc hàm: $\pi_{R_i}(F) = \{X \to Y \in F^+ \mid XY \subseteq R_i\}$.
- Một phụ thuộc hàm $X \to Y$ được bảo toàn nếu việc tính bao đóng lặp qua các lược đồ con $Z := Z \cup ((Z \cap R_i)^+ \cap R_i)$ cho kết quả $Y \subseteq Z$.
