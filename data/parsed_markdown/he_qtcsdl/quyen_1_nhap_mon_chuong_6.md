# Giáo trình Thực hành Cơ sở Dữ liệu (Phần I - Nhập môn) - Chương 6: Xử lý và Tối ưu hóa Câu hỏi Truy vấn

<!-- PAGE 186 -->
## 1. Lý Do Phải Tối Ưu Hóa Câu Hỏi Truy Vấn (Query Optimization)

Trong cơ sở dữ liệu quan hệ, một câu truy vấn viết bằng ngôn ngữ SQL có thể được dịch ra thành nhiều biểu thức đại số quan hệ khác nhau, tương ứng với nhiều chiến lược thực thi (Execution Plans) khác nhau.
- Các chiến lược thực thi này tuy cùng cho ra một kết quả duy nhất nhưng có **chi phí thực thi (về số lần truy xuất đĩa I/O, thời gian CPU, dung lượng bộ nhớ tạm)** chênh lệch nhau hàng trăm, thậm chí hàng triệu lần.
- Nhiệm vụ của **Bộ tối ưu hóa câu hỏi (Query Optimizer)** trong DBMS là tự động phân tích và lựa chọn kế hoạch thực thi có chi phí ước lượng thấp nhất.

```mermaid
graph LR
    SQL["Câu truy vấn SQL"] --> Parser["Phân tích cú pháp & ngữ nghĩa"]
    Parser --> RelTree["Cây đại số quan hệ ban đầu"]
    RelTree --> Opt["Bộ Tối Ưu Hóa (Query Optimizer)"]
    Opt --> BestPlan["Kế hoạch thực thi tối ưu nhất"]
    BestPlan --> Engine["Bộ máy thực thi (Execution Engine)"]
    Engine --> Result["Kết quả trả về cho người dùng"]
```

<!-- PAGE 188 -->
## 2. Định Giá Chi Phí Thực Thi Câu Hỏi (Query Cost Estimation)

Chi phí tổng quát của một kế hoạch thực thi câu hỏi được tính bằng:
$$\text{Cost} = C_{I/O} \times N_{blocks} + C_{CPU} \times N_{tuples} + C_{COM} \times N_{messages}$$
Trong đó:
- $C_{I/O}$: Chi phí một lần đọc/ghi khối nhớ từ đĩa vào RAM (thường là yếu tố chi phối chiếm tỉ trọng lớn nhất).
- $C_{CPU}$: Chi phí xử lý bộ nhớ trong (so sánh điều kiện, tính toán giá trị biểu thức, băm, sắp xếp).
- $C_{COM}$: Chi phí truyền thông điệp qua mạng (đối với hệ CSDL phân tán).

<!-- PAGE 191 -->
## 3. Các Quy Tắc Biến Đổi Đại Số Quan Hệ Tương Đương (Equivalence Rules)

Hai biểu thức đại số quan hệ $E_1$ và $E_2$ được gọi là tương đương ($E_1 \equiv E_2$) nếu chúng cho ra cùng một tập hợp các bộ giá trị trên bất kỳ thể hiện hợp lệ nào của cơ sở dữ liệu.

### 3.1. Các quy tắc hoán vị và kết hợp
1. **Giao hoán phép kết nối:**
   $$R \bowtie S \equiv S \bowtie R$$
2. **Kết hợp phép kết nối:**
   $$(R \bowtie S) \bowtie T \equiv R \bowtie (S \bowtie T)$$

### 3.2. Quy tắc đẩy phép chọn ($\sigma$) xuống sớm
Phép chọn $\sigma$ làm giảm số lượng hàng (cardinality), do đó đẩy phép chọn xuống thực hiện trước các phép kết nối hoặc tích Descartes sẽ làm giảm đáng kể kích thước quan hệ trung gian:
1. **Tách chuỗi các điều kiện chọn liên kết bằng phép VÀ ($\land$):**
   $$\sigma_{C_1 \land C_2 \land \dots \land C_n}(R) \equiv \sigma_{C_1}(\sigma_{C_2}(\dots(\sigma_{C_n}(R))\dots))$$
2. **Đẩy phép chọn qua phép kết nối:** Nếu điều kiện $C$ chỉ liên quan đến các thuộc tính của quan hệ $R$:
   $$\sigma_C(R \bowtie S) \equiv (\sigma_C(R)) \bowtie S$$
3. **Phân phối phép chọn qua phép kết nối:** Nếu $C = C_R \land C_S$, trong đó $C_R$ chỉ liên quan tới $R$ và $C_S$ chỉ liên quan tới $S$:
   $$\sigma_{C_R \land C_S}(R \bowtie S) \equiv (\sigma_{C_R}(R)) \bowtie (\sigma_{C_S}(S))$$

### 3.3. Quy tắc đẩy phép chiếu ($\pi$) xuống sớm
Phép chiếu $\pi$ loại bỏ các cột không cần thiết, làm giảm kích thước của từng bản ghi (bytes), do đó tăng hệ số đóng gói $bfr$ và giảm số khối đĩa cần cấp phát:
$$\pi_{L}(R \bowtie S) \equiv \pi_{L}(\pi_{L_R}(R) \bowtie \pi_{L_S}(S))$$

<!-- PAGE 194 -->
## 4. Thuật Toán Tối Ưu Hóa Heuristic Cho Cây Truy Vấn (Query Tree)

Quy trình chuẩn hóa 4 bước tối ưu hóa cây đại số quan hệ:
1. **Bước 1:** Tách các điều kiện chọn phức tạp thành chuỗi các phép chọn đơn nguyên theo quy tắc $\sigma_{C_1 \land C_2}(R) \equiv \sigma_{C_1}(\sigma_{C_2}(R))$.
2. **Bước 2 (Quan trọng nhất):** Đẩy từng phép chọn $\sigma$ xuống sâu nhất có thể dọc theo các nhánh của cây truy vấn để lọc dữ liệu ngay tại bảng cơ sở trước khi kết nối.
3. **Bước 3:** Sắp xếp lại các nút lá sao cho quan hệ nào có kích thước nhỏ nhất sau khi chọn sẽ được đưa vào kết nối trước.
4. **Bước 4:** Đẩy các phép chiếu $\pi$ xuống bên dưới cây truy vấn, chỉ giữ lại các thuộc tính tham gia vào điều kiện kết nối và các thuộc tính nằm trong danh sách đầu ra của lệnh `SELECT`.

<!-- PAGE 207 -->
## 5. Ví Dụ Bài Tập Tối Ưu Hóa Cây Truy Vấn Có Lời Giải

**Đề bài:** Cho câu truy vấn SQL sau:
```sql
SELECT SV.HoTen, KQ.Diem
FROM SINH_VIEN SV, KET_QUA KQ
WHERE SV.MaSV = KQ.MaSV AND SV.QueQuan = N'Huế' AND KQ.MaMH = 'CSDL';
```

**Phân tích và biến đổi tối ưu:**

1. *Biểu thức chưa tối ưu (Dịch thô sang đại số quan hệ):*
   $$E_{\text{tho}} = \pi_{HoTen, Diem}(\sigma_{SV.MaSV = KQ.MaSV \land QueQuan='Hue' \land MaMH='CSDL'}(SINH\_VIEN \times KET\_QUA))$$
   *Nhược điểm:* Phải tính tích Descartes $SINH\_VIEN \times KET\_QUA$, sinh ra hàng triệu bản ghi trung gian trước khi lọc.

2. *Biến đổi bằng quy tắc Heuristic:*
   - Đẩy điều kiện lọc $\sigma_{QueQuan='Hue'}$ xuống thực hiện trực tiếp trên bảng `SINH_VIEN`.
   - Đẩy điều kiện lọc $\sigma_{MaMH='CSDL'}$ xuống thực hiện trực tiếp trên bảng `KET_QUA`.
   - Chuyển tích Descartes $\times$ kết hợp điều kiện $SV.MaSV = KQ.MaSV$ thành phép kết tự nhiên hoặc kết bằng: $\bowtie_{SV.MaSV = KQ.MaSV}$.
   - Chiếu bớt các cột dư thừa trước khi kết: chỉ giữ lại `MaSV, HoTen` từ `SINH_VIEN` và `MaSV, Diem` từ `KET_QUA`.

3. *Biểu thức tối ưu cuối cùng:*
   $$E_{\text{toi\_uu}} = \pi_{HoTen, Diem}\left( \pi_{MaSV, HoTen}(\sigma_{QueQuan='Hue'}(SINH\_VIEN)) \bowtie_{SV.MaSV = KQ.MaSV} \pi_{MaSV, Diem}(\sigma_{MaMH='CSDL'}(KET\_QUA)) \right)$$
