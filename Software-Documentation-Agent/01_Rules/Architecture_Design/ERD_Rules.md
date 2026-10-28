# RULE-ARCH-004: Entity Relationship Diagram Rules

- **Mã quy tắc**: `RULE-ARCH-004`
- **Tên quy tắc**: ERD Notation and Editable Source Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định tiêu chuẩn biểu diễn sơ đồ thực thể quan hệ (ERD) và lưu trữ mã nguồn sơ đồ để người dùng có thể chỉnh sửa.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-004`.

## 3. Nguồn tiêu chuẩn
- Crow's Foot Notation & Mermaid.js ER Diagram Standard

## 4. Đầu vào bắt buộc
Danh sách thực thể, các thuộc tính, quan hệ (1-1, 1-n, n-n) và tính chất cardinalities.

## 5. Cấu trúc trường bắt buộc
Định nghĩa thực thể, Ma trận quan hệ, Mã nguồn sơ đồ Mermaid (`erDiagram`), Mô tả ý nghĩa từng quan hệ.

## 6. Quy tắc nội dung
1. Sơ đồ phải dựa trên các thực thể và quan hệ có căn cứ từ database schema.
2. BẮT BUỘC lưu trữ mã nguồn sơ đồ dưới dạng tệp `.mmd` hoặc khối mã Mermaid có thể chỉnh sửa, không được chỉ dán ảnh chết (static image).
3. Ký hiệu quan hệ phải chính xác (One-to-One, One-to-Many, Many-to-Many).

## 7. Tiêu chí chất lượng
Mã nguồn Mermaid biên dịch thành công không có lỗi cú pháp.

## 8. Quy tắc đặt tên
`DOC-ARCH-004_Entity_Relationship_Diagram.mmd`.

## 9. Truy xuất nguồn gốc
Ánh xạ 1:1 với `DOC-ARCH-003` (Database Design).

## 10. Cách kiểm tra
Kiểm tra cú pháp `erDiagram` trong file `.mmd`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ:
  ```mermaid
  erDiagram
      USER ||--o{ ORDER : places
      ORDER ||--|{ ORDER_ITEM : contains
  ```
- Không hợp lệ: Chỉ chụp ảnh màn hình và không có mã nguồn sơ đồ.

## 13. Tài liệu liên quan
`DOC-ARCH-003`.

## 14. Bằng chứng cần thiết
Schema DB và tệp Mermaid `.mmd`.

## 15. Giới hạn đã biết
Không có.
