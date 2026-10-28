# Official Sources Registry — Nguồn Tham Chiếu Chính Thức

Tài liệu này ghi nhận đầy đủ nguồn gốc, đường dẫn chính thức và ghi chú thẩm định cho từng tiêu chuẩn kỹ thuật được AI Agent sử dụng.

---

## 1. Scrum Guide

- **Tên chính thức**: The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game.
- **Tác giả**: Ken Schwaber and Jeff Sutherland.
- **Trang web chính thức**: [scrumguides.org](https://scrumguides.org/scrum-guide.html)
- **Trang tải và lịch sử phiên bản**: [scrumguides.org/download.html](https://scrumguides.org/download.html)
- **Bản tiếng Việt chính thức**: [2020-Scrum-Guide-Vietnamese.pdf](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Vietnamese.pdf)
- **Phiên bản hiện hành**: Tháng 11 năm 2020.
- **Giấy phép**: Creative Commons Attribution-ShareAlike (CC BY-SA 4.0).
- **Trạng thái**: `VERIFIED_OFFICIAL` (Đã xác minh toàn bộ văn bản gốc).
- **Quy tắc thời lượng bắt buộc (Scrum Timeboxes)**:
  - *Sprint Length*: 1 tháng hoặc ngắn hơn.
  - *Sprint Planning*: Tối đa 8 giờ đối với Sprint 1 tháng; Sprint ngắn hơn thường ngắn hơn (ví dụ Sprint 2 tuần thường tối đa 4 giờ).
  - *Daily Scrum*: 15 phút cho Developers.
  - *Sprint Review*: Tối đa 4 giờ đối với Sprint 1 tháng.
  - *Sprint Retrospective*: Tối đa 3 giờ đối với Sprint 1 tháng.
- **Các hiểu lầm thường gặp được làm rõ**:
  - Tám (8) giờ làm việc mỗi ngày **không** phải quy định của Scrum Guide (Scrum Guide chỉ quy định thời lượng sự kiện, không quy định giờ làm việc hành chính).
  - Sprint 2 tuần không bắt buộc cho mọi nhóm; nhóm có quyền chọn độ dài từ 1 tháng trở xuống.
  - Story Point, Velocity, Burndown chart, Daily Scrum Log, Definition of Ready (DoR) là thông lệ bổ sung phổ biến, **không** phải yêu cầu bắt buộc của Scrum Guide.
  - 3 Cam kết (Commitments) chính thức:
    - Product Backlog gắn với **Product Goal**.
    - Sprint Backlog gắn với **Sprint Goal**.
    - Increment gắn với **Definition of Done**.

---

## 2. Kỹ Thuật Yêu Cầu Phần Mềm (Requirements Engineering)

- **Tên chính thức**: ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering.
- **Tổ chức**: ISO / IEC / IEEE.
- **Cổng ISO tra cứu**: [iso.org/standard/72089.html](https://www.iso.org/standard/72089.html)
- **Phiên bản**: 2018 (Xác nhận lại năm 2024).
- **Trạng thái**: `VERIFIED_OFFICIAL` (Xác minh thông tin danh mục, mục tiêu và cấu trúc qua ISO portal).
- **Giới hạn**: Tiêu chuẩn có bản quyền. Tài liệu của Agent định hình theo cấu trúc mục tiêu và tiêu chuẩn chất lượng (tính rõ ràng, khả thi, truy xuất được, không mâu thuẫn).

---

## 3. Kiến Trúc Phần Mềm (Software Architecture)

- **Tên chính thức**: ISO/IEC/IEEE 42010:2022 Software, systems and enterprise — Architecture description.
- **Tổ chức**: ISO / IEC / IEEE.
- **Cổng ISO tra cứu**: [iso.org/standard/74393.html](https://www.iso.org/standard/74393.html)
- **Phiên bản**: 2022 (Ấn bản lần 3).
- **Trạng thái**: `VERIFIED_OFFICIAL`.
- **Phạm vi**: Khung khái niệm mô tả kiến trúc (Stakeholders, Concerns, Viewpoints, Views, Models, Decisions - ADR).
- **Lưu ý**: Tiêu chuẩn không áp đặt một mẫu SAD/SDD duy nhất, mà đưa ra các nguyên tắc cấu trúc góc nhìn kiến trúc.

---

## 4. Kiểm Thử Phần Mềm (Software Testing)

- **ISO/IEC/IEEE 29119-1:2022** (General concepts): [iso.org/standard/79427.html](https://www.iso.org/standard/79427.html)
- **ISO/IEC/IEEE 29119-2:2021** (Test processes): [iso.org/standard/79428.html](https://www.iso.org/standard/79428.html)
- **ISO/IEC/IEEE 29119-3:2021** (Test documentation): [iso.org/standard/79429.html](https://www.iso.org/standard/79429.html)
- **ISO/IEC/IEEE 29119-4:2021** (Test techniques): [iso.org/standard/79430.html](https://www.iso.org/standard/79430.html)
- **Trạng thái**: `VERIFIED_OFFICIAL` (Từng phần tiêu chuẩn đã được kiểm tra URL cụ thể theo yêu cầu).
- **Quy tắc kiểm thử**:
  - Phân biệt thiết kế kiểm thử (Test Case Spec) với kết quả thực thi kiểm thử (Test Execution Report).
  - Không được sao chép kết quả mong đợi thành kết quả thực tế khi chưa chạy test thực tế.

---

## 5. Quản Lý Dự Án (Project Management)

- **Tên chính thức**: ISO 21500:2021 Project, programme and portfolio management — Context and concepts.
- **Cổng ISO tra cứu**: [iso.org/standard/74620.html](https://www.iso.org/standard/74620.html)
- **Trạng thái**: `VERIFIED_OFFICIAL`.

---

## 6. Đặc Tả Giao Diện API & Bảo Mật

- **OpenAPI Specification 3.1.0**: [spec.openapis.org/oas/v3.1.0](https://spec.openapis.org/oas/v3.1.0) — `VERIFIED_OFFICIAL`.
- **OWASP Top 10 (2021)**: [owasp.org/Top10/](https://owasp.org/Top10/) — `VERIFIED_OFFICIAL`.
