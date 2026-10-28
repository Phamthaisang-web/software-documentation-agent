# RULE-DEL-001: Project Schedule Rules

- **Mã quy tắc**: `RULE-DEL-001`
- **Tên quy tắc**: Master Project Schedule and Milestone Tracking Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định cấu trúc và nguyên tắc quản lý tiến độ tổng thể, các mốc quan trọng (Milestones) theo ISO 21500.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-001`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6.4 (Schedule management)

## 4. Đầu vào bắt buộc
Các mốc bàn giao chính, ngày bắt đầu và kết thúc từng giai đoạn, tiến độ thực tế.

## 5. Cấu trúc trường bắt buộc
Các mốc dự án (Milestones), Tiến độ các gói công việc (Work Packages), Ngày kế hoạch vs Ngày thực tế, Tỷ lệ hoàn thành %, Phân tích độ lệch tiến độ (Schedule Variance).

## 6. Quy tắc nội dung
1. Không tự tạo ngày phát hành, cam kết mốc nếu chưa có kế hoạch được phê duyệt.
2. Các mốc phải có tính khả thi và logic thứ tự trước sau (Predecessor/Successor).

## 7. Tiêu chí chất lượng
Tiến độ các giai đoạn không mâu thuẫn với lịch Sprint (`DOC-SCRUM-010`).

## 8. Quy tắc đặt tên
`DOC-DEL-001_Project_Schedule.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-DEL-002` (WBS) và `DOC-DEL-008` (Progress Report).

## 10. Cách kiểm tra
Kiểm tra tính nhất quán giữa ngày bắt đầu và kết thúc của các giai đoạn.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Milestone M1: Hoàn thành thiết kế kiến trúc vào 15/11/2026.
- Không hợp lệ: Ghi nhận dự án đã hoàn thành trong khi mã nguồn mới ở giai đoạn dựng khung.

## 13. Tài liệu liên quan
`DOC-DEL-002`, `DOC-SCRUM-010`, `DOC-DEL-008`.

## 14. Bằng chứng cần thiết
Kế hoạch tiến độ dự án.

## 15. Giới hạn đã biết
Không có.
