# RULE-SCRUM-017: Sprint Deliverables Rules

- **Mã quy tắc**: `RULE-SCRUM-017`
- **Tên quy tắc**: Increment Deliverables Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Ghi nhận và kiểm chứng Increment thực tế hoàn thành sau Sprint đáp ứng Definition of Done.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-015`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Increment definition)

## 4. Đầu vào bắt buộc
Phiên bản build/package có thể chạy được, danh sách PBIs đã xác minh đạt DoD.

## 5. Cấu trúc trường bắt buộc
Increment Version/Tag, Danh sách PBIs đạt DoD, Tham chiếu mã nguồn/commit hash, Bằng chứng kiểm thử nghiệm thu, Trạng thái sẵn sàng phát hành.

## 6. Quy tắc nội dung
1. Increment phải ở trạng thái có thể sử dụng được (usable), bất kể Product Owner có quyết định phát hành nó ra thực tế hay không.
2. Mọi phần tính năng trong Increment phải đáp ứng đầy đủ Definition of Done.
3. Không tự tạo thông tin phát hành khi mã nguồn chưa build thành công hoặc test fail.

## 7. Tiêu chí chất lượng
Có commit hash hoặc artifact URL cụ thể.

## 8. Quy tắc đặt tên
`DOC-SCRUM-015_Increment_Deliverables.xlsx`.

## 9. Truy xuất nguồn gốc
Cơ sở để lập `DOC-DEL-009` (Release Notes).

## 10. Cách kiểm tra
Kiểm tra đối chiếu với `DOC-SCRUM-014` (DoD).

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Increment `v1.2.0` (commit `a1b2c3d`) hoàn thành 4 PBIs và pass toàn bộ test suite.
- Không hợp lệ: Ghi nhận bàn giao trong khi mã nguồn đang bị lỗi cú pháp không build được.

## 13. Tài liệu liên quan
`DOC-SCRUM-014`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Docker image tag, artifact repository hoặc Git release tag.

## 15. Giới hạn đã biết
Không có.
