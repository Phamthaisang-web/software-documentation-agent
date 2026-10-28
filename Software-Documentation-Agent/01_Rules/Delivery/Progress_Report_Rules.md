# RULE-DEL-008: Progress Report Rules

- **Mã quy tắc**: `RULE-DEL-008`
- **Tên quy tắc**: Periodic Progress Reporting and Objective Status Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Tổng hợp tình hình thực hiện, tiến độ, chỉ số, rủi ro và kế hoạch giai đoạn tiếp theo một cách trung thực và khách quan.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-008`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Performance Reporting)

## 4. Đầu vào bắt buộc
Kỳ báo cáo, các công việc đã hoàn thành, tình trạng tiến độ các mốc, các vấn đề và rủi ro nghiêm trọng, kế hoạch kỳ tới.

## 5. Cấu trúc trường bắt buộc
Kỳ báo cáo & Tác giả, Tóm tắt điều hành (Executive Summary), Thành tựu chính trong kỳ, Trạng thái mốc & Tiến độ, Các vấn đề & Rủi ro trọng yếu, Kế hoạch kỳ tiếp theo.

## 6. Quy tắc nội dung
1. Phản ánh trung thực tình trạng dự án: Trạng thái Xanh (On track), Vàng (Có rủi ro trễ), Đỏ (Đang trễ hạn nghiêm trọng).
2. Không tô hồng số liệu hoặc che giấu các vấn đề đang làm nghẽn tiến độ.

## 7. Tiêu chí chất lượng
Các số liệu hoàn thành phải đối chiếu được với commit git hoặc task completed trong Jira.

## 8. Quy tắc đặt tên
`DOC-DEL-008_Progress_Report_{PERIOD}.docx`.

## 9. Truy xuất nguồn gốc
Tổng hợp từ `DOC-DEL-001`, `DOC-DEL-003`, `DOC-DEL-004`, `DOC-TEST-008`.

## 10. Cách kiểm tra
Kiểm tra tính nhất quán giữa tiến độ báo cáo và trạng thái các deliverables.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Báo cáo trung thực: Module A hoàn thành 100%, Module B đang trễ 3 ngày do thiếu nhân sự backend.
- Không hợp lệ: Dự án đang gặp lỗi nghiêm trọng nhưng vẫn báo cáo "mọi thứ diễn ra hoàn hảo".

## 13. Tài liệu liên quan
`DOC-DEL-001`, `DOC-DEL-003`, `DOC-DEL-004`.

## 14. Bằng chứng cần thiết
Dữ liệu từ hệ thống quản lý công việc và CI/CD.

## 15. Giới hạn đã biết
Không có.
