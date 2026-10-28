# Output File Validation Rules — Quy Tắc Thẩm Định Tệp Đầu Ra

Tài liệu này quy định việc kiểm tra chất lượng tệp vật lý được xuất bản vào thư mục `output/`.

---

## 1. Tiêu Chí Thẩm Định Tệp Xuất Bản
1. **Kiểm tra sự tồn tại và kích thước**: Tệp phải tồn tại trên đĩa và có kích thước > 0 bytes (không được là tệp rỗng).
2. **Khả năng đọc và phân tích cú pháp**:
   - Tệp `.docx`: Thư viện `docx.Document()` đọc được các đoạn văn và bảng biểu thành công.
   - Tệp `.xlsx`: Thư viện `openpyxl.load_workbook()` mở được không có exception và đọc được các ô dữ liệu.
   - Tệp `.md`: Đọc được nội dung định dạng UTF-8, không chứa ký tự hỏng.
   - Tệp `.yaml`: `yaml.safe_load()` phân tích thành công.
   - Tệp `.mmd`: Bắt đầu bằng chỉ thị Mermaid hợp lệ (`flowchart`, `erDiagram`, `sequenceDiagram`).
3. **Kiểm tra Tệp Metadata Đồng Hành**: Mỗi tệp tài liệu xuất bản chính phải có tệp `{DOC_ID}.meta.yaml` đi kèm tuân thủ `config/document_metadata.schema.json`.
