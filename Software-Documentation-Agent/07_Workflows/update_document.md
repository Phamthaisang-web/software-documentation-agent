# Workflow D — Cập Nhật Tài Liệu Khi Thay Đổi (Document Update Workflow)

## 1. Mục Đích
Cập nhật tài liệu kỹ thuật khi mã nguồn, kiến trúc, yêu cầu hoặc quy trình dự án thay đổi mà vẫn bảo tồn nội dung đã duyệt trước đó.

## 2. Các Bước Thực Hiện
1. **Bước 1: Phân tích thay đổi (Diff & Impact Analysis)**:
   - So sánh commit/mã nguồn mới với phiên bản tài liệu hiện hành.
   - Xác định danh sách tài liệu bị ảnh hưởng trực tiếp và gián tiếp.
2. **Bước 2: Bảo tồn nội dung không đổi**:
   - Giữ nguyên các quyết định đã duyệt và các phần không bị tác động.
3. **Bước 3: Chỉnh sửa và cập nhật**:
   - Thêm/sửa đổi nội dung mới theo bằng chứng mã nguồn mới.
   - Tăng số hiệu phiên bản (`version` tăng từ `1.0.0` lên `1.1.0`).
   - Cập nhật bảng Lịch sử Thay đổi (Changelog).
4. **Bước 4: Cập nhật tài liệu phụ thuộc trong chuỗi truy xuất**:
   - Ví dụ: Thêm API mới -> Cập nhật API Spec (`DOC-ARCH-005`), bổ sung Test Case (`DOC-TEST-003`), cập nhật Ma trận RTM (`DOC-REQ-007`) và ghi nhận vào Release Notes (`DOC-DEL-009`).
5. **Bước 5: Thẩm định lại**: Chạy kiểm tra tính hợp lệ toàn diện.
