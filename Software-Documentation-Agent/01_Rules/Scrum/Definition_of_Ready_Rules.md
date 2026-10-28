# RULE-SCRUM-016: Definition of Ready Rules

- **Mã quy tắc**: `RULE-SCRUM-016`
- **Tên quy tắc**: Definition of Ready (Optional Practice) Rules
- **Loại quy tắc**: `RECOMMENDATION`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định tiêu chuẩn đánh giá PBI sẵn sàng đưa vào Sprint Planning (thông lệ tùy chọn của nhóm).

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-017`.

## 3. Nguồn tiêu chuẩn
- Agile Complementary Practices (Scrum Alliance / Scrum.org community practice).
- **LƯU Ý QUAN TRỌNG**: Definition of Ready KHÔNG PHẢI là một khái niệm hay quy tắc bắt buộc trong The Scrum Guide 2020.

## 4. Đầu vào bắt buộc
Checklist kiểm tra PBI trước khi đưa vào Sprint Planning.

## 5. Cấu trúc trường bắt buộc
Thông báo trạng thái tùy chọn (Optional Status Notice), Tiêu chuẩn độ rõ ràng của PBI, Độ rõ ràng của Acceptance Criteria, Đã được ước lượng, Sự phụ thuộc đã được giải quyết.

## 6. Quy tắc nội dung
1. **Bắt buộc phân loại đúng**: Phải đánh dấu rõ ràng Definition of Ready là `RECOMMENDATION` hoặc `INTERNAL_POLICY` của nhóm. Tuyệt đối không được gán nhãn DoR là quy tắc chính thức của Scrum Guide.
2. DoR không được dùng như một cánh cổng kiểm soát cứng nhắc (Stage-gate) ngăn cản sự cộng tác giữa PO và Developers.

## 7. Tiêu chí chất lượng
Có tuyên bố minh bạch về tính chất bổ trợ của DoR.

## 8. Quy tắc đặt tên
`DOC-SCRUM-017_Definition_of_Ready.docx`.

## 9. Truy xuất nguồn gốc
Hỗ trợ sàng lọc PBI trong `DOC-SCRUM-003`.

## 10. Cách kiểm tra
Chạy bài kiểm thử `test_sprint_constraints.py` để xác nhận DoR không bị ghi nhầm là `OFFICIAL_REQUIREMENT`.

## 11. Ngoại lệ
Nhóm hoàn toàn có quyền không sử dụng DoR nếu thấy không cần thiết.

## 12. Ví dụ
- Hợp lệ: DoR là checklist nội bộ của nhóm để hỗ trợ PO chuẩn bị story tốt hơn.
- Không hợp lệ: Khẳng định "Theo quy định Scrum Guide bắt buộc phải có Definition of Ready mới được Planning".

## 13. Tài liệu liên quan
`DOC-SCRUM-003`, `DOC-SCRUM-006`.

## 14. Bằng chứng cần thiết
Thỏa thuận nội bộ của nhóm phát triển.

## 15. Giới hạn đã biết
Không có.
