# Tóm tắt Học thuật: Giới hạn & Đạo hàm (Xuất từ NotebookLM)
**Môn học:** Giải tích 1 (`giai_tich_1`)

---

## 1. Các Ý Niệm Cốt Lõi (Key Takeaways)
- **Giới hạn hàm số:** Mô tả hành vi của hàm $f(x)$ khi biến số $x$ tiến dần về một giá trị $x_0$.
- **Định nghĩa Heine:** Dùng dãy số $(x_n) \to x_0 \implies f(x_n) \to L$.
- **Định nghĩa Cauchy ($\epsilon - \delta$):** Với mọi $\epsilon > 0$, tồn tại $\delta > 0$ sao cho nếu $0 < |x - x_0| < \delta$ thì $|f(x) - L| < \epsilon$.
- **Đạo hàm:** Đại lượng đo tốc độ biến thiên tức thời của hàm số tại điểm $x_0$:
  $$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

## 2. Các Dạng Vô Định Kinh Điển
- $\frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty, \infty - \infty, 1^\infty, 0^0, \infty^0$.
- Quy tắc L'Hôpital áp dụng cho dạng $\frac{0}{0}$ và $\frac{\infty}{\infty}$.
