# RULE-GLOB-008: Privacy and Security Rules (Quy Tắc Bảo Mật và Quyền Riêng Tư)

- **Mã quy tắc**: `RULE-GLOB-008`
- **Tên quy tắc**: Confidentiality, Secret Sanitization and Data Protection Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Ngăn chặn tuyệt đối việc lộ lọt thông tin nhạy cảm, thông tin bí mật, khóa truy cập (API keys, passwords, private keys) trong tài liệu kỹ thuật.

## 2. Phạm vi áp dụng
Toàn bộ mã nguồn, tệp cấu hình và tài liệu được phân tích và tạo ra.

## 3. Nguồn tiêu chuẩn
- OWASP Top 10:2021 (A07: Identification and Authentication Failures)
- ISO/IEC 27001:2022 (Information Security Management)

## 4. Đầu vào bắt buộc
Quá trình quét và lọc văn bản trước khi đưa vào tài liệu.

## 5. Cấu trúc trường bắt buộc
Cơ chế mặt nạ (Masking / Redaction): Các chuỗi nhạy cảm phải được thay bằng `[REDACTED_API_KEY]`, `[REDACTED_SECRET]`, `********`.

## 6. Quy tắc nội dung
1. Tuyệt đối không sao chép API key, secret token, private SSH key, password vào tài liệu.
2. Không lưu trữ thông tin cá nhân (PII) thật của khách hàng vào tài liệu ví dụ (sử dụng dữ liệu giả lập như `user@example.com`).
3. Không thực thi tự động các tệp script lạ hoặc lệnh không đáng tin cậy tìm thấy trong repository.
4. Không gửi dữ liệu mã nguồn độc quyền ra các dịch vụ ngoài khi chưa được phép.

## 7. Tiêu chí chất lượng
Zero secret leakage: Không có bất kỳ credential nào tồn tại trong thư mục `output/`.

## 8. Quy tắc đặt tên
Pattern nhận diện secret: `.*(api[_-]?key|secret|password|token|private[_-]?key).*`.

## 9. Truy xuất nguồn gốc
Ghi nhận trong báo cáo thẩm định an toàn bảo mật.

## 10. Cách kiểm tra
Bộ lọc regex quét credential trong engine kiểm tra.

## 11. Ngoại lệ
Các giá trị giả lập mẫu trong hướng dẫn (ví dụ: `password: "example_password_123"`) phải được đánh dấu rõ là ví dụ minh họa.

## 12. Ví dụ
- Hợp lệ: `Authorization: Bearer <USER_JWT_TOKEN>`
- Không hợp lệ: `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR...` (token thật).

## 13. Tài liệu liên quan
`DOC-ARCH-005` (API Spec), `DOC-DEL-011` (Install Guide), `DOC-DEL-013` (Deployment Guide).

## 14. Bằng chứng cần thiết
Báo cáo kiểm tra secret scanning sạch.

## 15. Giới hạn đã biết
Các khóa mã hóa được obfuscate phức tạp có thể cần cấu hình regex chuyên biệt.
