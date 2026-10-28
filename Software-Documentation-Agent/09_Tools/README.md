# 09_Tools — Công Cụ Thực Thi Của Documentation Agent

Thư mục này chứa toàn bộ các công cụ Python có thể thực thi trực tiếp từ dòng lệnh để phân tích dự án, sinh tài liệu, kiểm tra tính truy xuất và thẩm định hệ thống.

---

## 1. Danh Sách Công Cụ
- `cli.py`: Giao diện dòng lệnh hợp nhất (Unified CLI) cho người dùng và Agent.
- `project_analyzer.py`: Engine quét mã nguồn, nhận diện kiến trúc, schema, routes và tạo `project_profile.yaml`.
- `document_generator.py`: Engine sinh tài liệu dựa trên mẫu biểu DOCX, XLSX, MD, YAML, Mermaid với khả năng giữ nguyên định dạng.
- `traceability_engine.py`: Engine quản lý và kiểm tra đồ thị truy xuất nguồn gốc hai chiều giữa các tài liệu.
- `sprint_validator.py`: Engine kiểm tra tính tuân thủ các ràng buộc thời lượng và nguyên tắc cốt lõi của Scrum Guide 2020.
- `validator.py`: Engine thẩm định toàn diện các registry, mẫu biểu, tiêu chuẩn và tệp đầu ra.

---

## 2. Hướng Dẫn Sử Dụng Nhanh

### 2.1. Phân tích một dự án phần mềm
```bash
python 09_Tools/cli.py analyze --target <duong_dan_source_code>
```

### 2.2. Tạo một tài liệu kỹ thuật cụ thể
```bash
python 09_Tools/cli.py generate --doc-id DOC-REQ-001
```

### 2.3. Tạo trọn bộ 59 tài liệu
```bash
python 09_Tools/cli.py generate-set
```

### 2.4. Chạy thẩm định hệ thống tài liệu
```bash
python 09_Tools/cli.py validate
```

### 2.5. Kiểm tra trạng thái xác minh các nguồn tiêu chuẩn
```bash
python 09_Tools/cli.py verify-sources
```
