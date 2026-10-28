# Workflow B — Tạo Một Tài Liệu (Single Document Generation Workflow)

## 1. Mục Đích
Tạo một tài liệu kỹ thuật đơn lẻ dựa trên `document_id`, mẫu biểu và hồ sơ dự án.

## 2. Các Bước Thực Hiện
1. **Bước 1: Nhận diện mã tài liệu**:
   - Nhận `document_id` (ví dụ: `DOC-REQ-001`, `DOC-ARCH-005`).
2. **Bước 2: Nạp cấu hình & Quy tắc**:
   - Đọc bản ghi tài liệu từ `config/document_registry.yaml`.
   - Nạp tệp Rules tương ứng trong `01_Rules/`.
   - Nạp tiêu chuẩn liên quan từ `config/standards_registry.yaml`.
3. **Bước 3: Nạp mẫu tài liệu (Template)**:
   - Ưu tiên mẫu `USER_PROVIDED` nếu người dùng đã đặt trong workspace.
   - Nếu chưa có, sử dụng mẫu `GENERATED_TEMPLATE` trong `03_Templates/`.
4. **Bước 4: Thu thập dữ liệu từ Project Profile**:
   - Trích xuất các trường dữ liệu cần thiết từ `project_profile.yaml`.
5. **Bước 5: Render nội dung & Giữ định dạng**:
   - Thay thế placeholder, điền bảng dữ liệu, giữ nguyên công thức Excel, style Word và mã nguồn Mermaid.
6. **Bước 6: Thẩm định & Lưu trữ**:
   - Chạy kiểm tra chất lượng tệp.
   - Lưu vào `output/` kèm tệp metadata `{DOC_ID}.meta.yaml`.
