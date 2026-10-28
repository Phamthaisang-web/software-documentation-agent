# RULE-ARCH-006: UI/UX Specification Rules

- **Mã quy tắc**: `RULE-ARCH-006`
- **Tên quy tắc**: UI/UX Structure and Component Specification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Dặc tả cấu trúc màn hình, thành phần giao diện người dùng và luồng điều hướng của ứng dụng.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-006`.

## 3. Nguồn tiêu chuẩn
- ISO 9241-210:2019 (Human-centred design for interactive systems)

## 4. Đầu vào bắt buộc
Danh mục màn hình/trang, luồng điều hướng người dùng, danh sách component giao diện.

## 5. Cấu trúc trường bắt buộc
Nguyên tắc thiết kế & Style guide, Danh mục màn hình (Sitemap), Luồng điều hướng, Đặc tả component UI, Quy chuẩn Responsive & Khả năng tiếp cận (Accessibility - a11y).

## 6. Quy tắc nội dung
1. Dựa trên các trang/views/components thực tế trong mã nguồn Frontend (React, Vue, Angular, Mobile).
2. Mô tả rõ trạng thái của component: Default, Hover, Active, Disabled, Loading, Error.
3. Không tự tạo thiết kế màn hình không khớp với logic nghiệp vụ.

## 7. Tiêu chí chất lượng
Các tương tác người dùng được mô tả mạch lạc.

## 8. Quy tắc đặt tên
`DOC-ARCH-006_UI_UX_Specification.docx`.

## 9. Truy xuất nguồn gốc
Hiện thực hóa `DOC-REQ-005` (Use Cases) cho giao diện.

## 10. Cách kiểm tra
Kiểm tra đối chiếu với danh mục thư mục components/views trong frontend.

## 11. Ngoại lệ
Dự án thuần Backend/API (Headless) không cần tài liệu này (`is_optional: true`).

## 12. Ví dụ
- Hợp lệ: Nút "Thanh toán": Trạng thái Loading hiển thị spinner và disable click.
- Không hợp lệ: Mô tả chung chung "giao diện đẹp mắt".

## 13. Tài liệu liên quan
`DOC-REQ-005`, `DOC-DEL-010`.

## 14. Bằng chứng cần thiết
Source code components hoặc Figma link (nếu có).

## 15. Giới hạn đã biết
Không thể tự tạo mockups đồ họa cao cấp nếu không có design assets.
