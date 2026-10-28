# RULE-ARCH-003: Database Design Specification Rules

- **Mã quy tắc**: `RULE-ARCH-003`
- **Tên quy tắc**: Database Schema and Data Integrity Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định phương pháp đặc tả cơ sở dữ liệu dựa trên schema, migration, model, index và ràng buộc thực tế trong mã nguồn.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-003`.

## 3. Nguồn tiêu chuẩn
- Relational Database Normalization Standards & ISO/IEC 9075 (SQL)

## 4. Đầu vào bắt buộc
Tệp định nghĩa bảng, kiểu dữ liệu, khóa chính, khóa ngoại, chỉ mục (indexes).

## 5. Cấu trúc trường bắt buộc
Engine CSDL & Phiên bản, Mô hình dữ liệu logic, Đặc tả schema vật lý (Bảng, Cột, Kiểu, Ràng buộc, Giá trị mặc định), Chỉ mục & Tối ưu hóa, Chiến lược migration.

## 6. Quy tắc nội dung
1. Mọi bảng và cột phải được ánh xạ từ tệp schema/migration thật (ví dụ: `schema.prisma`, `migrations/*.sql`, ORM models).
2. Không tự nghĩ ra các bảng hoặc quan hệ không có trong mã nguồn.
3. Ghi rõ các ràng buộc toàn vẹn dữ liệu (Primary Key, Foreign Key, Unique, Check constraints).

## 7. Tiêu chí chất lượng
100% các cột có kiểu dữ liệu (data type) và quy định nullability rõ ràng.

## 8. Quy tắc đặt tên
`DOC-ARCH-003_Database_Design_Specification.docx`.

## 9. Truy xuất nguồn gốc
Phải đồng bộ 100% với sơ đồ `DOC-ARCH-004` (ERD).

## 10. Cách kiểm tra
Kiểm tra tên bảng và cột đối chiếu với schema code.

## 11. Ngoại lệ
Hệ thống NoSQL (MongoDB, DynamoDB) mô tả theo Document Schema / Collection structure.

## 12. Ví dụ
- Hợp lệ: Bảng `users` gồm cột `id UUID PRIMARY KEY`, `email VARCHAR(255) UNIQUE NOT NULL`.
- Không hợp lệ: Mô tả bảng không nêu kiểu dữ liệu hoặc bịa ra bảng không tồn tại.

## 13. Tài liệu liên quan
`DOC-ARCH-004`, `DOC-REQ-003`.

## 14. Bằng chứng cần thiết
Tệp migration hoặc schema file của dự án.

## 15. Giới hạn đã biết
Không có.
