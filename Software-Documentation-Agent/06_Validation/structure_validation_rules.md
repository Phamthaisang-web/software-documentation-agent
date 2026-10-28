# Structure Validation Rules — Quy Tắc Thẩm Định Cấu Trúc

Tài liệu này quy định việc kiểm tra tính đầy đủ về cấu trúc của các tài liệu sinh ra đối chiếu với `required_sections` trong `document_registry.yaml`.

---

## 1. Kiểm Tra Cấu Trúc Bắt Buộc
Mỗi tài liệu sinh ra phải chứa đầy đủ tất cả các đề mục bắt buộc (`required_sections`) được quy định cho loại tài liệu đó trong `config/document_registry.yaml`.

## 2. Tiêu Chí Đánh Giá
- **PASSED**: Toàn bộ các mục bắt buộc đều xuất hiện trong tài liệu và có nội dung tương ứng (không được để tiêu đề rỗng).
- **FAILED (CRITICAL)**: Thiếu bất kỳ đề mục bắt buộc nào được đăng ký trong Registry.
- **WARNING (MAJOR)**: Đề mục có xuất hiện nhưng chỉ chứa placeholder chưa được điền hoặc nội dung quá ngắn (< 1 câu hoàn chỉnh).
