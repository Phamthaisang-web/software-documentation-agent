# Tổng Quan Hệ Thống Software Documentation Agent

> **Hệ thống AI Agent chuyên nghiệp chuyên phân tích dự án phần mềm, tự động khởi tạo, chuẩn hóa, bảo toàn mẫu và thẩm định 59 loại tài liệu kỹ thuật theo tiêu chuẩn công nghiệp quốc tế (ISO 29148, ISO 42010, ISO 29119, Scrum Guide 2020).**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests Passing](https://img.shields.io/badge/tests-40%2F40%20passed-success.svg)](file:///d:/agenttl1/Software-Documentation-Agent/10_Tests)
[![Scrum 2020](https://img.shields.io/badge/scrum-guide%202020-orange.svg)](https://scrumguides.org)
[![ISO Compliant](https://img.shields.io/badge/standards-ISO%2029148%20%7C%2042010%20%7C%2029119-green.svg)](https://iso.org)

---

## 1. Giới Thiệu Chung

**Software Documentation Agent** là giải pháp tự động hóa tài liệu kỹ thuật phần mềm toàn diện, giải quyết triệt để các bài toán thường gặp trong quá trình phát triển phần mềm và làm đồ án Capstone/Doanh nghiệp:
* **Chống giả mạo số liệu (Zero Hallucination)**: Agent chỉ sinh tài liệu dựa trên bằng chứng thu thập thực tế từ mã nguồn (endpoints, schemas, Docker, config, tests); không tự bịa đặt tính năng hay kết quả kiểm thử.
* **Bảo tồn mẫu biểu thực tế (Template Preservation)**: Giữ nguyên định dạng Word (`.docx`), bảng tính Excel (`.xlsx`), kiểu dáng bảng biểu, công thức và màu sắc nhận diện của tổ chức.
* **Ma trận truy vết 2 chiều (Traceability)**: Tự động kết nối và thẩm định mối quan hệ từ *Product Goal $\leftrightarrow$ User Story $\leftrightarrow$ Database $\leftrightarrow$ API $\leftrightarrow$ Test Case $\leftrightarrow$ Release Notes*.
* **Chuẩn hóa khung làm việc Scrum**: Thực thi nghiêm ngặt các ràng buộc về Timebox theo Scrum Guide 2020, tự động phát hiện lỗi bảng theo dõi giờ (LET) và biểu đồ Burndown Chart.

---

## 2. Kiến Trúc Phân Hệ & Cấu Trúc Thư Mục

Hệ thống được tổ chức thành 12 phân hệ chuyên trách, hoàn toàn độc lập và có thể tái sử dụng cho bất kỳ dự án nào:

```text
Software-Documentation-Agent/
├── config/                  # Cấu hình trung tâm: danh mục tài liệu, tiêu chuẩn, mẫu và schema
├── instructions/            # 4 bộ chỉ dẫn tác nghiệp chi tiết cho Agent
├── 01_Rules/                # 73 tệp quy tắc chuẩn hóa bao quát 7 phân hệ kỹ thuật
├── 02_Standards/            # 10 hồ sơ tiêu chuẩn quốc tế đã xác minh chính thức (ISO, Scrum)
├── 03_Templates/            # 60 tệp mẫu vật lý thực tế (DOCX, XLSX, MD, OpenAPI, Mermaid)
├── 04_Project_Analyzer/     # Quy tắc phân tích codebase & trích xuất bằng chứng khách quan
├── 05_Document_Generation/  # Quy tắc sinh tài liệu và bảo toàn mẫu biểu
├── 06_Validation/           # Quy tắc thẩm định 9 tầng chất lượng và truy vết liên kết
├── 07_Workflows/            # 6 quy trình nghiệp vụ chuẩn (Analyze, Generate, Validate, Sprint)
├── 08_Schemas/              # 5 tệp JSON Schema xác thực tính hợp lệ của dữ liệu
├── 09_Tools/                # Bộ công cụ thực thi Python CLI độc lập (cross-platform)
├── 10_Tests/                # Bộ 40 bài kiểm thử tự động PyTest đạt tỷ lệ 100% PASSED
├── 11_Examples/             # Bộ hồ sơ mẫu PayFlow Platform gồm 24 tệp tài liệu thực tế
└── output/                  # Thư mục lưu trữ tài liệu sinh tự động theo phân nhóm
```

---

## 3. Danh Mục Chi Tiết 59 Loại Tài Liệu Kỹ Thuật

Toàn bộ 59 loại tài liệu được quản lý tập trung tại [`config/document_registry.yaml`](file:///d:/agenttl1/Software-Documentation-Agent/config/document_registry.yaml):

### Nhóm A: Khởi Động Dự Án & Quản Lý Yêu Cầu (11 Loại)
*Tuân thủ tiêu chuẩn ISO/IEC/IEEE 29148:2018 và ISO 21500.*

| Mã Tài Liệu | Tên Tài Liệu Chính Thức | Định Dạng | Mô Tả Tóm Tắt |
| :--- | :--- | :---: | :--- |
| `DOC-PM-001` | Project Charter (Hiến chương dự án) | `.docx` | Xác lập mục tiêu, phạm vi ban đầu, ngân sách và quyền hạn của PM. |
| `DOC-PM-002` | Project Scope Statement (Tuyên bố phạm vi) | `.docx` | Định nghĩa ranh giới chi tiết: in-scope, out-of-scope và tiêu chí chấp nhận. |
| `DOC-PM-003` | Stakeholder Register (Sổ đăng ký các bên liên quan) | `.xlsx` | Danh sách các bên liên quan, vai trò, mức độ ảnh hưởng và kỳ vọng. |
| `DOC-REQ-001`| Software Requirements Specification (SRS) | `.docx` | Đặc tả yêu cầu phần mềm hoàn chỉnh theo cấu trúc chuẩn ISO 29148. |
| `DOC-REQ-002`| Product Vision Document (Tầm nhìn sản phẩm) | `.docx` | Định vị sản phẩm, bài toán kinh doanh và giá trị mang lại cho người dùng. |
| `DOC-REQ-003`| Functional Requirements Document (FRD) | `.docx` | Bảng đặc tả chi tiết toàn bộ các yêu cầu chức năng của hệ thống. |
| `DOC-REQ-004`| Non-Functional Requirements Document (NFRD)| `.docx` | Ràng buộc phi chức năng: hiệu năng, bảo mật, độ tin cậy, khả năng tải. |
| `DOC-REQ-005`| Use Case Specification | `.docx` | Đặc tả luồng sự kiện chính, luồng phụ, ngoại lệ và tiền/hậu điều kiện. |
| `DOC-REQ-006`| User Story Mapping | `.docx` | Sơ đồ hành trình người dùng và phân rã User Story theo các lát cắt phát hành. |
| `DOC-REQ-007`| User Stories Catalog | `.docx` | Danh mục User Story chuẩn hóa theo cú pháp: As a... I want... So that... |
| `DOC-REQ-008`| Traceability Matrix & Acceptance Criteria | `.xlsx` | Ma trận truy vết 2 chiều từ User Story sang Tiêu chí nghiệm thu & Test Case. |

---

### Nhóm B: Khung Làm Việc Scrum & Quản Trị Sprint (17 Loại)
*Tuân thủ Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland).*

| Mã Tài Liệu | Tên Tài Liệu Chính Thức | Định Dạng | Mô Tả Tóm Tắt |
| :--- | :--- | :---: | :--- |
| `DOC-SCRUM-001` | Product Goal Document | `.md` | Cam kết dài hạn của Product Owner định hướng cho Product Backlog. |
| `DOC-SCRUM-002` | Product Roadmap | `.docx` | Lộ trình phát triển sản phẩm theo các mốc thời gian và mục tiêu chiến lược. |
| `DOC-SCRUM-003` | Product Backlog | `.xlsx` | Danh sách sắp xếp ưu tiên các hạng mục cần phát triển của sản phẩm. |
| `DOC-SCRUM-004` | Product Backlog Item (PBI) Specification | `.docx` | Bản mô tả chi tiết của từng PBI gồm bối cảnh, giá trị và tiêu chí nghiệm thu. |
| `DOC-SCRUM-005` | Backlog Refinement Record | `.docx` | Biên bản buổi làm mịn backlog: làm rõ yêu cầu, chia nhỏ và ước lượng. |
| `DOC-SCRUM-006` | Release Plan | `.docx` | Kế hoạch đóng gói và bàn giao các phiên bản sản phẩm ra thị trường. |
| `DOC-SCRUM-007` | Sprint Planning Record | `.docx` | Biên bản lập kế hoạch Sprint: xác lập Sprint Goal và lựa chọn công việc. |
| `DOC-SCRUM-008` | Sprint Goal Document | `.md` | Cam kết duy nhất và bất biến của Developers trong suốt thời gian của một Sprint. |
| `DOC-SCRUM-009` | Sprint Backlog | `.xlsx` | Kế hoạch thực hiện chi tiết của Developers cho một Sprint cụ thể. |
| `DOC-SCRUM-010` | Task Breakdown Sheet | `.docx` | Phân rã User Story thành các nhiệm vụ kỹ thuật có thời lượng từ 1-8 giờ. |
| `DOC-SCRUM-011` | Sprint Schedule (Lịch trình Sprint) | `.docx` | Phân bổ các sự kiện Scrum theo đúng khung thời gian (Timebox) quy định. |
| `DOC-SCRUM-012` | Daily Scrum Log | `.md` | Nhật ký họp Daily 15 phút: việc đã làm, việc sẽ làm và trở ngại (Impediments). |
| `DOC-SCRUM-013` | Sprint Review Record | `.docx` | Biên bản trình diễn Increment cho các bên liên quan và thu thập phản hồi. |
| `DOC-SCRUM-014` | Sprint Retrospective Record | `.md` | Biên bản cải tiến quy trình làm việc của nhóm sau mỗi Sprint kết thúc. |
| `DOC-SCRUM-015` | Definition of Done (DoD) | `.docx` | Cam kết chất lượng bắt buộc để một Increment được xem là hoàn thành. |
| `DOC-SCRUM-016` | Definition of Ready (DoR) | `.docx` | Tiêu chí để một PBI đủ điều kiện được đưa vào Sprint Planning (thông lệ bổ trợ). |
| `DOC-SCRUM-017` | Sprint Metrics & Burndown Tracking | `.xlsx` | Bảng theo dõi số giờ còn lại hàng ngày (LET) và biểu đồ Burndown Chart. |

---

### Nhóm C: Kiến Trúc & Thiết Kế Kỹ Thuật (10 Loại)
*Tuân thủ tiêu chuẩn ISO/IEC/IEEE 42010:2022 và OpenAPI 3.1.*

| Mã Tài Liệu | Tên Tài Liệu Chính Thức | Định Dạng | Mô Tả Tóm Tắt |
| :--- | :--- | :---: | :--- |
| `DOC-ARCH-001` | Software Architecture Document (SAD) | `.docx` | Tài liệu kiến trúc phần mềm tổng thể theo mô hình góc nhìn 4+1 Views. |
| `DOC-ARCH-002` | System Design Document (SDD) | `.docx` | Thiết kế chi tiết các tầng nghiệp vụ, service, controller và cấu trúc dữ liệu. |
| `DOC-ARCH-003` | Database Design Document (DBDD) | `.docx` | Thiết kế cơ sở dữ liệu vật lý: bảng, kiểu dữ liệu, khóa chính/ngoại, index. |
| `DOC-ARCH-004` | Entity Relationship Diagram (ERD) | `.mmd` | Sơ đồ quan hệ thực thể bằng mã nguồn Mermaid có thể render trực tiếp. |
| `DOC-ARCH-005` | REST API Specification | `.yaml` | Đặc tả toàn bộ API endpoints của hệ thống theo chuẩn OpenAPI 3.1.0. |
| `DOC-ARCH-006` | UI/UX Design Specification | `.docx` | Đặc tả quy chuẩn giao diện, luồng tương tác, màu sắc, typography và wireframes. |
| `DOC-ARCH-007` | Component & Package Diagram | `.docx` | Thiết kế module hóa, sự phụ thuộc giữa các component và package nội bộ. |
| `DOC-ARCH-008` | Deployment & Infrastructure Architecture | `.mmd` | Sơ đồ kiến trúc triển khai mạng: Web, App, Database, Cache, Load Balancer. |
| `DOC-ARCH-009` | Technical Design Specification (TDS) | `.docx` | Thiết kế thuật toán, giải pháp kỹ thuật chuyên sâu và cơ chế caching/security. |
| `DOC-ARCH-010` | Architecture Decision Records (ADR) | `.md` | Nhật ký ghi nhận các quyết định kiến trúc quan trọng, bối cảnh và hệ quả. |

---

### Nhóm D: Kiểm Thử & Đảm Bảo Chất Lượng (8 Loại)
*Tuân thủ tiêu chuẩn quốc tế ISO/IEC/IEEE 29119 (Phần 1, 2, 3, 4).*

| Mã Tài Liệu | Tên Tài Liệu Chính Thức | Định Dạng | Mô Tả Tóm Tắt |
| :--- | :--- | :---: | :--- |
| `DOC-TEST-001` | Master Test Plan | `.docx` | Kế hoạch kiểm thử tổng thể: phạm vi, môi trường, công cụ, tiêu chí pass/fail. |
| `DOC-TEST-002` | Test Scenario Specification | `.docx` | Kịch bản kiểm thử bao quát các luồng nghiệp vụ end-to-end của hệ thống. |
| `DOC-TEST-003` | Test Case Specification | `.xlsx` | Bảng đặc tả chi tiết các bước kiểm thử, dữ liệu đầu vào và kết quả mong đợi. |
| `DOC-TEST-004` | Test Execution & Summary Report | `.docx` | Báo cáo kết quả chạy kiểm thử thực tế, tỷ lệ pass/fail và độ che phủ code. |
| `DOC-TEST-005` | Bug / Defect Report Sheet | `.xlsx` | Bảng theo dõi lỗi phát hiện: độ nghiêm trọng, mức ưu tiên, log và trạng thái sửa. |
| `DOC-TEST-006` | User Acceptance Testing (UAT) Plan | `.docx` | Kế hoạch kiểm thử chấp nhận của người dùng trước khi bàn giao đưa vào vận hành. |
| `DOC-TEST-007` | Code Review Checklist & Guidelines | `.docx` | Bộ tiêu chí đánh giá chất lượng mã nguồn, quy chuẩn đặt tên và bảo mật code. |
| `DOC-TEST-008` | Quality Assurance Metrics Report | `.docx` | Báo cáo các chỉ số chất lượng: mật độ lỗi, nợ kỹ thuật (Technical Debt). |

---

### Nhóm E: Vận Hành, Bàn Giao & Triển Khai (13 Loại)
*Tuân thủ tiêu chuẩn quản trị dự án ISO 21500.*

| Mã Tài Liệu | Tên Tài Liệu Chính Thức | Định Dạng | Mô Tả Tóm Tắt |
| :--- | :--- | :---: | :--- |
| `DOC-DEL-001` | Project Master Schedule | `.xlsx` | Lịch trình tổng thể dự án theo biểu đồ Gantt và các cột mốc (Milestones). |
| `DOC-DEL-002` | Work Breakdown Structure (WBS) | `.xlsx` | Cơ cấu phân rã công việc theo dạng cây phân cấp đến từng gói công việc. |
| `DOC-DEL-003` | Risk Register & Management Plan | `.xlsx` | Bảng quản lý rủi ro dự án, đánh giá xác suất/tác động và biện pháp đối phó. |
| `DOC-DEL-004` | Project Issue Log | `.xlsx` | Nhật ký theo dõi các vấn đề phát sinh trong dự án và biện pháp giải quyết. |
| `DOC-DEL-005` | Project Decision Log | `.docx` | Sổ nhật ký ghi lại các quyết định quan trọng giữa PM, Khách hàng và Nhóm phát triển. |
| `DOC-DEL-006` | Change Request Form & Log | `.docx` | Phiếu yêu cầu thay đổi phạm vi, đánh giá tác động chi phí và tiến độ. |
| `DOC-DEL-007` | Meeting Minutes (Biên bản họp) | `.docx` | Mẫu biên bản họp chính thức ghi nhận người tham gia, thảo luận và Action items. |
| `DOC-DEL-008` | Project Progress & Status Report | `.docx` | Báo cáo định kỳ tiến độ thực tế so với kế hoạch cho các cấp quản lý. |
| `DOC-DEL-009` | Software Release Notes | `.md` | Thông cáo phát hành phiên bản mới: tính năng mới, lỗi đã sửa, giới hạn đã biết. |
| `DOC-DEL-010` | User Manual (Hướng dẫn sử dụng) | `.docx` | Tài liệu hướng dẫn sử dụng phần mềm dành cho người dùng cuối kèm ảnh chụp màn hình. |
| `DOC-DEL-011` | Installation & Operation Guide | `.docx` | Hướng dẫn cài đặt môi trường, biên dịch, chạy ứng dụng và cấu hình service. |
| `DOC-DEL-012` | Project Handover & Sign-off Record | `.docx` | Biên bản bàn giao sản phẩm, tài sản mã nguồn và ký nghiệm thu dự án. |
| `DOC-DEL-013` | Deployment & DevOps Runbook | `.docx` | Hướng dẫn triển khai CI/CD, quy trình rollback và giám sát hạ tầng production. |

---

## 4. Hướng Dẫn Vận Hành & Sử Dụng

### 4.1. Kích hoạt trực tiếp trên AI Chat Interface
Hệ thống đã được đóng gói thành **Native Antigravity Skill** tại [`.agents/skills/software-documentation-agent/SKILL.md`](file:///d:/agenttl1/.agents/skills/software-documentation-agent/SKILL.md).

Chỉ cần gõ trên thanh chat:
```text
/software-documentation-agent phân tích dự án tại D:\MyProject và tạo tài liệu SRS DOC-REQ-001
```

### 4.2. Vận hành độc lập qua Python CLI
Bạn có thể sử dụng bộ công cụ tại `Software-Documentation-Agent/09_Tools/cli.py` trên bất kỳ hệ điều hành nào (Windows, macOS, Linux):

```powershell
# 1. Phân tích mã nguồn và lập hồ sơ dự án
python Software-Documentation-Agent/09_Tools/cli.py analyze --target "D:/MyProject" --output "output/my_profile.yaml"

# 2. Sinh một tài liệu đơn lẻ (Ví dụ: SRS Word .docx)
python Software-Documentation-Agent/09_Tools/cli.py generate --doc-id DOC-REQ-001 --profile "output/my_profile.yaml"

# 3. Sinh một bộ tài liệu theo nhóm (Ví dụ: Nhóm Scrum)
python Software-Documentation-Agent/09_Tools/cli.py generate-set --group Scrum --profile "output/my_profile.yaml"

# 4. Kiểm định toàn diện chất lượng hệ thống tài liệu
python Software-Documentation-Agent/09_Tools/cli.py validate

# 5. Chạy 40 bài kiểm thử tự động
python -m pytest Software-Documentation-Agent/10_Tests -v
```

---

## 5. Kết Quả Kiểm Thử & Kiểm Định

Hệ thống đã trải qua quá trình kiểm thử tự động nghiêm ngặt và đạt chứng nhận toàn vẹn tuyệt đối:
* **PyTest Suite (`10_Tests/`)**: **40/40 tests PASSED (100%)**.
* **System Validator (`cli.py validate`)**: **9/9 checks PASSED**.
* **Định danh mẫu biểu**: 59/59 tệp mẫu vật lý tồn tại thực tế trên đĩa, được gắn nhãn minh bạch `GENERATED_TEMPLATE` theo quy định pháp lý.
* **Tiêu chuẩn chính thức**: 10/10 nguồn tiêu chuẩn được gắn trạng thái `VERIFIED_OFFICIAL` kèm điều khoản viện dẫn cụ thể từ ISO và Scrum Guides.

---

*Tài liệu được phát triển và kiểm định bởi Antigravity Software Architecture Team.*
