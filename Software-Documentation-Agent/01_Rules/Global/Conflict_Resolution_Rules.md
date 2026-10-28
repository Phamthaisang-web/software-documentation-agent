# RULE-GLOB-010: Conflict Resolution Rules (Quy Tắc Giải Quyết Mâu Thuẫn)

- **Mã quy tắc**: `RULE-GLOB-010`
- **Tên quy tắc**: Information Conflict Detection and Resolution Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định nguyên tắc phát hiện và thứ tự ưu tiên xử lý khi có sự mâu thuẫn giữa các nguồn thông tin trong dự án.

## 2. Phạm vi áp dụng
Khi phân tích dự án và đối chiếu giữa mã nguồn, tài liệu cũ, cấu hình và phản hồi của người dùng.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 (Conflict Resolution in Requirements)

## 4. Đầu vào bắt buộc
Hai hay nhiều nguồn dữ liệu cung cấp thông tin trái ngược nhau về cùng một tính năng hoặc thông số.

## 5. Cấu trúc trường bắt buộc
Bản ghi mâu thuẫn: `topic`, `source_a`, `source_b`, `conflict_description`, `resolution_status`.

## 6. Quy tắc nội dung (Thứ tự ưu tiên giải quyết)
1. **Xác nhận trực tiếp từ người dùng (User Confirmation)**: Có quyền quyết định cao nhất đối với định hướng nghiệp vụ.
2. **Mã nguồn và cấu hình thực tế đang chạy (Running Code & Config)**: Được ưu tiên hơn tài liệu mô tả cũ chưa cập nhật.
3. **Tiêu chuẩn chính thức (Official Standards)**: Được ưu tiên hơn thông lệ không chính thức khi xác định các ràng buộc quy trình (ví dụ: Timebox Scrum).
4. Khi phát hiện mâu thuẫn không thể tự giải quyết an toàn, hệ thống phải ghi nhãn `CONFLICT` và đưa vào danh sách câu hỏi cần làm rõ, không được tự ý thiên vị một bên.

## 7. Tiêu chí chất lượng
Mọi mâu thuẫn được ghi nhận minh bạch, không âm thầm giấu diếm.

## 8. Quy tắc đặt tên
Mã mâu thuẫn: `CONF-{NUMBER}`.

## 9. Truy xuất nguồn gốc
Liên kết trong `project_profile.yaml` mục `conflicting_information`.

## 10. Cách kiểm tra
Bài kiểm thử `test_validation.py`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Xung đột: README ghi cơ sở dữ liệu là MongoDB, nhưng mã nguồn dùng Prisma với PostgreSQL -> Gắn nhãn `CONFLICT`, ưu tiên schema thực tế và hỏi người dùng.

## 13. Tài liệu liên quan
`project_profile_rules.md`, `validation_rules.md`.

## 14. Bằng chứng cần thiết
Đoạn trích từ 2 nguồn mâu thuẫn.

## 15. Giới hạn đã biết
Không tự động phán đoán được ý định tương lai của khách hàng nếu mã nguồn chưa cập nhật.
