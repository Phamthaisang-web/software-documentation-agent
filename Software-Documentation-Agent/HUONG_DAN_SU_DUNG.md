# Hướng Dẫn Sử Dụng Chi Tiết — Software Documentation Agent

---

## 1. Hệ Thống Có Chức Năng Gì?
**Software Documentation Agent** là hệ thống AI Agent chuyên trách tự động hóa toàn diện quy trình kỹ thuật tài liệu phần mềm:
1. **Khảo sát & Phân tích dự án (Project Analysis)**: Quét toàn bộ repository, tệp cấu hình, migrations, routes, API controllers và kiểm thử để lập Hồ sơ dự án (`project_profile.yaml`).
2. **Quản lý danh mục 59 loại tài liệu chuẩn**: Phủ kín 5 nhóm: Quản lý dự án, Yêu cầu (ISO 29148), Scrum (Scrum Guide 2020), Kiến trúc & Thiết kế (ISO 42010), Kiểm thử (ISO 29119) và Bàn giao (ISO 21500).
3. **Sinh tài liệu đa định dạng**: Hỗ trợ Microsoft Word (`.docx`), Excel (`.xlsx`), Markdown (`.md`), OpenAPI 3.1 (`.yaml`), Mermaid (`.mmd`).
4. **Bảo tồn mẫu tài liệu (Template Preservation)**: Giữ nguyên style heading, bảng biểu, công thức tính toán Excel và mã nguồn sơ đồ có thể chỉnh sửa.
5. **Mạng lưới truy xuất nguồn gốc (Traceability Engine)**: Ràng buộc liên kết hai chiều từ Product Vision -> Backlog -> PBI -> Acceptance Criteria -> Test Case -> Release Notes.
6. **Thẩm định tự động (Automated Validation)**: Bộ kiểm thử và validator tự động phát hiện vi phạm tiêu chuẩn, thông tin thiếu, mâu thuẫn hoặc liên kết đứt gãy.

---

## 2. Những Gì Hệ Thống KHÔNG Thể Tự Xác Nhận (Giới Hạn & Ranh Giới)
Để đảm bảo tính trung thực tuyệt đối (Zero Hallucination), hệ thống tuân thủ nghiêm ngặt các ranh giới:
1. **Không tự bịa đặt kết quả kiểm thử**: Nếu dự án chưa chạy test trong phiên làm việc, báo cáo thực thi bắt buộc ghi nhãn `NOT_EXECUTED`. Agent không bao giờ tự điền kết quả `PASS` giả mạo.
2. **Không tự tạo sự kiện hoặc biên bản họp**: Nếu cuộc họp chưa diễn ra, Agent không tự bịa danh sách người tham gia, ngày họp hay nội dung thảo luận.
3. **Không tự tạo chữ ký hoặc phê duyệt**: Trạng thái tài liệu mới sinh luôn là `DRAFT` cho đến khi có người dùng có thẩm quyền duyệt.
4. **Không tự đưa ra cam kết ngân sách hoặc SLA**: Nếu không có cấu hình hạ tầng hoặc văn bản cam kết, các chỉ số hiệu năng được đánh dấu `TBD`.
5. **Không nhầm lẫn quy định nội bộ thành chuẩn quốc tế**: Story Points, Velocity, Burndown Charts và Definition of Ready (DoR) luôn được đánh dấu là thông lệ bổ trợ tùy chọn (`RECOMMENDATION`), không phải quy định bắt buộc của Scrum Guide.

---

## 3. Cấu Trúc Thư Mục Hệ Thống
```text
Software-Documentation-Agent/
├── README.md                           # Giới thiệu tổng quan hệ thống
├── HUONG_DAN_SU_DUNG.md                # Hướng dẫn sử dụng chi tiết (tệp này)
├── CHANGELOG.md                        # Lịch sử các phiên bản
├── LICENSES_AND_ATTRIBUTIONS.md        # Giấy phép và trích dẫn bản quyền
│
├── config/                             # Cấu hình trung tâm & schema
│   ├── agent_config.yaml               # Cấu hình vận hành Agent
│   ├── document_registry.yaml          # Danh mục 59 loại tài liệu
│   ├── standards_registry.yaml         # Danh mục tiêu chuẩn quốc tế
│   ├── template_registry.yaml          # Danh mục 59 mẫu tài liệu
│   ├── validation_config.yaml          # Ngưỡng và quy tắc thẩm định
│   ├── project_profile.schema.json     # Schema hồ sơ dự án
│   └── document_metadata.schema.json   # Schema metadata tài liệu
│
├── instructions/                       # Chỉ dẫn vận hành cho Agent
│   ├── system_instructions.md
│   ├── workflow_instructions.md
│   ├── source_verification_instructions.md
│   └── output_instructions.md
│
├── 01_Rules/                           # 73 tệp quy tắc chi tiết
│   ├── Global/                         # 11 quy tắc toàn cục
│   ├── Project_Management/             # 3 quy tắc quản lý dự án
│   ├── Requirements/                   # 8 quy tắc kỹ thuật yêu cầu
│   ├── Scrum/                          # 20 quy tắc Scrum chuẩn xác
│   ├── Architecture_Design/            # 10 quy tắc kiến trúc ISO 42010
│   ├── Testing_Quality/                # 8 quy tắc kiểm thử ISO 29119
│   └── Delivery/                       # 13 quy tắc bàn giao & triển khai
│
├── 02_Standards/                       # Hồ sơ tiêu chuẩn kỹ thuật
│   ├── standards_catalog.md
│   ├── official_sources.md
│   ├── source_verification_policy.md
│   └── standards_mapping.yaml
│
├── 03_Templates/                       # 60 tệp mẫu vật lý thực tế
│   ├── Project_Management/             # Mẫu Word, Excel quản lý dự án
│   ├── Requirements/                   # Mẫu SRS, Use Case, RTM, Stories
│   ├── Scrum/                          # Mẫu Backlog, Goals, Sprint records
│   ├── Architecture_Design/            # Mẫu SAD, SDD, DB, ERD, OpenAPI
│   ├── Testing/                        # Mẫu Test Plan, Test Cases, Bugs
│   ├── Delivery/                       # Mẫu Schedule, WBS, Release Notes
│   └── GENERATED_TEMPLATES_NOTICE.md   # Thông cáo bản quyền mẫu
│
├── 04_Project_Analyzer/                # Quy tắc phân tích codebase
├── 05_Document_Generation/             # Quy tắc sinh tài liệu & bảo tồn mẫu
├── 06_Validation/                      # Quy tắc thẩm định chất lượng
├── 07_Workflows/                       # 6 quy trình nghiệp vụ chi tiết
├── 08_Schemas/                         # Bộ JSON Schemas kiểm tra
├── 09_Tools/                           # Bộ công cụ thực thi Python CLI
├── 10_Tests/                           # 40 bài kiểm thử tự động PyTest
├── 11_Examples/                        # Dữ liệu và bộ tài liệu mẫu thực tế
└── output/                             # Thư mục xuất bản tài liệu
```

---

## 4. Cách Cài Đặt và Kích Hoạt

### 4.1. Môi Trường Yêu Cầu
- Hệ điều hành: Windows 10/11, Linux, macOS.
- Python: Phiên bản 3.10 trở lên (đã kiểm nghiệm thành công trên Python 3.11.9).
- Các thư viện Python cần thiết:
  ```bash
  pip install pyyaml jsonschema python-docx openpyxl pytest
  ```

### 4.2. Kích Hoạt Dưới Dạng Antigravity Workspace Skill
Hệ thống đã tự động tích hợp native skill tại:
[`.agents/skills/software-documentation-agent/SKILL.md`](file:///d:/agenttl1/.agents/skills/software-documentation-agent/SKILL.md)
Khi mở workspace trong Google Antigravity, skill sẽ tự động được phát hiện và kích hoạt mỗi khi người dùng yêu cầu phân tích dự án hoặc tạo tài liệu.

---

## 5. Hướng Dẫn Thực Thi Từng Tác Vụ

### 5.1. Phân Tích Dự Án (Project Analysis)
Để quét mã nguồn thư mục hiện tại và tạo hồ sơ dự án:
```powershell
python Software-Documentation-Agent/09_Tools/cli.py analyze --target .
```
Kết quả sẽ lưu tại: `Software-Documentation-Agent/output/Project_Profile/project_profile.yaml`.

### 5.2. Tạo Một Tài Liệu Kỹ Thuật Đơn Lẻ
Để tạo một tài liệu (ví dụ SRS `DOC-REQ-001` hoặc API Spec `DOC-ARCH-005`):
```powershell
python Software-Documentation-Agent/09_Tools/cli.py generate --doc-id DOC-REQ-001
```
Tài liệu được sinh ra trong `output/{Group}/` kèm theo tệp metadata `.meta.yaml`.

### 5.3. Tạo Trọn Bộ 59 Tài Liệu Hoàn Chỉnh
```powershell
python Software-Documentation-Agent/09_Tools/cli.py generate-set
```

### 5.4. Chạy Thẩm Định Hệ Thống Tài Liệu
```powershell
python Software-Documentation-Agent/09_Tools/cli.py validate
```
Báo cáo sẽ được xuất ra dưới 2 dạng:
- Dạng máy đọc được: `output/Validation_Reports/validation_report.json`
- Dạng tài liệu Markdown: `output/Validation_Reports/validation_report.md`

### 5.5. Chạy Toàn Bộ 40 Bài Kiểm Thử Tự Động (PyTest)
```powershell
python -m pytest Software-Documentation-Agent/10_Tests -v
```

---

## 6. Hướng Dẫn Cấu Hình và Mở Rộng Hệ Thống

### 6.1. Cách Thêm Tiêu Chuẩn Mới
1. Mở tệp [standards_registry.yaml](file:///d:/agenttl1/Software-Documentation-Agent/config/standards_registry.yaml).
2. Thêm một block mới tuân thủ cấu trúc:
   ```yaml
   - standard_id: "STD-NEW-CODE"
     official_name: "Tên tiêu chuẩn đầy đủ"
     issuing_organization: "Tổ chức ban hành"
     source_type: "STANDARD"
     url: "https://chinh-thuc.org/standard"
     version: "2026"
     verification_status: "VERIFIED_OFFICIAL"
   ```
3. Khai báo ánh xạ trong [02_Standards/standards_mapping.yaml](file:///d:/agenttl1/Software-Documentation-Agent/02_Standards/standards_mapping.yaml).

### 6.2. Cách Thêm Mẫu Biểu Mới An Toàn
1. Đặt tệp mẫu của tổ chức bạn (ví dụ `Company_SRS_Template.docx`) vào thư mục `03_Templates/Requirements/`.
2. Mở tệp [template_registry.yaml](file:///d:/agenttl1/Software-Documentation-Agent/config/template_registry.yaml).
3. Đăng ký bản ghi mới với `origin_type: USER_PROVIDED` và `status: USER_PROVIDED`.
4. Cập nhật trường `preferred_template_id` trong [document_registry.yaml](file:///d:/agenttl1/Software-Documentation-Agent/config/document_registry.yaml) trỏ tới ID mẫu mới.
5. Hệ thống sẽ tự động sử dụng mẫu của bạn và bảo tồn nguyên vẹn header/footer/styles.

### 6.3. Cách Thêm Quy Tắc Kỹ Thuật Mới (Rules)
1. Tạo tệp markdown mới trong thư mục tương ứng của `01_Rules/` (ví dụ: `01_Rules/Security/Security_Audit_Rules.md`).
2. Viết nội dung tuân thủ đủ 17 mục quy chuẩn (Mục đích, Phạm vi, Đầu vào, Quy tắc nội dung, Tiêu chí chất lượng, Ví dụ, v.v.).
3. Khai báo tên tệp rule trong danh sách `rule_references` của tài liệu liên quan trong `document_registry.yaml`.

---

## 7. Khắc Phục Sự Cố Phổ Biến (Troubleshooting)
1. **Lỗi `UnicodeEncodeError: 'charmap'` trên Windows**:
   - Khắc phục: Đặt biến môi trường `set PYTHONIOENCODING=utf-8` hoặc sử dụng các công cụ trong `09_Tools/` (đã tích hợp sẵn `reconfigure(encoding='utf-8')`).
2. **Lỗi thiếu thư viện Python**:
   - Chạy lệnh: `pip install -r requirements.txt` hoặc cài đặt bổ sung `python-docx openpyxl pyyaml jsonschema pytest`.
3. **Cảnh báo `BROKEN_LINK` trong Traceability**:
   - Mở báo cáo `validation_report.md` để kiểm tra ID bị đứt gãy và bổ sung liên kết tương ứng trong `document_registry.yaml` hoặc metadata.
