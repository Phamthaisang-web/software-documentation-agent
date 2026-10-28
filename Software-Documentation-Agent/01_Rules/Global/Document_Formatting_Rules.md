# RULE-GLOB-004: Document Formatting Rules (Quy Tắc Định Dạng Tài Liệu)

- **Mã quy tắc**: `RULE-GLOB-004`
- **Tên quy tắc**: Document Formatting and Template Preservation Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Đảm bảo khi xuất bản tài liệu trên các mẫu biểu (DOCX, XLSX, PPTX, MD, YAML, MMD), định dạng gốc, thẩm mỹ và tính toàn vẹn kỹ thuật được giữ nguyên vẹn.

## 2. Phạm vi áp dụng
Mọi thao tác render và xuất bản tài liệu ra thư mục `output/`.

## 3. Nguồn tiêu chuẩn
- Microsoft OpenXML Specification (ISO/IEC 29500)
- OpenAPI Specification 3.1.0
- Mermaid.js Syntax Specification

## 4. Đầu vào bắt buộc
Tệp mẫu nguồn từ `03_Templates/` hoặc do người dùng cung cấp.

## 5. Cấu trúc bắt buộc
- **DOCX**: Giữ nguyên Styles, Header, Footer, Table Grid, Font Family.
- **XLSX**: Giữ nguyên Worksheets, Header color (#1F497D), Freeze Panes, AutoFilter, Formulas.
- **Mermaid**: Cú pháp sơ đồ hợp lệ, lưu trữ mã nguồn để người dùng chỉnh sửa được.

## 6. Quy tắc nội dung
1. Với Word (DOCX): Thay thế placeholder (ví dụ `{{PROJECT_NAME}}`), không xóa bảng, không làm lệch trang.
2. Với Excel (XLSX): Không ghi đè công thức tính toán (`SUM`, `AVERAGE`) bằng giá trị tĩnh.
3. Với Markdown / YAML / JSON: Cú pháp hợp lệ, validate được bằng parser tương ứng.
4. Không được tuyên bố giữ nguyên định dạng nếu chưa chạy kiểm tra tệp thực tế.

## 7. Tiêu chí chất lượng
Các tệp sinh ra mở được bằng Microsoft Office / LibreOffice / VS Code mà không có cảnh báo corrupt.

## 8. Quy tắc đặt tên
Tên tệp không dấu, sử dụng dấu gạch dưới: `{DOC_ID}_{Document_Name}.{ext}`.

## 9. Truy xuất nguồn gốc
Lưu kèm tệp `{DOC_ID}.meta.yaml` ghi nhận template gốc được sử dụng.

## 10. Cách kiểm tra
Chạy bài kiểm thử `test_template_preservation.py`.

## 11. Ngoại lệ
Nếu định dạng tệp không được hỗ trợ xử lý sâu (ví dụ binary proprietary), phải ghi nhận rõ hạn chế.

## 12. Ví dụ
- Hợp lệ: Giữ nguyên công thức `=SUM(E2:E20)` trong bảng chấm công / burndown Excel.
- Không hợp lệ: Xóa công thức và gõ cứng số `50`.

## 13. Tài liệu liên quan
Tất cả các tài liệu định dạng `.docx`, `.xlsx`, `.md`, `.yaml`, `.mmd`.

## 14. Bằng chứng cần thiết
Tệp đầu ra có thể mở và đọc thành công.

## 15. Giới hạn đã biết
Không thể kiểm tra trực quan giao diện đồ họa nếu môi trường thiếu Word viewer; kiểm tra cấu trúc XML bên trong.
