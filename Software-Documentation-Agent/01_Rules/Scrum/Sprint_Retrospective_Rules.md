# RULE-SCRUM-014: Sprint Retrospective Rules

- **Mã quy tắc**: `RULE-SCRUM-014`
- **Tên quy tắc**: Sprint Retrospective Event and Continuous Improvement Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định nội dung và thời lượng của sự kiện Sprint Retrospective theo Scrum Guide 2020 nhằm cải tiến liên tục.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-013`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Sprint Retrospective Event)

## 4. Đầu vào bắt buộc
Những điều làm tốt, những khó khăn vướng mắc, các hành động cải tiến cụ thể.

## 5. Cấu trúc trường bắt buộc
Sprint ID, Thành phần tham dự (Scrum Team), Điểm tích cực / Thành công, Khó khăn / Trở ngại, Kế hoạch hành động cải tiến cho Sprint tới (có Người phụ trách), Cải tiến Definition of Done (nếu có).

## 6. Quy tắc nội dung
1. **Timebox bắt buộc**: Sprint Retrospective có thời lượng tối đa **3 giờ** đối với Sprint một tháng; Sprint ngắn hơn thường ngắn hơn (ví dụ Sprint 2 tuần thường tối đa 1.5 giờ).
2. Sự kiện tập trung vào con người, mối quan hệ, quy trình và công cụ để nâng cao chất lượng và hiệu quả.
3. Nhóm xác định các thay đổi hữu ích nhất và đưa ít nhất một hành động cải tiến có tác động cao vào Sprint Backlog của Sprint tiếp theo.
4. Không tự bịa đặt nội dung họp nếu sự kiện chưa diễn ra.

## 7. Tiêu chí chất lượng
Mỗi hành động cải tiến phải có người phụ trách và cách đo lường kết quả.

## 8. Quy tắc đặt tên
`DOC-SCRUM-013_Sprint_Retrospective.docx`.

## 9. Truy xuất nguồn gốc
Hành động cải tiến chuyển vào `DOC-SCRUM-006` của Sprint kế tiếp.

## 10. Cách kiểm tra
Kiểm tra Timebox <= 3h trong `test_sprint_constraints.py`.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn 3 giờ.

## 12. Ví dụ
- Hợp lệ: Sprint 2 tuần, Retro 1 giờ, thống nhất hành động: "Tự động hóa linting trước khi commit để giảm lỗi code review."
- Không hợp lệ: Retrospective kéo dài 5 giờ.

## 13. Tài liệu liên quan
`DOC-SCRUM-006`, `DOC-SCRUM-014`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Biên bản Sprint Retrospective thực tế.

## 15. Giới hạn đã biết
Không có.
