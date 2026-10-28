# RULE-PM-002: Project Scope Statement Rules

- **Mã quy tắc**: `RULE-PM-002`
- **Tên quy tắc**: Scope Definition and Boundary Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định phương pháp xác định ranh giới phạm vi dự án, phân định rõ những gì thuộc phạm vi và ngoài phạm vi.

## 2. Phạm vi áp dụng
Tài liệu `DOC-PM-002`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6.3 (Scope management)
- ISO/IEC/IEEE 29148:2018

## 4. Đầu vào bắt buộc
- Danh mục công việc trong phạm vi (`in_scope`)
- Danh mục loại trừ ngoài phạm vi (`out_of_scope`)
- Kết quả bàn giao chính (`deliverables`)

## 5. Cấu trúc trường bắt buộc
Mô tả phạm vi, Kết quả bàn giao chính, Tiêu chí chấp nhận, Loại trừ (Out of Scope), Ràng buộc và Giả định.

## 6. Quy tắc nội dung
1. Bắt buộc phải có mục "Ngoài phạm vi" (Out of Scope) để chống phình phạm vi (Scope Creep).
2. Các kết quả bàn giao phải cụ thể, có thể nghiệm thu được.
3. Không ngầm định các tính năng không được liệt kê là nằm trong phạm vi.

## 7. Tiêu chí chất lượng
Ranh giới rõ ràng, không có sự nhập nhằng giữa in-scope và out-of-scope.

## 8. Quy tắc đặt tên
`DOC-PM-002_Project_Scope_Statement.docx`.

## 9. Truy xuất nguồn gốc
Phải trỏ tới `DOC-REQ-001` (SRS) và `DOC-DEL-002` (WBS).

## 10. Cách kiểm tra
Kiểm tra trường `out_of_scope` không được rỗng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Trong phạm vi: Đăng nhập bằng Email/Password. Ngoài phạm vi: Đăng nhập sinh trắc học và SSO Google trong Phase 1."
- Không hợp lệ: "Hệ thống bao gồm mọi chức năng người dùng mong muốn."

## 13. Tài liệu liên quan
`DOC-PM-001`, `DOC-REQ-001`, `DOC-DEL-002`.

## 14. Bằng chứng cần thiết
Biên bản thỏa thuận phạm vi.

## 15. Giới hạn đã biết
Không có.
