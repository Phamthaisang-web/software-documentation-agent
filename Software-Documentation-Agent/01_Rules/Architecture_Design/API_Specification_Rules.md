# RULE-ARCH-005: API Specification Rules

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
