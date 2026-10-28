# RULE-SCRUM-018: Sprint Metrics Rules

- **Mã quy tắc**: `RULE-SCRUM-018`
- **Tên quy tắc**: Sprint Metrics and Burndown Tracking Rules
- **Loại quy tắc**: `RECOMMENDATION`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định việc theo dõi các chỉ số Sprint (Velocity, Burndown Chart) dựa trên dữ liệu thực tế (thông lệ tùy chọn).

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-016`.

## 3. Nguồn tiêu chuẩn
- Agile Practice Guide (Complementary practice, NOT mandatory in Scrum Guide).

## 4. Đầu vào bắt buộc
Dữ liệu công việc còn lại thực tế qua các ngày của Sprint.

## 5. Cấu trúc trường bắt buộc
Sprint ID, Điểm kế hoạch vs Điểm thực tế hoàn thành, Bảng số liệu Burndown hàng ngày, Phân tích Velocity, Thông báo tính chất bổ trợ.

## 6. Quy tắc nội dung
1. **Tính chất bổ trợ**: Phải nêu rõ Burndown chart và Velocity là công cụ bổ trợ, KHÔNG PHẢI quy định bắt buộc của Scrum Guide.
2. **Cấm bịa đặt số liệu**: Tuyệt đối không tự bịa đặt dữ liệu burndown giả nếu không có log theo dõi công việc thực tế từ nhóm.
3. Velocity chỉ mang tính tham khảo nội bộ nhóm để hỗ trợ lập kế hoạch, không dùng để so sánh năng suất giữa các nhóm khác nhau.

## 7. Tiêu chí chất lượng
Biểu đồ và bảng số liệu khớp nhau 100%.

## 8. Quy tắc đặt tên
`DOC-SCRUM-016_Sprint_Metrics_Burndown.xlsx`.

## 9. Truy xuất nguồn gốc
Hỗ trợ dữ liệu cho `DOC-DEL-008` (Progress Report).

## 10. Cách kiểm tra
Kiểm tra cấm số liệu bịa đặt và nhãn `RECOMMENDATION`.

## 11. Ngoại lệ
Nhóm làm theo Kanban/Flow metrics có thể dùng CFD (Cumulative Flow Diagram) thay thế.

## 12. Ví dụ
- Hợp lệ: Nhóm ghi nhận điểm hoàn thành thực tế của Sprint 1 là 24 story points.
- Không hợp lệ: Tự vẽ đường burndown thẳng tắp hoàn hảo trong khi dự án chưa từng chạy Sprint.

## 13. Tài liệu liên quan
`DOC-SCRUM-007`, `DOC-DEL-008`.

## 14. Bằng chứng cần thiết
Dữ liệu log từ issue tracker.

## 15. Giới hạn đã biết
Không có.
