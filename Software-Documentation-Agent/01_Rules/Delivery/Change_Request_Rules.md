# RULE-DEL-006: Change Request Rules

- **Mã quy tắc**: `RULE-DEL-006`
- **Tên quy tắc**: Change Control and Impact Analysis Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định quy trình kiểm soát thay đổi (Change Control): ghi nhận, đánh giá tác động và phê duyệt thay đổi phạm vi, tiến độ hoặc chi phí.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-006`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 & ISO/IEC/IEEE 29148:2018

## 4. Đầu vào bắt buộc
Mô tả thay đổi, lý do yêu cầu, đánh giá tác động (Impact Analysis) đến phạm vi, thời gian và chi phí.

## 5. Cấu trúc trường bắt buộc
CR ID, Ngày yêu cầu, Người yêu cầu, Mô tả thay đổi, Phân tích tác động (Scope, Schedule, Cost, Quality), Trạng thái phê duyệt (Pending/Approved/Rejected), Bằng chứng triển khai.

## 6. Quy tắc nội dung
1. Mọi thay đổi làm ảnh hưởng tới phạm vi đã duyệt (Baseline Scope) phải được lập phiếu Yêu cầu Thay đổi (CR).
2. Phải phân tích tác động toàn diện trước khi trình cấp có thẩm quyền phê duyệt.
3. Không tự ý thực hiện thay đổi khi CR chưa được phê duyệt chính thức.

## 7. Tiêu chí chất lượng
Đánh giá tác động định lượng rõ số ngày trễ hạn hoặc chi phí phát sinh nếu có.

## 8. Quy tắc đặt tên
`DOC-DEL-006_Change_Request_Log.xlsx`.

## 9. Truy xuất nguồn gốc
Cập nhật vào `DOC-REQ-001` (SRS) và `DOC-DEL-001` (Schedule).

## 10. Cách kiểm tra
Kiểm tra trường phân tích tác động không rỗng.

## 11. Ngoại lệ
Các thay đổi nhỏ bên trong Sprint do PO và Developers thỏa thuận theo quy tắc Scrum không cần phiếu CR hợp đồng nặng nề.

## 12. Ví dụ
- Hợp lệ: `CR-001`: Yêu cầu bổ sung cổng thanh toán Apple Pay. Đánh giá tác động: Tăng thêm 5 ngày công, không đổi ngày release.
- Không hợp lệ: Thay đổi tính năng âm thầm không qua kiểm soát.

## 13. Tài liệu liên quan
`DOC-PM-002`, `DOC-REQ-001`.

## 14. Bằng chứng cần thiết
Phiếu yêu cầu thay đổi có chữ ký duyệt.

## 15. Giới hạn đã biết
Không có.
