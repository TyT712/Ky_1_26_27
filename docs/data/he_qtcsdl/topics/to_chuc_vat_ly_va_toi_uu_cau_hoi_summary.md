# TỔ CHỨC VẬT LÝ DỮ LIỆU & TỐI ƯU HÓA CÂU HỎI TRUY VÂN

## 1. TỔNG QUAN VÀ KHÁI NIỆM CỐT LÕI (OVERVIEW)
Tổ chức tệp vật lý và tối ưu hóa câu hỏi truy vấn là hai khía cạnh nền tảng quyết định hiệu năng thực tế của một Hệ Quản trị Cơ sở Dữ liệu (DBMS). Trong khi tổ chức vật lý quy định cách các bản ghi dữ liệu và chỉ mục được lưu trữ trên bộ nhớ thứ cấp (khối đĩa - disk block), thì bộ tối ưu hóa truy vấn (Query Optimizer) chịu trách nhiệm lựa chọn cây thực thi có chi phí vào/ra (I/O) và thời gian thực hiện tối thiểu cho mỗi câu lệnh đại số quan hệ / SQL.

---

## 2. TỔ CHỨC DỮ LIỆU TRÊN BỘ NHỚ NGOÀI
### 2.1. Đơn vị lưu trữ và Hệ số kết khối ($bfr$)
- Dữ liệu trên đĩa từ được chia thành các **khối (Block)** có kích thước cố định $B$ (thường là 4KB, 8KB,...).
- Mỗi bản ghi có kích thước $R$ byte.
- **Hệ số kết khối (Blocking Factor - $bfr$)**: Số bản ghi tối đa chứa được trong 1 khối:
  $$bfr = \left\lfloor \frac{B}{R} \right\rfloor$$
- Số khối cần thiết để lưu trữ một tệp gồm $r$ bản ghi:
  $$b = \left\lceil \frac{r}{bfr} \right\rceil$$

### 2.2. Các dạng tổ chức tệp cơ bản
1. **Tệp đống (Heap File / Unordered File):**
   - Bản ghi được chèn vào cuối tệp khi có không gian trống.
   - Thao tác chèn nhanh: $O(1)$.
   - Tìm kiếm tuyến tính: Chi phí trung bình $\approx b/2$ khối, xấu nhất $b$ khối.
2. **Tệp tuần tự sắp thứ tự (Ordered / Sequential File):**
   - Bản ghi được sắp xếp theo giá trị của trường khóa sắp xếp (Ordering Key).
   - Tìm kiếm nhị phân theo trường khóa: Chi phí $\approx \lceil \log_2 b \rceil$ lần đọc khối.
   - Thao tác chèn và xóa tốn kém do phải dịch chuyển các bản ghi (cần vùng tràn - overflow area).
3. **Tệp băm (Hash File):**
   - Áp dụng hàm băm $h(K)$ lên khóa băm để xác định trực tiếp địa chỉ khối (Bucket).
   - Truy xuất theo khóa chính đạt chi phí lý thuyết $\approx 1$ I/O.
   - Không hỗ trợ hiệu quả truy vấn theo khoảng giá trị (Range query).

---

## 3. CẤU TRÚC CHỈ MỤC (INDEXING TECHNIQUES)
### 3.1. Phân loại chỉ mục
- **Chỉ mục chính (Primary Index):** Xây dựng trên tệp dữ liệu đã sắp thứ tự theo khóa chính. Chỉ mục thưa (Sparse Index) chỉ lưu giá trị khóa đầu tiên của mỗi khối (Anchor record).
- **Chỉ mục gom cụm (Clustering Index):** Xây dựng trên tệp đã sắp thứ tự theo một trường không phải khóa chính (các bản ghi trùng giá trị gom vào các khối liền kề).
- **Chỉ mục phụ (Secondary Index):** Xây dựng trên một trường bất kỳ của tệp (tệp có thể chưa sắp xếp). Thường là chỉ mục dày (Dense Index) với mỗi bản ghi tương ứng một mục trong chỉ mục.

### 3.2. Cây chỉ mục đa mức B-Tree và B+ Tree
- **Cây B+ (B+ Tree):** Cấu trúc cân bằng vượt trội dùng làm tiêu chuẩn trong RDBMS:
  - Tất cả các khóa dữ liệu và con trỏ bản ghi thực tế chỉ nằm ở các **nút lá**.
  - Các nút lá được liên kết kép với nhau tuần tự, cho phép duyệt theo khoảng giá trị cực kỳ nhanh.
  - Các nút trong (nút chỉ mục) chỉ chứa khóa dẫn đường và con trỏ đến nút con.
  - Chi phí tìm kiếm, chèn, xóa luôn được bảo đảm ở mức $O(\log_m N)$, với $m$ là bậc của cây (thường rất lớn, từ vài chục đến hàng trăm, giúp cây có độ cao thấp chỉ 2 - 4 mức).

---

## 4. BỘ TỐI ƯU HÓA CÂU HỎI TRUY VẤN (QUERY OPTIMIZATION)
### 4.1. Quy trình xử lý câu truy vấn
1. **Phân tích cú pháp và kiểm tra ngữ nghĩa (Parser & Translator):** Chuyển câu lệnh SQL thành biểu thức Đại số quan hệ và Cây truy vấn ban đầu.
2. **Tối ưu hóa logic (Heuristic / Rule-based Optimization):** Sử dụng các luật biến đổi đại số tương đương để tái cấu trúc cây truy vấn thành dạng hiệu quả hơn.
3. **Tối ưu hóa vật lý (Cost-based Optimization):** Ước lượng chi phí thực thi dựa trên thống kê danh mục (Catalogue stats: số bản ghi, số khối, số giá trị phân biệt $V(A, R)$) và chọn thuật toán cụ thể (Nested Loop Join, Hash Join, Index Scan...).
4. **Sinh mã thực thi (Code Generator):** Tạo kế hoạch thực thi (Execution Plan) để chuyển cho Engine xử lý.

### 4.2. Các quy tắc biến đổi đại số tương đương quan trọng
- Giao hoán và kết hợp phép tích Descartes và phép kết:
  $$E_1 \bowtie E_2 \equiv E_2 \bowtie E_1$$
  $$(E_1 \bowtie E_2) \bowtie E_3 \equiv E_1 \bowtie (E_2 \bowtie E_3)$$
- Tách và đẩy phép chọn $\sigma$ xuống sớm (Pushing Selection down):
  $$\sigma_{c_1 \land c_2}(R) \equiv \sigma_{c_1}(\sigma_{c_2}(R))$$
  $$\sigma_{c}(E_1 \bowtie E_2) \equiv (\sigma_c(E_1)) \bowtie E_2 \quad \text{(khi } c \text{ chỉ liên quan đến các thuộc tính của } E_1\text{)}$$
- Đẩy phép chiếu $\pi$ xuống sớm (Pushing Projection down):
  $$\pi_{L}(E_1 \bowtie E_2) \equiv \pi_{L}(\pi_{L_1}(E_1) \bowtie \pi_{L_2}(E_2))$$
  Loại bỏ sớm các thuộc tính không cần thiết để giảm độ rộng bản ghi $R$, từ đó tăng $bfr$ và giảm số khối cần nạp vào bộ nhớ RAM.

### 4.3. Các chiến lược Heuristic cốt lõi
1. **Thực hiện phép chọn $\sigma$ càng sớm càng tốt:** Giảm triệt để số lượng bộ (cardinality) trước khi thực hiện các phép kết đắt đỏ.
2. **Thực hiện phép chiếu $\pi$ càng sớm càng tốt:** Giảm kích thước mỗi bộ (tuple width), tiết kiệm bộ đệm Buffer Pool.
3. **Thay thế tích Descartes kèm phép chọn bằng phép kết tự nhiên hoặc kết bằng:** Chuyển $\sigma_{R.A = S.A}(R \times S) \longrightarrow R \bowtie_{R.A = S.A} S$.
4. **Xác định thứ tự kết hợp tối ưu:** Kết các quan hệ có kích thước kết quả trung gian nhỏ nhất trước.
