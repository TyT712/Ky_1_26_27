# CHƯƠNG 3: MÔ HÌNH DỮ LIỆU QUAN HỆ & ĐẠI SỐ QUAN HỆ

### 1. Bản Đồ Các Phép Toán Đại Số Quan Hệ (Relational Algebra)
```mermaid
graph TD
    RA["Đại Số Quan Hệ (Relational Algebra)"] --> SetOps["Phép Toán Tập Hợp Khả Hợp"]
    RA --> SpecOps["Phép Toán Quan Hệ Chuyên Biệt"]
    
    SetOps --> Union["Phép Hợp: R ∪ S"]
    SetOps --> Inter["Phép Giao: R ∩ S"]
    SetOps --> Diff["Phép Trừ: R - S"]
    SetOps --> Cartesian["Tích Descartes: R × S"]
    
    SpecOps --> Select["Phép Chọn: σ_C(R) (Lọc hàng)"]
    SpecOps --> Project["Phép Chiếu: π_L(R) (Lọc cột)"]
    SpecOps --> Join["Phép Kết: R ⋈_C S (Gộp hàng theo điều kiện)"]
    SpecOps --> Divide["Phép Chia: R ÷ S (Điều kiện 'với mọi')"]
```

### 2. Các Phép Toán Cốt Lõi & Ký Hiệu Hình Thức

| Phép toán | Ký hiệu | Ý nghĩa đại số | Điều kiện áp dụng |
| :--- | :---: | :--- | :--- |
| **Phép Chọn (Selection)** | $\sigma_C(R)$ | Lọc các bộ dữ liệu trong quan hệ $R$ thỏa mãn điều kiện logic $C$. | Điều kiện $C$ là biểu thức logic boolean trên các thuộc tính của $R$. |
| **Phép Chiếu (Projection)** | $\pi_L(R)$ | Trích xuất danh sách các thuộc tính $L$ từ $R$ và tự động loại bỏ các bộ trùng lặp. | $L$ là tập con các thuộc tính của $R$. |
| **Phép Hợp (Union)** | $R \cup S$ | Tập các bộ thuộc về $R$ hoặc thuộc về $S$ hoặc cả hai. | $R$ và $S$ phải **khả hợp** (cùng bậc và tương thích miền giá trị từng cặp thuộc tính). |
| **Phép Giao (Intersection)** | $R \cap S$ | Tập các bộ đồng thời xuất hiện ở cả $R$ và $S$. | $R$ và $S$ phải khả hợp. ($R \cap S = R - (R - S)$). |
| **Phép Trừ (Difference)** | $R - S$ | Tập các bộ thuộc về $R$ nhưng không thuộc về $S$. | $R$ và $S$ phải khả hợp. |
| **Tích Descartes (Cartesian)** | $R \times S$ | Ghép nối từng bộ của $R$ với mọi bộ của $S$. Bậc bằng $|R| + |S|$, số bộ bằng $|R| \times |S|$. | Không cần điều kiện khả hợp. |
| **Phép Kết Nối (Join)** | $R \bowtie_C S$ | Thực hiện tích Descartes $R \times S$ sau đó lọc theo điều kiện kết nối $C$: $\sigma_C(R \times S)$. | $C$ liên kết các thuộc tính tương thích giữa $R$ và $S$. |
| **Kết Tự Nhiên (Natural Join)** | $R \bowtie S$ | Kết bằng trên tất cả các thuộc tính trùng tên giữa $R$ và $S$, sau đó tự động khử một cột trùng. | Phải có ít nhất 1 thuộc tính trùng tên. |
| **Phép Chia (Division)** | $R \div S$ | Tìm các bộ trong $R$ liên kết được với **TẤT CẢ** các bộ trong $S$ (mệnh đề "với mọi"). | Thuộc tính của $S$ là tập con thực sự của $R$. |

---

## Tinh Hoa Kiến Thức & Tóm Tắt Chuyên Sâu (Key Takeaways)
> **Chuyên đề mở rộng:** Đại số Quan hệ & Ràng buộc Toàn vẹn

### 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Đại số quan hệ:** Ngôn ngữ hình thức toán học làm nền tảng cho việc tối ưu hóa truy vấn SQL.
- **Ràng buộc toàn vẹn cốt lõi:**
  1. *Ràng buộc thực thể (Entity Integrity):* Khóa chính không bao giờ được chứa giá trị `NULL`.
  2. *Ràng buộc tham chiếu (Referential Integrity):* Giá trị khóa ngoại phải xuất hiện trong tập khóa chính của bảng tham chiếu hoặc mang giá trị `NULL`.

### 2. Bảng Ký Hiệu Phép Toán Đại Số Quan Hệ

| Ký hiệu | Tên phép toán | Ý nghĩa & Cú pháp | Ví dụ |
| :--- | :--- | :--- | :--- |
| $\sigma$ | Phép chọn (Select) | Lọc các dòng thỏa mãn điều kiện $C$: $\sigma_C(R)$ | $\sigma_{Diem \ge 8.0}(KET\_QUA)$ |
| $\pi$ | Phép chiếu (Project) | Trích xuất danh sách cột $L$: $\pi_L(R)$ | $\pi_{MaSV, HoTen}(SINH\_VIEN)$ |
| $\bowtie$ | Phép kết tự nhiên (Natural Join) | Kết nối 2 bảng dựa trên các cột cùng tên: $R \bowtie S$ | $SINH\_VIEN \bowtie KHOA$ |
| $\bowtie_\theta$ | Phép kết điều kiện ($\theta$-Join) | Kết nối theo điều kiện $\theta$: $\sigma_\theta(R \times S)$ | $R \bowtie_{R.A < S.B} S$ |
| $\times$ | Tích Descartes | Ghép mọi dòng của $R$ với mọi dòng của $S$ | $R \times S$ |
| $\cup$ | Phép hợp (Union) | Tập hợp các dòng thuộc $R$ hoặc $S$ | $R \cup S$ |
| $\cap$ | Phép giao (Intersect) | Tập hợp các dòng cùng thuộc $R$ và $S$ | $R \cap S$ |
| $-$ | Phép trừ (Difference) | Tập hợp các dòng thuộc $R$ nhưng không thuộc $S$ | $R - S$ |
| $\div$ | Phép chia (Division) | Tìm đối tượng liên kết với **tất cả** đối tượng khác | $R \div S$ |

### 3. Mẹo Nhớ Giải Bài Tập Đại Số Quan Hệ
- Câu hỏi chứa từ **"Tìm ... có đặc điểm ..."** $\to$ Dùng $\sigma$ kết hợp $\pi$.
- Câu hỏi chứa từ **"Tìm ... thuộc cả hai danh sách"** $\to$ Dùng $\cap$ hoặc phép kết $\bowtie$.
- Câu hỏi chứa từ **"Tìm ... mà KHÔNG ..."** $\to$ Dùng phép trừ $-$.
- Câu hỏi chứa từ **"Tìm ... đã tham gia TẤT CẢ ..."** $\to$ Dùng phép chia $\div$.
