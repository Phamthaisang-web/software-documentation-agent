# RULE-GLOB-003: Document Registry Rules (Quy Tắc Quản Lý Danh Mục Tài Liệu)

- **Mã quy tắc**: `RULE-GLOB-003`
- **Tên quy tắc**: Document Registry Management and Integrity Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Đảm bảo toàn bộ 59 loại tài liệu phần mềm được khai báo đầy đủ, chuẩn xác, không trùng lặp và có cấu trúc liên kết hoàn chỉnh.

## 2. Phạm vi áp dụng
Áp dụng cho tệp trung tâm `config/document_registry.yaml`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Project Governance)
- ISO/IEC/IEEE 29148:2018 (Information Items)

## 4. Đầu vào bắt buộc
Tệp cấu hình `config/document_registry.yaml`.

## 5. Cấu trúc trường bắt buộc
Mỗi bản ghi tài liệu phải có: `document_id`, `official_name`, `group`, `purpose`, `applicability`, `required_inputs`, `output_formats`, `rule_references`, `preferred_template_id`, `related_standards`, `required_sections`, `validation_profile`.

## 6. Quy tắc nội dung
1. Tuyệt đối không trùng lặp `document_id`.
2. Đầy đủ cả 5 nhóm tài liệu (Nhóm A: Quản lý & Yêu cầu, Nhóm B: Scrum, Nhóm C: Kiến trúc & Thiết kế, Nhóm D: Kiểm thử & Chất lượng, Nhóm E: Bàn giao & Theo dõi).
3. Đủ tối thiểu 59 loại tài liệu theo quy định.
4. Mọi `preferred_template_id` phải tồn tại trong `template_registry.yaml`.
5. Mọi `rule_references` phải trỏ tới tệp Rules thực tế tồn tại trong `01_Rules/`.
6. Mọi `related_standards` phải tồn tại trong `standards_registry.yaml`.

## 7. Tiêu chí chất lượng
100% tài liệu vượt qua kiểm tra JSON schema `document_record.schema.json`.

## 8. Quy tắc mã định danh
Mã tài liệu phải tuân thủ regex `^DOC-[A-Z]+-[0-9]{3}$`.

## 9. Quy tắc truy xuất nguồn gốc
Trường `dependencies` và `traceability_requirements` phải trỏ tới các `document_id` hợp lệ.

## 10. Cách kiểm tra
Chạy bài kiểm thử `test_document_registry.py`.

## 11. Ngoại lệ
Không có ngoại lệ.

## 12. Ví dụ hợp lệ và không hợp lệ
- **Hợp lệ**: `DOC-REQ-001` trỏ đến `SRS_Rules.md` và `TPL-REQ-001`.
- **Không hợp lệ**: `DOC-REQ-001` trỏ đến `None` hoặc rule file không tồn tại.

## 13. Tài liệu liên quan
59 tài liệu trong hệ thống.

## 14. Bằng chứng cần thiết
Tệp `config/document_registry.yaml`.

## 15. Giới hạn đã biết
Không có.
