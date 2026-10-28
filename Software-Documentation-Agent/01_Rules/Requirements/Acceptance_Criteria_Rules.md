# RULE-REQ-007: Acceptance Criteria Rules

- **Mã quy tắc**: `RULE-REQ-007`
- **Tên quy tắc**: Acceptance Criteria Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định tiêu chuẩn viết tiêu chí chấp nhận (Acceptance Criteria) theo định dạng Given-When-Then hoặc Checklist kiểm chứng được.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-008`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 & Agile Standards

## 4. Đầu vào bắt buộc
Story ID, Điều kiện đầu vào, Hành động thực hiện, Kết quả mong đợi.

## 5. Cấu trúc trường bắt buộc
Story ID, Criterion ID, Scenario Title, Given, When, Then, Verification Status.

## 6. Quy tắc nội dung
1. Mỗi tiêu chí phải có thể kiểm chứng được một cách khách quan không thể chối cãi.
2. Bao quát cả trường hợp biên (boundary cases) và trường hợp dữ liệu sai.
3. Không viết tiêu chí chấp nhận một cách chung chung như "hệ thống không bị lỗi".

## 7. Tiêu chí chất lượng
100% tiêu chí có thể chuyển đổi trực tiếp thành Automated Test Case.

## 8. Quy tắc đặt tên
`DOC-REQ-008_Acceptance_Criteria.xlsx`.

## 9. Truy xuất nguồn gốc
Trỏ từ `DOC-REQ-006` tới `DOC-TEST-003` (Test Case).

## 10. Cách kiểm tra
Kiểm tra cấu trúc Given-When-Then.

## 11. Ngoại lệ
Checklist ngắn đối với các thay đổi giao diện đơn giản.

## 12. Ví dụ
- Hợp lệ: "Given người dùng nhập mật khẩu dưới 8 ký tự, When nhấn Đăng ký, Then thông báo lỗi màu đỏ 'Mật khẩu phải từ 8 ký tự trở lên' xuất hiện."
- Không hợp lệ: "Đăng ký phải chạy ngon lành."

## 13. Tài liệu liên quan
`DOC-REQ-006`, `DOC-TEST-003`.

## 14. Bằng chứng cần thiết
Logic validation trên frontend/backend.

## 15. Giới hạn đã biết
Không có.
