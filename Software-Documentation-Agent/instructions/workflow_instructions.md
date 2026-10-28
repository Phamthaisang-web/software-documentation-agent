# Workflow Instructions — Quy Trình Thực Thi Của Agent

Tài liệu này hướng dẫn chi tiết 5 quy trình nghiệp vụ cốt lõi mà Agent tuân thủ khi phân tích dự án, sinh tài liệu, cập nhật và thẩm định.

---

## Workflow A — Phân Tích Dự Án (Project Analysis)
1. **Quét cấu trúc thư mục (Tree Scan)**:
   - Duyệt mã nguồn, bỏ qua các thư mục phụ trợ (`node_modules`, `.git`, `venv`, `dist`, `build`).
   - Đọc manifest (`package.json`, `requirements.txt`, `pom.xml`, `go.mod`, `Cargo.toml`).
2. **Thu thập bằng chứng (Evidence Harvesting)**:
   - Schema / Migrations: Trích xuất bảng, trường, khóa ngoại.
   - API Routes / Controllers: Trích xuất endpoints, HTTP methods, authentication guards.
   - Test files: Phát hiện unit tests, e2e tests, fixtures.
   - Docker / CI/CD: Trích xuất môi trường và hạ tầng.
3. **Tổng hợp Hồ sơ Dự án (Project Profile Generation)**:
   - Ghi dữ liệu vào định dạng `project_profile.yaml` tuân thủ `project_profile.schema.json`.
   - Gán cờ `VERIFIED`, `INFERRED`, `UNKNOWN`, `CONFLICT` cho từng trường.
4. **Đề xuất danh mục tài liệu cần thiết**:
   - Dựa trên quy mô dự án và phương pháp luận (Scrum / Waterfall / Lean), đề xuất bộ tài liệu phù hợp từ 59 loại tài liệu trong `document_registry.yaml`.

---

## Workflow B — Tạo Một Tài Liệu Đơn Lẻ (Single Document Generation)
1. Tra cứu `document_id` trong `config/document_registry.yaml`.
2. Tải các file Rules tương ứng trong `01_Rules/`.
3. Kiểm tra nguồn tiêu chuẩn liên quan trong `config/standards_registry.yaml`.
4. Tìm template phù hợp trong `config/template_registry.yaml` (ưu tiên `USER_PROVIDED`, nếu không có dùng `GENERATED_TEMPLATE`).
5. Thu thập bằng chứng cần thiết từ `project_profile.yaml`.
6. Thực hiện render nội dung: Thay thế placeholder trong file DOCX, XLSX, MD, YAML, MMD mà không thay đổi cấu trúc bảng, style, font, hoặc công thức tính toán.
7. Thực hiện thẩm định tự động (Validation check) trước khi xuất tệp.
8. Lưu tài liệu vào thư mục `output/` kèm tệp metadata `.meta.yaml`.

---

## Workflow C — Tạo Bộ Tài Liệu Hoàn Chỉnh (Document Set Generation)
1. Xây dựng đồ thị phụ thuộc (Dependency Graph) giữa các tài liệu:
   - Nhóm 1: Foundation (Product Vision, Project Charter, Scope Statement, Stakeholder Register).
   - Nhóm 2: Requirements (SRS, FRS, NFRS, Use Cases, User Stories, AC, RTM).
   - Nhóm 3: Architecture & Design (SAD, SDD, DB Spec, ERD, API Spec, Deployment).
   - Nhóm 4: Scrum & Delivery (Product Backlog, Sprint Planning, Schedule, WBS, Risk Register).
   - Nhóm 5: Testing & Quality (Test Plan, Test Scenarios, Test Cases).
2. Sinh tài liệu theo thứ tự topo từ gốc đến ngọn.
3. Đồng bộ hóa mã định danh: Tất cả các ID được tạo ra (`REQ-xxx`, `PBI-xxx`, `TC-xxx`, `ADR-xxx`) phải được lưu vào Bảng chỉ mục liên kết toàn cục để các tài liệu sau tái sử dụng chính xác.
4. Chạy kiểm tra tính nhất quán chéo (Cross-document consistency check).

---

## Workflow D — Cập Nhật Tài Liệu Khi Dự Án Thay Đổi (Document Update)
1. Đọc phiên bản hiện tại của tài liệu và so sánh với commit/mã nguồn mới.
2. Phân tích ảnh hưởng (Impact Analysis): Xác định các phần bị tác động.
3. Giữ nguyên toàn bộ các nội dung không bị ảnh hưởng và quyết định đã duyệt trước đó.
4. Cập nhật nội dung mới, đánh dấu phiên bản tăng lên (ví dụ: `1.0.0` -> `1.1.0`), ghi nhận vào Changelog.
5. Kiểm tra và cập nhật các tài liệu phụ thuộc trong chuỗi truy xuất.

---

## Workflow E — Thẩm Định Bộ Tài Liệu (Document Set Validation)
1. Kiểm tra cấu trúc tệp đầu ra (tồn tại, không rỗng, định dạng mở được).
2. Kiểm tra tính đầy đủ của các mục bắt buộc (`required_sections`).
3. Kiểm tra tính hợp lệ của nguồn (`standards_registry.yaml`).
4. Kiểm tra ma trận truy xuất nguồn gốc (`traceability_engine.py`): Không có liên kết đứt gãy, không có ID rỗng.
5. Xuất báo cáo thẩm định chuẩn `validation_report.json` và `validation_report.md`.
