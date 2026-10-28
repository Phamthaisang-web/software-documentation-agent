# RULE-TEST-007: Code Review Checklist Rules

- **Mã quy tắc**: `RULE-TEST-007`
- **Tên quy tắc**: Code Review Checklist and Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định danh mục kiểm tra mã nguồn (Code Review Checklist) nhằm đảm bảo an toàn bảo mật OWASP, hiệu năng và chất lượng mã trước khi merge.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-007`.

## 3. Nguồn tiêu chuẩn
- OWASP Secure Coding Practices
- Clean Code Standards

## 4. Đầu vào bắt buộc
Các tiêu chí kiểm tra: Cú pháp, phong cách, bảo mật, hiệu năng, kiểm thử tự động.

## 5. Cấu trúc trường bắt buộc
Các danh mục kiểm tra: Quy chuẩn mã nguồn, Kiểm soát an toàn bảo mật (OWASP), Quản lý tài nguyên & Hiệu năng, Độ bao phủ kiểm thử, Quy tắc thẩm định của Reviewer.

## 6. Quy tắc nội dung
1. Phải quy định rõ: Checklist là bộ tiêu chí hướng dẫn đánh giá, KHÔNG PHẢI là bằng chứng rằng code đã được review (phải có PR approvals thực tế trên GitHub/GitLab).
2. Kiểm tra các lỗi phổ biến: SQL Injection, Hardcoded secrets, Unhandled Promise rejections, Memory leaks.

## 7. Tiêu chí chất lượng
Checklist có thể áp dụng trực tiếp vào PR template của dự án.

## 8. Quy tắc đặt tên
`DOC-TEST-007_Code_Review_Checklist.md`.

## 9. Truy xuất nguồn gốc
Gắn liền với `DOC-SCRUM-014` (Definition of Done).

## 10. Cách kiểm tra
Kiểm tra các mục kiểm tra bảo mật trong checklist.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Checklist yêu cầu xác minh không có credential nhạy cảm trong code diff.
- Không hợp lệ: Tự tuyên bố "Code đã được review 100%" khi repo không có bất kỳ pull request approval nào.

## 13. Tài liệu liên quan
`DOC-SCRUM-014`.

## 14. Bằng chứng cần thiết
Pull request comments hoặc template file `.github/pull_request_template.md`.

## 15. Giới hạn đã biết
Không có.
