# RULE-SCRUM-010: Task Breakdown Rules

- **Mã quy tắc**: `RULE-SCRUM-010`
- **Tên quy tắc**: Work Decomposition and Task Sizing Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định kỹ thuật phân rã PBI thành các tác vụ kỹ thuật cụ thể cho Developers.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-009`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020

## 4. Đầu vào bắt buộc
Parent PBI ID, mô tả công việc kỹ thuật.

## 5. Cấu trúc trường bắt buộc
Task ID, Parent PBI ID, Task Description, Task Type (Frontend/Backend/DB/Testing), Estimate (giờ/points), Status, Assignee.

## 6. Quy tắc nội dung
1. Mỗi tác vụ kỹ thuật phải đủ nhỏ để có thể hoàn thành trong vòng một ngày hoặc vài ngày làm việc.
2. Các task phải gắn trực tiếp với một PBI cha; không tạo task vô định hướng.

## 7. Tiêu chí chất lượng
Mô tả hành động cụ thể (ví dụ: "Viết migration bảng users", không viết "làm database").

## 8. Quy tắc đặt tên
`DOC-SCRUM-009_Task_Breakdown.xlsx`.

## 9. Truy xuất nguồn gốc
Thuộc `DOC-SCRUM-007` (Sprint Backlog).

## 10. Cách kiểm tra
Kiểm tra `parent_pbi_id` phải tồn tại trong danh sách PBIs của Sprint.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `TASK-001` (thuộc `PBI-001`): Tạo endpoint `/api/v1/auth/login` với validation express-validator.
- Không hợp lệ: `TASK-999`: Làm việc chung chung.

## 13. Tài liệu liên quan
`DOC-SCRUM-007`, `DOC-SCRUM-003`.

## 14. Bằng chứng cần thiết
Danh sách task kỹ thuật của nhóm.

## 15. Giới hạn đã biết
Không có.
