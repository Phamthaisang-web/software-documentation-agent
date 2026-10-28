# RULE-SCRUM-007: Sprint Planning Rules

- **Mã quy tắc**: `RULE-SCRUM-007`
- **Tên quy tắc**: Sprint Planning Event and Topics Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định nội dung và giới hạn thời lượng (Timebox) của sự kiện Sprint Planning theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-006`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Sprint Planning Event)

## 4. Đầu vào bắt buộc
Product Goal, Product Backlog đã làm mịn, năng lực khả dụng của nhóm (Capacity), Increment gần nhất.

## 5. Cấu trúc trường bắt buộc
Bao gồm đủ 3 chủ đề (Topics) của Scrum Guide 2020:
- Chủ đề 1: Tại sao Sprint này có giá trị? (Why is this Sprint valuable? -> Định hình **Sprint Goal**).
- Chủ đề 2: Những gì có thể Hoàn thành trong Sprint này? (What can be Done this Sprint? -> Chọn các **PBIs**).
- Chủ đề 3: Công việc đã chọn sẽ được hoàn thành như thế nào? (How will the chosen work get done? -> Lập kế hoạch hành động / phân rã tasks).
- Giới hạn thời gian (Timebox Compliance): Tối đa 8 giờ cho Sprint 1 tháng.

## 6. Quy tắc nội dung
1. Thời lượng sự kiện Sprint Planning tối đa là 8 giờ đối với Sprint 1 tháng; Sprint ngắn hơn thường có thời lượng ngắn hơn (ví dụ: Sprint 2 tuần thường tối đa 4 giờ).
2. Sprint Goal phải được thống nhất trong sự kiện này trước khi kết thúc phiên họp.
3. Chỉ Developers mới có quyền quyết định lượng công việc có thể hoàn thành trong Sprint.
4. Không tự bịa đặt nội dung phiên họp nếu Sprint chưa diễn ra.

## 7. Tiêu chí chất lượng
Trả lời trọn vẹn cả 3 câu hỏi Chủ đề 1, 2, 3 của Scrum Guide.

## 8. Quy tắc đặt tên
`DOC-SCRUM-006_Sprint_Planning.docx`.

## 9. Truy xuất nguồn gốc
Tạo ra `DOC-SCRUM-007` (Sprint Backlog) và `DOC-SCRUM-008` (Sprint Goal).

## 10. Cách kiểm tra
Kiểm tra Timebox <= 8h và sự hiện diện của cả 3 Topics trong `test_sprint_constraints.py`.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn timebox.

## 12. Ví dụ
- Hợp lệ: Sprint 2 tuần, thời lượng Planning 3.5 giờ, xác lập Sprint Goal và chọn 5 PBIs.
- Không hợp lệ: Sprint Planning kéo dài 12 giờ cho Sprint 2 tuần (vi phạm nghiêm trọng timebox).

## 13. Tài liệu liên quan
`DOC-SCRUM-007`, `DOC-SCRUM-008`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Biên bản Sprint Planning thực tế.

## 15. Giới hạn đã biết
Không có.
