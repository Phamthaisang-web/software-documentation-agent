# RULE-REQ-001: Software Requirements Specification Rules

- **Mã quy tắc**: `RULE-REQ-001`
- **Tên quy tắc**: Software Requirements Specification Structure and Quality Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định cấu trúc và tiêu chuẩn chất lượng của tài liệu Đặc tả Yêu cầu Phần mềm (SRS) tuân thủ tiêu chuẩn quốc tế ISO/IEC/IEEE 29148:2018.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-001` (SRS).

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 Clause 9.5 (Software Requirements Specification)

## 4. Đầu vào bắt buộc
- Danh sách yêu cầu chức năng (`functional_requirements`)
- Danh sách yêu cầu phi chức năng (`non_functional_requirements`)
- Giao diện hệ thống bên ngoài (`external_interfaces`)

## 5. Cấu trúc trường bắt buộc
Mục tiêu & Phạm vi, Mô tả tổng quan, Tính năng hệ thống, Yêu cầu phi chức năng, Giao diện ngoài, Tiêu chí kiểm chứng.

## 6. Quy tắc nội dung
1. Mỗi yêu cầu phải có một mã định danh duy nhất không đổi (`REQ-xxx`).
2. Mọi yêu cầu phải đáp ứng 8 tiêu chí ISO 29148: Cần thiết, Rõ ràng, Nhất quán, Hoàn chỉnh, Đơn nhất, Khả thi, Kiểm chứng được, Truy xuất được.
3. Không tự đặt số liệu hiệu năng, SLA mà chưa có cơ sở từ cấu hình hoặc cam kết kỹ thuật; nếu chưa rõ ghi `TBD`.
4. Phân biệt rõ yêu cầu của người dùng (User requirements) và yêu cầu kỹ thuật hệ thống (System requirements).

## 7. Tiêu chí chất lượng
100% yêu cầu có phương pháp kiểm chứng (Test, Inspection, Analysis, Demonstration).

## 8. Quy tắc đặt tên
`DOC-REQ-001_Software_Requirements_Specification.docx`.

## 9. Truy xuất nguồn gốc
Phải trỏ tới `DOC-PM-002` (Scope) và làm cơ sở cho `DOC-ARCH-001` (SAD) và `DOC-TEST-001` (Test Plan).

## 10. Cách kiểm tra
Kiểm tra cấu trúc và tính duy nhất của ID yêu cầu qua `validator.py`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "REQ-FUNC-001: Hệ thống cho phép người dùng đăng nhập bằng email và mật khẩu qua giao thức HTTPS."
- Không hợp lệ: "Hệ thống hỗ trợ đăng nhập tốt và bảo mật."

## 13. Tài liệu liên quan
`DOC-PM-002`, `DOC-REQ-003`, `DOC-REQ-004`, `DOC-REQ-007`.

## 14. Bằng chứng cần thiết
Code router, authentication middleware, controller.

## 15. Giới hạn đã biết
Không có.
