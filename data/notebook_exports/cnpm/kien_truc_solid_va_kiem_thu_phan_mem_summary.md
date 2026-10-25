# Chuyên Đề: Clean Code, Chiến Lược Kiểm Thử & TDD Trong Kỹ Nghệ Phần Mềm

## 1. Triết Lý Clean Code và Nợ Kỹ Thuật
- Mã nguồn được đọc nhiều gấp 10 lần so với thời gian viết ra nó. Viết code sạch là sự tôn trọng dành cho chính bạn và đồng nghiệp trong tương lai.
- Refactoring không phải là viết lại từ đầu mà là cải tiến cấu trúc bên trong của mã nguồn mà không làm thay đổi hành vi bên ngoài của hệ thống.

## 2. Cốt Lõi Kim Tự Tháp Kiểm Thử Hiện Đại
- Phá vỡ mô hình 'Cây kem ốc quế đảo ngược' (Anti-pattern: quá nhiều E2E test thủ công, quá ít unit test) giúp pipeline CI chạy nhanh từ vài chục phút xuống vài chục giây.
- Mocking và Stubbing là kỹ thuật sống còn để unit test đạt tốc độ mili-giây và chạy hoàn toàn độc lập với môi trường ngoài.

## 3. Sức Mạnh của Chu Trình TDD
- Viết test trước buộc lập trình viên phải đóng vai người sử dụng API trước khi lập trình cài đặt; từ đó thiết kế ra các hàm có giao diện trong sáng, dễ gọi và ít khớp nối.
