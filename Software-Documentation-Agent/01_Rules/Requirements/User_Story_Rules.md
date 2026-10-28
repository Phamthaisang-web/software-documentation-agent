# RULE-REQ-006: User Story Rules

- **Mã quy tắc**: `RULE-REQ-006`
- **Tên quy tắc**: Agile User Story Construction Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Đặc tả yêu cầu phần mềm dưới dạng User Story chuẩn Agile theo cấu trúc As a / I want / So that.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-006`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 & Agile Practice Guide

## 4. Đầu vào bắt buộc
Vai trò người dùng, Mong muốn hành động, Giá trị nhận được.

## 5. Cấu trúc trường bắt buộc
Story ID, Title, Persona (As a), Action (I want), Benefit (So that), Priority, Acceptance Criteria Ref.

## 6. Quy tắc nội dung
1. Bắt buộc tuân thủ mẫu 3 thành phần: "Là [vai trò], tôi muốn [hành động], để [giá trị mang lại]".
2. Phải nêu bật được giá trị kinh doanh trong mệnh đề "So that" (không được viết sáo rỗng).
3. Tuân thủ nguyên tắc INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).

## 7. Tiêu chí chất lượng
100% User Stories có tiêu chí chấp nhận đi kèm.

## 8. Quy tắc đặt tên
`DOC-REQ-006_User_Story_Specification.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-REQ-008` (Acceptance Criteria) và `DOC-SCRUM-003` (PBI).

## 10. Cách kiểm tra
Kiểm tra định dạng As a / I want / So that bằng regex.

## 11. Ngoại lệ
Các PBI kỹ thuật nội bộ (Spike, Refactoring) có thể viết dạng Technical Task.

## 12. Ví dụ
- Hợp lệ: "Là Người mua hàng, tôi muốn lọc sản phẩm theo mức giá, để nhanh chóng tìm thấy món đồ phù hợp túi tiền."
- Không hợp lệ: "Tôi muốn làm bộ lọc."

## 13. Tài liệu liên quan
`DOC-REQ-008`, `DOC-SCRUM-003`.

## 14. Bằng chứng cần thiết
Tính năng frontend/backend tương ứng.

## 15. Giới hạn đã biết
Không có.
