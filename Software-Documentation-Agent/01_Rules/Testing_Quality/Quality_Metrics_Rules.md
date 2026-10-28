# RULE-TEST-008: Quality Metrics Report Rules

- **Mã quy tắc**: `RULE-TEST-008`
- **Tên quy tắc**: Quality Metrics Quantification and Sourcing Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc tính toán và báo cáo các chỉ số chất lượng phần mềm (Test Pass Rate, Code Coverage, Defect Density) dựa trên dữ liệu đo đạc thực tế.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-008`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-1:2022
- ISO/IEC 25010:2023

## 4. Đầu vào bắt buộc
Nguồn dữ liệu đo đạc, công thức tính toán, thời điểm đo, giá trị chỉ số thực tế.

## 5. Cấu trúc trường bắt buộc
Phạm vi & Khoảng thời gian đo, Nguồn dữ liệu & Công thức tính, Bảng chỉ số chất lượng (Pass Rate, Defect Density, Code Coverage), Phân tích & Hạn chế, Đánh giá ngưỡng mục tiêu.

## 6. Quy tắc nội dung
1. Mọi số liệu báo cáo phải nêu rõ công thức tính toán và nguồn công cụ đo đạc (ví dụ: SonarQube, Jest coverage, JaCoCo, pytest-cov).
2. Tuyệt đối không tự bịa đặt chỉ số code coverage (ví dụ: ghi 95% khi dự án không có file coverage report nào).
3. Nếu chưa đo đạc được, phải ghi rõ `NOT_MEASURED` kèm lý do kỹ thuật.

## 7. Tiêu chí chất lượng
Chỉ số có nguồn dữ liệu đối chiếu minh bạch.

## 8. Quy tắc đặt tên
`DOC-TEST-008_Quality_Metrics_Report.xlsx`.

## 9. Truy xuất nguồn gốc
Hỗ trợ dữ liệu cho `DOC-DEL-008` (Progress Report).

## 10. Cách kiểm tra
Kiểm tra tệp coverage hoặc test log tương ứng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Code coverage: 82.4% dựa trên báo cáo `coverage/lcov.info` tạo ngày 28/10/2026."
- Không hợp lệ: Tự điền 100% test pass rate và 100% coverage mà không có log.

## 13. Tài liệu liên quan
`DOC-TEST-004`, `DOC-DEL-008`.

## 14. Bằng chứng cần thiết
Tệp `coverage.xml`, `lcov.info` hoặc log thực thi CI.

## 15. Giới hạn đã biết
Không có.
