# Source Validation Rules — Quy Tắc Thẩm Định Nguồn Tham Chiếu

Tài liệu này quy định việc thẩm tra tính hợp lệ của các nguồn tiêu chuẩn và chính sách được viện dẫn.

---

## 1. Tiêu Chí Kiểm Tra Nguồn
1. **Kiểm tra tồn tại**: Mọi mã nguồn `related_standards` được trích dẫn trong tài liệu hoặc registry phải tồn tại thật trong `config/standards_registry.yaml`.
2. **Kiểm tra trạng thái xác minh**:
   - Chỉ các nguồn có trạng thái `VERIFIED_OFFICIAL` hoặc `VERIFIED_AUTHORITATIVE` mới được sử dụng làm căn cứ cho các quy tắc `OFFICIAL_REQUIREMENT`.
   - Các nguồn `USER_PROVIDED` và `INTERNAL_POLICY` chỉ áp dụng trong phạm vi dự án, không được gắn nhãn tiêu chuẩn quốc tế.
3. **Kiểm tra liên kết URL**: URL phải trỏ tới đúng tên miền chính thức của tổ chức tiêu chuẩn (ví dụ: `scrumguides.org`, `iso.org`, `spec.openapis.org`).
