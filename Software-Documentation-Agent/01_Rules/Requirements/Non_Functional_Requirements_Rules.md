# RULE-REQ-004: Non-Functional Requirements Rules

- **Mã quy tắc**: `RULE-REQ-004`
- **Tên quy tắc**: Non-Functional Requirements Quantification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Xác định và định lượng các yêu cầu phi chức năng (hiệu năng, bảo mật, độ tin cậy, khả năng bảo trì) theo ISO 29148 và ISO 25010.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-004`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018
- OWASP Top 10:2021

## 4. Đầu vào bắt buộc
Chỉ tiêu đo lường, ngưỡng chấp nhận, phương pháp đo.

## 5. Cấu trúc trường bắt buộc
NFR ID, Category (Performance/Security/Reliability/Usability), Target Metric, Measurement Method, Architecture Impact.

## 6. Quy tắc nội dung
1. Mọi chỉ tiêu phải có con số cụ thể hoặc ngưỡng đo lường được (không dùng từ chung chung).
2. Nếu không có căn cứ từ cấu hình hoặc benchmark, bắt buộc phải đánh dấu `TBD`.
3. Yêu cầu bảo mật phải tham chiếu tới các kiểm soát của OWASP Top 10.

## 7. Tiêu chí chất lượng
100% NFR có đơn vị đo rõ ràng (ms, %, req/s, bits).

## 8. Quy tắc đặt tên
`DOC-REQ-004_Non_Functional_Requirements.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-ARCH-001` (SAD) và `DOC-ARCH-010` (ADR).

## 10. Cách kiểm tra
Kiểm tra sự tồn tại của trường `target_metric`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `REQ-NF-PERF-001`: Thời gian phản hồi trang dashboard <= 1.5s ở tải 500 CCU.
- Không hợp lệ: `REQ-NF-PERF-001`: Trang dashboard phải load nhanh.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-TEST-001`.

## 14. Bằng chứng cần thiết
Cấu hình cache, pool kết nối, kết quả load test.

## 15. Giới hạn đã biết
Không có.
