# Workflow C — Tạo Bộ Tài Liệu Hoàn Chỉnh (Document Set Generation Workflow)

## 1. Mục Đích
Tạo toàn bộ bộ tài liệu dự án một cách tự động, tuần tự và đảm bảo tính nhất quán chéo.

## 2. Các Bước Thực Hiện
1. **Bước 1: Phân tích dự án**: Chạy Workflow A để có `project_profile.yaml` mới nhất.
2. **Bước 2: Xây dựng Đồ thị Phụ thuộc (Dependency Graph)**:
   - Sắp xếp thứ tự sinh tài liệu:
     1. Nhóm Khởi tạo & Định hướng: `DOC-PM-001`, `DOC-PM-002`, `DOC-REQ-002`, `DOC-PM-003`.
     2. Nhóm Yêu cầu & Backlog: `DOC-REQ-001`, `DOC-REQ-003`, `DOC-REQ-004`, `DOC-REQ-005`, `DOC-REQ-006`, `DOC-REQ-008`, `DOC-SCRUM-001`, `DOC-SCRUM-002`.
     3. Nhóm Kiến trúc & Thiết kế: `DOC-ARCH-001` đến `DOC-ARCH-010`.
     4. Nhóm Kế hoạch & Sprint: `DOC-SCRUM-006` đến `DOC-SCRUM-017`, `DOC-DEL-001` đến `DOC-DEL-003`.
     5. Nhóm Kiểm thử: `DOC-TEST-001` đến `DOC-TEST-008`.
     6. Nhóm Ma trận & Bàn giao: `DOC-REQ-007` (RTM), `DOC-DEL-008`, `DOC-DEL-009`, `DOC-DEL-010`, `DOC-DEL-011`, `DOC-DEL-012`, `DOC-DEL-013`.
3. **Bước 3: Sinh tuần tự và chia sẻ định danh**:
   - Lưu trữ toàn bộ các ID sinh ra (`REQ-*`, `PBI-*`, `TC-*`, `ADR-*`) vào bộ nhớ cache chung để các tài liệu phụ thuộc tái sử dụng chính xác.
4. **Bước 4: Thẩm định chéo toàn bộ**:
   - Chạy `validator.py` kiểm tra ma trận truy xuất và tính nhất quán chéo.
5. **Bước 5: Báo cáo hoàn tất**:
   - Xuất báo cáo tổng quan số lượng tài liệu đã tạo và danh sách các phần còn thiếu.
