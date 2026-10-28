# RULE-REQ-008: Requirements Traceability Matrix Rules

- **Mã quy tắc**: `RULE-REQ-008`
- **Tên quy tắc**: Traceability Matrix Generation and Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Đảm bảo ma trận truy xuất nguồn gốc (RTM) liên kết toàn diện mọi yêu cầu với thiết kế, ca kiểm thử và lần phát hành.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-007`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 Clause 9.6

## 4. Đầu vào bắt buộc
Danh sách `REQ-*`, `ARCH-*`, `TC-*`, `REL-*`.

## 5. Cấu trúc trường bắt buộc
Bảng RTM: Requirement ID, Description, Architecture ID, Test Case ID, Test Execution Status, Release Tag.

## 6. Quy tắc nội dung
1. Phát hiện ngay các yêu cầu không có ca kiểm thử (Uncovered Requirements).
2. Phát hiện các ca kiểm thử không có yêu cầu liên kết (Orphan Test Cases).
3. Không tự tạo liên kết giả giữa các thành phần không liên quan.

## 7. Tiêu chí chất lượng
Zero broken references: 100% ID được tham chiếu phải tồn tại trong hệ thống.

## 8. Quy tắc đặt tên
`DOC-REQ-007_Requirements_Traceability_Matrix.xlsx`.

## 9. Truy xuất nguồn gốc
Tài liệu trung tâm của toàn bộ mạng lưới liên kết.

## 10. Cách kiểm tra
Chạy `test_traceability.py`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `REQ-FUNC-001` -> `ARCH-API-001` -> `TC-AUTH-001` -> `v1.0.0`.
- Không hợp lệ: `REQ-FUNC-001` -> trỏ tới `TC-999` (không tồn tại).

## 13. Tài liệu liên quan
`DOC-REQ-001`, `DOC-TEST-003`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Tệp RTM hoàn chỉnh.

## 15. Giới hạn đã biết
Không có.
