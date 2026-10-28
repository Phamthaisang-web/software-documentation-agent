# Project Analysis Rules — Quy Tắc Phân Tích Dự Án

Tài liệu này quy định các bước và tiêu chuẩn phân tích một dự án phần mềm trước khi sinh tài liệu kỹ thuật.

---

## 1. Mục Tiêu Phân Tích
Project Analyzer có nhiệm vụ khảo sát thực địa toàn bộ workspace, phân loại công nghệ, nhận diện chức năng, sơ đồ dữ liệu, API, cấu hình hạ tầng và bằng chứng kiểm thử đang tồn tại.

## 2. Các Thành Phần Khảo Sát
1. **Cấu trúc Repository**: Bố cục thư mục, quy ước monorepo hoặc single-service.
2. **Tệp cấu hình & Quản lý thư viện**:
   - NodeJS: `package.json`, `pnpm-lock.yaml`, `tsconfig.json`.
   - Python: `requirements.txt`, `pyproject.toml`, `Pipfile`.
   - Java: `pom.xml`, `build.gradle`.
   - Go: `go.mod`, `go.sum`.
   - Rust: `Cargo.toml`.
3. **Mô hình Dữ liệu & Schema**:
   - Prisma (`schema.prisma`), TypeORM/MikroORM entities, SQLAlchemy models, Django models, SQL migrations.
4. **API & Endpoints**:
   - Router files, Controllers, FastAPI routers, Express routes, Spring `@RestController`, Swagger/OpenAPI yaml.
5. **Giao diện người dùng (Frontend)**:
   - React components, Next.js pages/app router, Vue components, Flutter widgets.
6. **Bảo mật & Phân quyền**:
   - Auth middleware, JWT configuration, RBAC guards, OAuth providers.
7. **Hạ tầng & Triển khai**:
   - `Dockerfile`, `docker-compose.yml`, Kubernetes manifests, Helm charts, `.github/workflows`.
8. **Kiểm thử tự động**:
   - Test suites (`*.test.ts`, `*_test.py`, `*Test.java`), fixtures, coverage reports, test runner logs.
9. **Tài liệu & Mẫu sẵn có**:
   - Tệp `README.md`, `CONTRIBUTING.md`, các mẫu Word/Excel do người dùng đặt trong workspace.

## 3. Quy Tắc Gán Nhãn Xác Minh
Mọi thành phần trích xuất được phải gắn một trong 4 nhãn:
- `VERIFIED`: Có bằng chứng tệp tin, dòng code cụ thể.
- `INFERRED`: Suy luận logic có cơ sở rõ ràng (kèm lý do suy luận).
- `UNKNOWN`: Chưa có thông tin trong repo (đánh dấu TBD, không đoán mò).
- `CONFLICT`: Có hai hoặc nhiều nguồn dữ liệu mâu thuẫn nhau.
