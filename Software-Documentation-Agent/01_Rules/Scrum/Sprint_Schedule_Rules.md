# RULE-SCRUM-011: Sprint Schedule Rules

- **Mã quy tắc**: `RULE-SCRUM-011`
- **Tên quy tắc**: Sprint Duration and Events Calendar Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định giới hạn độ dài của Sprint và lịch trình các sự kiện Scrum theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-010`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (The Sprint definition & timeboxes)

## 4. Đầu vào bắt buộc
Ngày bắt đầu Sprint (`start_date`), Ngày kết thúc Sprint (`end_date`).

## 5. Cấu trúc trường bắt buộc
Sprint ID, Ngày bắt đầu, Ngày kết thúc, Độ dài (tuần/ngày), Lịch các sự kiện Scrum, Kiểm tra giới hạn Timebox.

## 6. Quy tắc nội dung
1. **Độ dài Sprint**: Bắt buộc là một tháng hoặc ngắn hơn (thường từ 1 đến 4 tuần). Tuyệt đối không được vượt quá 1 tháng (tối đa 31 ngày).
2. Một Sprint mới bắt đầu ngay lập tức sau khi Sprint trước đó kết thúc; không có khoảng trống (Sprint 0, hardening sprint, v.v. không thuộc Scrum chính thức).
3. Lịch các sự kiện phải thể hiện rõ: Sprint Planning ở đầu Sprint, Daily Scrum hàng ngày, Sprint Review và Sprint Retrospective ở cuối Sprint.

## 7. Tiêu chí chất lượng
Ngày kết thúc phải lớn hơn ngày bắt đầu và hiệu số ngày <= 31 ngày.

## 8. Quy tắc đặt tên
`DOC-SCRUM-010_Sprint_Schedule.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-DEL-001` (Project Schedule).

## 10. Cách kiểm tra
Chạy bài kiểm thử `test_sprint_constraints.py` kiểm tra `end_date - start_date <= 31 days`.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn tối đa một tháng của Sprint.

## 12. Ví dụ
- Hợp lệ: Sprint 1 từ 01/11/2026 đến 14/11/2026 (14 ngày).
- Không hợp lệ: Sprint kéo dài 45 ngày hoặc 2 tháng (vi phạm nguyên tắc cốt lõi của Scrum).

## 13. Tài liệu liên quan
`DOC-SCRUM-006`, `DOC-SCRUM-012`, `DOC-SCRUM-013`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Lịch Sprint của dự án.

## 15. Giới hạn đã biết
Không có.
