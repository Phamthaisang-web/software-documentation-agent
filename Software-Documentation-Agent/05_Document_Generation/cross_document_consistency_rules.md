# Cross-Document Consistency Rules — Quy Tắc Tính Nhất Quán Giữa Các Tài Liệu

Tài liệu này quy định các kiểm tra đảm bảo thông tin đồng nhất xuyên suốt toàn bộ bộ tài liệu dự án.

---

## 1. Các Trục Nhất Quán Bắt Buộc
1. **Thông tin chung của dự án**: Tên dự án (`project_name`), phiên bản (`version`), tác giả, ngày phát hành phải hoàn toàn trùng khớp giữa tất cả các tài liệu trong cùng một đợt phát hành.
2. **Thuật ngữ & Danh từ riêng**: Thuật ngữ chuyên ngành, tên module và vai trò người dùng phải đồng nhất (ví dụ: nếu trong SRS gọi là "Quản trị viên hệ thống" thì không được đổi thành "Admin cấp cao" ở User Manual nếu cùng chỉ một thực thể).
3. **Mã định danh (Identifiers)**:
   - Một yêu cầu chức năng có ID là `REQ-FUNC-001` trong `DOC-REQ-003` thì khi xuất hiện ở `DOC-REQ-007` (RTM) và `DOC-TEST-003` (Test Case) phải giữ nguyên ID `REQ-FUNC-001`.
4. **Phạm vi & Tính năng**:
   - Các tính năng được mô tả là "Hoàn thành" trong `DOC-DEL-009` (Release Notes) phải xuất hiện trong `DOC-SCRUM-015` (Increment Deliverables) và có test case tương ứng `PASS` trong `DOC-TEST-004`.
5. **Cơ sở dữ liệu & API**:
   - Các trường dữ liệu trong `DOC-ARCH-005` (API Specification) phải tương thích với kiểu dữ liệu trong `DOC-ARCH-003` (Database Design).

## 2. Xử Lý Khi Phát Hiện Không Nhất Quán
1. Cảnh báo lỗi mức `CRITICAL` trong báo cáo thẩm định chéo.
2. Đồng bộ hóa lại từ nguồn `project_profile.yaml`.
