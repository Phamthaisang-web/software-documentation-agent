# RULE-REQ-003: Functional Requirements Rules

- **Mã quy tắc**: `RULE-REQ-003`
- **Tên quy tắc**: Functional Requirements Specification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả chi tiết từng yêu cầu chức năng, logic nghiệp vụ, dữ liệu đầu vào và đầu ra theo ISO 29148.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-003`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018

## 4. Đầu vào bắt buộc
Danh mục chức năng, mô tả chi tiết, quy tắc nghiệp vụ.

## 5. Cấu trúc trường bắt buộc
Bảng: Feature ID, Module, Feature Name, Detailed Description, Business Rules, Verification Method.

## 6. Quy tắc nội dung
1. Mỗi chức năng phải có logic nghiệp vụ rõ ràng, mô tả luồng chính và luồng ngoại lệ.
2. Không gộp nhiều chức năng độc lập vào một ID duy nhất (vi phạm tính đơn nhất).

## 7. Tiêu chí chất lượng
100% chức năng có thể kiểm thử độc lập.

## 8. Quy tắc đặt tên
`DOC-REQ-003_Functional_Requirements.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-REQ-005` (Use Case) và `DOC-TEST-003` (Test Case).

## 10. Cách kiểm tra
Kiểm tra ID dạng `REQ-FUNC-xxx`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `REQ-FUNC-001`: Đăng ký tài khoản với email, xác thực OTP trong vòng 5 phút.
- Không hợp lệ: `REQ-FUNC-001`: Hệ thống quản lý toàn bộ người dùng và thanh toán và báo cáo.

## 13. Tài liệu liên quan
`DOC-REQ-001`, `DOC-REQ-005`, `DOC-TEST-003`.

## 14. Bằng chứng cần thiết
Code controller, service logic trong dự án.

## 15. Giới hạn đã biết
Không có.
