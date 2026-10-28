# RULE-TEST-003: Test Case Specification Rules

- **Mã quy tắc**: `RULE-TEST-003`
- **Tên quy tắc**: Test Case Specificity and Verifiability Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả chi tiết từng ca kiểm thử (Test Case) theo tiêu chuẩn ISO/IEC/IEEE 29119-3:2021.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-003`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-3:2021 (Test Case Specification)
- ISO/IEC/IEEE 29119-4:2021 (Test design techniques)

## 4. Đầu vào bắt buộc
Tiền điều kiện, dữ liệu kiểm thử đầu vào, các bước thực hiện từng bước, kết quả mong đợi.

## 5. Cấu trúc trường bắt buộc
Test Case ID, Tham chiếu Scenario/Requirement, Tiêu đề, Tiền điều kiện (Preconditions), Các bước thực hiện & Dữ liệu đầu vào (Steps & Input Data), Kết quả mong đợi (Expected Result), Phương pháp xác minh.

## 6. Quy tắc nội dung
1. Test Case phải có tính lặp lại (Repeatable): Bất kỳ kiểm thử viên nào đọc cũng có thể thực thi chính xác như nhau.
2. Kết quả mong đợi phải chi tiết, đo lường được (không viết "chạy bình thường").
3. PHÂN BIỆT RẠCH RÒI: Test Case Specification chỉ định nghĩa "Kết quả mong đợi" (Expected Result), KHÔNG ĐƯỢC tự điền "Kết quả thực tế" (Actual Result). Kết quả thực tế chỉ thuộc về Test Execution Report khi đã chạy thật.

## 7. Tiêu chí chất lượng
Các bước thực hiện rõ ràng, có dữ liệu cụ thể.

## 8. Quy tắc đặt tên
`DOC-TEST-003_Test_Case_Specification.xlsx`.

## 9. Truy xuất nguồn gốc
Phải trỏ tới `DOC-REQ-003` (Functional Requirements) và `DOC-REQ-007` (RTM).

## 10. Cách kiểm tra
Kiểm tra cấu trúc ID dạng `TC-{MODULE}-{NUMBER}` và trường Expected Result.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Bước 1: Truy cập `/login`. Bước 2: Nhập email `test@example.com`, pass `Secret123!`. Bước 3: Bấm Đăng nhập. Kết quả mong đợi: Chuyển hướng sang `/dashboard`, hiển thị thông báo 'Chào mừng' và cookie JWT được lưu."
- Không hợp lệ: "Kiểm tra xem login có được không."

## 13. Tài liệu liên quan
`DOC-TEST-002`, `DOC-TEST-004`, `DOC-REQ-007`.

## 14. Bằng chứng cần thiết
Code logic và tiêu chí chấp nhận.

## 15. Giới hạn đã biết
Không có.
