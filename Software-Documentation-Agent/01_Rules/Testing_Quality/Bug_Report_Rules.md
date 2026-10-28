# RULE-TEST-005: Defect / Bug Report Rules

- **Mã quy tắc**: `RULE-TEST-005`
- **Tên quy tắc**: Defect Reporting Structure and Reproducibility Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định cấu trúc báo cáo sự cố phần mềm (Bug Report) theo ISO/IEC/IEEE 29119-3:2021 đảm bảo khả năng tái hiện lỗi.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-005`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-3:2021 (Incident / Defect Report)

## 4. Đầu vào bắt buộc
Hành vi thực tế quan sát được, hành vi mong đợi, các bước tái hiện, mức độ nghiêm trọng (Severity: Blocker/Critical/Major/Minor), môi trường phát hiện.

## 5. Cấu trúc trường bắt buộc
Defect ID, Tóm tắt lỗi, Test Case/Requirement liên quan, Severity, Priority, Môi trường, Các bước tái hiện (Steps to Reproduce), Kết quả mong đợi vs Kết quả thực tế, Bằng chứng (Log/Stack trace), Trạng thái (Open/In Progress/Fixed/Closed).

## 6. Quy tắc nội dung
1. Các bước tái hiện phải được ghi chi tiết từng bước, kèm dữ liệu đầu vào cụ thể.
2. Đính kèm log lỗi hoặc stack trace thực tế khi có.
3. Phân biệt rõ mức độ nghiêm trọng kỹ thuật (Severity) và mức độ ưu tiên xử lý kinh doanh (Priority).

## 7. Tiêu chí chất lượng
Lập trình viên có thể tái hiện được lỗi chỉ dựa vào mô tả trong báo cáo.

## 8. Quy tắc đặt tên
`DOC-TEST-005_Bug_Report.xlsx`.

## 9. Truy xuất nguồn gốc
Trỏ từ `DOC-TEST-004` (Test Run) và liên kết tới `DOC-DEL-004` (Issue Log).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của `steps_to_reproduce` và `severity`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "BUG-001: Lỗi 500 khi email chứa dấu cộng. Các bước tái hiện: 1. Đăng ký với `a+b@test.com`. Kết quả mong đợi: Tạo tài khoản thành công. Thực tế: Ném NullPointerException tại UserController:45."
- Không hợp lệ: "Website bị lỗi rồi sửa đi."

## 13. Tài liệu liên quan
`DOC-TEST-004`, `DOC-DEL-004`.

## 14. Bằng chứng cần thiết
Stack trace, server logs, network payload.

## 15. Giới hạn đã biết
Không có.
