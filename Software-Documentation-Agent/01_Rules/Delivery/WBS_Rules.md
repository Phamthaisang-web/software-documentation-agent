# RULE-DEL-002: Work Breakdown Structure Rules

- **Mã quy tắc**: `RULE-DEL-002`
- **Tên quy tắc**: WBS Decomposition and 100% Rule
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc phân rã toàn bộ phạm vi dự án thành các gói công việc quản lý được theo ISO 21500.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-002`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 & PMI WBS Practice Standard

## 4. Đầu vào bắt buộc
Danh mục kết quả bàn giao, các gói công việc chi tiết.

## 5. Cấu trúc trường bắt buộc
Mã WBS (WBS Code dạng 1.1, 1.1.1), Cấp độ (Level), Tên gói công việc, Mô tả công việc, Kết quả bàn giao (Deliverable), Tiêu chí hoàn thành.

## 6. Quy tắc nội dung
1. Tuân thủ **Quy tắc 100% (100% Rule)**: WBS phải bao gồm toàn bộ 100% công việc được định nghĩa trong phạm vi dự án, không thừa và không thiếu.
2. Cấp thấp nhất của WBS là Gói công việc (Work Package), có thể gán người chịu trách nhiệm và ước tính chi phí, thời gian.

## 7. Tiêu chí chất lượng
Mã phân cấp WBS chuẩn xác, không nhảy cóc.

## 8. Quy tắc đặt tên
`DOC-DEL-002_WBS.xlsx`.

## 9. Truy xuất nguồn gốc
Phân rã từ `DOC-PM-002` (Scope Statement).

## 10. Cách kiểm tra
Kiểm tra cấu trúc phân cấp số của `wbs_code`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `1.0 Hệ thống E-Commerce` -> `1.1 Module Giỏ hàng` -> `1.1.1 Xây dựng logic tính thuế`.
- Không hợp lệ: Liệt kê các đầu mục lộn xộn không có cấu trúc phân cấp.

## 13. Tài liệu liên quan
`DOC-PM-002`, `DOC-DEL-001`.

## 14. Bằng chứng cần thiết
Danh mục phạm vi công việc.

## 15. Giới hạn đã biết
Không có.
