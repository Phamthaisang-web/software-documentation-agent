# Changelog — Lịch Sử Phiên Bản Software Documentation Agent

Tất cả các thay đổi đáng chú ý của hệ thống được ghi nhận trong tệp này theo định dạng [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) và tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-29

### Added
- **Core Architecture & Platform Integration**:
  - Tích hợp Native Workspace Skill cho Google Antigravity tại `.agents/skills/software-documentation-agent/SKILL.md`.
  - Cấu trúc thư mục chuẩn 12 phân vùng theo Master Prompt.
- **Document Registry (59 loại tài liệu)**:
  - Khai báo trọn vẹn 59 loại tài liệu thuộc 5 nhóm:
    - Nhóm A: Quản lý dự án & Kỹ thuật yêu cầu (`DOC-PM-001` đến `DOC-REQ-008` - 11 tài liệu).
    - Nhóm B: Scrum Framework (`DOC-SCRUM-001` đến `DOC-SCRUM-017` - 17 tài liệu).
    - Nhóm C: Kiến trúc & Thiết kế (`DOC-ARCH-001` đến `DOC-ARCH-010` - 10 tài liệu).
    - Nhóm D: Kiểm thử & Đảm bảo chất lượng (`DOC-TEST-001` đến `DOC-TEST-008` - 8 tài liệu).
    - Nhóm E: Theo dõi & Bàn giao (`DOC-DEL-001` đến `DOC-DEL-013` - 13 tài liệu).
- **Rules Suite (73 tệp quy tắc chi tiết)**:
  - 11 tệp Global Rules (`RULE-GLOB-001` đến `RULE-GLOB-011`).
  - 3 tệp Project Management Rules (`RULE-PM-001` đến `RULE-PM-003`).
  - 8 tệp Requirements Rules (`RULE-REQ-001` đến `RULE-REQ-008`).
  - 20 tệp Scrum Rules (`RULE-SCRUM-001` đến `RULE-SCRUM-020`) chuẩn hóa chặt chẽ theo Scrum Guide 2020.
  - 10 tệp Architecture Rules (`RULE-ARCH-001` đến `RULE-ARCH-010`) theo ISO/IEC/IEEE 42010.
  - 8 tệp Testing Rules (`RULE-TEST-001` đến `RULE-TEST-008`) theo ISO/IEC/IEEE 29119.
  - 13 tệp Delivery Rules (`RULE-DEL-001` đến `RULE-DEL-013`) theo ISO 21500.
- **Templates Suite (60 tệp mẫu vật lý)**:
  - 59 tệp mẫu thực tế định dạng Microsoft Word (`.docx`), Excel (`.xlsx`), Markdown (`.md`), OpenAPI (`.yaml`), Mermaid (`.mmd`).
  - Tệp thông cáo `GENERATED_TEMPLATES_NOTICE.md` minh bạch nguồn gốc khởi tạo.
- **Validation & Execution Engine**:
  - `project_analyzer.py`: Quét mã nguồn, trích xuất schema, API, tests, lập `project_profile.yaml`.
  - `document_generator.py`: Điền dữ liệu và bảo tồn định dạng Word, Excel, sơ đồ.
  - `traceability_engine.py`: Xây dựng và kiểm tra đồ thị liên kết hai chiều.
  - `sprint_validator.py`: Thẩm định timebox và các cam kết Scrum.
  - `validator.py`: Master validator chạy tự động và xuất báo cáo JSON / MD.
  - `cli.py`: Giao diện dòng lệnh hợp nhất hỗ trợ Unicode UTF-8 trên Windows.
- **Automated Test Suite (40 bài test PyTest)**:
  - `test_document_registry.py` (7 tests).
  - `test_rule_coverage.py` (4 tests).
  - `test_template_registry.py` (5 tests).
  - `test_source_registry.py` (4 tests).
  - `test_sprint_constraints.py` (7 tests).
  - `test_template_preservation.py` (4 tests).
  - `test_traceability.py` (4 tests).
  - `test_validation.py` (5 tests).
  - Kết quả: **40/40 tests PASSED (100%)**.
