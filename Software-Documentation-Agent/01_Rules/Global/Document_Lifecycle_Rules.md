# RULE-GLOB-011: Document Lifecycle Rules (Quy Tắc Vòng Đời Tài Liệu)

- **Mã quy tắc**: `RULE-GLOB-011`
- **Tên quy tắc**: Document Lifecycle and State Transition Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định các trạng thái và điều kiện chuyển đổi trạng thái của tài liệu từ lúc khởi tạo đến khi lưu trữ.

## 2. Phạm vi áp dụng
Tất cả các tài liệu kỹ thuật trong hệ thống.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Document and Records Control)

## 4. Đầu vào bắt buộc
Trường `lifecycle_status` trong metadata.

## 5. Cấu trúc trường bắt buộc
Trạng thái hợp lệ: `DRAFT`, `UNDER_REVIEW`, `APPROVED`, `SUPERSEDED`, `DEPRECATED`.

## 6. Quy tắc nội dung
1. Tài liệu mới sinh ra tự động có trạng thái `DRAFT` cho đến khi vượt qua bộ kiểm tra chất lượng.
2. Tài liệu chuyển sang `APPROVED` chỉ khi có xác nhận chính thức hoặc phê duyệt từ người dùng/stakeholder có thẩm quyền.
3. Tuyệt đối không tự động gán nhãn `APPROVED` khi chưa có bằng chứng phê duyệt.
4. Khi tài liệu được cập nhật phiên bản mới, phiên bản cũ chuyển sang trạng thái `SUPERSEDED`.
5. Tài liệu không còn áp dụng chuyển sang `DEPRECATED`.

## 7. Tiêu chí chất lượng
100% tài liệu có trạng thái vòng đời xác định.

## 8. Quy tắc đặt tên
Trạng thái chữ hoa chuẩn enum.

## 9. Truy xuất nguồn gốc
Theo dõi trong metadata `{DOC_ID}.meta.yaml`.

## 10. Cách kiểm tra
Kiểm tra qua schema `document_metadata.schema.json`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Agent sinh tài liệu xong để trạng thái `DRAFT` và chờ người dùng duyệt.
- Không hợp lệ: Agent tự ý ghi "Approved by CTO John Doe" khi chưa có xác nhận.

## 13. Tài liệu liên quan
Tất cả 59 tài liệu.

## 14. Bằng chứng cần thiết
Biên bản phê duyệt hoặc xác nhận của người dùng.

## 15. Giới hạn đã biết
Không có.
