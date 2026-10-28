# RULE-SCRUM-013: Sprint Review Rules

- **Mã quy tắc**: `RULE-SCRUM-013`
- **Tên quy tắc**: Sprint Review Event and Timebox Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định nội dung và thời lượng của sự kiện Sprint Review theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-012`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Sprint Review Event)

## 4. Đầu vào bắt buộc
Increment thực tế hoàn thành đáp ứng DoD, phản hồi của bên liên quan (Stakeholders).

## 5. Cấu trúc trường bắt buộc
Sprint ID, Đánh giá mức độ đạt được Sprint Goal, Các mục Done (đáp ứng DoD), Các mục Chưa Done (trả về Product Backlog), Trình diễn Increment, Phản hồi của Stakeholders & Điều chỉnh Backlog tiếp theo.

## 6. Quy tắc nội dung
1. **Timebox bắt buộc**: Sprint Review có thời lượng tối đa **4 giờ** đối với Sprint một tháng; Sprint ngắn hơn thường có sự kiện ngắn hơn (ví dụ Sprint 2 tuần thường tối đa 2 giờ).
2. Sprint Review là một buổi làm việc cộng tác (working session) để kiểm tra kết quả và xác định các điều chỉnh tiếp theo, KHÔNG chỉ đơn thuần là buổi thuyết trình (demo/presentation).
3. Chỉ những PBI đáp ứng trọn vẹn Definition of Done mới được trình diễn và coi là hoàn thành.
4. Những mục chưa hoàn thành không được coi là Increment và phải được chuyển lại về Product Backlog.
5. Không tự bịa đặt người tham dự hoặc biên bản review nếu sự kiện chưa diễn ra.

## 7. Tiêu chí chất lượng
Có phản hồi thực chất từ các bên liên quan và điều chỉnh Backlog cụ thể.

## 8. Quy tắc đặt tên
`DOC-SCRUM-012_Sprint_Review_Report.docx`.

## 9. Truy xuất nguồn gốc
Cập nhật lại `DOC-SCRUM-001` (Product Backlog).

## 10. Cách kiểm tra
Kiểm tra Timebox <= 4h trong `test_sprint_constraints.py`.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn 4 giờ.

## 12. Ví dụ
- Hợp lệ: Sprint 2 tuần, Review 1.5 giờ, PO và khách hàng dùng thử tính năng tìm kiếm và gợi ý thêm bộ lọc.
- Không hợp lệ: Họp Sprint Review 6 giờ hoặc tự nhận các PBI lỗi là Done.

## 13. Tài liệu liên quan
`DOC-SCRUM-008`, `DOC-SCRUM-014`, `DOC-SCRUM-015`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Biên bản Sprint Review thực tế.

## 15. Giới hạn đã biết
Không có.
