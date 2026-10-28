# RULE-DEL-010: User Manual Rules

- **Mã quy tắc**: `RULE-DEL-010`
- **Tên quy tắc**: End-User Guidance and Accessibility Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Hướng dẫn người dùng cuối cách sử dụng các tính năng của phần mềm một cách trực quan, dễ hiểu, từng bước.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-010`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 26511:2018 (Requirements for managers of information for users of software)

## 4. Đầu vào bắt buộc
Kịch bản sử dụng thực tế, vai trò người dùng, thông điệp lỗi thường gặp.

## 5. Cấu trúc trường bắt buộc
Tổng quan hệ thống & Đối tượng độc giả, Bắt đầu sử dụng & Đăng nhập, Hướng dẫn từng bước các tính năng chính, Các thông báo lỗi thường gặp & Xử lý sự cố (FAQ), Kênh hỗ trợ.

## 6. Quy tắc nội dung
1. Ngôn từ hướng tới người dùng cuối, không lạm dụng thuật ngữ kỹ thuật chuyên sâu (developer jargons).
2. Các bước hướng dẫn phải đi kèm hành động cụ thể trên giao diện (ví dụ: "Nhấn nút 'Lưu'", "Chọn ngày trong lịch").
3. Có phần hướng dẫn tự khắc phục lỗi đơn giản (Troubleshooting).

## 7. Tiêu chí chất lượng
Người dùng mới có thể hoàn thành tác vụ cơ bản sau khi đọc tài liệu.

## 8. Quy tắc đặt tên
`DOC-DEL-010_User_Manual.docx`.

## 9. Truy xuất nguồn gốc
Dựa trên `DOC-REQ-003` (Chức năng) và `DOC-ARCH-006` (Giao diện).

## 10. Cách kiểm tra
Kiểm tra tính đầy đủ của các chức năng chính dành cho người dùng.

## 11. Ngoại lệ
Hệ thống API backend không có giao diện người dùng thì thay thế bằng API Documentation.

## 12. Ví dụ
- Hợp lệ: "Để đặt lại mật khẩu: 1. Tại màn hình Đăng nhập, nhấn 'Quên mật khẩu'. 2. Nhập email đã đăng ký..."
- Không hợp lệ: "Hệ thống gọi API POST /auth/forgot-password với body JSON..."

## 13. Tài liệu liên quan
`DOC-REQ-003`, `DOC-ARCH-006`.

## 14. Bằng chứng cần thiết
Giao diện ứng dụng và luồng thao tác thực tế.

## 15. Giới hạn đã biết
Không có.
