# Software Documentation Agent System

> **Hệ thống AI Agent chuyên nghiệp chuyên phân tích dự án phần mềm, tự động khởi tạo, chuẩn hóa, bảo toàn mẫu và thẩm định 59 loại tài liệu kỹ thuật theo tiêu chuẩn công nghiệp quốc tế (ISO 29148, ISO 42010, ISO 29119, Scrum Guide 2020).**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests Passing](https://img.shields.io/badge/tests-40%2F40%20passed-success.svg)](file:///d:/agenttl1/Software-Documentation-Agent/10_Tests)
[![Scrum 2020](https://img.shields.io/badge/scrum-guide%202020-orange.svg)](https://scrumguides.org)
[![ISO Compliant](https://img.shields.io/badge/standards-ISO%2029148%20%7C%2042010%20%7C%2029119-green.svg)](https://iso.org)

---

## 1. Điểm Nổi Bật Của Hệ Thống

* **Chống giả mạo số liệu (Zero Hallucination)**: Agent chỉ sinh tài liệu dựa trên bằng chứng thu thập thực tế từ mã nguồn (endpoints, schemas, Docker, config, tests); không tự bịa đặt tính năng hay kết quả kiểm thử.
* **Bảo tồn mẫu biểu thực tế (Template Preservation)**: Giữ nguyên định dạng Word (`.docx`), bảng tính Excel (`.xlsx`), kiểu dáng bảng biểu, công thức và màu sắc nhận diện của tổ chức.
* **Ma trận truy vết 2 chiều (Traceability)**: Tự động kết nối và thẩm định mối quan hệ từ *Product Goal $\leftrightarrow$ User Story $\leftrightarrow$ Database $\leftrightarrow$ API $\leftrightarrow$ Test Case $\leftrightarrow$ Release Notes*.
* **Chuẩn hóa khung làm việc Scrum**: Thực thi nghiêm ngặt các ràng buộc về Timebox theo Scrum Guide 2020, tự động phát hiện lỗi bảng theo dõi giờ (LET) và biểu đồ Burndown Chart.

---

## 2. Cấu Trúc Kho Lưu Trữ

```text
d:\agenttl1\
├── .agents/skills/          # Native Antigravity Skill entry point
├── Software-Documentation-Agent/
│   ├── config/              # 7 tệp cấu hình registry và JSON schema
│   ├── instructions/        # 4 tệp hướng dẫn vận hành chi tiết
│   ├── 01_Rules/            # 73 tệp quy tắc chuẩn hóa theo 7 phân hệ
│   ├── 02_Standards/        # 4 tệp danh mục tiêu chuẩn và quy chế xác minh nguồn
│   ├── 03_Templates/        # 60 tệp mẫu vật lý (DOCX, XLSX, MD, YAML, MMD)
│   ├── 04_Project_Analyzer/ # 4 tệp quy tắc phân tích codebase & trích xuất bằng chứng
│   ├── 05_Document_Generation/# 4 tệp quy tắc sinh tài liệu và bảo toàn mẫu
│   ├── 06_Validation/       # 6 tệp quy tắc kiểm định chất lượng đa tầng
│   ├── 07_Workflows/        # 6 quy trình nghiệp vụ chuẩn hóa
│   ├── 08_Schemas/          # 5 tệp JSON Schema xác thực dữ liệu
│   ├── 09_Tools/            # 6 công cụ Python CLI và xử lý nghiệp vụ
│   ├── 10_Tests/            # 8 bộ test tự động PyTest (40 tests - 100% Passed)
│   ├── 11_Examples/         # Bộ hồ sơ mẫu dự án PayFlow (24 tệp tài liệu + metadata)
│   └── output/              # Thư mục lưu trữ tài liệu sinh tự động
├── SOFTWARE_DOCUMENTATION_AGENT_OVERVIEW.md # Bảng mô tả chi tiết 59 loại tài liệu
└── README.md                # Tệp giới thiệu tổng quan repo này
```

---

## 3. Danh Mục 59 Loại Tài Liệu Kỹ Thuật (5 Phân Hệ)

Hệ thống hỗ trợ tự động hóa trọn gói **59 loại tài liệu kỹ thuật** được phân chia theo 5 nhóm:

* **Nhóm A: Khởi động & Quản lý Yêu cầu (11 loại)**: Project Charter, Scope Statement, Stakeholder Register, SRS (ISO 29148), Product Vision, FRD, NFRD, Use Cases, User Story Mapping, User Stories Catalog, Traceability Matrix (RTM).
* **Nhóm B: Khung làm việc Scrum & Sprint (17 loại)**: Product Goal, Roadmap, Product Backlog, PBI Specification, Refinement Record, Release Plan, Sprint Planning, Sprint Goal, Sprint Backlog, Task Breakdown, Sprint Schedule, Daily Scrum Log, Sprint Review, Sprint Retrospective, DoD, DoR, Sprint Metrics & Burndown Tracking.
* **Nhóm C: Kiến trúc & Thiết kế Kỹ thuật (10 loại)**: Software Architecture Document (SAD - ISO 42010), System Design (SDD), Database Design (DBDD), ERD Mermaid, OpenAPI 3.1 REST API Specification, UI/UX Specification, Component Diagram, Deployment Diagram Mermaid, Technical Design Specification, ADR.
* **Nhóm D: Kiểm thử & Đảm bảo Chất lượng (8 loại)**: Master Test Plan (ISO 29119-3), Test Scenario, Test Cases Excel, Test Execution & Summary Report, Bug Report Sheet, UAT Plan, Code Review Checklist, QA Metrics Report.
* **Nhóm E: Vận hành, Bàn giao & Triển khai (13 loại)**: Project Master Schedule, WBS, Risk Register, Issue Log, Decision Log, Change Request, Meeting Minutes, Status Report, Release Notes, User Manual, Installation Guide, Project Handover, Deployment Runbook.

👉 *Xem chi tiết bảng mô tả, định dạng và tiêu chuẩn từng tài liệu tại:* [`SOFTWARE_DOCUMENTATION_AGENT_OVERVIEW.md`](file:///d:/agenttl1/SOFTWARE_DOCUMENTATION_AGENT_OVERVIEW.md)

---

## 4. Hướng Dẫn Cài Đặt & Sử Dụng

### Yêu cầu môi trường:
* Python 3.10 trở lên.
* Cài đặt thư viện:
  ```bash
  pip install pyyaml jsonschema python-docx openpyxl pytest
  ```

### Các lệnh điều phối chính (CLI):
```powershell
# 1. Phân tích mã nguồn dự án bất kỳ trên máy
python Software-Documentation-Agent/09_Tools/cli.py analyze --target "D:/MyProject" --output "output/my_profile.yaml"

# 2. Sinh tài liệu từ hồ sơ phân tích (Ví dụ: SRS Word .docx)
python Software-Documentation-Agent/09_Tools/cli.py generate --doc-id DOC-REQ-001 --profile "output/my_profile.yaml"

# 3. Sinh một bộ tài liệu theo nhóm (Ví dụ: Nhóm Scrum)
python Software-Documentation-Agent/09_Tools/cli.py generate-set --group Scrum --profile "output/my_profile.yaml"

# 4. Chạy kiểm định toàn diện hệ thống
python Software-Documentation-Agent/09_Tools/cli.py validate

# 5. Chạy bộ 40 bài kiểm thử tự động
python -m pytest Software-Documentation-Agent/10_Tests -v
```

---

## 5. Kết Quả Kiểm Thử (Verification Status)

* **Unit Tests**: `40 passed, 0 failed, 0 skipped` (Thời gian: 10.00s).
* **System Validator**: `9/9 checks PASSED`.
* **Templates**: 60 tệp mẫu vật lý thực tế (38 Word `.docx`, 8 Excel `.xlsx`, 10 Markdown `.md`, 1 OpenAPI `.yaml`, 2 Mermaid `.mmd`, 1 Notice).
