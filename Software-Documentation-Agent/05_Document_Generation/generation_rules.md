# Document Generation Rules — Quy Tắc Sinh Tài Liệu

Tài liệu này quy định quy trình chuyển đổi từ Hồ sơ dự án (`project_profile.yaml`) và mẫu biểu (`03_Templates/`) thành tài liệu xuất bản hoàn chỉnh.

---

## 1. Nguyên Tắc Sinh Nội Dung
1. **Một Nguồn Chân Lý (Single Source of Truth)**: Toàn bộ dữ liệu (tên dự án, công nghệ, API, requirements, test status) phải lấy trực tiếp từ `project_profile.yaml`.
2. **Không Tự Bịa Đặt**: Trường nào trong profile có giá trị `UNKNOWN` hoặc rỗng thì ghi `TBD` hoặc `Chưa xác định`, không tự điền dữ liệu giả lập.
3. **Tuân Thủ Rules Cụ Thể**: Mỗi tài liệu khi được sinh ra phải nạp tệp Rule tương ứng trong `01_Rules/` để áp dụng các ràng buộc nội dung đặc thù.

## 2. Quy Trình 6 Bước Khi Tạo Một Tài Liệu
1. Tra cứu bản ghi trong `config/document_registry.yaml`.
2. Xác định template tương ứng từ `config/template_registry.yaml`.
3. Tải tệp template gốc (Word, Excel, Markdown, YAML, Mermaid).
4. Thay thế các placeholder kỹ thuật (`{{PROJECT_NAME}}`, `{{VERSION}}`, `{{TABLE_DATA}}`, `{{SECTION_CONTENT}}`).
5. Gắn nhãn phân loại nguồn gốc (`TEMPLATE_ORIGIN: GENERATED_TEMPLATE` hoặc `USER_PROVIDED`).
6. Xuất bản tệp vào thư mục `output/` kèm tệp metadata `.meta.yaml`.
