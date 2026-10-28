# RULE-PM-001: Project Charter Rules

- **Mã quy tắc**: `RULE-PM-001`
- **Tên quy tắc**: Project Charter Definition and Authority Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định tiêu chuẩn lập tài liệu Khởi tạo Dự án (Project Charter) theo ISO 21500, xác lập sự tồn tại chính thức của dự án và quyền hạn của Giám đốc dự án.

## 2. Phạm vi áp dụng
Tài liệu `DOC-PM-001` (Project Charter).

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6 (Project Governance & Initiation)

## 4. Đầu vào bắt buộc
- Bối cảnh kinh doanh (`business_need`)
- Mục tiêu tổng quát của dự án (`project_objectives`)
- Danh sách các bên liên quan chính (`key_stakeholders`)

## 5. Cấu trúc trường bắt buộc
Bao gồm: Mục tiêu dự án, Trường hợp kinh doanh, Tóm tắt phạm vi, Các mốc ban đầu, Bên liên quan chính, Thẩm quyền và phê duyệt.

## 6. Quy tắc nội dung
1. Phải nêu rõ lý do tại sao dự án cần được thực hiện và bài toán nghiệp vụ giải quyết.
2. Không tự bịa đặt ngân sách, nguồn vốn hoặc tên người tài trợ (Sponsor) nếu chưa có thông tin xác thực; đánh dấu `TBD`.
3. Mục tiêu phải tuân thủ nguyên tắc SMART (Specific, Measurable, Achievable, Relevant, Time-bound).
4. Phân định rõ quyền hạn của Project Manager và ban chỉ đạo.

## 7. Tiêu chí chất lượng
Mục tiêu dự án có chỉ số đo lường thành công định lượng hoặc định tính rõ ràng.

## 8. Quy tắc đặt tên
Tệp xuất bản: `DOC-PM-001_Project_Charter.docx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-PM-002` (Scope Statement) và `DOC-PM-003` (Stakeholder Register).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của các phần bắt buộc qua `validator.py`.

## 11. Ngoại lệ
Dự án nội bộ nhỏ (Pet project/PoC) có thể rút gọn phần phân bổ ngân sách.

## 12. Ví dụ
- Hợp lệ: "Mục tiêu: Xây dựng cổng thanh toán trực tuyến xử lý 10,000 giao dịch/ngày hoàn thành vào Q4/2026."
- Không hợp lệ: "Xây dựng hệ thống tốt nhất thế giới."

## 13. Tài liệu liên quan
`DOC-PM-002`, `DOC-PM-003`.

## 14. Bằng chứng cần thiết
Văn bản yêu cầu dự án hoặc tài liệu đề xuất giải pháp.

## 15. Giới hạn đã biết
Không thể xác minh thông tin tài chính nếu doanh nghiệp bảo mật.
