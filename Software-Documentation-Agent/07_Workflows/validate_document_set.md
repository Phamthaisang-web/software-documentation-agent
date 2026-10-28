# Workflow E — Thẩm Định Bộ Tài Liệu (Document Set Validation Workflow)

## 1. Mục Đích
Kiểm tra tự động, toàn diện tính hợp lệ, đầy đủ, nhất quán và toàn vẹn của toàn bộ tài liệu dự án.

## 2. Các Bước Thực Hiện
1. **Bước 1: Kiểm tra cấu hình và Registry**:
   - Xác minh đủ 59 loại tài liệu, không trùng lặp ID, mọi rule và standard tham chiếu đều tồn tại.
2. **Bước 2: Kiểm tra nguồn tham chiếu**:
   - Kiểm tra trạng thái xác minh và URL chính thức.
3. **Bước 3: Kiểm tra cấu trúc & đề mục bắt buộc**:
   - Đối chiếu tài liệu với `required_sections`.
4. **Bước 4: Kiểm tra ràng buộc Scrum**:
   - Kiểm tra timebox Sprint (<= 31 ngày), Planning (<= 8h), Review (<= 4h), Retro (<= 3h), Daily Scrum (15 phút).
   - Kiểm tra cấm nhận nhầm DoR thành quy định bắt buộc.
5. **Bước 5: Kiểm tra ma trận truy xuất nguồn gốc (Traceability Engine)**:
   - Phát hiện Broken links, Orphan items, Missing test cases.
6. **Bước 6: Kiểm tra tệp vật lý**:
   - Kiểm tra tệp mở được, không rỗng, giữ đúng format.
7. **Bước 7: Xuất báo cáo thẩm định**:
   - Xuất tệp `validation_report.json` và `validation_report.md`.
