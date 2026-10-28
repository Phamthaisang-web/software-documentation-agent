import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_DIR = os.path.join(BASE_DIR, "01_Rules")

def write_rule(category, filename, content):
    target_dir = os.path.join(RULES_DIR, category)
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, filename)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {category}/{filename}")

# ==============================================================================
# ARCHITECTURE & DESIGN RULES (10 files)
# ==============================================================================

write_rule("Architecture_Design", "Architecture_Rules.md", """# RULE-ARCH-001: Software Architecture Description Rules

- **Mã quy tắc**: `RULE-ARCH-001`
- **Tên quy tắc**: Architectural Viewpoints and ISO 42010 Conformance Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định phương pháp mô tả kiến trúc phần mềm toàn diện qua các góc nhìn kiến trúc (Architectural Views) theo tiêu chuẩn ISO/IEC/IEEE 42010:2022.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-001` (SAD).

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 (Architecture description conceptual framework)

## 4. Đầu vào bắt buộc
Bối cảnh hệ thống, các bên liên quan, các mối quan tâm kiến trúc (concerns), các quyết định then chốt.

## 5. Cấu trúc trường bắt buộc
Bối cảnh kiến trúc & Stakeholders, Các góc nhìn kiến trúc (Component View, Runtime/Execution View, Deployment View), Hiện thực hóa các thuộc tính chất lượng (Quality Attributes).

## 6. Quy tắc nội dung
1. Phân biệt rõ ranh giới giữa:
   - Kiến trúc ĐÃ TRIỂN KHAI THỰC TẾ (Implemented Architecture - có code chứng minh).
   - Kiến trúc ĐƯỢC ĐỀ XUẤT (Proposed Architecture - định hướng tương lai).
   - Kiến trúc ĐANG THỬ NGHIỆM (Experimental).
2. Không tuyên bố rằng ISO 42010 áp đặt một mẫu tài liệu duy nhất (tiêu chuẩn quy định khung khái niệm và các viewpoint).
3. Mỗi góc nhìn kiến trúc phải giải quyết các mối quan tâm cụ thể của các nhóm stakeholder tương ứng.

## 7. Tiêu chí chất lượng
Mỗi sơ đồ kiến trúc phải có chú thích rõ ràng về giao thức kết nối, luồng dữ liệu và trách nhiệm của từng node.

## 8. Quy tắc đặt tên
`DOC-ARCH-001_Software_Architecture_Description.docx`.

## 9. Truy xuất nguồn gốc
Liên kết trực tiếp tới `DOC-REQ-001` (SRS), `DOC-ARCH-007` (Component Diagram) và `DOC-ARCH-008` (Deployment).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của các Views và chú thích trạng thái triển khai.

## 11. Ngoại lệ
Hệ thống script đơn lẻ (CLI tool nhỏ) có thể rút gọn Runtime View.

## 12. Ví dụ
- Hợp lệ: "Hệ thống áp dụng mô hình Clean Architecture gồm các tầng Domain, Application, Infrastructure và Presentation."
- Không hợp lệ: Tự nhận hệ thống là Microservices phân tán trong khi toàn bộ mã nguồn nằm chung 1 tệp monolith.

## 13. Tài liệu liên quan
`DOC-ARCH-002`, `DOC-ARCH-007`, `DOC-ARCH-008`, `DOC-ARCH-010`.

## 14. Bằng chứng cần thiết
Mã nguồn cấu trúc thư mục dự án, Docker Compose hoặc sơ đồ dịch vụ.

## 15. Giới hạn đã biết
Không thể phân tích các dịch vụ SaaS của bên thứ 3 nếu không có thông số cấu hình.
""")

write_rule("Architecture_Design", "System_Design_Rules.md", """# RULE-ARCH-002: Software Design Description Rules

- **Mã quy tắc**: `RULE-ARCH-002`
- **Tên quy tắc**: Detailed System Design Description Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả chi tiết thiết kế các module, lớp, giao diện lập trình nội bộ và cơ chế xử lý lỗi.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-002` (SDD).

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022

## 4. Đầu vào bắt buộc
Giao diện module, sơ đồ tương tác, cấu trúc dữ liệu nội bộ.

## 5. Cấu trúc trường bắt buộc
Tổng quan thiết kế, Phân rã module, Đặc tả giao diện chi tiết, Luồng tương tác, Chiến lược xử lý lỗi & ngoại lệ.

## 6. Quy tắc nội dung
1. Chi tiết hóa kiến trúc mức cao thành các thành phần code cụ thể (classes, services, repositories).
2. Quy định rõ cơ chế bắt và chuyển đổi ngoại lệ (Exception Handling).

## 7. Tiêu chí chất lượng
Mô tả rõ hợp đồng giao tiếp giữa các module.

## 8. Quy tắc đặt tên
`DOC-ARCH-002_Software_Design_Description.docx`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-ARCH-001` và chi tiết hóa `DOC-REQ-003`.

## 10. Cách kiểm tra
Kiểm tra cấu trúc module phân rã.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Thiết kế module AuthService sử dụng repository pattern với UserRepository interface.
- Không hợp lệ: Mô tả chung chung không nêu tên lớp hay phương thức.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-REQ-003`.

## 14. Bằng chứng cần thiết
Code interfaces, classes, services.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Architecture_Design", "Database_Design_Rules.md", """# RULE-ARCH-003: Database Design Specification Rules

- **Mã quy tắc**: `RULE-ARCH-003`
- **Tên quy tắc**: Database Schema and Data Integrity Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định phương pháp đặc tả cơ sở dữ liệu dựa trên schema, migration, model, index và ràng buộc thực tế trong mã nguồn.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-003`.

## 3. Nguồn tiêu chuẩn
- Relational Database Normalization Standards & ISO/IEC 9075 (SQL)

## 4. Đầu vào bắt buộc
Tệp định nghĩa bảng, kiểu dữ liệu, khóa chính, khóa ngoại, chỉ mục (indexes).

## 5. Cấu trúc trường bắt buộc
Engine CSDL & Phiên bản, Mô hình dữ liệu logic, Đặc tả schema vật lý (Bảng, Cột, Kiểu, Ràng buộc, Giá trị mặc định), Chỉ mục & Tối ưu hóa, Chiến lược migration.

## 6. Quy tắc nội dung
1. Mọi bảng và cột phải được ánh xạ từ tệp schema/migration thật (ví dụ: `schema.prisma`, `migrations/*.sql`, ORM models).
2. Không tự nghĩ ra các bảng hoặc quan hệ không có trong mã nguồn.
3. Ghi rõ các ràng buộc toàn vẹn dữ liệu (Primary Key, Foreign Key, Unique, Check constraints).

## 7. Tiêu chí chất lượng
100% các cột có kiểu dữ liệu (data type) và quy định nullability rõ ràng.

## 8. Quy tắc đặt tên
`DOC-ARCH-003_Database_Design_Specification.docx`.

## 9. Truy xuất nguồn gốc
Phải đồng bộ 100% với sơ đồ `DOC-ARCH-004` (ERD).

## 10. Cách kiểm tra
Kiểm tra tên bảng và cột đối chiếu với schema code.

## 11. Ngoại lệ
Hệ thống NoSQL (MongoDB, DynamoDB) mô tả theo Document Schema / Collection structure.

## 12. Ví dụ
- Hợp lệ: Bảng `users` gồm cột `id UUID PRIMARY KEY`, `email VARCHAR(255) UNIQUE NOT NULL`.
- Không hợp lệ: Mô tả bảng không nêu kiểu dữ liệu hoặc bịa ra bảng không tồn tại.

## 13. Tài liệu liên quan
`DOC-ARCH-004`, `DOC-REQ-003`.

## 14. Bằng chứng cần thiết
Tệp migration hoặc schema file của dự án.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Architecture_Design", "ERD_Rules.md", """# RULE-ARCH-004: Entity Relationship Diagram Rules

- **Mã quy tắc**: `RULE-ARCH-004`
- **Tên quy tắc**: ERD Notation and Editable Source Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định tiêu chuẩn biểu diễn sơ đồ thực thể quan hệ (ERD) và lưu trữ mã nguồn sơ đồ để người dùng có thể chỉnh sửa.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-004`.

## 3. Nguồn tiêu chuẩn
- Crow's Foot Notation & Mermaid.js ER Diagram Standard

## 4. Đầu vào bắt buộc
Danh sách thực thể, các thuộc tính, quan hệ (1-1, 1-n, n-n) và tính chất cardinalities.

## 5. Cấu trúc trường bắt buộc
Định nghĩa thực thể, Ma trận quan hệ, Mã nguồn sơ đồ Mermaid (`erDiagram`), Mô tả ý nghĩa từng quan hệ.

## 6. Quy tắc nội dung
1. Sơ đồ phải dựa trên các thực thể và quan hệ có căn cứ từ database schema.
2. BẮT BUỘC lưu trữ mã nguồn sơ đồ dưới dạng tệp `.mmd` hoặc khối mã Mermaid có thể chỉnh sửa, không được chỉ dán ảnh chết (static image).
3. Ký hiệu quan hệ phải chính xác (One-to-One, One-to-Many, Many-to-Many).

## 7. Tiêu chí chất lượng
Mã nguồn Mermaid biên dịch thành công không có lỗi cú pháp.

## 8. Quy tắc đặt tên
`DOC-ARCH-004_Entity_Relationship_Diagram.mmd`.

## 9. Truy xuất nguồn gốc
Ánh xạ 1:1 với `DOC-ARCH-003` (Database Design).

## 10. Cách kiểm tra
Kiểm tra cú pháp `erDiagram` trong file `.mmd`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ:
  ```mermaid
  erDiagram
      USER ||--o{ ORDER : places
      ORDER ||--|{ ORDER_ITEM : contains
  ```
- Không hợp lệ: Chỉ chụp ảnh màn hình và không có mã nguồn sơ đồ.

## 13. Tài liệu liên quan
`DOC-ARCH-003`.

## 14. Bằng chứng cần thiết
Schema DB và tệp Mermaid `.mmd`.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Architecture_Design", "API_Specification_Rules.md", """# RULE-ARCH-005: API Specification Rules

- **Mã quy tắc**: `RULE-ARCH-005`
- **Tên quy tắc**: OpenAPI 3.1 REST API Specification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Dặc tả chuẩn xác và đầy đủ toàn bộ giao diện REST API của dự án theo chuẩn OpenAPI Specification 3.1.0.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-005`.

## 3. Nguồn tiêu chuẩn
- OpenAPI Specification Version 3.1.0 (`STD-API-OAS31`)

## 4. Đầu vào bắt buộc
Endpoints, HTTP methods, Parameters, Request body schemas, Response schemas, Mã trạng thái HTTP, Cơ chế xác thực.

## 5. Cấu trúc trường bắt buộc
Tệp OpenAPI 3.1 hợp lệ: `openapi`, `info`, `servers`, `paths`, `components` (`schemas`, `securitySchemes`), `security`.

## 6. Quy tắc nội dung
1. Phải dựa trên các router/controller thực tế trong mã nguồn dự án.
2. Mọi endpoint phải nêu rõ phương thức (GET, POST, PUT, DELETE, PATCH).
3. Mô tả rõ payload đầu vào, kiểu dữ liệu từng trường và các mã trạng thái phản hồi (200, 201, 400, 401, 403, 404, 500).
4. Khai báo rõ cơ chế bảo mật (BearerAuth, APIKey, OAuth2, Cookie).
5. Không tự bịa endpoint không có trong mã nguồn.

## 7. Tiêu chí chất lượng
Vượt qua công cụ thẩm định OpenAPI schema validator (zero schema errors).

## 8. Quy tắc đặt tên
`DOC-ARCH-005_API_Specification.yaml`.

## 9. Truy xuất nguồn gốc
Hiện thực hóa `DOC-REQ-003` (Functional Requirements) và làm cơ sở cho `DOC-TEST-003` (API Test Cases).

## 10. Cách kiểm tra
Validate cú pháp OpenAPI bằng PyYAML và schema OpenAPI 3.1.

## 11. Ngoại lệ
Hệ thống GraphQL sử dụng Schema Definition Language (SDL) thay thế.

## 12. Ví dụ
- Hợp lệ: Khai báo `/api/v1/auth/login` với POST method, body yêu cầu email & password, trả về token JWT 200 OK.
- Không hợp lệ: Tệp YAML thiếu trường `responses` hoặc sai cú pháp OpenAPI.

## 13. Tài liệu liên quan
`DOC-REQ-003`, `DOC-TEST-003`.

## 14. Bằng chứng cần thiết
Tệp routes trong source code (Express router, FastAPI routers, Spring controllers).

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Architecture_Design", "UI_UX_Specification_Rules.md", """# RULE-ARCH-006: UI/UX Specification Rules

- **Mã quy tắc**: `RULE-ARCH-006`
- **Tên quy tắc**: UI/UX Structure and Component Specification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Dặc tả cấu trúc màn hình, thành phần giao diện người dùng và luồng điều hướng của ứng dụng.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-006`.

## 3. Nguồn tiêu chuẩn
- ISO 9241-210:2019 (Human-centred design for interactive systems)

## 4. Đầu vào bắt buộc
Danh mục màn hình/trang, luồng điều hướng người dùng, danh sách component giao diện.

## 5. Cấu trúc trường bắt buộc
Nguyên tắc thiết kế & Style guide, Danh mục màn hình (Sitemap), Luồng điều hướng, Đặc tả component UI, Quy chuẩn Responsive & Khả năng tiếp cận (Accessibility - a11y).

## 6. Quy tắc nội dung
1. Dựa trên các trang/views/components thực tế trong mã nguồn Frontend (React, Vue, Angular, Mobile).
2. Mô tả rõ trạng thái của component: Default, Hover, Active, Disabled, Loading, Error.
3. Không tự tạo thiết kế màn hình không khớp với logic nghiệp vụ.

## 7. Tiêu chí chất lượng
Các tương tác người dùng được mô tả mạch lạc.

## 8. Quy tắc đặt tên
`DOC-ARCH-006_UI_UX_Specification.docx`.

## 9. Truy xuất nguồn gốc
Hiện thực hóa `DOC-REQ-005` (Use Cases) cho giao diện.

## 10. Cách kiểm tra
Kiểm tra đối chiếu với danh mục thư mục components/views trong frontend.

## 11. Ngoại lệ
Dự án thuần Backend/API (Headless) không cần tài liệu này (`is_optional: true`).

## 12. Ví dụ
- Hợp lệ: Nút "Thanh toán": Trạng thái Loading hiển thị spinner và disable click.
- Không hợp lệ: Mô tả chung chung "giao diện đẹp mắt".

## 13. Tài liệu liên quan
`DOC-REQ-005`, `DOC-DEL-010`.

## 14. Bằng chứng cần thiết
Source code components hoặc Figma link (nếu có).

## 15. Giới hạn đã biết
Không thể tự tạo mockups đồ họa cao cấp nếu không có design assets.
""")

write_rule("Architecture_Design", "Component_Diagram_Rules.md", """# RULE-ARCH-007: Component Diagram Rules

- **Mã quy tắc**: `RULE-ARCH-007`
- **Tên quy tắc**: Component Decomposition and Modular Interface Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Mô tả trực quan các thành phần phần mềm (packages, modules, microservices) và mối quan hệ phụ thuộc giữa chúng.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-007`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 & UML 2.5 Component Diagram standard

## 4. Đầu vào bắt buộc
Danh sách components, interfaces công khai, phụ thuộc (dependencies).

## 5. Cấu trúc trường bắt buộc
Danh mục Component, Định nghĩa Interfaces, Mã nguồn sơ đồ Mermaid (`flowchart TD` / `graph TD`), Giải thích phụ thuộc.

## 6. Quy tắc nội dung
1. Sơ đồ phản ánh đúng kiến trúc phân rã module thực tế trong code.
2. Lưu trữ mã nguồn sơ đồ dưới dạng tệp `.mmd` để chỉnh sửa được.
3. Chỉ rõ chiều phụ thuộc (Dependency direction) và giao thức truyền tải (HTTP, gRPC, Queue, Function call).

## 7. Tiêu chí chất lượng
Mã nguồn Mermaid hợp lệ và hiển thị rõ ràng các phân tầng.

## 8. Quy tắc đặt tên
`DOC-ARCH-007_Component_Diagram.mmd`.

## 9. Truy xuất nguồn gốc
Chi tiết hóa `DOC-ARCH-001` (SAD).

## 10. Cách kiểm tra
Kiểm tra cú pháp Mermaid flowchart.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Controller -> Service -> Repository -> Database Driver.
- Không hợp lệ: Mũi tên phụ thuộc lòng vòng không rõ hướng.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-ARCH-002`.

## 14. Bằng chứng cần thiết
Tệp package.json, go.mod hoặc cấu trúc modules.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Architecture_Design", "Deployment_Architecture_Rules.md", """# RULE-ARCH-008: Deployment Architecture Rules

- **Mã quy tắc**: `RULE-ARCH-008`
- **Tên quy tắc**: Infrastructure and Deployment Topology Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả hạ tầng phần cứng, mạng, container, cụm máy chủ và vị trí thực thi của các thành phần phần mềm.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-008`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 (Deployment Viewpoint)

## 4. Đầu vào bắt buộc
Cấu hình Docker, Kubernetes, CI/CD, máy chủ, mạng, cổng (ports).

## 5. Cấu trúc trường bắt buộc
Topo triển khai (Topology), Phân bổ Node & Tài nguyên, Mạng & Cổng kết nối, Mã nguồn sơ đồ Mermaid Deployment, Cấu hình phục hồi sau sự cố (DR).

## 6. Quy tắc nội dung
1. Phải dựa trên các tệp cấu hình triển khai thực tế (`Dockerfile`, `docker-compose.yml`, Helm charts, k8s manifests).
2. Lưu trữ mã nguồn sơ đồ Mermaid để có thể hiệu chỉnh.
3. Phân biệt rõ các môi trường: Development, Staging, Production.

## 7. Tiêu chí chất lượng
Mọi cổng dịch vụ (ports) và kết nối mạng phải có căn cứ từ cấu hình.

## 8. Quy tắc đặt tên
`DOC-ARCH-008_Deployment_Architecture.mmd`.

## 9. Truy xuất nguồn gốc
Cơ sở để viết `DOC-DEL-011` (Installation Guide) và `DOC-DEL-013` (Deployment Guide).

## 10. Cách kiểm tra
Kiểm tra sự phù hợp giữa Dockerfile/docker-compose và sơ đồ triển khai.

## 11. Ngoại lệ
Ứng dụng serverless mô tả theo kiến trúc cloud functions và gateway.

## 12. Ví dụ
- Hợp lệ: Nginx reverse proxy (Port 80/443) -> Web App container (Port 3000) -> PostgreSQL container (Port 5432).
- Không hợp lệ: Bịa đặt cụm Kubernetes đa vùng trong khi dự án chỉ chạy trên 1 VPS đơn lẻ.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-DEL-011`, `DOC-DEL-013`.

## 14. Bằng chứng cần thiết
Tệp Dockerfile, docker-compose.yml, CI/CD workflows.

## 15. Giới hạn đã biết
Không thể truy cập thông tin hạ tầng nội bộ nếu không có file cấu hình.
""")

write_rule("Architecture_Design", "Technical_Design_Rules.md", """# RULE-ARCH-009: Technical Design Document Rules

- **Mã quy tắc**: `RULE-ARCH-009`
- **Tên quy tắc**: Technical Design and Security Realization Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc lập tài liệu thiết kế kỹ thuật hợp nhất cho các tính năng phức tạp, kết hợp kiến trúc, thuật toán và kiểm soát bảo mật OWASP.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-009`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022
- OWASP Top 10:2021

## 4. Đầu vào bắt buộc
Kiến trúc tính năng, thuật toán, mô hình bảo mật.

## 5. Cấu trúc trường bắt buộc
Tổng quan kỹ thuật, Thiết kế giải pháp chi tiết, Thuật toán & Cấu trúc dữ liệu, Kiểm soát bảo mật (OWASP defenses), Cân nhắc hiệu năng & Khả năng mở rộng.

## 6. Quy tắc nội dung
1. Tích hợp trực tiếp các biện pháp phòng ngừa rủi ro bảo mật OWASP (chống SQL Injection, XSS, CSRF, Broken Auth).
2. Phân tích rõ các đánh đổi kỹ thuật (Trade-offs): CPU vs Memory, Latency vs Consistency.

## 7. Tiêu chí chất lượng
Các giải pháp kỹ thuật có luận chứng chặt chẽ.

## 8. Quy tắc đặt tên
`DOC-ARCH-009_Technical_Design_Document.docx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-ARCH-001` và `DOC-REQ-004` (NFR).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của mục Security Controls.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Thuật toán hash mật khẩu sử dụng bcrypt với salt rounds = 12 để chống brute-force.
- Không hợp lệ: Không đề cập đến phương thức bảo vệ mật khẩu.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-REQ-004`.

## 14. Bằng chứng cần thiết
Source code xử lý thuật toán và mã hóa.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Architecture_Design", "ADR_Rules.md", """# RULE-ARCH-010: Architecture Decision Record Rules

- **Mã quy tắc**: `RULE-ARCH-010`
- **Tên quy tắc**: Architecture Decision Record (ADR) Integrity Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Ghi nhận bối cảnh, quyết định, các phương án cân nhắc, hệ quả và trạng thái của một quyết định kiến trúc quan trọng theo chuẩn Michael Nygard / ISO 42010.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-010`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 (Architecture decisions & rationale)
- ADR Standard format (Michael Nygard)

## 4. Đầu vào bắt buộc
Bối cảnh vấn đề, quyết định được chọn, các phương án đã cân nhắc, hệ quả (tích cực và tiêu cực).

## 5. Cấu trúc trường bắt buộc
ADR ID & Title, Status (Proposed / Accepted / Deprecated / Superseded), Context, Considered Options, Decision Outcome & Rationale, Consequences (Positive & Negative).

## 6. Quy tắc nội dung
1. Mỗi quyết định kiến trúc lớn phải có một bản ghi ADR riêng.
2. BẮT BUỘC phải nêu cả hệ quả tiêu cực (Trade-offs / Negatives) của quyết định, không có giải pháp nào là hoàn hảo tuyệt đối.
3. Không tự tạo quyết định là "Accepted" khi chưa có sự phê chuẩn của Tech Lead / Architect.

## 7. Tiêu chí chất lượng
Nêu bật lý do chọn và lý do loại bỏ các phương án khác.

## 8. Quy tắc đặt tên
`DOC-ARCH-010_ADR_{NUMBER}_{Title}.md`.

## 9. Truy xuất nguồn gốc
Hậu thuẫn cho các lựa chọn trong `DOC-ARCH-001` (SAD) và `DOC-DEL-005` (Decision Log).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của phần `Consequences` và `Considered Options`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Quyết định sử dụng PostgreSQL thay vì MongoDB vì yêu cầu tính toàn vẹn giao dịch ACID cao. Hệ quả tiêu cực: Khó mở rộng ngang hơn NoSQL."
- Không hợp lệ: Chỉ ghi "Chọn PostgreSQL vì nó tốt" mà không nêu bối cảnh và hệ quả.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-DEL-005`.

## 14. Bằng chứng cần thiết
Thảo luận kỹ thuật hoặc ghi chú trong repository.

## 15. Giới hạn đã biết
Không có.
""")

print("Architecture rules created successfully.")

# ==============================================================================
# TESTING & QUALITY RULES (8 files)
# ==============================================================================

write_rule("Testing_Quality", "Test_Plan_Rules.md", """# RULE-TEST-001: Software Test Plan Rules

- **Mã quy tắc**: `RULE-TEST-001`
- **Tên quy tắc**: Test Strategy and ISO 29119-3 Test Plan Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định phương pháp lập Kế hoạch Kiểm thử Phần mềm (Test Plan) theo tiêu chuẩn quốc tế ISO/IEC/IEEE 29119-3:2021.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-001`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-1:2022 (Concepts)
- ISO/IEC/IEEE 29119-2:2021 (Processes)
- ISO/IEC/IEEE 29119-3:2021 (Test Documentation)

## 4. Đầu vào bắt buộc
Phạm vi kiểm thử, các cấp độ kiểm thử (Unit, Integration, System, Acceptance), tiêu chí dừng/tiếp tục kiểm thử (Suspension & Resumption criteria).

## 5. Cấu trúc trường bắt buộc
Chiến lược & Phương pháp tiếp cận, Phạm vi kiểm thử (In-scope & Out-of-scope), Cấp độ kiểm thử, Tiêu chí bắt đầu & Kết thúc (Entry/Exit criteria), Yêu cầu môi trường, Lịch trình & Nhân sự.

## 6. Quy tắc nội dung
1. Phân biệt rõ thiết kế kiểm thử (Test Design) với thực thi kiểm thử (Test Execution).
2. Tiêu chí kết thúc kiểm thử (Exit criteria) phải rõ ràng (ví dụ: 100% Blocker/Critical bugs được đóng, Pass rate >= 95%).
3. Xác định rõ các loại kiểm thử: Kiểm thử chức năng, hiệu năng, bảo mật, tương thích.

## 7. Tiêu chí chất lượng
Kế hoạch kiểm thử bao phủ toàn bộ các yêu cầu trong phạm vi dự án.

## 8. Quy tắc đặt tên
`DOC-TEST-001_Test_Plan.docx`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-REQ-001` (SRS) và định hướng cho `DOC-TEST-003` (Test Cases).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của Entry và Exit criteria.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Exit criteria: Unit test pass rate = 100%, Integration test pass rate >= 98%, không còn lỗi mức Critical.
- Không hợp lệ: "Kiểm thử cho đến khi thấy phần mềm ổn."

## 13. Tài liệu liên quan
`DOC-REQ-001`, `DOC-TEST-003`, `DOC-TEST-004`.

## 14. Bằng chứng cần thiết
Yêu cầu kiểm thử và hạ tầng test.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Testing_Quality", "Test_Scenario_Rules.md", """# RULE-TEST-002: Test Scenario Rules

- **Mã quy tắc**: `RULE-TEST-002`
- **Tên quy tắc**: Test Scenario Design and Technique Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định việc thiết kế các kịch bản kiểm thử (Test Scenarios) theo ISO/IEC/IEEE 29119-4.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-002`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-3:2021 & ISO/IEC/IEEE 29119-4:2021 (Test Techniques)

## 4. Đầu vào bắt buộc
Mã tính năng, mô tả kịch bản, kỹ thuật kiểm thử áp dụng.

## 5. Cấu trúc trường bắt buộc
Scenario ID, Feature Ref, Tiêu đề kịch bản, Mô tả, Kỹ thuật áp dụng (Phân vùng tương đương, Giá trị biên, Bảng quyết định), Mức độ ưu tiên.

## 6. Quy tắc nội dung
1. Mỗi kịch bản đại diện cho một luồng nghiệp vụ hoàn chỉnh từ đầu đến cuối.
2. Bao quát cả kịch bản tích cực (Positive scenarios) và tiêu cực (Negative scenarios).

## 7. Tiêu chí chất lượng
Kịch bản mô tả rõ ràng mục tiêu kiểm chứng.

## 8. Quy tắc đặt tên
`DOC-TEST-002_Test_Scenario.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết `DOC-REQ-005` (Use Case) tới `DOC-TEST-003` (Test Case).

## 10. Cách kiểm tra
Kiểm tra ID dạng `TS-{MODULE}-{NUMBER}`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `TS-AUTH-001`: Đăng nhập thành công với tài khoản hợp lệ. `TS-AUTH-002`: Khóa tài khoản sau 5 lần nhập sai mật khẩu liên tiếp.
- Không hợp lệ: Kịch bản mơ hồ không rõ điều kiện.

## 13. Tài liệu liên quan
`DOC-REQ-005`, `DOC-TEST-003`.

## 14. Bằng chứng cần thiết
Ca sử dụng và luồng nghiệp vụ.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Testing_Quality", "Test_Case_Rules.md", """# RULE-TEST-003: Test Case Specification Rules

- **Mã quy tắc**: `RULE-TEST-003`
- **Tên quy tắc**: Test Case Specificity and Verifiability Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả chi tiết từng ca kiểm thử (Test Case) theo tiêu chuẩn ISO/IEC/IEEE 29119-3:2021.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-003`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-3:2021 (Test Case Specification)
- ISO/IEC/IEEE 29119-4:2021 (Test design techniques)

## 4. Đầu vào bắt buộc
Tiền điều kiện, dữ liệu kiểm thử đầu vào, các bước thực hiện từng bước, kết quả mong đợi.

## 5. Cấu trúc trường bắt buộc
Test Case ID, Tham chiếu Scenario/Requirement, Tiêu đề, Tiền điều kiện (Preconditions), Các bước thực hiện & Dữ liệu đầu vào (Steps & Input Data), Kết quả mong đợi (Expected Result), Phương pháp xác minh.

## 6. Quy tắc nội dung
1. Test Case phải có tính lặp lại (Repeatable): Bất kỳ kiểm thử viên nào đọc cũng có thể thực thi chính xác như nhau.
2. Kết quả mong đợi phải chi tiết, đo lường được (không viết "chạy bình thường").
3. PHÂN BIỆT RẠCH RÒI: Test Case Specification chỉ định nghĩa "Kết quả mong đợi" (Expected Result), KHÔNG ĐƯỢC tự điền "Kết quả thực tế" (Actual Result). Kết quả thực tế chỉ thuộc về Test Execution Report khi đã chạy thật.

## 7. Tiêu chí chất lượng
Các bước thực hiện rõ ràng, có dữ liệu cụ thể.

## 8. Quy tắc đặt tên
`DOC-TEST-003_Test_Case_Specification.xlsx`.

## 9. Truy xuất nguồn gốc
Phải trỏ tới `DOC-REQ-003` (Functional Requirements) và `DOC-REQ-007` (RTM).

## 10. Cách kiểm tra
Kiểm tra cấu trúc ID dạng `TC-{MODULE}-{NUMBER}` và trường Expected Result.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Bước 1: Truy cập `/login`. Bước 2: Nhập email `test@example.com`, pass `Secret123!`. Bước 3: Bấm Đăng nhập. Kết quả mong đợi: Chuyển hướng sang `/dashboard`, hiển thị thông báo 'Chào mừng' và cookie JWT được lưu."
- Không hợp lệ: "Kiểm tra xem login có được không."

## 13. Tài liệu liên quan
`DOC-TEST-002`, `DOC-TEST-004`, `DOC-REQ-007`.

## 14. Bằng chứng cần thiết
Code logic và tiêu chí chấp nhận.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Testing_Quality", "Test_Execution_Rules.md", """# RULE-TEST-004: Test Execution Report Rules

- **Mã quy tắc**: `RULE-TEST-004`
- **Tên quy tắc**: Test Execution Authenticity and Zero-Fake-Pass Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định nguyên tắc ghi nhận kết quả thực thi kiểm thử thực tế và nghiêm cấm tuyệt đối việc tạo kết quả kiểm thử giả.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-004`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-2:2021 & ISO/IEC/IEEE 29119-3:2021 (Test Execution Log & Report)

## 4. Đầu vào bắt buộc
Ngày thực thi thực tế, kết quả thực tế quan sát được, trạng thái thực thi (`PASS`, `FAIL`, `BLOCKED`, `NOT_EXECUTED`), tệp log/bằng chứng.

## 5. Cấu trúc trường bắt buộc
Run ID, Ngày thực thi, Cấu hình môi trường, Test Case ID, Kết quả thực tế quan sát được (Actual Result Observed), Trạng thái thực thi, Bằng chứng thực thi (Log/Screenshot), Tham chiếu Bug ID (nếu Fail).

## 6. Quy tắc nội dung BẮT BUỘC
1. **NGUYÊN TẮC ZERO-FAKE-PASS**:
   - Tuyệt đối KHÔNG tự sao chép "Kết quả mong đợi" thành "Kết quả thực tế".
   - Chỉ được ghi trạng thái `PASS` khi có tệp log thực thi thật (JUnit XML, Playwright trace, Jest report, console output thực) chứng minh test case đã chạy và thành công.
   - Nếu test case chưa được chạy trong phiên làm việc, BẮT BUỘC ghi trạng thái là `NOT_EXECUTED`.
2. Mọi ca kiểm thử bị `FAIL` phải liên kết trực tiếp tới một mã lỗi trong `DOC-TEST-005` (Bug Report).
3. Không tự tạo ngày chạy kiểm thử, tên người chạy test hoặc số liệu pass rate ảo.

## 7. Tiêu chí chất lượng
100% kết quả PASS có bằng chứng log đi kèm.

## 8. Quy tắc đặt tên
`DOC-TEST-004_Test_Execution_Report.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết giữa `DOC-TEST-003` (Test Case) và `DOC-TEST-005` (Bug Report).

## 10. Cách kiểm tra
Bài kiểm thử `test_validation.py` quét kiểm tra cấm kết quả giả mạo.

## 11. Ngoại lệ
Không có ngoại lệ đối với việc cấm tạo test pass giả.

## 12. Ví dụ
- Hợp lệ: "Test Case `TC-AUTH-001`: Trạng thái `NOT_EXECUTED` (Chưa chạy kiểm thử tự động trong môi trường này)."
- Không hợp lệ: Tự ý ghi "Trạng thái PASS 100/100 ca" trong khi chưa chạy bất kỳ lệnh test nào.

## 13. Tài liệu liên quan
`DOC-TEST-003`, `DOC-TEST-005`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Tệp test results XML/JSON hoặc console log từ runner.

## 15. Giới hạn đã biết
Nếu workspace không có công cụ chạy test (ví dụ thiếu browser cho e2e), phải ghi nhận `NOT_EXECUTED`.
""")

write_rule("Testing_Quality", "Bug_Report_Rules.md", """# RULE-TEST-005: Defect / Bug Report Rules

- **Mã quy tắc**: `RULE-TEST-005`
- **Tên quy tắc**: Defect Reporting Structure and Reproducibility Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định cấu trúc báo cáo sự cố phần mềm (Bug Report) theo ISO/IEC/IEEE 29119-3:2021 đảm bảo khả năng tái hiện lỗi.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-005`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-3:2021 (Incident / Defect Report)

## 4. Đầu vào bắt buộc
Hành vi thực tế quan sát được, hành vi mong đợi, các bước tái hiện, mức độ nghiêm trọng (Severity: Blocker/Critical/Major/Minor), môi trường phát hiện.

## 5. Cấu trúc trường bắt buộc
Defect ID, Tóm tắt lỗi, Test Case/Requirement liên quan, Severity, Priority, Môi trường, Các bước tái hiện (Steps to Reproduce), Kết quả mong đợi vs Kết quả thực tế, Bằng chứng (Log/Stack trace), Trạng thái (Open/In Progress/Fixed/Closed).

## 6. Quy tắc nội dung
1. Các bước tái hiện phải được ghi chi tiết từng bước, kèm dữ liệu đầu vào cụ thể.
2. Đính kèm log lỗi hoặc stack trace thực tế khi có.
3. Phân biệt rõ mức độ nghiêm trọng kỹ thuật (Severity) và mức độ ưu tiên xử lý kinh doanh (Priority).

## 7. Tiêu chí chất lượng
Lập trình viên có thể tái hiện được lỗi chỉ dựa vào mô tả trong báo cáo.

## 8. Quy tắc đặt tên
`DOC-TEST-005_Bug_Report.xlsx`.

## 9. Truy xuất nguồn gốc
Trỏ từ `DOC-TEST-004` (Test Run) và liên kết tới `DOC-DEL-004` (Issue Log).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của `steps_to_reproduce` và `severity`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "BUG-001: Lỗi 500 khi email chứa dấu cộng. Các bước tái hiện: 1. Đăng ký với `a+b@test.com`. Kết quả mong đợi: Tạo tài khoản thành công. Thực tế: Ném NullPointerException tại UserController:45."
- Không hợp lệ: "Website bị lỗi rồi sửa đi."

## 13. Tài liệu liên quan
`DOC-TEST-004`, `DOC-DEL-004`.

## 14. Bằng chứng cần thiết
Stack trace, server logs, network payload.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Testing_Quality", "UAT_Rules.md", """# RULE-TEST-006: User Acceptance Testing Rules

- **Mã quy tắc**: `RULE-TEST-006`
- **Tên quy tắc**: User Acceptance Testing Signoff Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Ghi nhận kết quả kiểm thử nghiệm thu người dùng (UAT) và quy định thẩm quyền ký duyệt nghiệm thu.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-006`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-3:2021 & ISO 21500

## 4. Đầu vào bắt buộc
Kịch bản nghiệm thu người dùng, danh sách người tham gia UAT, kết quả đánh giá, quyết định nghiệm thu.

## 5. Cấu trúc trường bắt buộc
Phạm vi & Môi trường UAT, Kịch bản nghiệp vụ đã nghiệm thu, Danh sách người tham gia & Vai trò, Tồn đọng còn mở, Quyết định nghiệm thu chính thức (Signoff).

## 6. Quy tắc nội dung
1. Tuyệt đối KHÔNG tự động đánh dấu chấp nhận nghiệm thu (Accepted) khi chưa có sự xác nhận của người dùng hoặc đại diện nghiệp vụ có thẩm quyền.
2. Mọi tồn đọng chưa được giải quyết phải được ghi rõ kèm điều kiện chấp nhận (ví dụ: Chấp nhận có điều kiện).

## 7. Tiêu chí chất lượng
Có chữ ký hoặc biên bản xác nhận đính kèm.

## 8. Quy tắc đặt tên
`DOC-TEST-006_UAT_Record.docx`.

## 9. Truy xuất nguồn gốc
Làm căn cứ pháp lý cho `DOC-DEL-012` (Project Handover Report).

## 10. Cách kiểm tra
Kiểm tra trường quyết định nghiệm thu.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Biên bản UAT ghi nhận người dùng Nguyễn Văn A (Đại diện phòng Kế toán) xác nhận đạt yêu cầu ngày 28/10/2026.
- Không hợp lệ: Agent tự ý ghi "Đã nghiệm thu thành công bởi ban giám đốc" mà không có căn cứ.

## 13. Tài liệu liên quan
`DOC-REQ-008`, `DOC-DEL-012`.

## 14. Bằng chứng cần thiết
Email xác nhận hoặc văn bản ký duyệt UAT.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Testing_Quality", "Code_Review_Rules.md", """# RULE-TEST-007: Code Review Checklist Rules

- **Mã quy tắc**: `RULE-TEST-007`
- **Tên quy tắc**: Code Review Checklist and Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định danh mục kiểm tra mã nguồn (Code Review Checklist) nhằm đảm bảo an toàn bảo mật OWASP, hiệu năng và chất lượng mã trước khi merge.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-007`.

## 3. Nguồn tiêu chuẩn
- OWASP Secure Coding Practices
- Clean Code Standards

## 4. Đầu vào bắt buộc
Các tiêu chí kiểm tra: Cú pháp, phong cách, bảo mật, hiệu năng, kiểm thử tự động.

## 5. Cấu trúc trường bắt buộc
Các danh mục kiểm tra: Quy chuẩn mã nguồn, Kiểm soát an toàn bảo mật (OWASP), Quản lý tài nguyên & Hiệu năng, Độ bao phủ kiểm thử, Quy tắc thẩm định của Reviewer.

## 6. Quy tắc nội dung
1. Phải quy định rõ: Checklist là bộ tiêu chí hướng dẫn đánh giá, KHÔNG PHẢI là bằng chứng rằng code đã được review (phải có PR approvals thực tế trên GitHub/GitLab).
2. Kiểm tra các lỗi phổ biến: SQL Injection, Hardcoded secrets, Unhandled Promise rejections, Memory leaks.

## 7. Tiêu chí chất lượng
Checklist có thể áp dụng trực tiếp vào PR template của dự án.

## 8. Quy tắc đặt tên
`DOC-TEST-007_Code_Review_Checklist.md`.

## 9. Truy xuất nguồn gốc
Gắn liền với `DOC-SCRUM-014` (Definition of Done).

## 10. Cách kiểm tra
Kiểm tra các mục kiểm tra bảo mật trong checklist.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Checklist yêu cầu xác minh không có credential nhạy cảm trong code diff.
- Không hợp lệ: Tự tuyên bố "Code đã được review 100%" khi repo không có bất kỳ pull request approval nào.

## 13. Tài liệu liên quan
`DOC-SCRUM-014`.

## 14. Bằng chứng cần thiết
Pull request comments hoặc template file `.github/pull_request_template.md`.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Testing_Quality", "Quality_Metrics_Rules.md", """# RULE-TEST-008: Quality Metrics Report Rules

- **Mã quy tắc**: `RULE-TEST-008`
- **Tên quy tắc**: Quality Metrics Quantification and Sourcing Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc tính toán và báo cáo các chỉ số chất lượng phần mềm (Test Pass Rate, Code Coverage, Defect Density) dựa trên dữ liệu đo đạc thực tế.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-008`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-1:2022
- ISO/IEC 25010:2023

## 4. Đầu vào bắt buộc
Nguồn dữ liệu đo đạc, công thức tính toán, thời điểm đo, giá trị chỉ số thực tế.

## 5. Cấu trúc trường bắt buộc
Phạm vi & Khoảng thời gian đo, Nguồn dữ liệu & Công thức tính, Bảng chỉ số chất lượng (Pass Rate, Defect Density, Code Coverage), Phân tích & Hạn chế, Đánh giá ngưỡng mục tiêu.

## 6. Quy tắc nội dung
1. Mọi số liệu báo cáo phải nêu rõ công thức tính toán và nguồn công cụ đo đạc (ví dụ: SonarQube, Jest coverage, JaCoCo, pytest-cov).
2. Tuyệt đối không tự bịa đặt chỉ số code coverage (ví dụ: ghi 95% khi dự án không có file coverage report nào).
3. Nếu chưa đo đạc được, phải ghi rõ `NOT_MEASURED` kèm lý do kỹ thuật.

## 7. Tiêu chí chất lượng
Chỉ số có nguồn dữ liệu đối chiếu minh bạch.

## 8. Quy tắc đặt tên
`DOC-TEST-008_Quality_Metrics_Report.xlsx`.

## 9. Truy xuất nguồn gốc
Hỗ trợ dữ liệu cho `DOC-DEL-008` (Progress Report).

## 10. Cách kiểm tra
Kiểm tra tệp coverage hoặc test log tương ứng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Code coverage: 82.4% dựa trên báo cáo `coverage/lcov.info` tạo ngày 28/10/2026."
- Không hợp lệ: Tự điền 100% test pass rate và 100% coverage mà không có log.

## 13. Tài liệu liên quan
`DOC-TEST-004`, `DOC-DEL-008`.

## 14. Bằng chứng cần thiết
Tệp `coverage.xml`, `lcov.info` hoặc log thực thi CI.

## 15. Giới hạn đã biết
Không có.
""")

print("Testing rules created successfully.")

# ==============================================================================
# DELIVERY RULES (13 files)
# ==============================================================================

write_rule("Delivery", "Project_Schedule_Rules.md", """# RULE-DEL-001: Project Schedule Rules

- **Mã quy tắc**: `RULE-DEL-001`
- **Tên quy tắc**: Master Project Schedule and Milestone Tracking Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định cấu trúc và nguyên tắc quản lý tiến độ tổng thể, các mốc quan trọng (Milestones) theo ISO 21500.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-001`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6.4 (Schedule management)

## 4. Đầu vào bắt buộc
Các mốc bàn giao chính, ngày bắt đầu và kết thúc từng giai đoạn, tiến độ thực tế.

## 5. Cấu trúc trường bắt buộc
Các mốc dự án (Milestones), Tiến độ các gói công việc (Work Packages), Ngày kế hoạch vs Ngày thực tế, Tỷ lệ hoàn thành %, Phân tích độ lệch tiến độ (Schedule Variance).

## 6. Quy tắc nội dung
1. Không tự tạo ngày phát hành, cam kết mốc nếu chưa có kế hoạch được phê duyệt.
2. Các mốc phải có tính khả thi và logic thứ tự trước sau (Predecessor/Successor).

## 7. Tiêu chí chất lượng
Tiến độ các giai đoạn không mâu thuẫn với lịch Sprint (`DOC-SCRUM-010`).

## 8. Quy tắc đặt tên
`DOC-DEL-001_Project_Schedule.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-DEL-002` (WBS) và `DOC-DEL-008` (Progress Report).

## 10. Cách kiểm tra
Kiểm tra tính nhất quán giữa ngày bắt đầu và kết thúc của các giai đoạn.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Milestone M1: Hoàn thành thiết kế kiến trúc vào 15/11/2026.
- Không hợp lệ: Ghi nhận dự án đã hoàn thành trong khi mã nguồn mới ở giai đoạn dựng khung.

## 13. Tài liệu liên quan
`DOC-DEL-002`, `DOC-SCRUM-010`, `DOC-DEL-008`.

## 14. Bằng chứng cần thiết
Kế hoạch tiến độ dự án.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "WBS_Rules.md", """# RULE-DEL-002: Work Breakdown Structure Rules

- **Mã quy tắc**: `RULE-DEL-002`
- **Tên quy tắc**: WBS Decomposition and 100% Rule
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc phân rã toàn bộ phạm vi dự án thành các gói công việc quản lý được theo ISO 21500.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-002`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 & PMI WBS Practice Standard

## 4. Đầu vào bắt buộc
Danh mục kết quả bàn giao, các gói công việc chi tiết.

## 5. Cấu trúc trường bắt buộc
Mã WBS (WBS Code dạng 1.1, 1.1.1), Cấp độ (Level), Tên gói công việc, Mô tả công việc, Kết quả bàn giao (Deliverable), Tiêu chí hoàn thành.

## 6. Quy tắc nội dung
1. Tuân thủ **Quy tắc 100% (100% Rule)**: WBS phải bao gồm toàn bộ 100% công việc được định nghĩa trong phạm vi dự án, không thừa và không thiếu.
2. Cấp thấp nhất của WBS là Gói công việc (Work Package), có thể gán người chịu trách nhiệm và ước tính chi phí, thời gian.

## 7. Tiêu chí chất lượng
Mã phân cấp WBS chuẩn xác, không nhảy cóc.

## 8. Quy tắc đặt tên
`DOC-DEL-002_WBS.xlsx`.

## 9. Truy xuất nguồn gốc
Phân rã từ `DOC-PM-002` (Scope Statement).

## 10. Cách kiểm tra
Kiểm tra cấu trúc phân cấp số của `wbs_code`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `1.0 Hệ thống E-Commerce` -> `1.1 Module Giỏ hàng` -> `1.1.1 Xây dựng logic tính thuế`.
- Không hợp lệ: Liệt kê các đầu mục lộn xộn không có cấu trúc phân cấp.

## 13. Tài liệu liên quan
`DOC-PM-002`, `DOC-DEL-001`.

## 14. Bằng chứng cần thiết
Danh mục phạm vi công việc.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Risk_Register_Rules.md", """# RULE-DEL-003: Risk Register Rules

- **Mã quy tắc**: `RULE-DEL-003`
- **Tên quy tắc**: Risk Identification and Mitigation Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc nhận diện, đánh giá xác suất, tác động và kế hoạch giảm thiểu rủi ro dự án theo ISO 21500 và ISO 31000.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-003`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6.7 (Risk management) & ISO 31000:2018

## 4. Đầu vào bắt buộc
Mô tả rủi ro, xác suất xảy ra (Probability), mức độ tác động (Impact), chiến lược ứng phó.

## 5. Cấu trúc trường bắt buộc
Risk ID, Mô tả rủi ro, Xác suất (1-5 hoặc Thấp/TB/Cao), Tác động (1-5), Điểm rủi ro (Risk Score), Chiến lược giảm thiểu (Mitigation), Kế hoạch dự phòng (Contingency), Người chịu trách nhiệm (Owner), Trạng thái.

## 6. Quy tắc nội dung
1. Mỗi rủi ro phải phân tích rõ nguyên nhân gốc rễ và hệ quả nếu xảy ra.
2. Bắt buộc phải có hành động giảm thiểu cụ thể và người theo dõi.
3. Nếu rủi ro trở thành hiện thực, nó phải được chuyển sang theo dõi tại `DOC-DEL-004` (Issue Log).

## 7. Tiêu chí chất lượng
Tính điểm rủi ro nhất quán: `Risk Score = Probability * Impact`.

## 8. Quy tắc đặt tên
`DOC-DEL-003_Risk_Register.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-DEL-004` (Issue Log) và `DOC-DEL-005` (Decision Log).

## 10. Cách kiểm tra
Kiểm tra công thức tính điểm và trường hành động giảm thiểu.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `RISK-001`: Nghẽn cổng thanh toán bên thứ ba vào giờ cao điểm. Giảm thiểu: Tích hợp thêm cổng thanh toán dự phòng B.
- Không hợp lệ: Ghi rủi ro chung chung "Dự án có thể gặp rủi ro."

## 13. Tài liệu liên quan
`DOC-PM-001`, `DOC-DEL-004`.

## 14. Bằng chứng cần thiết
Đánh giá rủi ro kỹ thuật và vận hành.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Issue_Log_Rules.md", """# RULE-DEL-004: Issue Log Rules

- **Mã quy tắc**: `RULE-DEL-004`
- **Tên quy tắc**: Issue Resolution and Escalation Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Ghi nhận và theo dõi các vấn đề thực tế phát sinh trong dự án cần hành động giải quyết.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-004`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021

## 4. Đầu vào bắt buộc
Mô tả sự cố, mức độ ảnh hưởng, người phụ trách xử lý, phương án giải quyết.

## 5. Cấu trúc trường bắt buộc
Issue ID, Ngày phát hiện, Mô tả vấn đề, Mức độ nghiêm trọng, Rủi ro/PBI liên quan, Người phụ trách, Kế hoạch hành động, Hạn xử lý, Trạng thái (Open/In Progress/Resolved/Closed).

## 6. Quy tắc nội dung
1. Phân biệt rõ RỦI RO (chưa xảy ra, chỉ có xác suất) và VẤN ĐỀ / SỰ CỐ (đã thực sự xảy ra).
2. Mọi sự cố phải có hạn chót giải quyết (Target Resolution Date) và cập nhật tiến độ thường xuyên.

## 7. Tiêu chí chất lượng
Các sự cố nghiêm trọng (Blocker) phải có phương án xử lý ngay trong 24-48 giờ.

## 8. Quy tắc đặt tên
`DOC-DEL-004_Issue_Log.xlsx`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-DEL-003` và báo cáo trong `DOC-DEL-008`.

## 10. Cách kiểm tra
Kiểm tra trạng thái của các issue quá hạn.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `ISSUE-001`: Khóa tài khoản Google Cloud do hết hạn thẻ thanh toán. Hành động: Cập nhật thẻ công ty và mở lại dịch vụ.
- Không hợp lệ: Ghi nhận sự cố mà không có người phụ trách.

## 13. Tài liệu liên quan
`DOC-DEL-003`, `DOC-DEL-008`.

## 14. Bằng chứng cần thiết
Biên bản sự cố hoặc log hệ thống.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Decision_Log_Rules.md", """# RULE-DEL-005: Decision Log Rules

- **Mã quy tắc**: `RULE-DEL-005`
- **Tên quy tắc**: Project Decision Tracking and Rationale Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Ghi nhận các quyết định quản lý và nghiệp vụ quan trọng trong dự án, người ra quyết định và lý do.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-005`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Governance & Change Control)

## 4. Đầu vào bắt buộc
Chủ đề quyết định, nội dung quyết định, người/cấp có thẩm quyền quyết định, lý do.

## 5. Cấu trúc trường bắt buộc
Decision ID, Ngày quyết định, Vấn đề/Chủ đề, Quyết định được đưa ra, Người phê duyệt, Lý do & Các phương án thay thế, Phạm vi ảnh hưởng, Trạng thái.

## 6. Quy tắc nội dung
1. Tuyệt đối không tự bịa đặt các quyết định quan trọng khi chưa có biên bản hoặc sự đồng thuận của người dùng.
2. Ghi nhận rõ ràng căn cứ tại sao quyết định được đưa ra.

## 7. Tiêu chí chất lượng
Quyết định có căn cứ pháp lý hoặc biên bản họp đối chiếu.

## 8. Quy tắc đặt tên
`DOC-DEL-005_Decision_Log.xlsx`.

## 9. Truy xuất nguồn gốc
Tương hỗ với `DOC-ARCH-010` (ADR) và `DOC-DEL-007` (Meeting Minutes).

## 10. Cách kiểm tra
Kiểm tra trường `decision_maker` không được rỗng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `DEC-001`: Lựa chọn dịch vụ AWS thay vì Azure do đội ngũ đã có kinh nghiệm sâu về AWS. Người quyết định: CTO.
- Không hợp lệ: Tự ý ghi "Đã quyết định thay đổi toàn bộ ngôn ngữ lập trình."

## 13. Tài liệu liên quan
`DOC-ARCH-010`, `DOC-DEL-007`.

## 14. Bằng chứng cần thiết
Email hoặc biên bản xác nhận quyết định.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Change_Request_Rules.md", """# RULE-DEL-006: Change Request Rules

- **Mã quy tắc**: `RULE-DEL-006`
- **Tên quy tắc**: Change Control and Impact Analysis Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định quy trình kiểm soát thay đổi (Change Control): ghi nhận, đánh giá tác động và phê duyệt thay đổi phạm vi, tiến độ hoặc chi phí.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-006`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 & ISO/IEC/IEEE 29148:2018

## 4. Đầu vào bắt buộc
Mô tả thay đổi, lý do yêu cầu, đánh giá tác động (Impact Analysis) đến phạm vi, thời gian và chi phí.

## 5. Cấu trúc trường bắt buộc
CR ID, Ngày yêu cầu, Người yêu cầu, Mô tả thay đổi, Phân tích tác động (Scope, Schedule, Cost, Quality), Trạng thái phê duyệt (Pending/Approved/Rejected), Bằng chứng triển khai.

## 6. Quy tắc nội dung
1. Mọi thay đổi làm ảnh hưởng tới phạm vi đã duyệt (Baseline Scope) phải được lập phiếu Yêu cầu Thay đổi (CR).
2. Phải phân tích tác động toàn diện trước khi trình cấp có thẩm quyền phê duyệt.
3. Không tự ý thực hiện thay đổi khi CR chưa được phê duyệt chính thức.

## 7. Tiêu chí chất lượng
Đánh giá tác động định lượng rõ số ngày trễ hạn hoặc chi phí phát sinh nếu có.

## 8. Quy tắc đặt tên
`DOC-DEL-006_Change_Request_Log.xlsx`.

## 9. Truy xuất nguồn gốc
Cập nhật vào `DOC-REQ-001` (SRS) và `DOC-DEL-001` (Schedule).

## 10. Cách kiểm tra
Kiểm tra trường phân tích tác động không rỗng.

## 11. Ngoại lệ
Các thay đổi nhỏ bên trong Sprint do PO và Developers thỏa thuận theo quy tắc Scrum không cần phiếu CR hợp đồng nặng nề.

## 12. Ví dụ
- Hợp lệ: `CR-001`: Yêu cầu bổ sung cổng thanh toán Apple Pay. Đánh giá tác động: Tăng thêm 5 ngày công, không đổi ngày release.
- Không hợp lệ: Thay đổi tính năng âm thầm không qua kiểm soát.

## 13. Tài liệu liên quan
`DOC-PM-002`, `DOC-REQ-001`.

## 14. Bằng chứng cần thiết
Phiếu yêu cầu thay đổi có chữ ký duyệt.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Meeting_Minutes_Rules.md", """# RULE-DEL-007: Meeting Minutes Rules

- **Mã quy tắc**: `RULE-DEL-007`
- **Tên quy tắc**: Meeting Minutes Authenticity and Action Tracking Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc lập biên bản cuộc họp dự án dựa trên cuộc họp thực tế đã diễn ra.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-007`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Communications Management)

## 4. Đầu vào bắt buộc
Ngày họp, thời gian, địa điểm, thành phần tham dự, các nội dung thảo luận chính, quyết định đạt được, các hành động tiếp theo.

## 5. Cấu trúc trường bắt buộc
Thông tin phiên họp, Danh sách tham dự & Vắng mặt, Chủ đề chương trình, Thảo luận chính, Quyết định đã thống nhất, Danh sách hành động (Action, Người phụ trách, Hạn chót).

## 6. Quy tắc nội dung
1. Tuyệt đối KHÔNG tự tạo biên bản cuộc họp giả khi cuộc họp chưa diễn ra trên thực tế.
2. Không tự bịa đặt danh sách người tham dự hoặc chữ ký biên bản.
3. Mỗi hành động phát sinh sau cuộc họp phải có người phụ trách (Owner) và hạn hoàn thành rõ ràng.

## 7. Tiêu chí chất lượng
Ghi chép trung thực các kết luận và phân công trách nhiệm.

## 8. Quy tắc đặt tên
`DOC-DEL-007_Meeting_Minutes_{DATE}.docx`.

## 9. Truy xuất nguồn gốc
Hành động chuyển vào `DOC-DEL-004` hoặc Backlog.

## 10. Cách kiểm tra
Kiểm tra tính có thật của phiên họp qua log hoặc xác nhận của người dùng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Biên bản họp kỹ thuật ngày 25/10/2026 thống nhất phương án xử lý lỗi timeout với đối tác vận chuyển.
- Không hợp lệ: Agent tự bịa ra cuộc họp ngày hôm qua và tự điền tên người tham dự.

## 13. Tài liệu liên quan
`DOC-DEL-005`.

## 14. Bằng chứng cần thiết
Bản ghi âm, ghi chú cuộc họp hoặc email tóm tắt sau họp.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Progress_Report_Rules.md", """# RULE-DEL-008: Progress Report Rules

- **Mã quy tắc**: `RULE-DEL-008`
- **Tên quy tắc**: Periodic Progress Reporting and Objective Status Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Tổng hợp tình hình thực hiện, tiến độ, chỉ số, rủi ro và kế hoạch giai đoạn tiếp theo một cách trung thực và khách quan.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-008`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Performance Reporting)

## 4. Đầu vào bắt buộc
Kỳ báo cáo, các công việc đã hoàn thành, tình trạng tiến độ các mốc, các vấn đề và rủi ro nghiêm trọng, kế hoạch kỳ tới.

## 5. Cấu trúc trường bắt buộc
Kỳ báo cáo & Tác giả, Tóm tắt điều hành (Executive Summary), Thành tựu chính trong kỳ, Trạng thái mốc & Tiến độ, Các vấn đề & Rủi ro trọng yếu, Kế hoạch kỳ tiếp theo.

## 6. Quy tắc nội dung
1. Phản ánh trung thực tình trạng dự án: Trạng thái Xanh (On track), Vàng (Có rủi ro trễ), Đỏ (Đang trễ hạn nghiêm trọng).
2. Không tô hồng số liệu hoặc che giấu các vấn đề đang làm nghẽn tiến độ.

## 7. Tiêu chí chất lượng
Các số liệu hoàn thành phải đối chiếu được với commit git hoặc task completed trong Jira.

## 8. Quy tắc đặt tên
`DOC-DEL-008_Progress_Report_{PERIOD}.docx`.

## 9. Truy xuất nguồn gốc
Tổng hợp từ `DOC-DEL-001`, `DOC-DEL-003`, `DOC-DEL-004`, `DOC-TEST-008`.

## 10. Cách kiểm tra
Kiểm tra tính nhất quán giữa tiến độ báo cáo và trạng thái các deliverables.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Báo cáo trung thực: Module A hoàn thành 100%, Module B đang trễ 3 ngày do thiếu nhân sự backend.
- Không hợp lệ: Dự án đang gặp lỗi nghiêm trọng nhưng vẫn báo cáo "mọi thứ diễn ra hoàn hảo".

## 13. Tài liệu liên quan
`DOC-DEL-001`, `DOC-DEL-003`, `DOC-DEL-004`.

## 14. Bằng chứng cần thiết
Dữ liệu từ hệ thống quản lý công việc và CI/CD.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Release_Notes_Rules.md", """# RULE-DEL-009: Release Notes Rules

- **Mã quy tắc**: `RULE-DEL-009`
- **Tên quy tắc**: Release Documentation and Semantic Versioning Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Công bố các tính năng mới, sửa lỗi, cải tiến kỹ thuật, thay đổi đột phá (Breaking changes) và hướng dẫn nâng cấp của phiên bản phát hành.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-009`.

## 3. Nguồn tiêu chuẩn
- Keep a Changelog standard & SemVer 2.0.0

## 4. Đầu vào bắt buộc
Số hiệu phiên bản (`version`), Ngày phát hành (`release_date`), Danh sách tính năng mới, Lỗi đã sửa, Thay đổi có thể gây lỗi hệ thống cũ (Breaking changes).

## 5. Cấu trúc trường bắt buộc
Tiêu đề phiên bản & Ngày phát hành, Tóm tắt phát hành, Tính năng mới (Added), Cải tiến (Changed), Sửa lỗi (Fixed), Thay đổi đột phá & Hướng dẫn di chuyển dữ liệu (Breaking Changes & Migration), Lỗi đã biết (Known Issues).

## 6. Quy tắc nội dung
1. Phân biệt rõ ràng giữa thay đổi ĐÃ XÁC MINH (Verified in build) và thay đổi DỰ KIẾN (Planned).
2. Bắt buộc phải có mục "Breaking Changes" nếu có thay đổi cấu trúc API hoặc DB làm ảnh hưởng người dùng cũ.
3. Liệt kê các lỗi còn tồn tại (Known Issues) để người dùng chủ động ứng phó.

## 7. Tiêu chí chất lượng
Mọi bug fix phải tham chiếu tới Bug ID tương ứng.

## 8. Quy tắc đặt tên
`DOC-DEL-009_Release_Notes_{VERSION}.md`.

## 9. Truy xuất nguồn gốc
Tổng hợp từ `DOC-REQ-007` (RTM), `DOC-SCRUM-015` (Increment), `DOC-TEST-004`.

## 10. Cách kiểm tra
Kiểm tra sự phù hợp với commit git tag tương ứng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "v1.2.0 (2026-10-29): Added: Tìm kiếm theo mã vận đơn. Fixed: BUG-002 lỗi tràn bộ nhớ khi xuất file Excel."
- Không hợp lệ: Ghi chung chung "Cập nhật ứng dụng và sửa một số lỗi vặt."

## 13. Tài liệu liên quan
`DOC-SCRUM-015`, `DOC-TEST-004`.

## 14. Bằng chứng cần thiết
Git commit log và tag repository.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "User_Manual_Rules.md", """# RULE-DEL-010: User Manual Rules

- **Mã quy tắc**: `RULE-DEL-010`
- **Tên quy tắc**: End-User Guidance and Accessibility Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Hướng dẫn người dùng cuối cách sử dụng các tính năng của phần mềm một cách trực quan, dễ hiểu, từng bước.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-010`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 26511:2018 (Requirements for managers of information for users of software)

## 4. Đầu vào bắt buộc
Kịch bản sử dụng thực tế, vai trò người dùng, thông điệp lỗi thường gặp.

## 5. Cấu trúc trường bắt buộc
Tổng quan hệ thống & Đối tượng độc giả, Bắt đầu sử dụng & Đăng nhập, Hướng dẫn từng bước các tính năng chính, Các thông báo lỗi thường gặp & Xử lý sự cố (FAQ), Kênh hỗ trợ.

## 6. Quy tắc nội dung
1. Ngôn từ hướng tới người dùng cuối, không lạm dụng thuật ngữ kỹ thuật chuyên sâu (developer jargons).
2. Các bước hướng dẫn phải đi kèm hành động cụ thể trên giao diện (ví dụ: "Nhấn nút 'Lưu'", "Chọn ngày trong lịch").
3. Có phần hướng dẫn tự khắc phục lỗi đơn giản (Troubleshooting).

## 7. Tiêu chí chất lượng
Người dùng mới có thể hoàn thành tác vụ cơ bản sau khi đọc tài liệu.

## 8. Quy tắc đặt tên
`DOC-DEL-010_User_Manual.docx`.

## 9. Truy xuất nguồn gốc
Dựa trên `DOC-REQ-003` (Chức năng) và `DOC-ARCH-006` (Giao diện).

## 10. Cách kiểm tra
Kiểm tra tính đầy đủ của các chức năng chính dành cho người dùng.

## 11. Ngoại lệ
Hệ thống API backend không có giao diện người dùng thì thay thế bằng API Documentation.

## 12. Ví dụ
- Hợp lệ: "Để đặt lại mật khẩu: 1. Tại màn hình Đăng nhập, nhấn 'Quên mật khẩu'. 2. Nhập email đã đăng ký..."
- Không hợp lệ: "Hệ thống gọi API POST /auth/forgot-password với body JSON..."

## 13. Tài liệu liên quan
`DOC-REQ-003`, `DOC-ARCH-006`.

## 14. Bằng chứng cần thiết
Giao diện ứng dụng và luồng thao tác thực tế.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Installation_Guide_Rules.md", """# RULE-DEL-011: Installation Guide Rules

- **Mã quy tắc**: `RULE-DEL-011`
- **Tên quy tắc**: Installation Environment and Command Verifiability Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Hướng dẫn chi tiết, chính xác các bước chuẩn bị môi trường, cài đặt thư viện, cấu hình và khởi chạy ứng dụng từ mã nguồn repository.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-011`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 26514:2022 (Design and development of user documentation)

## 4. Đầu vào bắt buộc
Yêu cầu tiên quyết (Prerequisites), biến môi trường mẫu (`.env.example`), lệnh cài đặt, lệnh khởi chạy, lệnh kiểm tra (smoke test).

## 5. Cấu trúc trường bắt buộc
Yêu cầu hệ thống & Điều kiện tiên quyết (OS, Node/Python/Java version, Docker), Cấu hình biến môi trường, Các bước cài đặt chi tiết từng câu lệnh, Các bước kiểm tra chạy thử (Smoke testing), Xử lý lỗi cài đặt phổ biến.

## 6. Quy tắc nội dung
1. Mọi câu lệnh cài đặt phải phù hợp chính xác với repository thực tế (ví dụ: dùng `npm install` hoặc `pnpm install` hoặc `pip install -r requirements.txt` dựa vào tệp manifest có trong repo).
2. Tuyệt đối không đưa mật khẩu hoặc key thật vào phần biến môi trường mẫu.
3. Phải có câu lệnh chạy thử để người cài đặt kiểm tra hệ thống đã hoạt động bình thường hay chưa.

## 7. Tiêu chí chất lượng
Một lập trình viên mới clone repo về có thể cài đặt và chạy thành công mà không gặp lỗi thiếu bước.

## 8. Quy tắc đặt tên
`DOC-DEL-011_Installation_Guide.md`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-ARCH-008` (Deployment Architecture).

## 10. Cách kiểm tra
Kiểm tra sự khớp nhau giữa file manifest trong repo và các lệnh cài đặt trong tài liệu.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ:
  ```bash
  git clone <repo-url>
  cd project
  cp .env.example .env
  npm install
  npm run dev
  ```
- Không hợp lệ: Hướng dẫn gõ `pip install` cho một dự án thuần NodeJS / React.

## 13. Tài liệu liên quan
`DOC-ARCH-008`, `DOC-DEL-013`.

## 14. Bằng chứng cần thiết
Tệp package.json, requirements.txt, .env.example trong repository.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Project_Handover_Rules.md", """# RULE-DEL-012: Project Handover Rules

- **Mã quy tắc**: `RULE-DEL-012`
- **Tên quy tắc**: Formal Project Handover and Asset Transfer Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Ghi nhận việc bàn giao toàn diện tài sản phần mềm, mã nguồn, tài liệu, tài nguyên hạ tầng và trách nhiệm bảo hành/vận hành giữa các bên.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-012`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6.8 (Project Closeout & Asset Transfer)

## 4. Đầu vào bắt buộc
Danh mục tài sản bàn giao, danh sách bên bàn giao và bên nhận, tóm tắt kết quả nghiệm thu, cam kết bảo hành và hỗ trợ.

## 5. Cấu trúc trường bắt buộc
Thông tin bàn giao & Các bên liên quan, Danh mục tài sản bàn giao (Mã nguồn, Tài liệu, Môi trường, Tài khoản quản trị), Tóm tắt nghiệm thu, Các hạng mục tồn đọng & Điều khoản bảo hành, Xác nhận bàn giao chính thức.

## 6. Quy tắc nội dung
1. Tuyệt đối không tự tạo biên bản bàn giao có chữ ký giả khi chưa có sự thống nhất giữa hai bên.
2. Danh mục tài sản phải kiểm kê đầy đủ: Đường dẫn kho mã nguồn (Git repo), các tài liệu kỹ thuật, quyền quản trị cloud/hosting, tên miền.
3. Ghi rõ thời gian bảo hành và cam kết hỗ trợ sau bàn giao (nếu có).

## 7. Tiêu chí chất lượng
Danh mục tài sản kiểm kê đầy đủ, không thiếu sót thành phần cốt lõi.

## 8. Quy tắc đặt tên
`DOC-DEL-012_Project_Handover_Report.docx`.

## 9. Truy xuất nguồn gốc
Dựa trên `DOC-TEST-006` (UAT) và tổng kết toàn bộ dự án.

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của danh mục tài sản và xác nhận giữa hai bên.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Bàn giao quyền sở hữu repository `github.com/org/repo` và tài khoản AWS quản trị cho đại diện khách hàng.
- Không hợp lệ: Tự ý tuyên bố bàn giao hoàn tất trong khi khách hàng chưa nhận mã nguồn.

## 13. Tài liệu liên quan
`DOC-PM-001`, `DOC-TEST-006`.

## 14. Bằng chứng cần thiết
Văn bản bàn giao có chữ ký của đại diện có thẩm quyền hai bên.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Delivery", "Deployment_Rules.md", """# RULE-DEL-013: Production Deployment Rules

- **Mã quy tắc**: `RULE-DEL-013`
- **Tên quy tắc**: Production Deployment Runbook and Rollback Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả quy trình triển khai môi trường Production, di chuyển dữ liệu (DB Migration), kiểm tra sau deploy và quy trình rollback khẩn cấp.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-013`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 & DevOps / SRE Standard Operating Procedures

## 4. Đầu vào bắt buộc
Các bước triển khai, quy trình rollback khi gặp sự cố, checklist kiểm tra sau deploy (Smoke tests), kế hoạch backup dữ liệu.

## 5. Cấu trúc trường bắt buộc
Môi trường mục tiêu, Checklist trước triển khai & Sao lưu dữ liệu (Pre-deployment Backup), Các bước thực thi triển khai (Deployment steps), Quy trình chạy migration CSDL, Quy trình Rollback khẩn cấp, Kiểm tra xác thực sau deploy (Post-deployment Smoke Testing).

## 6. Quy tắc nội dung
1. BẮT BUỘC phải có **Quy trình Rollback (Khôi phục trạng thái cũ)** chi tiết từng bước. Không bao giờ triển khai production mà không có phương án rollback.
2. Bắt buộc có bước sao lưu dữ liệu (Database Backup) trước khi chạy bất kỳ migration nào.
3. Quy định rõ thời gian bảo trì (Maintenance Window) và kịch bản thông báo người dùng nếu có downtime.

## 7. Tiêu chí chất lượng
Các lệnh rollback phải có thể thực thi nhanh chóng để phục hồi hệ thống khi có sự cố.

## 8. Quy tắc đặt tên
`DOC-DEL-013_Deployment_Guide.md`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-ARCH-008` (Deployment Architecture) và hỗ trợ phát hành `DOC-DEL-009`.

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của phần `Rollback Procedure` và `Backup Checklist`.

## 11. Ngoại lệ
Không có ngoại lệ đối với việc bắt buộc phải có quy trình Rollback.

## 12. Ví dụ
- Hợp lệ: "Nếu migration DB thất bại: 1. Dừng container mới. 2. Khôi phục backup DB từ `s3://backup/pre-deploy.dump`. 3. Khởi chạy lại image phiên bản cũ v1.1.0."
- Không hợp lệ: Hướng dẫn deploy mà không có bất kỳ dòng nào về cách cứu vãn hệ thống nếu lỗi.

## 13. Tài liệu liên quan
`DOC-ARCH-008`, `DOC-DEL-011`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Tệp CI/CD pipeline (`.github/workflows/deploy.yml`) hoặc deployment script.

## 15. Giới hạn đã biết
Không có.
""")

print("All Delivery rules created successfully.")
