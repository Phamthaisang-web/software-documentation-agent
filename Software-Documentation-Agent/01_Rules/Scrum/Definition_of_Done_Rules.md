# RULE-SCRUM-015: Definition of Done Rules

- **Mã quy tắc**: `RULE-SCRUM-015`
- **Tên quy tắc**: Definition of Done Commitment and Quality Standard Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định tiêu chuẩn chất lượng bắt buộc của Definition of Done (DoD) — cam kết chính thức của Increment theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-014`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Artifact Commitment: Definition of Done)

## 4. Đầu vào bắt buộc
Tiêu chuẩn chất lượng tổ chức, yêu cầu kiểm thử tự động, chuẩn code review.

## 5. Cấu trúc trường bắt buộc
Phạm vi áp dụng DoD, Chuẩn mã nguồn & phong cách code, Yêu cầu kiểm thử tự động (Unit/Integration Test Coverage), Tiêu chuẩn Code Review, Tài liệu hóa đầy đủ, Tiêu chuẩn triển khai và xác minh.

## 6. Quy tắc nội dung
1. Definition of Done là mô tả hình thức về trạng thái của Increment khi nó đáp ứng đầy đủ các biện pháp chất lượng cần thiết cho sản phẩm.
2. Thời điểm một PBI đáp ứng Definition of Done, một **Increment** được sinh ra.
3. Nếu một PBI không đáp ứng Definition of Done, nó KHÔNG ĐƯỢC coi là một phần của Increment, không được phát hành và không được trình diễn tại Sprint Review (phải đưa lại về Product Backlog).
4. Nếu tổ chức đã có DoD cấp doanh nghiệp, Scrum Team phải kế thừa và có thể làm cho nó nghiêm ngặt hơn.
5. Không hạ thấp tiêu chuẩn DoD trong quá trình chạy Sprint để cố tình "hoàn thành" công việc.

## 7. Tiêu chí chất lượng
Các tiêu chí trong DoD phải đo đếm và kiểm tra được (Automated checks).

## 8. Quy tắc đặt tên
`DOC-SCRUM-014_Definition_of_Done.docx`.

## 9. Truy xuất nguồn gốc
Kiểm chứng trực tiếp cho `DOC-SCRUM-015` (Increment) và `DOC-TEST-007` (Code Review Checklist).

## 10. Cách kiểm tra
Kiểm tra sự tồn tại của tiêu chuẩn kiểm thử và tiêu chuẩn mã nguồn trong DoD.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: DoD quy định: Mã nguồn được review bởi ít nhất 1 peer, Unit test pass 100%, Code coverage >= 80%, Deploy thành công lên Staging.
- Không hợp lệ: Tính năng còn bug nghiêm trọng nhưng vẫn đánh dấu Done.

## 13. Tài liệu liên quan
`DOC-SCRUM-015`, `DOC-TEST-007`.

## 14. Bằng chứng cần thiết
Văn bản DoD được thống nhất bởi Scrum Team.

## 15. Giới hạn đã biết
Không có.
