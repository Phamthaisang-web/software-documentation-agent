# Template Validation Rules — Quy Tắc Thẩm Định Mẫu Tài Liệu

Tài liệu này quy định việc kiểm tra các tệp mẫu và bản ghi template trong hệ thống.

---

## 1. Tiêu Chí Kiểm Tra Bản Ghi Template
1. **Kiểm tra file thực tế**: File template được trỏ tới bởi `file_path` trong `template_registry.yaml` phải thực sự tồn tại trên đĩa cứng; nếu không tìm thấy tệp, trạng thái bản ghi bắt buộc phải là `MISSING`.
2. **Quy tắc phân loại trung thực**:
   - Mẫu do hệ thống AI khởi tạo bắt buộc phải có `origin_type: GENERATED_TEMPLATE` hoặc `status: GENERATED_TEMPLATE`.
   - Tuyệt đối KHÔNG gán nhãn `OFFICIAL_SOURCE` cho mẫu do AI tạo.
   - Khi người dùng cung cấp mẫu, chuyển trạng thái sang `USER_PROVIDED`.
3. **Kiểm tra tính toàn vẹn của tệp mẫu**:
   - Tệp `.docx` phải mở được và đọc được cấu trúc XML chuẩn.
   - Tệp `.xlsx` phải mở được và đọc được các sheets bằng `openpyxl`.
   - Tệp `.yaml` / `.json` phải parse được không có syntax error.
   - Tệp `.mmd` phải là cú pháp Mermaid hợp lệ.
