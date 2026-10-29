# CHƯƠNG 5: TRIỂN KHAI, BẢO TRÌ VÀ VĂN HÓA DEVOPS

## 1. Môi Trường Vận Hành và Quy Trình Triển Khai (Software Deployment)

### 1.1. Các Môi Trường Trong Vòng Đời Triển Khai
- **Development (Dev):** Môi trường cục bộ hoặc máy chủ dùng cho lập trình viên viết code và thử nghiệm tính năng sơ bộ.
- **Testing / QA (Quality Assurance):** Môi trường để đội kiểm thử chạy automated tests và manual test scenarios.
- **Staging (UAT / Pre-production):** Môi trường sao chép gần như 100% cấu hình, tài nguyên và cấu trúc dữ liệu của môi trường thật (Production) nhằm kiểm thử nghiệm thu người dùng (UAT) và tải chịu lực trước khi phát hành.
- **Production (Prod):** Môi trường thật (live) phục vụ người dùng cuối trực tiếp. Đòi hỏi tính sẵn sàng (Availability), bảo mật và hiệu năng cao nhất.

### 1.2. Các Chiến Lược Triển Khai (Deployment Strategies)
1. **Recreate (Big Bang):**
   - Tắt toàn bộ phiên bản cũ (v1) rồi mới bật phiên bản mới (v2).
   - *Ưu điểm:* Đơn giản, không xung đột dữ liệu phiên bản.
   - *Nhược điểm:* Thời gian ngừng hoạt động (downtime) lớn, rủi ro cao nếu v2 gặp lỗi.
2. **Rolling Update:**
   - Cập nhật tuần tự từng nhóm server/container từ v1 lên v2. Khi v2 của nhóm đó đã khởi động và sẵn sàng, mới cập nhật nhóm kế tiếp.
   - *Ưu điểm:* Không có downtime toàn phần, tiết kiệm tài nguyên bổ sung.
   - *Nhược điểm:* Trong thời gian chuyển đổi, cả v1 và v2 cùng hoạt động đồng thời (cần cơ sở dữ liệu tương thích ngược).
3. **Blue-Green Deployment:**
   - Duy trì hai môi trường giống hệt nhau: Blue (đang chạy live) và Green (nhàn rỗi).
   - Triển khai phiên bản mới lên Green, kiểm thử hoàn tất rồi chuyển đổi Router/Load Balancer trỏ toàn bộ traffic từ Blue sang Green.
   - *Ưu điểm:* Zero downtime, rollback tức thì nếu có lỗi phát sinh bằng cách trỏ router ngược lại Blue.
   - *Nhược điểm:* Tốn gấp đôi chi phí tài nguyên hạ tầng.
4. **Canary Release:**
   - Triển khai phiên bản mới đến một tỷ lệ nhỏ người dùng trước (ví dụ 5% traffic hoặc nhóm beta tester), 95% còn lại vẫn dùng bản cũ.
   - Giám sát các chỉ số (lỗi, CPU, trải nghiệm). Nếu ổn định, tăng dần traffic lên 25%, 50%, 100%.
   - *Ưu điểm:* Rủi ro cực thấp, phát hiện lỗi thực tế ở phạm vi hẹp.

---

## 2. Tích Hợp Liên Tục và Triển Khai Liên Tục (CI/CD)

### 2.1. Phân Biệt CI, CD, CD
- **Continuous Integration (CI):** Lập trình viên thường xuyên merge code về nhánh chính (ít nhất hàng ngày). Mỗi commit tự động kích hoạt tiến trình Build và chạy Automated Unit/Integration Tests để phát hiện xung đột sớm.
- **Continuous Delivery (CD):** Tự động đóng gói và triển khai ứng dụng lên các môi trường thử nghiệm (Staging). Quá trình đưa lên Production luôn sẵn sàng nhưng cần phê duyệt thủ công (Manual Approval).
- **Continuous Deployment (CD):** Mọi thay đổi vượt qua toàn bộ pipeline kiểm thử tự động sẽ được đẩy thẳng trực tiếp lên Production mà không cần bất kỳ sự can thiệp thủ công nào.

### 2.2. CI/CD Pipeline với GitHub Actions
- Cấu hình qua tệp YAML đặt tại `.github/workflows/`.
- Bao gồm các thành phần:
  - **Workflow:** Quy trình tự động tổng thể.
  - **Event (on):** Sự kiện kích hoạt (push, pull_request, release, schedule).
  - **Jobs:** Tập hợp các bước thực thi chạy trên máy ảo runner (ubuntu-latest, windows-latest).
  - **Steps:** Các bước thực thi tuần tự (chạy action có sẵn hoặc lệnh shell command qua `run`).
  - **Secrets:** Quản lý an toàn các API keys, SSH keys, credentials nhạy cảm.

---

## 3. Bảo Trì Phần Mềm (Software Maintenance)

### 3.1. Định Nghĩa và Chi Phí
Bảo trì phần mềm là quá trình sửa đổi hệ thống phần mềm sau khi đã bàn giao cho khách hàng nhằm sửa lỗi, cải thiện hiệu năng, hoặc thích ứng với môi trường thay đổi.
Chi phí bảo trì thường chiếm **60% - 80%** tổng chi phí trong toàn bộ vòng đời phần mềm (Software Lifecycle Cost).

### 3.2. Bốn Loại Hình Bảo Trì (4 Maintenance Types)
1. **Bảo trì sửa sai (Corrective Maintenance):**
   - Khắc phục các lỗi (bug, defect, crash) phát sinh trong quá trình vận hành thực tế mà giai đoạn kiểm thử chưa phát hiện ra.
   - Tỷ lệ: Chiếm khoảng 20% công việc bảo trì.
2. **Bảo trì thích nghi (Adaptive Maintenance):**
   - Sửa đổi phần mềm để tiếp tục hoạt động tương thích khi môi trường bên ngoài thay đổi (nâng cấp hệ điều hành, đổi cơ sở dữ liệu, thay đổi phần cứng, thay đổi luật pháp hoặc giao thức API đối tác).
   - Tỷ lệ: Chiếm khoảng 25% công việc bảo trì.
3. **Bảo trì hoàn thiện (Perfective Maintenance):**
   - Bổ sung tính năng mới theo yêu cầu người dùng, tối ưu hóa thuật toán, cải tiến giao diện người dùng (UI/UX) và tăng tốc độ xử lý.
   - Tỷ lệ: Chiếm tỷ trọng lớn nhất, khoảng **50%** công việc bảo trì.
4. **Bảo trì phòng ngừa (Preventive Maintenance / Software Re-engineering):**
   - Tái cấu trúc mã nguồn (Refactoring), dọn dẹp nợ kỹ thuật (Technical Debt), cập nhật tài liệu nhằm tăng tính dễ bảo trì và ngăn ngừa lỗi tiềm ẩn trong tương lai.
   - Tỷ lệ: Chiếm khoảng 5% công việc bảo trì.

### 3.3. Quy Luật Tiến Hóa Phần Mềm Của Lehman (Lehman's Laws)
- **Luật 1 - Thay đổi liên tục (Continuing Change):** Hệ thống thực tế phải liên tục thích ứng, nếu không sẽ trở nên lỗi thời và kém hữu ích.
- **Luật 2 - Độ phức tạp tăng dần (Increasing Complexity):** Khi hệ thống tiến hóa, độ phức tạp của nó ngày càng tăng trừ khi có hành động tái cấu trúc cụ thể.
- **Luật 6 - Tăng trưởng liên tục (Continuing Growth):** Chức năng của hệ thống phải liên tục tăng để duy trì sự hài lòng của người dùng.

---

## 4. Văn Hóa DevOps và Thực Hành Vận Hành Hiện Đại

### 4.1. Khái Niệm DevOps
DevOps là sự kết hợp giữa **Development (Phát triển)** và **Operations (Vận hành)**, cùng với triết lý văn hóa, thực hành và các công cụ nhằm tăng cường khả năng cung cấp ứng dụng và dịch vụ của tổ chức với vận tốc cao và độ tin cậy vượt trội.
Xóa bỏ "bức tường ngăn cách" (Wall of Confusion) giữa đội Dev (ưu tiên thay đổi, tính năng mới) và đội Ops (ưu tiên độ ổn định, không muốn rủi ro).

### 4.2. Khung Mô Hình CAMS
- **Culture (Văn hóa):** Chia sẻ trách nhiệm chung, thấu cảm, không đổ lỗi (Blameless Post-mortem), cộng tác liên chức năng.
- **Automation (Tự động hóa):** Tự động hóa mọi bước có thể (CI/CD, kiểm thử, cấp phát hạ tầng, giám sát).
- **Measurement (Đo lường):** Đo lường dữ liệu định lượng (thời gian build, tần suất triển khai, tỷ lệ lỗi, MTTR).
- **Sharing (Chia sẻ):** Chia sẻ tri thức, công cụ, bài học kinh nghiệm và phản hồi giữa các phòng ban.

### 4.3. Các Chỉ Số Hiệu Suất DevOps Cốt Lõi (DORA Metrics)
1. **Deployment Frequency (Tần suất triển khai):** Mức độ thường xuyên code được triển khai thành công lên Production.
2. **Lead Time for Changes (Thời gian dẫn cho các thay đổi):** Thời gian từ khi commit code đến khi code chạy thành công trên Production.
3. **Change Failure Rate (Tỷ lệ thay đổi thất bại):** Tỷ lệ phần trăm các lần triển khai gây ra sự cố nghiêm trọng cần rollback hoặc hotfix.
4. **Mean Time to Recovery / Restore (MTTR - Thời gian trung bình để phục hồi):** Thời gian cần thiết để khôi phục dịch vụ khi có sự cố xảy ra.

### 4.4. Giám Sát và Khả Năng Quan Sát (Monitoring & Observability)
- **Three Pillars of Observability:**
  1. **Metrics:** Số liệu định lượng theo thời gian (CPU, RAM, Request Rate, Error Rate - ví dụ Prometheus, Grafana).
  2. **Logs:** Nhật ký sự kiện có dấu thời gian ghi nhận chi tiết ngữ cảnh lỗi (ELK Stack, Loki).
  3. **Traces:** Theo dõi hành trình phân tán của một request đi qua nhiều microservices (Jaeger, Zipkin, OpenTelemetry).

---

## Tinh Hoa Kiến Thức & Tóm Tắt Chuyên Sâu (Key Takeaways)
> **Chuyên đề mở rộng:** TRIỂN KHAI, BẢO TRÌ & DEVOPS

### 1. Trọng Tâm Lý Thuyết
- **4 Chiến Lược Triển Khai:**
  - *Recreate:* Tắt cũ bật mới, có downtime.
  - *Rolling Update:* Cập nhật từng node tuần tự, zero downtime, cần tương thích ngược phiên bản.
  - *Blue-Green:* 2 môi trường độc lập, switch router tức thì, rollback dễ, tốn gấp đôi tài nguyên.
  - *Canary:* Mở cho một tỷ lệ nhỏ traffic (5-10%) trước, giám sát ổn định rồi nhân rộng dần.
- **CI/CD:**
  - *CI (Continuous Integration):* Thường xuyên merge code, tự động build & test.
  - *Continuous Delivery:* Tự động đóng gói & deploy lên Staging, deploy lên Production cần bấm nút duyệt (Manual Approval).
  - *Continuous Deployment:* Tự động deploy thẳng lên Production không cần can thiệp người.
- **4 Loại Hình Bảo Trì Phần Mềm:**
  - *Corrective (Sửa sai - 20%):* Vá lỗi phát sinh khi vận hành.
  - *Adaptive (Thích nghi - 25%):* Thay đổi cho tương thích môi trường mới (OS, phần cứng, API đối tác).
  - *Perfective (Hoàn thiện - 50%):* Thêm tính năng mới, tối ưu tốc độ, nâng cao UX (chiếm tỷ trọng cao nhất).
  - *Preventive (Phòng ngừa - 5%):* Refactoring, giảm technical debt, bảo vệ mã nguồn tương lai.
- **Chi phí bảo trì:** Chiếm **60% - 80%** tổng vòng đời dự án phần mềm.
- **Văn Hóa DevOps & CAMS:** Culture (không đổ lỗi), Automation (CI/CD), Measurement (DORA), Sharing (tri thức).
- **4 Chỉ Số DORA:** Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR.

### 2. Công Thức & Chỉ Số Tính Toán Cần Nhớ
- **Uptime / Availability (%):**
  $$\text{Availability} = \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}} \times 100\%$$
- **MTTR (Mean Time To Recovery):**
  $$\text{MTTR} = \frac{\text{Tổng thời gian khắc phục sự cố}}{\text{Tổng số sự cố}}$$
- **Change Failure Rate (%):**
  $$\text{CFR} = \frac{\text{Số lần deploy gặp lỗi phải rollback}}{\text{Tổng số lần deploy}} \times 100\%$$
