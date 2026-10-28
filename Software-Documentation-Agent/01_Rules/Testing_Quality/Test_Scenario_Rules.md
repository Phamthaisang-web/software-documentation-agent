# RULE-TEST-002: Test Scenario Rules

- **Mã quy tắc**: `RULE-TEST-002`
- **Tên quy tắc**: Test Scenario Design and Technique Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định việc thiết kế các kịch bản kiểm thử (Test Scenarios) theo ISO/IEC/IEEE 29119-4.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-002`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-3:2021 & ISO/IEC/IEEE 29119-4:2021 (Test Techniques)

## 4. Đầu vào bắt buộc
Mã tính năng, mô tả kịch bản, kỹ thuật kiểm thử áp dụng.

## 5. Cấu trúc trường bắt buộc
Scenario ID, Feature Ref, Tiêu đề kịch bản, Mô tả, Kỹ thuật áp dụng (Phân vùng tương đương, Giá trị biên, Bảng quyết định), Mức độ ưu tiên.

## 6. Quy tắc nội dung
1. Mỗi kịch bản đại diện cho một luồng nghiệp vụ hoàn chỉnh từ đầu đến cuối.
2. Bao quát cả kịch bản tích cực (Positive scenarios) và tiêu cực (Negative scenarios).

## 7. Tiêu chí chất lượng
Kịch bản mô tả rõ ràng mục tiêu kiểm chứng.

## 8. Quy tắc đặt tên
`DOC-TEST-002_Test_Scenario.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết `DOC-REQ-005` (Use Case) tới `DOC-TEST-003` (Test Case).

## 10. Cách kiểm tra
Kiểm tra ID dạng `TS-{MODULE}-{NUMBER}`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `TS-AUTH-001`: Đăng nhập thành công với tài khoản hợp lệ. `TS-AUTH-002`: Khóa tài khoản sau 5 lần nhập sai mật khẩu liên tiếp.
- Không hợp lệ: Kịch bản mơ hồ không rõ điều kiện.

## 13. Tài liệu liên quan
`DOC-REQ-005`, `DOC-TEST-003`.

## 14. Bằng chứng cần thiết
Ca sử dụng và luồng nghiệp vụ.

## 15. Giới hạn đã biết
Không có.
