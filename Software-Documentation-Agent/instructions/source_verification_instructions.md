# Source Verification Instructions — Hướng Dẫn Thẩm Định Nguồn Tham Chiếu

Tài liệu này quy định chi tiết các bước xác minh nguồn dữ liệu đầu vào cho AI Agent.

---

## 1. Quy Trình Thẩm Định Nguồn Ngoài (External Standards)
1. **Truy cập cổng chính thức**:
   - Scrum: https://scrumguides.org/scrum-guide.html
   - ISO Portal: https://www.iso.org/standard/{standard_id}.html
   - OpenAPI: https://spec.openapis.org/oas/v3.1.0
   - OWASP: https://owasp.org/Top10/
2. **Kiểm tra trạng thái hiệu lực**:
   - Tiêu chuẩn còn hiệu lực hay đã bị hủy bỏ/thay thế (Superseded/Withdrawn).
   - Nếu là ISO, xác định rõ năm ban hành (ví dụ: ISO/IEC/IEEE 29148:2018).
3. **Phạm vi thẩm định bản quyền**:
   - Đối với tài liệu có phí: Chỉ ghi nhận phạm vi đã kiểm chứng qua Catalog, Tóm tắt mục tiêu (Abstract) và Bảng mục lục công khai.
   - Không được tuyên bố đã thẩm định chi tiết từng trang nội dung có phí nếu chỉ tiếp cận tài liệu mở.

---

## 2. Quy Trình Thẩm Định Nguồn Nội Bộ Dự Án (Internal Code & Docs)
1. **Mã nguồn thực tế**:
   - Trích xuất file path chính xác (ví dụ: `src/controllers/auth.controller.ts:45`).
   - Ghi nhận hàm/lớp xử lý, không được viện dẫn chung chung "trong thư mục src/".
2. **Cơ sở dữ liệu**:
   - Dựa vào migration files hoặc schema definition (`prisma/schema.prisma`, `migrations/001_init.sql`, `models/user.py`).
3. **Kiểm thử tự động**:
   - Chỉ xác nhận Test Passed khi có tệp log chạy test thực tế (JUnit XML, coverage report, console output thực).
   - Nếu dự án chỉ có test file nhưng chưa chạy trong phiên làm việc, đánh dấu trạng thái là `NOT_EXECUTED`.
4. **Phát hiện mâu thuẫn**:
   - Nếu mã nguồn viết một đằng (ví dụ API nhận `POST /users/register`) nhưng tài liệu cũ ghi một nẻo (`POST /api/signup`), lập tức gắn nhãn `CONFLICT` và yêu cầu xác nhận.
