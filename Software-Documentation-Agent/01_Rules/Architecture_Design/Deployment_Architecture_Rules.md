# RULE-ARCH-008: Deployment Architecture Rules

- **Mã quy tắc**: `RULE-ARCH-008`
- **Tên quy tắc**: Infrastructure and Deployment Topology Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả hạ tầng phần cứng, mạng, container, cụm máy chủ và vị trí thực thi của các thành phần phần mềm.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-008`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 (Deployment Viewpoint)

## 4. Đầu vào bắt buộc
Cấu hình Docker, Kubernetes, CI/CD, máy chủ, mạng, cổng (ports).

## 5. Cấu trúc trường bắt buộc
Topo triển khai (Topology), Phân bổ Node & Tài nguyên, Mạng & Cổng kết nối, Mã nguồn sơ đồ Mermaid Deployment, Cấu hình phục hồi sau sự cố (DR).

## 6. Quy tắc nội dung
1. Phải dựa trên các tệp cấu hình triển khai thực tế (`Dockerfile`, `docker-compose.yml`, Helm charts, k8s manifests).
2. Lưu trữ mã nguồn sơ đồ Mermaid để có thể hiệu chỉnh.
3. Phân biệt rõ các môi trường: Development, Staging, Production.

## 7. Tiêu chí chất lượng
Mọi cổng dịch vụ (ports) và kết nối mạng phải có căn cứ từ cấu hình.

## 8. Quy tắc đặt tên
`DOC-ARCH-008_Deployment_Architecture.mmd`.

## 9. Truy xuất nguồn gốc
Cơ sở để viết `DOC-DEL-011` (Installation Guide) và `DOC-DEL-013` (Deployment Guide).

## 10. Cách kiểm tra
Kiểm tra sự phù hợp giữa Dockerfile/docker-compose và sơ đồ triển khai.

## 11. Ngoại lệ
Ứng dụng serverless mô tả theo kiến trúc cloud functions và gateway.

## 12. Ví dụ
- Hợp lệ: Nginx reverse proxy (Port 80/443) -> Web App container (Port 3000) -> PostgreSQL container (Port 5432).
- Không hợp lệ: Bịa đặt cụm Kubernetes đa vùng trong khi dự án chỉ chạy trên 1 VPS đơn lẻ.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-DEL-011`, `DOC-DEL-013`.

## 14. Bằng chứng cần thiết
Tệp Dockerfile, docker-compose.yml, CI/CD workflows.

## 15. Giới hạn đã biết
Không thể truy cập thông tin hạ tầng nội bộ nếu không có file cấu hình.
