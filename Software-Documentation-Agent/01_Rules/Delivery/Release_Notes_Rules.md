# RULE-DEL-009: Release Notes Rules

- **Mã quy tắc**: `RULE-DEL-009`
- **Tên quy tắc**: Release Documentation and Semantic Versioning Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Công bố các tính năng mới, sửa lỗi, cải tiến kỹ thuật, thay đổi đột phá (Breaking changes) và hướng dẫn nâng cấp của phiên bản phát hành.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-009`.

## 3. Nguồn tiêu chuẩn
- Keep a Changelog standard & SemVer 2.0.0

## 4. Đầu vào bắt buộc
Số hiệu phiên bản (`version`), Ngày phát hành (`release_date`), Danh sách tính năng mới, Lỗi đã sửa, Thay đổi có thể gây lỗi hệ thống cũ (Breaking changes).

## 5. Cấu trúc trường bắt buộc
Tiêu đề phiên bản & Ngày phát hành, Tóm tắt phát hành, Tính năng mới (Added), Cải tiến (Changed), Sửa lỗi (Fixed), Thay đổi đột phá & Hướng dẫn di chuyển dữ liệu (Breaking Changes & Migration), Lỗi đã biết (Known Issues).

## 6. Quy tắc nội dung
1. Phân biệt rõ ràng giữa thay đổi ĐÃ XÁC MINH (Verified in build) và thay đổi DỰ KIẾN (Planned).
2. Bắt buộc phải có mục "Breaking Changes" nếu có thay đổi cấu trúc API hoặc DB làm ảnh hưởng người dùng cũ.
3. Liệt kê các lỗi còn tồn tại (Known Issues) để người dùng chủ động ứng phó.

## 7. Tiêu chí chất lượng
Mọi bug fix phải tham chiếu tới Bug ID tương ứng.

## 8. Quy tắc đặt tên
`DOC-DEL-009_Release_Notes_{VERSION}.md`.

## 9. Truy xuất nguồn gốc
Tổng hợp từ `DOC-REQ-007` (RTM), `DOC-SCRUM-015` (Increment), `DOC-TEST-004`.

## 10. Cách kiểm tra
Kiểm tra sự phù hợp với commit git tag tương ứng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "v1.2.0 (2026-10-29): Added: Tìm kiếm theo mã vận đơn. Fixed: BUG-002 lỗi tràn bộ nhớ khi xuất file Excel."
- Không hợp lệ: Ghi chung chung "Cập nhật ứng dụng và sửa một số lỗi vặt."

## 13. Tài liệu liên quan
`DOC-SCRUM-015`, `DOC-TEST-004`.

## 14. Bằng chứng cần thiết
Git commit log và tag repository.

## 15. Giới hạn đã biết
Không có.
