# RULE-DEL-004: Issue Log Rules

- **Mã quy tắc**: `RULE-DEL-004`
- **Tên quy tắc**: Issue Resolution and Escalation Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Ghi nhận và theo dõi các vấn đề thực tế phát sinh trong dự án cần hành động giải quyết.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-004`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021

## 4. Đầu vào bắt buộc
Mô tả sự cố, mức độ ảnh hưởng, người phụ trách xử lý, phương án giải quyết.

## 5. Cấu trúc trường bắt buộc
Issue ID, Ngày phát hiện, Mô tả vấn đề, Mức độ nghiêm trọng, Rủi ro/PBI liên quan, Người phụ trách, Kế hoạch hành động, Hạn xử lý, Trạng thái (Open/In Progress/Resolved/Closed).

## 6. Quy tắc nội dung
1. Phân biệt rõ RỦI RO (chưa xảy ra, chỉ có xác suất) và VẤN ĐỀ / SỰ CỐ (đã thực sự xảy ra).
2. Mọi sự cố phải có hạn chót giải quyết (Target Resolution Date) và cập nhật tiến độ thường xuyên.

## 7. Tiêu chí chất lượng
Các sự cố nghiêm trọng (Blocker) phải có phương án xử lý ngay trong 24-48 giờ.

## 8. Quy tắc đặt tên
`DOC-DEL-004_Issue_Log.xlsx`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-DEL-003` và báo cáo trong `DOC-DEL-008`.

## 10. Cách kiểm tra
Kiểm tra trạng thái của các issue quá hạn.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `ISSUE-001`: Khóa tài khoản Google Cloud do hết hạn thẻ thanh toán. Hành động: Cập nhật thẻ công ty và mở lại dịch vụ.
- Không hợp lệ: Ghi nhận sự cố mà không có người phụ trách.

## 13. Tài liệu liên quan
`DOC-DEL-003`, `DOC-DEL-008`.

## 14. Bằng chứng cần thiết
Biên bản sự cố hoặc log hệ thống.

## 15. Giới hạn đã biết
Không có.
