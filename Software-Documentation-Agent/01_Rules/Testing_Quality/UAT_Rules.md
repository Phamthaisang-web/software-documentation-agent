# RULE-TEST-006: User Acceptance Testing Rules

- **Mã quy tắc**: `RULE-TEST-006`
- **Tên quy tắc**: User Acceptance Testing Signoff Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Ghi nhận kết quả kiểm thử nghiệm thu người dùng (UAT) và quy định thẩm quyền ký duyệt nghiệm thu.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-006`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-3:2021 & ISO 21500

## 4. Đầu vào bắt buộc
Kịch bản nghiệm thu người dùng, danh sách người tham gia UAT, kết quả đánh giá, quyết định nghiệm thu.

## 5. Cấu trúc trường bắt buộc
Phạm vi & Môi trường UAT, Kịch bản nghiệp vụ đã nghiệm thu, Danh sách người tham gia & Vai trò, Tồn đọng còn mở, Quyết định nghiệm thu chính thức (Signoff).

## 6. Quy tắc nội dung
1. Tuyệt đối KHÔNG tự động đánh dấu chấp nhận nghiệm thu (Accepted) khi chưa có sự xác nhận của người dùng hoặc đại diện nghiệp vụ có thẩm quyền.
2. Mọi tồn đọng chưa được giải quyết phải được ghi rõ kèm điều kiện chấp nhận (ví dụ: Chấp nhận có điều kiện).

## 7. Tiêu chí chất lượng
Có chữ ký hoặc biên bản xác nhận đính kèm.

## 8. Quy tắc đặt tên
`DOC-TEST-006_UAT_Record.docx`.

## 9. Truy xuất nguồn gốc
Làm căn cứ pháp lý cho `DOC-DEL-012` (Project Handover Report).

## 10. Cách kiểm tra
Kiểm tra trường quyết định nghiệm thu.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Biên bản UAT ghi nhận người dùng Nguyễn Văn A (Đại diện phòng Kế toán) xác nhận đạt yêu cầu ngày 28/10/2026.
- Không hợp lệ: Agent tự ý ghi "Đã nghiệm thu thành công bởi ban giám đốc" mà không có căn cứ.

## 13. Tài liệu liên quan
`DOC-REQ-008`, `DOC-DEL-012`.

## 14. Bằng chứng cần thiết
Email xác nhận hoặc văn bản ký duyệt UAT.

## 15. Giới hạn đã biết
Không có.
