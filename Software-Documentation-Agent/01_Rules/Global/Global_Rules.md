# RULE-GLOB-001: General Operating Principles (Nguyên Tắc Hoạt Động Chung)

- **Mã quy tắc**: `RULE-GLOB-001`
- **Tên quy tắc**: General Operating Principles for Software Documentation
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định các nguyên tắc hoạt động tối cao, bắt buộc áp dụng xuyên suốt hệ thống Software Documentation Agent nhằm đảm bảo tính chân thực, chính xác và có thể kiểm chứng của mọi tài liệu kỹ thuật.

## 2. Phạm vi áp dụng
Áp dụng cho toàn bộ các module phân tích dự án, tạo tài liệu, cập nhật tài liệu và kiểm thử chất lượng trong hệ thống.

## 3. Nguồn tiêu chuẩn hoặc chính sách
- ISO/IEC/IEEE 29148:2018 (Requirements engineering processes)
- ISO/IEC/IEEE 42010:2022 (Architecture description)
- The Scrum Guide (Nov 2020)
- ISO/IEC/IEEE 29119 (Software testing series)

## 4. Đầu vào bắt buộc
- Bằng chứng thực tế từ mã nguồn (source code files)
- Cấu hình dự án (package manifests, environment configs, dockerfiles)
- Lược đồ cơ sở dữ liệu (migrations, schemas, models)
- Báo cáo và log thực thi kiểm thử thực tế

## 5. Cấu trúc tài liệu hoặc trường dữ liệu bắt buộc
Mỗi tài liệu sinh ra phải có:
- Định danh tài liệu chuẩn `document_id`
- Phiên bản (`version`) và ngày cập nhật (`updated_at`)
- Trạng thái xác minh của từng mục (`VERIFIED`, `INFERRED`, `UNKNOWN`, `CONFLICT`)
- Tham chiếu bằng chứng cụ thể (`evidence_refs`)

## 6. Quy tắc nội dung
1. Luôn phân tích dự án kỹ lưỡng trước khi sinh bất kỳ tài liệu nào.
2. Ưu tiên tuyệt đối bằng chứng từ mã nguồn, tệp cấu hình, cơ sở dữ liệu, API route và kết quả kiểm thử.
3. Không tự bịa đặt tính năng, yêu cầu, vai trò, kiến trúc, công nghệ, số liệu đo lường hoặc kết quả kiểm thử.
4. Không tự xác nhận một tính năng là hoàn thành (Done) chỉ vì tìm thấy một đoạn mã nguồn liên quan.
5. Không tự xác nhận phần mềm hoạt động tốt chỉ vì mã nguồn biên dịch thành công.
6. Không tự tạo thông tin phê duyệt, chữ ký, ngày họp, thành phần tham dự khi chưa có biên bản thực tế.
7. Không nhầm lẫn giữa tiêu chuẩn chính thức (Official Standard), quy định nội bộ (Internal Policy) và đề xuất của AI (Recommendation).
8. Không tự ý sửa đổi các quyết định đã được người dùng phê duyệt trước đó.
9. Không ghi đè trực tiếp lên mẫu gốc (original template) do người dùng cung cấp.
10. Đánh dấu rõ các mục thiếu thông tin là `UNKNOWN` hoặc `TBD`.

## 7. Tiêu chí chất lượng
- Tính xác thực (Authenticity): 100% dữ liệu quan trọng có nguồn gốc rõ ràng.
- Tính nhất quán (Consistency): Không mâu thuẫn giữa các tài liệu trong cùng một bộ.
- Tính đầy đủ (Completeness): Đầy đủ các mục bắt buộc theo registry.

## 8. Quy tắc mã định danh và đặt tên
- Mã tài liệu: `DOC-{NHOM}-{SO}` (ví dụ: `DOC-REQ-001`)
- Mã yêu cầu: `REQ-{LOAI}-{SO}` (ví dụ: `REQ-FUNC-001`)
- Mã ca kiểm thử: `TC-{MODULE}-{SO}` (ví dụ: `TC-AUTH-001`)

## 9. Quy tắc truy xuất nguồn gốc
Mọi yêu cầu phải liên kết hai chiều từ Vision -> Backlog -> Design -> Test Case -> Release Note.

## 10. Cách kiểm tra
- Chạy công cụ kiểm tra tự động `validator.py` kiểm tra `evidence_refs`.
- Kiểm tra tính hợp lệ của schema `document_metadata.schema.json`.

## 11. Ngoại lệ và điều kiện áp dụng
Không có ngoại lệ đối với việc cấm bịa đặt thông tin.

## 12. Ví dụ hợp lệ và không hợp lệ
- **Hợp lệ**: "Hệ thống sử dụng JWT token cho xác thực API dựa trên khai báo trong `src/middleware/auth.ts:25`."
- **Không hợp lệ**: "Hệ thống đạt 99.99% uptime và chịu tải 10,000 req/s" (trong khi mã nguồn không có bất kỳ cấu hình cluster, benchmark hay cam kết SLA nào).

## 13. Tài liệu liên quan
Tất cả 59 tài liệu trong danh mục.

## 14. Bằng chứng cần thiết
Đường dẫn tệp, số dòng, commit hash hoặc cấu hình hệ thống.

## 15. Giới hạn đã biết
Agent không thể suy đoán các thỏa thuận miệng của ban lãnh đạo nếu không có ghi chép bằng văn bản.
