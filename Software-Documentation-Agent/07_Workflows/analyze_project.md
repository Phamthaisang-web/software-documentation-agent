# Workflow A — Phân Tích Dự Án (Project Analysis Workflow)

## 1. Mục Đích
Khảo sát và trích xuất thông tin kỹ thuật từ repository hiện có để lập Hồ sơ dự án (`project_profile.yaml`).

## 2. Các Bước Thực Hiện
1. **Bước 1: Quét cấu trúc workspace**:
   - Chạy lệnh `python 09_Tools/cli.py analyze --target <dir>`.
   - Bỏ qua các thư mục `node_modules`, `.git`, `venv`, `dist`, `build`.
2. **Bước 2: Thu thập bằng chứng**:
   - Trích xuất công nghệ, thư viện, framework.
   - Trích xuất bảng dữ liệu và quan hệ từ migrations/schema.
   - Trích xuất endpoints từ router/controllers.
   - Tìm kiếm test suites và log thực thi kiểm thử.
3. **Bước 3: Lập Project Profile**:
   - Điền dữ liệu vào `project_profile.yaml` tuân thủ `project_profile.schema.json`.
   - Gán cờ `VERIFIED`, `INFERRED`, `UNKNOWN`, `CONFLICT`.
4. **Bước 4: Đề xuất bộ tài liệu phù hợp**:
   - Lọc danh mục tài liệu cần thiết từ 59 tài liệu trong registry.
   - Đánh dấu tài liệu bắt buộc và tài liệu tùy chọn.
5. **Bước 5: Báo cáo kết quả**:
   - Hiển thị tóm tắt cho người dùng và các câu hỏi cần làm rõ nếu có `CONFLICT` hoặc thiếu thông tin nghiêm trọng.
