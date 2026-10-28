# RULE-DEL-005: Decision Log Rules

- **Mã quy tắc**: `RULE-DEL-005`
- **Tên quy tắc**: Project Decision Tracking and Rationale Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Ghi nhận các quyết định quản lý và nghiệp vụ quan trọng trong dự án, người ra quyết định và lý do.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-005`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Governance & Change Control)

## 4. Đầu vào bắt buộc
Chủ đề quyết định, nội dung quyết định, người/cấp có thẩm quyền quyết định, lý do.

## 5. Cấu trúc trường bắt buộc
Decision ID, Ngày quyết định, Vấn đề/Chủ đề, Quyết định được đưa ra, Người phê duyệt, Lý do & Các phương án thay thế, Phạm vi ảnh hưởng, Trạng thái.

## 6. Quy tắc nội dung
1. Tuyệt đối không tự bịa đặt các quyết định quan trọng khi chưa có biên bản hoặc sự đồng thuận của người dùng.
2. Ghi nhận rõ ràng căn cứ tại sao quyết định được đưa ra.

## 7. Tiêu chí chất lượng
Quyết định có căn cứ pháp lý hoặc biên bản họp đối chiếu.

## 8. Quy tắc đặt tên
`DOC-DEL-005_Decision_Log.xlsx`.

## 9. Truy xuất nguồn gốc
Tương hỗ với `DOC-ARCH-010` (ADR) và `DOC-DEL-007` (Meeting Minutes).

## 10. Cách kiểm tra
Kiểm tra trường `decision_maker` không được rỗng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `DEC-001`: Lựa chọn dịch vụ AWS thay vì Azure do đội ngũ đã có kinh nghiệm sâu về AWS. Người quyết định: CTO.
- Không hợp lệ: Tự ý ghi "Đã quyết định thay đổi toàn bộ ngôn ngữ lập trình."

## 13. Tài liệu liên quan
`DOC-ARCH-010`, `DOC-DEL-007`.

## 14. Bằng chứng cần thiết
Email hoặc biên bản xác nhận quyết định.

## 15. Giới hạn đã biết
Không có.
