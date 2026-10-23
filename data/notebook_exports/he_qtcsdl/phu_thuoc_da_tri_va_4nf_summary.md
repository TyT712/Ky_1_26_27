# Tóm tắt Học thuật: Phụ thuộc Đa trị & Dạng chuẩn 4 (4NF) (Xuất từ NotebookLM)
**Môn học:** Hệ Quản trị Cơ sở dữ liệu (`he_qtcsdl`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Hạn chế của BCNF:** BCNF không loại bỏ được sự dư thừa dữ liệu phát sinh từ hai hay nhiều mối liên kết 1-nhiều độc lập trong cùng một bảng (dẫn đến tích Descartes các bộ).
- **Phụ thuộc đa trị (MVD):** $X \twoheadrightarrow Y$ biểu thị rằng tập giá trị $Y$ đi kèm với $X$ hoàn toàn độc lập với các thuộc tính còn lại $Z = U \setminus XY$.
  *MVD tầm thường:* $Y \subseteq X$ hoặc $X \cup Y = U$.
- **Mối quan hệ giữa FD và MVD:** Mọi phụ thuộc hàm đều là một phụ thuộc đa trị ($X \to Y \implies X \twoheadrightarrow Y$).

## 2. Các Tiên Đề Phụ Thuộc Đa Trị & Định Lý Fagin
- **Luật bù (Complementation):** $X \twoheadrightarrow Y \implies X \twoheadrightarrow U \setminus (XY)$. (MVD luôn tồn tại theo cặp bù).
- **Định lý Fagin:** Phép phân tách $R$ thành hai lược đồ con $\{R_1, R_2\}$ là bảo toàn thông tin $\iff$
  $$(R_1 \cap R_2) \twoheadrightarrow (R_1 \setminus R_2) \quad \text{HOẶC} \quad (R_1 \cap R_2) \twoheadrightarrow (R_2 \setminus R_1)$$

## 3. Dạng Chuẩn 4 (4NF - Fourth Normal Form)
- **Định nghĩa 4NF:** Lược đồ quan hệ $R(U, D)$ đạt 4NF nếu với mọi phụ thuộc đa trị không tầm thường $X \twoheadrightarrow Y \in D^+$, thì $X$ **bắt buộc phải là siêu khóa** của $R$.
- **Thứ bậc bao hàm:**
  $$\text{4NF} \subset \text{BCNF} \subset \text{3NF} \subset \text{2NF} \subset \text{1NF}$$
  *Nhận xét:* Nếu $R$ đạt 4NF thì $R$ chắc chắn đạt BCNF.
- **Thuật toán chuẩn hóa về 4NF:**
  Phân tách đệ quy không mất thông tin dựa trên MVD vi phạm $X \twoheadrightarrow Y$:
  $$R_1 = X \cup Y, \quad R_2 = R \setminus (Y \setminus X)$$
