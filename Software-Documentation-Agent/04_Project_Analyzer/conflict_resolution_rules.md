# Conflict Resolution Rules — Quy Tắc Xử Lý Mâu Thuẫn Thông Tin

Tài liệu này quy định cách xử lý khi Project Analyzer phát hiện mâu thuẫn giữa các thành phần khác nhau trong dự án.

---

## 1. Các Dạng Mâu Thuẫn Thường Gặp
- **Mã nguồn vs Tài liệu cũ**: Code đã chuyển sang MongoDB nhưng README cũ ghi PostgreSQL.
- **API Spec vs Implementation**: Swagger ghi endpoint trả về 200 nhưng code trả về 201.
- **Code vs User Statement**: Người dùng nói hệ thống chưa hỗ trợ thanh toán nhưng trong code đã có module Stripe hoàn chỉnh.

## 2. Ma Trận Quyết Định Giải Quyết Xung Đột
1. **Ưu tiên 1 - Xác nhận từ Người dùng**: Người dùng có quyền quyết định mục tiêu kinh doanh và phạm vi thực sự muốn phát hành.
2. **Ưu tiên 2 - Mã nguồn thực tế đang chạy (Active Code)**: Code thực tế phản ánh chính xác hành vi phần mềm hơn tài liệu văn bản tĩnh.
3. **Ưu tiên 3 - Tiêu chuẩn quốc tế**: Đối với quy trình (Scrum / ISO), tiêu chuẩn chính thức có thẩm quyền cao hơn các cách hiểu sai lệch của nhóm.

## 3. Quy Trình Cảnh Báo
Khi phát hiện xung đột:
1. Ghi nhận vào mục `conflicting_information` trong `project_profile.yaml`.
2. Tạo câu hỏi làm rõ (Clarification Item) cho người dùng trong báo cáo phân tích.
3. Trong lúc chờ xác nhận, tài liệu sinh ra phải ghi chú rõ ràng về sự không nhất quán này, không được âm thầm tự chọn một phương án rồi bỏ qua phương án kia.
