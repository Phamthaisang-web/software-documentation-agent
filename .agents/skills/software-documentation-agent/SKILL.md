---
name: software-documentation-agent
description: >-
  Use this skill when the user asks to analyze a software codebase, create, update, or validate technical documentation across Project Management, Requirements, Scrum, Architecture, Testing, and Delivery (59 document types). Supports DOCX, XLSX, Markdown, OpenAPI, and Mermaid formats with strict traceability, template preservation, and official standards conformance (ISO 29148, ISO 42010, ISO 29119, Scrum Guide 2020).
---

# Software Documentation Agent — Native Workspace Skill

Chuyên gia kiến trúc phần mềm, kỹ sư yêu cầu, Scrum Master và kiểm thử chất lượng phần mềm tự động hóa toàn diện quy trình tài liệu hóa dự án.

---

## 1. Các Năng Lực Cốt Lõi
1. **Phân tích dự án (Project Analysis)**: Tự động quét cấu trúc repository, manifest thư viện, migrations, routes và tests để tạo `project_profile.yaml` chuẩn hóa.
2. **Sinh 59 Loại Tài Liệu Kỹ Thuật**: Bao quát 5 nhóm tài liệu:
   - Nhóm A: Quản lý dự án & Yêu cầu (`DOC-PM-001` đến `DOC-REQ-008`).
   - Nhóm B: Scrum Framework (`DOC-SCRUM-001` đến `DOC-SCRUM-017`).
   - Nhóm C: Kiến trúc & Thiết kế (`DOC-ARCH-001` đến `DOC-ARCH-010`).
   - Nhóm D: Kiểm thử & Chất lượng (`DOC-TEST-001` đến `DOC-TEST-008`).
   - Nhóm E: Theo dõi & Bàn giao (`DOC-DEL-001` đến `DOC-DEL-013`).
3. **Bảo tồn định dạng mẫu (Template Preservation)**: Giữ nguyên style heading, bảng biểu Word, công thức Excel và sơ đồ Mermaid có thể chỉnh sửa.
4. **Mạng lưới truy xuất nguồn gốc (Traceability Engine)**: Đảm bảo liên kết hai chiều từ Vision -> Backlog -> Design -> Test Case -> Release Notes.
5. **Thẩm định tự động (Automated Validation)**: Bộ kiểm thử và validator tự động phát hiện vi phạm tiêu chuẩn, thông tin thiếu hoặc mâu thuẫn.

---

## 2. Hướng Dẫn Kích Hoạt Nhanh

### Phân tích dự án hiện tại
```powershell
python Software-Documentation-Agent/09_Tools/cli.py analyze --target .
```

### Tạo một tài liệu đơn lẻ
```powershell
python Software-Documentation-Agent/09_Tools/cli.py generate --doc-id DOC-REQ-001
```

### Tạo trọn bộ tài liệu
```powershell
python Software-Documentation-Agent/09_Tools/cli.py generate-set
```

### Chạy thẩm định hệ thống
```powershell
python Software-Documentation-Agent/09_Tools/cli.py validate
```

### Chạy toàn bộ 40 bài kiểm thử tự động
```powershell
python -m pytest Software-Documentation-Agent/10_Tests -v
```

---

## 3. Tham Chiếu Cấu Trúc
- Toàn bộ mã nguồn, cấu hình, quy tắc và mẫu biểu nằm tại [Software-Documentation-Agent](file:///d:/agenttl1/Software-Documentation-Agent).
- Hướng dẫn chi tiết: [HUONG_DAN_SU_DUNG.md](file:///d:/agenttl1/Software-Documentation-Agent/HUONG_DAN_SU_DUNG.md).
- Danh mục 59 tài liệu: [document_registry.yaml](file:///d:/agenttl1/Software-Documentation-Agent/config/document_registry.yaml).
- Danh mục tiêu chuẩn chính thức: [standards_registry.yaml](file:///d:/agenttl1/Software-Documentation-Agent/config/standards_registry.yaml).
