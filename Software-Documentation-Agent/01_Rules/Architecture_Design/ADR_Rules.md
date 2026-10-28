# RULE-ARCH-010: Architecture Decision Record Rules

- **Mã quy tắc**: `RULE-ARCH-010`
- **Tên quy tắc**: Architecture Decision Record (ADR) Integrity Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Ghi nhận bối cảnh, quyết định, các phương án cân nhắc, hệ quả và trạng thái của một quyết định kiến trúc quan trọng theo chuẩn Michael Nygard / ISO 42010.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-010`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 (Architecture decisions & rationale)
- ADR Standard format (Michael Nygard)

## 4. Đầu vào bắt buộc
Bối cảnh vấn đề, quyết định được chọn, các phương án đã cân nhắc, hệ quả (tích cực và tiêu cực).

## 5. Cấu trúc trường bắt buộc
ADR ID & Title, Status (Proposed / Accepted / Deprecated / Superseded), Context, Considered Options, Decision Outcome & Rationale, Consequences (Positive & Negative).

## 6. Quy tắc nội dung
1. Mỗi quyết định kiến trúc lớn phải có một bản ghi ADR riêng.
2. BẮT BUỘC phải nêu cả hệ quả tiêu cực (Trade-offs / Negatives) của quyết định, không có giải pháp nào là hoàn hảo tuyệt đối.
3. Không tự tạo quyết định là "Accepted" khi chưa có sự phê chuẩn của Tech Lead / Architect.

## 7. Tiêu chí chất lượng
Nêu bật lý do chọn và lý do loại bỏ các phương án khác.

## 8. Quy tắc đặt tên
`DOC-ARCH-010_ADR_{NUMBER}_{Title}.md`.

## 9. Truy xuất nguồn gốc
Hậu thuẫn cho các lựa chọn trong `DOC-ARCH-001` (SAD) và `DOC-DEL-005` (Decision Log).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của phần `Consequences` và `Considered Options`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Quyết định sử dụng PostgreSQL thay vì MongoDB vì yêu cầu tính toàn vẹn giao dịch ACID cao. Hệ quả tiêu cực: Khó mở rộng ngang hơn NoSQL."
- Không hợp lệ: Chỉ ghi "Chọn PostgreSQL vì nó tốt" mà không nêu bối cảnh và hệ quả.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-DEL-005`.

## 14. Bằng chứng cần thiết
Thảo luận kỹ thuật hoặc ghi chú trong repository.

## 15. Giới hạn đã biết
Không có.
