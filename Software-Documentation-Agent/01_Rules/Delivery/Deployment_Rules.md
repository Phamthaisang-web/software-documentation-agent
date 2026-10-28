# RULE-DEL-013: Production Deployment Rules

- **Mã quy tắc**: `RULE-DEL-013`
- **Tên quy tắc**: Production Deployment Runbook and Rollback Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả quy trình triển khai môi trường Production, di chuyển dữ liệu (DB Migration), kiểm tra sau deploy và quy trình rollback khẩn cấp.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-013`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 & DevOps / SRE Standard Operating Procedures

## 4. Đầu vào bắt buộc
Các bước triển khai, quy trình rollback khi gặp sự cố, checklist kiểm tra sau deploy (Smoke tests), kế hoạch backup dữ liệu.

## 5. Cấu trúc trường bắt buộc
Môi trường mục tiêu, Checklist trước triển khai & Sao lưu dữ liệu (Pre-deployment Backup), Các bước thực thi triển khai (Deployment steps), Quy trình chạy migration CSDL, Quy trình Rollback khẩn cấp, Kiểm tra xác thực sau deploy (Post-deployment Smoke Testing).

## 6. Quy tắc nội dung
1. BẮT BUỘC phải có **Quy trình Rollback (Khôi phục trạng thái cũ)** chi tiết từng bước. Không bao giờ triển khai production mà không có phương án rollback.
2. Bắt buộc có bước sao lưu dữ liệu (Database Backup) trước khi chạy bất kỳ migration nào.
3. Quy định rõ thời gian bảo trì (Maintenance Window) và kịch bản thông báo người dùng nếu có downtime.

## 7. Tiêu chí chất lượng
Các lệnh rollback phải có thể thực thi nhanh chóng để phục hồi hệ thống khi có sự cố.

## 8. Quy tắc đặt tên
`DOC-DEL-013_Deployment_Guide.md`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-ARCH-008` (Deployment Architecture) và hỗ trợ phát hành `DOC-DEL-009`.

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của phần `Rollback Procedure` và `Backup Checklist`.

## 11. Ngoại lệ
Không có ngoại lệ đối với việc bắt buộc phải có quy trình Rollback.

## 12. Ví dụ
- Hợp lệ: "Nếu migration DB thất bại: 1. Dừng container mới. 2. Khôi phục backup DB từ `s3://backup/pre-deploy.dump`. 3. Khởi chạy lại image phiên bản cũ v1.1.0."
- Không hợp lệ: Hướng dẫn deploy mà không có bất kỳ dòng nào về cách cứu vãn hệ thống nếu lỗi.

## 13. Tài liệu liên quan
`DOC-ARCH-008`, `DOC-DEL-011`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Tệp CI/CD pipeline (`.github/workflows/deploy.yml`) hoặc deployment script.

## 15. Giới hạn đã biết
Không có.
