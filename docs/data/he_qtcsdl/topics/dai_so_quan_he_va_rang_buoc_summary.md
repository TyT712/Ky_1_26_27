# Tóm tắt Học thuật: Đại số Quan hệ & Ràng buộc Toàn vẹn (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Đại số quan hệ:** Ngôn ngữ hình thức toán học làm nền tảng cho việc tối ưu hóa truy vấn SQL.
- **Ràng buộc toàn vẹn cốt lõi:**
  1. *Ràng buộc thực thể (Entity Integrity):* Khóa chính không bao giờ được chứa giá trị `NULL`.
  2. *Ràng buộc tham chiếu (Referential Integrity):* Giá trị khóa ngoại phải xuất hiện trong tập khóa chính của bảng tham chiếu hoặc mang giá trị `NULL`.

## 2. Bảng Ký Hiệu Phép Toán Đại Số Quan Hệ

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

## 3. Mẹo Nhớ Giải Bài Tập Đại Số Quan Hệ
- Câu hỏi chứa từ **"Tìm ... có đặc điểm ..."** $\to$ Dùng $\sigma$ kết hợp $\pi$.
- Câu hỏi chứa từ **"Tìm ... thuộc cả hai danh sách"** $\to$ Dùng $\cap$ hoặc phép kết $\bowtie$.
- Câu hỏi chứa từ **"Tìm ... mà KHÔNG ..."** $\to$ Dùng phép trừ $-$.
- Câu hỏi chứa từ **"Tìm ... đã tham gia TẤT CẢ ..."** $\to$ Dùng phép chia $\div$.
