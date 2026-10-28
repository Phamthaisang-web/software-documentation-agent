# RULE-SCRUM-001: Foundational Scrum Framework Rules

- **Mã quy tắc**: `RULE-SCRUM-001`
- **Tên quy tắc**: Official Scrum Guide 2020 Core Governance Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định việc áp dụng khuôn khổ Scrum đúng định nghĩa chính thức của The Scrum Guide (Nov 2020), loại bỏ các hiểu lầm và ngăn chặn việc gán nhãn sai các thông lệ tùy chọn thành luật Scrum bắt buộc.

## 2. Phạm vi áp dụng
Toàn bộ quy trình và tài liệu Scrum (`DOC-SCRUM-001` đến `DOC-SCRUM-017`).

## 3. Nguồn tiêu chuẩn
- The Scrum Guide (November 2020), Ken Schwaber & Jeff Sutherland (`STD-SCRUM-2020`).

## 4. Đầu vào bắt buộc
Khai báo cấu hình Scrum Team, độ dài Sprint, các sự kiện và hiện vật Scrum.

## 5. Cấu trúc trường bắt buộc
Các vai trò (Accountabilities: Product Owner, Scrum Master, Developers), Các sự kiện (Events: Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective), Các hiện vật (Artifacts: Product Backlog, Sprint Backlog, Increment) kèm 3 Cam kết (Commitments: Product Goal, Sprint Goal, Definition of Done).

## 6. Quy tắc nội dung
1. Sprint có độ dài cố định từ một tháng trở xuống. Không bắt buộc mọi Sprint phải dài 2 tuần.
2. 3 Hiện vật và 3 Cam kết chính thức:
   - Product Backlog gắn với Cam kết: **Product Goal**.
   - Sprint Backlog gắn với Cam kết: **Sprint Goal**.
   - Increment gắn với Cam kết: **Definition of Done**.
3. Product Owner chịu trách nhiệm tối đa hóa giá trị sản phẩm và quản lý Product Backlog.
4. Developers chịu trách nhiệm tạo ra Increment có thể sử dụng được mỗi Sprint đáp ứng DoD.
5. Không được diễn giải "8 giờ làm việc mỗi ngày" là quy định của Scrum Guide (Scrum Guide chỉ quy định thời lượng timebox cho các sự kiện, không quy định giờ làm việc hành chính).
6. Phân biệt rõ: Story Points, Velocity, Burndown Charts, Definition of Ready (DoR), Daily Scrum Log là các kỹ thuật/thông lệ bổ trợ (Complementary Practices), KHÔNG phải là quy tắc bắt buộc của Scrum Guide.
7. Không tự bịa đặt nhiệm vụ hoàn thành, kết quả họp, người tham dự hoặc dữ liệu Velocity giả.

## 7. Tiêu chí chất lượng
100% tài liệu Scrum tuân thủ đúng định nghĩa thuật ngữ của Scrum Guide 2020.

## 8. Quy tắc đặt tên
`DOC-SCRUM-{NUMBER}_{Name}`.

## 9. Truy xuất nguồn gốc
Liên kết với `02_Standards/official_sources.md`.

## 10. Cách kiểm tra
Chạy bài kiểm thử tự động `test_sprint_constraints.py`.

## 11. Ngoại lệ
Nếu nhóm áp dụng quy định riêng, phải ghi chú rõ là `INTERNAL_POLICY`, không được ghi là Scrum Guide.

## 12. Ví dụ
- Hợp lệ: "Nhóm chọn Sprint 3 tuần; Sprint Planning kéo dài tối đa 6 giờ."
- Không hợp lệ: "Scrum Guide bắt buộc mọi nhóm phải làm việc 8 tiếng/ngày và phải dùng Story Point."

## 13. Tài liệu liên quan
`DOC-SCRUM-001` đến `DOC-SCRUM-017`.

## 14. Bằng chứng cần thiết
Cấu hình dự án và biên bản phiên họp Scrum.

## 15. Giới hạn đã biết
Không có.
