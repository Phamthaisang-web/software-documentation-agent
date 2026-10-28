# RULE-GLOB-006: Traceability Rules (Quy Tắc Truy Xuất Nguồn Gốc)

- **Mã quy tắc**: `RULE-GLOB-006`
- **Tên quy tắc**: Bidirectional Requirements and Artifacts Traceability
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định cơ chế theo dõi mối liên kết hai chiều giữa các thành phần tài liệu xuyên suốt vòng đời phát triển phần mềm.

## 2. Phạm vi áp dụng
Mọi thực thể: Yêu cầu, Ca sử dụng, Thiết kế, Quyết định kiến trúc, PBI, Ca kiểm thử, Lỗi, Ghi chú phát hành.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 (Requirements Traceability)
- ISO/IEC/IEEE 29119-3:2021 (Test Traceability)

## 4. Đầu vào bắt buộc
Danh sách định danh thực thể: `REQ-*`, `PBI-*`, `ARCH-*`, `TC-*`, `BUG-*`, `REL-*`.

## 5. Cấu trúc trường bắt buộc
Mỗi thực thể phải lưu trữ danh sách `parent_refs` và `child_refs`.

## 6. Quy tắc nội dung
1. Mọi Functional Requirement (`REQ-FUNC-xxx`) phải có ít nhất một Test Case (`TC-xxx`) kiểm chứng.
2. Không cho phép mồ côi (Orphan Item): Không tạo Test Case không gắn với yêu cầu hay PBI nào.
3. Không tham chiếu đến ID không tồn tại (Broken link).
4. Chuỗi truy xuất mẫu:
   `Product Vision -> Product Goal -> Product Backlog -> PBI -> Acceptance Criteria -> Test Case -> Test Execution -> Release Notes`.

## 7. Tiêu chí chất lượng
Độ bao phủ truy xuất đạt 100% đối với các yêu cầu chức năng cốt lõi.

## 8. Quy tắc đặt tên
Định dạng mã: `REQ-[LOAI]-[SO]`, `TC-[MODULE]-[SO]`.

## 9. Truy xuất nguồn gốc
Tài liệu `DOC-REQ-007` (RTM) là trung tâm thể hiện ma trận truy xuất.

## 10. Cách kiểm tra
Chạy bài kiểm thử tự động `test_traceability.py`.

## 11. Ngoại lệ
Các yêu cầu phi chức năng cấp hệ thống (NFR) có thể liên kết trực tiếp tới quyết định kiến trúc (`DOC-ARCH-010`).

## 12. Ví dụ
- Hợp lệ: `TC-AUTH-001` kiểm chứng cho `REQ-FUNC-001` (User Login).
- Không hợp lệ: `TC-MISC-999` kiểm chứng cho `REQ-9999` (ID không tồn tại).

## 13. Tài liệu liên quan
`DOC-REQ-001`, `DOC-REQ-007`, `DOC-TEST-003`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Bảng ma trận truy xuất nguồn gốc RTM.

## 15. Giới hạn đã biết
Không tự động phát hiện được liên kết logic nếu người dùng không gán ID.
