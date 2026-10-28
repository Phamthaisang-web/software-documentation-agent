# RULE-ARCH-002: Software Design Description Rules

- **Mã quy tắc**: `RULE-ARCH-002`
- **Tên quy tắc**: Detailed System Design Description Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả chi tiết thiết kế các module, lớp, giao diện lập trình nội bộ và cơ chế xử lý lỗi.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-002` (SDD).

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022

## 4. Đầu vào bắt buộc
Giao diện module, sơ đồ tương tác, cấu trúc dữ liệu nội bộ.

## 5. Cấu trúc trường bắt buộc
Tổng quan thiết kế, Phân rã module, Đặc tả giao diện chi tiết, Luồng tương tác, Chiến lược xử lý lỗi & ngoại lệ.

## 6. Quy tắc nội dung
1. Chi tiết hóa kiến trúc mức cao thành các thành phần code cụ thể (classes, services, repositories).
2. Quy định rõ cơ chế bắt và chuyển đổi ngoại lệ (Exception Handling).

## 7. Tiêu chí chất lượng
Mô tả rõ hợp đồng giao tiếp giữa các module.

## 8. Quy tắc đặt tên
`DOC-ARCH-002_Software_Design_Description.docx`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-ARCH-001` và chi tiết hóa `DOC-REQ-003`.

## 10. Cách kiểm tra
Kiểm tra cấu trúc module phân rã.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Thiết kế module AuthService sử dụng repository pattern với UserRepository interface.
- Không hợp lệ: Mô tả chung chung không nêu tên lớp hay phương thức.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-REQ-003`.

## 14. Bằng chứng cần thiết
Code interfaces, classes, services.

## 15. Giới hạn đã biết
Không có.
