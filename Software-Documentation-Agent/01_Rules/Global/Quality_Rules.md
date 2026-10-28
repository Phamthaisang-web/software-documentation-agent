# RULE-GLOB-005: Quality Rules (Quy Tắc Chất Lượng Nội Dung)

- **Mã quy tắc**: `RULE-GLOB-005`
- **Tên quy tắc**: Documentation Quality & Precision Criteria
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Xác lập các tiêu chí chất lượng kỹ thuật bắt buộc cho toàn bộ nội dung tài liệu phần mềm.

## 2. Phạm vi áp dụng
Toàn bộ văn bản và dữ liệu được tạo ra trong tài liệu.

## 3. Nguồn tiêu chuẩn
- ISO/IEC 25010:2023 (Systems and software quality models)
- ISO/IEC/IEEE 29148:2018 (Requirements quality criteria)

## 4. Đầu vào bắt buộc
Nội dung tài liệu được sinh ra.

## 5. Cấu trúc bắt buộc
Mỗi mệnh đề yêu cầu kỹ thuật phải rõ ràng, đo lường được, có thể kiểm chứng được.

## 6. Quy tắc nội dung
1. Tính rõ ràng (Unambiguous): Không dùng các từ mơ hồ như "nhanh chóng", "thân thiện", "tối ưu" mà không có chỉ số cụ thể.
2. Tính kiểm chứng được (Verifiable): Mỗi yêu cầu phải có phương pháp kiểm thử hoặc tiêu chí nghiệm thu rõ ràng.
3. Tính nhất quán (Consistent): Không có hai điều khoản mâu thuẫn nhau trong tài liệu.
4. Tính khả thi (Feasible): Phù hợp với năng lực công nghệ và phạm vi dự án.
5. Không gán nhãn PASS cho các mục chưa được kiểm thử thực tế.

## 7. Tiêu chí chất lượng
100% các tiêu chí chất lượng được đánh giá trước khi phát hành.

## 8. Mã định danh
Quy định chất lượng: `RULE-GLOB-005`.

## 9. Truy xuất nguồn gốc
Liên kết với `06_Validation/content_validation_rules.md`.

## 10. Cách kiểm tra
Sử dụng công cụ `validator.py`.

## 11. Ngoại lệ
Tài liệu phác thảo giai đoạn đầu (DRAFT) có thể có một số mục TBD.

## 12. Ví dụ
- Hợp lệ: "Thời gian phản hồi của API `/login` phải <= 200ms với 100 concurrent requests."
- Không hợp lệ: "API đăng nhập phải chạy cực kỳ nhanh."

## 13. Tài liệu liên quan
Tất cả các tài liệu yêu cầu và kiến trúc.

## 14. Bằng chứng cần thiết
Báo cáo kiểm thử hoặc benchmark đo đạc cụ thể.

## 15. Giới hạn đã biết
Không có.
