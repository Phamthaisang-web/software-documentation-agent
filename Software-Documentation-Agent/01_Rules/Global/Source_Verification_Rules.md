# RULE-GLOB-002: Source Verification Rules (Quy Tắc Xác Minh Nguồn Tham Chiếu)

- **Mã quy tắc**: `RULE-GLOB-002`
- **Tên quy tắc**: Source Verification and Integrity Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định quy chuẩn xác minh nguồn tham khảo, phân loại thẩm quyền của nguồn và ngăn chặn trích dẫn giả mạo.

## 2. Phạm vi áp dụng
Mọi tài liệu, chuẩn kỹ thuật, đường dẫn URL hoặc chính sách được tham chiếu trong tài liệu dự án.

## 3. Nguồn tiêu chuẩn hoặc chính sách
- Chính sách kiểm tra nguồn: `02_Standards/source_verification_policy.md`
- Danh mục chuẩn: `config/standards_registry.yaml`

## 4. Đầu vào bắt buộc
- Bản ghi nguồn (`source_reference`) gồm: `source_id`, `source_name`, `url`, `version`, `verification_status`.

## 5. Cấu trúc trường dữ liệu bắt buộc
- `verification_status` bắt buộc phải là một trong các giá trị:
  - `VERIFIED_OFFICIAL`
  - `VERIFIED_AUTHORITATIVE`
  - `USER_PROVIDED`
  - `INTERNAL_POLICY`
  - `UNVERIFIED`
  - `UNAVAILABLE`
  - `SUPERSEDED`

## 6. Quy tắc nội dung
1. Luôn ưu tiên trang chính thức của tổ chức ban hành tiêu chuẩn hoặc tác giả gốc.
2. Kiểm tra phiên bản, phạm vi áp dụng và tình trạng hiệu lực trước khi gán nhãn `VERIFIED_OFFICIAL`.
3. Không tự bịa đặt URL, mã điều khoản, số trang hoặc nội dung trích dẫn.
4. Nếu chỉ tiếp cận được phần tóm tắt của tiêu chuẩn có bản quyền trả phí, phải ghi rõ giới hạn đó, không tuyên bố đã đọc toàn văn.
5. Phân biệt nội dung bắt buộc của tiêu chuẩn với tài liệu hướng dẫn triển khai phụ trợ.
6. Không sao chép trái phép toàn bộ nội dung tiêu chuẩn thương mại có bản quyền.
7. Nếu không kiểm tra được nguồn mới nhất, phải công khai hạn chế trong báo cáo.

## 7. Tiêu chí chất lượng
100% các tiêu chuẩn chính thức có URL hợp lệ trỏ tới tên miền của tổ chức ban hành.

## 8. Quy tắc mã định danh
Định danh nguồn: `STD-{LINH_VUC}-{MA}` (ví dụ: `STD-SCRUM-2020`, `STD-REQ-29148`).

## 9. Quy tắc truy xuất nguồn gốc
Mỗi `document_record` trong `document_registry.yaml` phải trỏ đến các `source_id` hợp lệ trong `standards_registry.yaml`.

## 10. Cách kiểm tra
Chạy bài kiểm thử tự động `test_source_registry.py` để quét trạng thái và định dạng nguồn.

## 11. Ngoại lệ và điều kiện áp dụng
Tài liệu nội bộ dự án không có URL công khai thì ghi nhận đường dẫn tệp trong workspace.

## 12. Ví dụ hợp lệ và không hợp lệ
- **Hợp lệ**: `STD-SCRUM-2020` trỏ tới `https://scrumguides.org/scrum-guide.html` (VERIFIED_OFFICIAL).
- **Không hợp lệ**: Trỏ tới blog cá nhân nhưng gán nhãn `VERIFIED_OFFICIAL` cho Scrum Guide.

## 13. Tài liệu liên quan
Tất cả các tài liệu thuộc Nhóm A, B, C, D, E.

## 14. Bằng chứng cần thiết
URL hợp lệ hoặc tệp nội bộ đã xác minh.

## 15. Giới hạn đã biết
Một số tiêu chuẩn ISO cần tài khoản trả phí để tải toàn văn; hệ thống chỉ thẩm định qua danh mục chính thức của ISO.org.
