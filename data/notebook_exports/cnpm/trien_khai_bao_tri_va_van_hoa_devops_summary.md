# TỔNG HỢP ÔN TẬP CHƯƠNG 5: TRIỂN KHAI, BẢO TRÌ & DEVOPS

## 1. Trọng Tâm Lý Thuyết
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

## 2. Công Thức & Chỉ Số Tính Toán Cần Nhớ
- **Uptime / Availability (%):**
  $$\text{Availability} = \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}} \times 100\%$$
- **MTTR (Mean Time To Recovery):**
  $$\text{MTTR} = \frac{\text{Tổng thời gian khắc phục sự cố}}{\text{Tổng số sự cố}}$$
- **Change Failure Rate (%):**
  $$\text{CFR} = \frac{\text{Số lần deploy gặp lỗi phải rollback}}{\text{Tổng số lần deploy}} \times 100\%$$
