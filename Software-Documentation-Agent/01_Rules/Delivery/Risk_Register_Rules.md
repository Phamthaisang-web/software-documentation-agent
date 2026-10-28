# RULE-DEL-003: Risk Register Rules

- **Mã quy tắc**: `RULE-DEL-003`
- **Tên quy tắc**: Risk Identification and Mitigation Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc nhận diện, đánh giá xác suất, tác động và kế hoạch giảm thiểu rủi ro dự án theo ISO 21500 và ISO 31000.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-003`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6.7 (Risk management) & ISO 31000:2018

## 4. Đầu vào bắt buộc
Mô tả rủi ro, xác suất xảy ra (Probability), mức độ tác động (Impact), chiến lược ứng phó.

## 5. Cấu trúc trường bắt buộc
Risk ID, Mô tả rủi ro, Xác suất (1-5 hoặc Thấp/TB/Cao), Tác động (1-5), Điểm rủi ro (Risk Score), Chiến lược giảm thiểu (Mitigation), Kế hoạch dự phòng (Contingency), Người chịu trách nhiệm (Owner), Trạng thái.

## 6. Quy tắc nội dung
1. Mỗi rủi ro phải phân tích rõ nguyên nhân gốc rễ và hệ quả nếu xảy ra.
2. Bắt buộc phải có hành động giảm thiểu cụ thể và người theo dõi.
3. Nếu rủi ro trở thành hiện thực, nó phải được chuyển sang theo dõi tại `DOC-DEL-004` (Issue Log).

## 7. Tiêu chí chất lượng
Tính điểm rủi ro nhất quán: `Risk Score = Probability * Impact`.

## 8. Quy tắc đặt tên
`DOC-DEL-003_Risk_Register.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-DEL-004` (Issue Log) và `DOC-DEL-005` (Decision Log).

## 10. Cách kiểm tra
Kiểm tra công thức tính điểm và trường hành động giảm thiểu.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `RISK-001`: Nghẽn cổng thanh toán bên thứ ba vào giờ cao điểm. Giảm thiểu: Tích hợp thêm cổng thanh toán dự phòng B.
- Không hợp lệ: Ghi rủi ro chung chung "Dự án có thể gặp rủi ro."

## 13. Tài liệu liên quan
`DOC-PM-001`, `DOC-DEL-004`.

## 14. Bằng chứng cần thiết
Đánh giá rủi ro kỹ thuật và vận hành.

## 15. Giới hạn đã biết
Không có.
