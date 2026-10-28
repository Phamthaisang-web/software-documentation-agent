# RULE-SCRUM-019: Scrum Timebox Rules

- **Mã quy tắc**: `RULE-SCRUM-019`
- **Tên quy tắc**: Strict Scrum Events Timeboxing Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định chặt chẽ và chính xác giới hạn thời gian (Timebox) cho tất cả các sự kiện Scrum theo đúng quy định của The Scrum Guide (Nov 2020).

## 2. Phạm vi áp dụng
Tất cả các tài liệu về sự kiện và lịch trình Scrum (`DOC-SCRUM-006`, `DOC-SCRUM-010`, `DOC-SCRUM-011`, `DOC-SCRUM-012`, `DOC-SCRUM-013`).

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (The Events of Scrum)

## 4. Đầu vào bắt buộc
Độ dài Sprint (`sprint_duration`), thời lượng dự kiến của từng sự kiện.

## 5. Cấu trúc trường bắt buộc
Bảng kiểm tra tuân thủ Timebox cho từng sự kiện.

## 6. Quy tắc nội dung bắt buộc
1. **The Sprint**: Tối đa 1 tháng (<= 31 ngày).
2. **Sprint Planning**: Tối đa **8 giờ** cho Sprint 1 tháng. Đối với Sprint ngắn hơn (ví dụ Sprint 2 tuần), sự kiện thường ngắn hơn (thường tối đa 4 giờ).
3. **Daily Scrum**: Đúng **15 phút** cho Developers.
4. **Sprint Review**: Tối đa **4 giờ** cho Sprint 1 tháng. Đối với Sprint ngắn hơn, sự kiện thường ngắn hơn (thường tối đa 2 giờ).
5. **Sprint Retrospective**: Tối đa **3 giờ** cho Sprint 1 tháng. Đối với Sprint ngắn hơn, sự kiện thường ngắn hơn (thường tối đa 1.5 giờ).
6. **LÀM RÕ CÁC HIỂU LẦM**:
   - Scrum Guide **KHÔNG** quy định ngày làm việc phải là 8 giờ (đây là luật lao động hành chính, không phải quy tắc Scrum).
   - Scrum Guide **KHÔNG** bắt buộc mọi Sprint phải dài 2 tuần.
   - Khi hết thời lượng timebox quy định, sự kiện kết thúc ngay lập tức.

## 7. Tiêu chí chất lượng
100% thời lượng sự kiện khai báo trong tài liệu không vượt quá ngưỡng tối đa của Scrum Guide.

## 8. Quy tắc đặt tên
`RULE-SCRUM-019`.

## 9. Truy xuất nguồn gốc
Được kiểm tra tự động qua bộ test suite `test_sprint_constraints.py`.

## 10. Cách kiểm tra
Hàm kiểm tra `validate_sprint_timeboxes()` kiểm tra các giá trị giờ.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn trần của timebox.

## 12. Ví dụ
- Hợp lệ: Sprint 1 tháng có Sprint Planning 7 giờ, Review 3.5 giờ, Retro 2.5 giờ, Daily Scrum 15 phút.
- Không hợp lệ: Sprint 2 tuần mà xếp lịch Sprint Planning 10 giờ (vi phạm nghiêm trọng).

## 13. Tài liệu liên quan
`DOC-SCRUM-006`, `DOC-SCRUM-010`, `DOC-SCRUM-011`, `DOC-SCRUM-012`, `DOC-SCRUM-013`.

## 14. Bằng chứng cần thiết
Lịch biểu sự kiện Scrum trong dự án.

## 15. Giới hạn đã biết
Không có.
