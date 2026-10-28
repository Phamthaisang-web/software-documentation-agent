# RULE-ARCH-007: Component Diagram Rules

- **Mã quy tắc**: `RULE-ARCH-007`
- **Tên quy tắc**: Component Decomposition and Modular Interface Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Mô tả trực quan các thành phần phần mềm (packages, modules, microservices) và mối quan hệ phụ thuộc giữa chúng.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-007`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 & UML 2.5 Component Diagram standard

## 4. Đầu vào bắt buộc
Danh sách components, interfaces công khai, phụ thuộc (dependencies).

## 5. Cấu trúc trường bắt buộc
Danh mục Component, Định nghĩa Interfaces, Mã nguồn sơ đồ Mermaid (`flowchart TD` / `graph TD`), Giải thích phụ thuộc.

## 6. Quy tắc nội dung
1. Sơ đồ phản ánh đúng kiến trúc phân rã module thực tế trong code.
2. Lưu trữ mã nguồn sơ đồ dưới dạng tệp `.mmd` để chỉnh sửa được.
3. Chỉ rõ chiều phụ thuộc (Dependency direction) và giao thức truyền tải (HTTP, gRPC, Queue, Function call).

## 7. Tiêu chí chất lượng
Mã nguồn Mermaid hợp lệ và hiển thị rõ ràng các phân tầng.

## 8. Quy tắc đặt tên
`DOC-ARCH-007_Component_Diagram.mmd`.

## 9. Truy xuất nguồn gốc
Chi tiết hóa `DOC-ARCH-001` (SAD).

## 10. Cách kiểm tra
Kiểm tra cú pháp Mermaid flowchart.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Controller -> Service -> Repository -> Database Driver.
- Không hợp lệ: Mũi tên phụ thuộc lòng vòng không rõ hướng.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-ARCH-002`.

## 14. Bằng chứng cần thiết
Tệp package.json, go.mod hoặc cấu trúc modules.

## 15. Giới hạn đã biết
Không có.
