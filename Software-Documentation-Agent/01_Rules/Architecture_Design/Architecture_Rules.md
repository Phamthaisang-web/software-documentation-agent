# RULE-ARCH-001: Software Architecture Description Rules

- **Mã quy tắc**: `RULE-ARCH-001`
- **Tên quy tắc**: Architectural Viewpoints and ISO 42010 Conformance Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định phương pháp mô tả kiến trúc phần mềm toàn diện qua các góc nhìn kiến trúc (Architectural Views) theo tiêu chuẩn ISO/IEC/IEEE 42010:2022.

## 2. Phạm vi áp dụng
Tài liệu `DOC-ARCH-001` (SAD).

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 42010:2022 (Architecture description conceptual framework)

## 4. Đầu vào bắt buộc
Bối cảnh hệ thống, các bên liên quan, các mối quan tâm kiến trúc (concerns), các quyết định then chốt.

## 5. Cấu trúc trường bắt buộc
Bối cảnh kiến trúc & Stakeholders, Các góc nhìn kiến trúc (Component View, Runtime/Execution View, Deployment View), Hiện thực hóa các thuộc tính chất lượng (Quality Attributes).

## 6. Quy tắc nội dung
1. Phân biệt rõ ranh giới giữa:
   - Kiến trúc ĐÃ TRIỂN KHAI THỰC TẾ (Implemented Architecture - có code chứng minh).
   - Kiến trúc ĐƯỢC ĐỀ XUẤT (Proposed Architecture - định hướng tương lai).
   - Kiến trúc ĐANG THỬ NGHIỆM (Experimental).
2. Không tuyên bố rằng ISO 42010 áp đặt một mẫu tài liệu duy nhất (tiêu chuẩn quy định khung khái niệm và các viewpoint).
3. Mỗi góc nhìn kiến trúc phải giải quyết các mối quan tâm cụ thể của các nhóm stakeholder tương ứng.

## 7. Tiêu chí chất lượng
Mỗi sơ đồ kiến trúc phải có chú thích rõ ràng về giao thức kết nối, luồng dữ liệu và trách nhiệm của từng node.

## 8. Quy tắc đặt tên
`DOC-ARCH-001_Software_Architecture_Description.docx`.

## 9. Truy xuất nguồn gốc
Liên kết trực tiếp tới `DOC-REQ-001` (SRS), `DOC-ARCH-007` (Component Diagram) và `DOC-ARCH-008` (Deployment).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của các Views và chú thích trạng thái triển khai.

## 11. Ngoại lệ
Hệ thống script đơn lẻ (CLI tool nhỏ) có thể rút gọn Runtime View.

## 12. Ví dụ
- Hợp lệ: "Hệ thống áp dụng mô hình Clean Architecture gồm các tầng Domain, Application, Infrastructure và Presentation."
- Không hợp lệ: Tự nhận hệ thống là Microservices phân tán trong khi toàn bộ mã nguồn nằm chung 1 tệp monolith.

## 13. Tài liệu liên quan
`DOC-ARCH-002`, `DOC-ARCH-007`, `DOC-ARCH-008`, `DOC-ARCH-010`.

## 14. Bằng chứng cần thiết
Mã nguồn cấu trúc thư mục dự án, Docker Compose hoặc sơ đồ dịch vụ.

## 15. Giới hạn đã biết
Không thể phân tích các dịch vụ SaaS của bên thứ 3 nếu không có thông số cấu hình.
