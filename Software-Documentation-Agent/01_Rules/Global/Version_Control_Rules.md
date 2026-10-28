# RULE-GLOB-007: Version Control Rules (Quy Tắc Quản Lý Phiên Bản)

- **Mã quy tắc**: `RULE-GLOB-007`
- **Tên quy tắc**: Document Versioning and Change Tracking Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định chuẩn quản lý phiên bản cho toàn bộ tài liệu kỹ thuật nhằm đảm bảo khả năng theo dõi lịch sử và tính nhất quán với mã nguồn.

## 2. Phạm vi áp dụng
Mọi tài liệu được tạo hoặc cập nhật trong hệ thống.

## 3. Nguồn tiêu chuẩn
- Semantic Versioning 2.0.0 (SemVer)
- ISO 21500:2021 (Configuration & Document Management)

## 4. Đầu vào bắt buộc
Trường `version` dạng `MAJOR.MINOR.PATCH`.

## 5. Cấu trúc trường bắt buộc
Bảng lịch sử thay đổi (Changelog / Revision History) ở đầu mỗi tài liệu: `Version`, `Date`, `Author`, `Description of Change`, `Approver`.

## 6. Quy tắc nội dung
1. Phiên bản khởi tạo ban đầu là `1.0.0` (hoặc `0.1.0` nếu là bản nháp).
2. Tăng `MAJOR` khi có thay đổi lớn làm thay đổi cấu trúc hoặc phạm vi cốt lõi.
3. Tăng `MINOR` khi thêm tính năng, phần mới mà không phá vỡ cấu trúc cũ.
4. Tăng `PATCH` khi sửa lỗi chính tả, làm rõ câu từ hoặc sửa định dạng nhỏ.
5. Không sửa đổi nội dung mà giữ nguyên phiên bản cũ.

## 7. Tiêu chí chất lượng
100% tài liệu có lịch sử thay đổi rõ ràng.

## 8. Quy tắc đặt tên
`v{MAJOR}.{MINOR}.{PATCH}`.

## 9. Truy xuất nguồn gốc
Ghi nhận trong metadata `{DOC_ID}.meta.yaml`.

## 10. Cách kiểm tra
Kiểm tra cấu trúc header của tài liệu.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Cập nhật thêm 2 API endpoint -> tăng từ `1.0.0` lên `1.1.0`.
- Không hợp lệ: Thay đổi toàn bộ kiến trúc từ Monolith sang Microservices nhưng vẫn để `1.0.0`.

## 13. Tài liệu liên quan
Tất cả 59 tài liệu.

## 14. Bằng chứng cần thiết
Bảng revision history trong tài liệu.

## 15. Giới hạn đã biết
Không có.
