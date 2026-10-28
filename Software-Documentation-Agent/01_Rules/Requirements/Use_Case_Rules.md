# RULE-REQ-005: Use Case Specification Rules

- **Mã quy tắc**: `RULE-REQ-005`
- **Tên quy tắc**: Use Case Flow Specification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Đặc tả luồng tương tác giữa tác nhân (Actor) và hệ thống để hoàn thành mục tiêu nghiệp vụ.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-005`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 (Use Case model)

## 4. Đầu vào bắt buộc
Tác nhân, Tiền điều kiện, Luồng cơ bản, Luồng ngoại lệ, Hậu điều kiện.

## 5. Cấu trúc trường bắt buộc
Use Case ID, Use Case Name, Primary Actor, Preconditions, Basic Flow (Step-by-step), Alternative/Exception Flows, Postconditions.

## 6. Quy tắc nội dung
1. Luồng cơ bản (Basic flow) phải thể hiện chuỗi bước thành công lý tưởng.
2. Luồng ngoại lệ phải mô tả cách hệ thống xử lý khi có lỗi hoặc dữ liệu không hợp lệ.
3. Tiền điều kiện và hậu điều kiện phải phản ánh trạng thái dữ liệu chính xác.

## 7. Tiêu chí chất lượng
Các bước tương tác giữa User và System được phân định rõ ràng.

## 8. Quy tắc đặt tên
`DOC-REQ-005_Use_Case_Specification.docx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-REQ-003` và `DOC-TEST-002` (Test Scenario).

## 10. Cách kiểm tra
Kiểm tra cấu trúc step-by-step của Basic flow.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Bước 1: Người dùng nhấn nút Thanh toán. Bước 2: Hệ thống kiểm tra số dư ví..."
- Không hợp lệ: "Người dùng thực hiện thanh toán xong xuôi."

## 13. Tài liệu liên quan
`DOC-REQ-003`, `DOC-TEST-002`.

## 14. Bằng chứng cần thiết
Code luồng xử lý hoặc controller.

## 15. Giới hạn đã biết
Không có.
