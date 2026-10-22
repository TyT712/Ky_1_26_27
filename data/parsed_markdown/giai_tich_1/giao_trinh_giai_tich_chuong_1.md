# Giáo trình Giải tích 1 - Chương 1: Hàm số, Giới hạn và Đạo hàm

<!-- PAGE 15 -->
## 1. Định nghĩa Hình thức về Giới hạn
Cho hàm số $y = f(x)$ xác định trên khoảng $(a, b)$ chứa điểm $x_0$ (có thể trừ điểm $x_0$).
Ta nói $L$ là giới hạn của hàm số $f(x)$ khi $x$ dần tới $x_0$, ký hiệu:
$$\lim_{x \to x_0} f(x) = L$$
nếu với mọi số $\epsilon > 0$ bé tùy ý, luôn tồn tại một số $\delta > 0$ sao cho với mọi $x$ thỏa mãn:
$$0 < |x - x_0| < \delta \implies |f(x) - L| < \epsilon$$

<!-- PAGE 22 -->
## 2. Bảng Đạo hàm Các Hàm Cơ bản và Quy tắc Tính Đạo hàm
1. Đạo hàm tích: $(u \cdot v)' = u'v + uv'$
2. Đạo hàm thương: $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ ($v \neq 0$)
3. Đạo hàm của hàm hợp: $[f(u(x))]' = f'(u) \cdot u'(x)$
4. Đạo hàm hàm lượng giác:
   - $(\sin x)' = \cos x$
   - $(\cos x)' = -\sin x$
   - $(\tan x)' = \frac{1}{\cos^2 x} = 1 + \tan^2 x$

<!-- PAGE 35 -->
## 3. Định lý Lagrange (Định lý Giá trị Trung bình)
Nếu hàm số $f(x)$ liên tục trên đoạn $[a, b]$ và có đạo hàm trên khoảng $(a, b)$, thì tồn tại ít nhất một điểm $c \in (a, b)$ sao cho:
$$f(b) - f(a) = f'(c)(b - a) \iff f'(c) = \frac{f(b) - f(a)}{b - a}$$
