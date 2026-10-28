# Software Documentation Agent

> **AI Agent chuyên phân tích dự án, tạo, cập nhật và kiểm tra tài liệu phần mềm theo chuẩn quốc tế.**

Hệ thống được thiết kế và xây dựng từ đầu dành riêng cho môi trường **Google Antigravity**, cung cấp giải pháp toàn diện từ khảo sát mã nguồn, sinh 59 loại tài liệu kỹ thuật, bảo tồn mẫu biểu Microsoft Office, ràng buộc liên kết hai chiều đến tự động kiểm thử và thẩm định.

---

## 🌟 Tính Năng Nổi Bật

- **Phân tích dự án thông minh (Project Analyzer)**: Tự động trích xuất công nghệ, cấu trúc thư mục, schema cơ sở dữ liệu, API routes, kiểm thử tự động và hạ tầng triển khai thành Hồ sơ dự án (`project_profile.yaml`).
- **59 Loại tài liệu kỹ thuật hoàn chỉnh**: Đăng ký và chuẩn hóa trọn vẹn 5 nhóm tài liệu (Quản lý dự án, Kỹ thuật yêu cầu, Scrum, Kiến trúc & Thiết kế, Kiểm thử, Bàn giao).
- **Tuân thủ tiêu chuẩn quốc tế đã xác minh**:
  - **The Scrum Guide 2020** (Ken Schwaber & Jeff Sutherland): Kiểm soát timebox nghiêm ngặt, phân biệt rõ ràng các thông lệ bổ trợ (Story Points, DoR, Burndown).
  - **ISO/IEC/IEEE 29148:2018**: Chuẩn hóa đặc tả yêu cầu phần mềm (SRS, Use Cases, RTM).
  - **ISO/IEC/IEEE 42010:2022**: Chuẩn hóa mô tả kiến trúc phần mềm và quyết định kiến trúc (ADR).
  - **ISO/IEC/IEEE 29119-1..4**: Chuẩn hóa tài liệu kiểm thử (Test Plan, Test Cases, Defect Reports).
  - **ISO 21500:2021**: Chuẩn hóa quản trị và bàn giao dự án.
  - **OpenAPI 3.1.0 & OWASP Top 10:2021**: Chuẩn hóa đặc tả API và bảo mật hệ thống.
- **Bảo tồn định dạng mẫu (Template Preservation)**:
  - Giữ nguyên Styles, Header, Footer, Table Grid trong Word (`.docx`).
  - Giữ nguyên Sheet, Công thức tính toán (`SUM`, `AVERAGE`), Màu nền, Căn lề trong Excel (`.xlsx`).
  - Giữ nguyên mã nguồn sơ đồ Mermaid (`.mmd`) cho phép chỉnh sửa trực tiếp.
- **Nguyên tắc không bịa đặt (Zero Hallucination)**: Không tự tạo PASS giả cho kiểm thử, không tự bịa biên bản họp hoặc chữ ký phê duyệt.
- **Mạng lưới truy xuất nguồn gốc (Traceability Engine)**: Ràng buộc liên kết chặt chẽ hai chiều từ Yêu cầu -> Thiết kế -> Kiểm thử -> Bàn giao.
- **Bộ kiểm thử tự động 100% đạt chuẩn**: 40/40 bài test tự động (PyTest) xác thực toàn bộ hệ thống.

---

## 📂 Bố Cục Thư Mục

| Thư Mục / Tệp Tin | Mục Đích |
| :--- | :--- |
| [`.agents/skills/software-documentation-agent/`](file:///d:/agenttl1/.agents/skills/software-documentation-agent/SKILL.md) | Điểm khởi chạy Workspace Skill cho Google Antigravity |
| [`config/`](file:///d:/agenttl1/Software-Documentation-Agent/config/) | Cấu hình trung tâm, Registries (59 tài liệu, 59 mẫu, 10 tiêu chuẩn) & Schemas |
| [`instructions/`](file:///d:/agenttl1/Software-Documentation-Agent/instructions/) | Chỉ dẫn hệ thống, quy trình thực thi, thẩm định nguồn và định dạng đầu ra |
| [`01_Rules/`](file:///d:/agenttl1/Software-Documentation-Agent/01_Rules/) | 73 tệp quy tắc kỹ thuật chuyên sâu (Global, PM, REQ, Scrum, ARCH, Test, Delivery) |
| [`02_Standards/`](file:///d:/agenttl1/Software-Documentation-Agent/02_Standards/) | Danh mục tiêu chuẩn, cổng tra cứu chính thức và chính sách thẩm định nguồn |
| [`03_Templates/`](file:///d:/agenttl1/Software-Documentation-Agent/03_Templates/) | 60 tệp mẫu vật lý thực tế (DOCX, XLSX, MD, YAML, MMD) |
| [`04_Project_Analyzer/`](file:///d:/agenttl1/Software-Documentation-Agent/04_Project_Analyzer/) | Quy tắc phân tích codebase, thu thập bằng chứng và xử lý mâu thuẫn |
| [`05_Document_Generation/`](file:///d:/agenttl1/Software-Documentation-Agent/05_Document_Generation/) | Quy tắc sinh tài liệu và bảo tồn cấu trúc mẫu biểu |
| [`06_Validation/`](file:///d:/agenttl1/Software-Documentation-Agent/06_Validation/) | Quy tắc thẩm định nội dung, cấu trúc, nguồn và tệp xuất bản |
| [`07_Workflows/`](file:///d:/agenttl1/Software-Documentation-Agent/07_Workflows/) | 6 quy trình làm việc chuẩn hóa từ phân tích đến xuất bản |
| [`08_Schemas/`](file:///d:/agenttl1/Software-Documentation-Agent/08_Schemas/) | Bộ JSON Schema kiểm tra Profile, Document, Rule, Template và Report |
| [`09_Tools/`](file:///d:/agenttl1/Software-Documentation-Agent/09_Tools/) | Bộ công cụ Python CLI thực thi tự động (`cli.py`, `validator.py`, v.v.) |
| [`10_Tests/`](file:///d:/agenttl1/Software-Documentation-Agent/10_Tests/) | Bộ 40 bài kiểm thử tự động PyTest đạt 100% tỷ lệ pass |
| [`11_Examples/`](file:///d:/agenttl1/Software-Documentation-Agent/11_Examples/) | Dữ liệu mẫu (Profile, Metadata, Validation Report) & Bộ tài liệu mẫu đã sinh |
| [`output/`](file:///d:/agenttl1/Software-Documentation-Agent/output/) | Thư mục lưu trữ tài liệu xuất bản và báo cáo thẩm định |

---

## 🚀 Hướng Dẫn Sử Dụng Nhanh

Xem hướng dẫn chi tiết tại [HUONG_DAN_SU_DUNG.md](file:///d:/agenttl1/Software-Documentation-Agent/HUONG_DAN_SU_DUNG.md).

```powershell
# 1. Phân tích mã nguồn dự án
python Software-Documentation-Agent/09_Tools/cli.py analyze --target .

# 2. Tạo một tài liệu kỹ thuật cụ thể (ví dụ: SRS DOC-REQ-001)
python Software-Documentation-Agent/09_Tools/cli.py generate --doc-id DOC-REQ-001

# 3. Tạo trọn bộ 59 tài liệu
python Software-Documentation-Agent/09_Tools/cli.py generate-set

# 4. Thẩm định toàn diện hệ thống
python Software-Documentation-Agent/09_Tools/cli.py validate

# 5. Chạy bộ kiểm thử tự động PyTest
python -m pytest Software-Documentation-Agent/10_Tests -v
```

---

## 📜 Bản Quyền và Tác Quyền
Xem chi tiết tại [LICENSES_AND_ATTRIBUTIONS.md](file:///d:/agenttl1/Software-Documentation-Agent/LICENSES_AND_ATTRIBUTIONS.md).
Mã nguồn phát hành theo giấy phép **MIT License**. Các tiêu chuẩn quốc tế được trích dẫn và tôn trọng bản quyền theo quy định của tổ chức phát hành.
