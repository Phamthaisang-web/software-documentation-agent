# RULE-TEST-001: Software Test Plan Rules

- **Mã quy tắc**: `RULE-TEST-001`
- **Tên quy tắc**: Test Strategy and ISO 29119-3 Test Plan Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định phương pháp lập Kế hoạch Kiểm thử Phần mềm (Test Plan) theo tiêu chuẩn quốc tế ISO/IEC/IEEE 29119-3:2021.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-001`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-1:2022 (Concepts)
- ISO/IEC/IEEE 29119-2:2021 (Processes)
- ISO/IEC/IEEE 29119-3:2021 (Test Documentation)

## 4. Đầu vào bắt buộc
Phạm vi kiểm thử, các cấp độ kiểm thử (Unit, Integration, System, Acceptance), tiêu chí dừng/tiếp tục kiểm thử (Suspension & Resumption criteria).

## 5. Cấu trúc trường bắt buộc
Chiến lược & Phương pháp tiếp cận, Phạm vi kiểm thử (In-scope & Out-of-scope), Cấp độ kiểm thử, Tiêu chí bắt đầu & Kết thúc (Entry/Exit criteria), Yêu cầu môi trường, Lịch trình & Nhân sự.

## 6. Quy tắc nội dung
1. Phân biệt rõ thiết kế kiểm thử (Test Design) với thực thi kiểm thử (Test Execution).
2. Tiêu chí kết thúc kiểm thử (Exit criteria) phải rõ ràng (ví dụ: 100% Blocker/Critical bugs được đóng, Pass rate >= 95%).
3. Xác định rõ các loại kiểm thử: Kiểm thử chức năng, hiệu năng, bảo mật, tương thích.

## 7. Tiêu chí chất lượng
Kế hoạch kiểm thử bao phủ toàn bộ các yêu cầu trong phạm vi dự án.

## 8. Quy tắc đặt tên
`DOC-TEST-001_Test_Plan.docx`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-REQ-001` (SRS) và định hướng cho `DOC-TEST-003` (Test Cases).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của Entry và Exit criteria.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Exit criteria: Unit test pass rate = 100%, Integration test pass rate >= 98%, không còn lỗi mức Critical.
- Không hợp lệ: "Kiểm thử cho đến khi thấy phần mềm ổn."

## 13. Tài liệu liên quan
`DOC-REQ-001`, `DOC-TEST-003`, `DOC-TEST-004`.

## 14. Bằng chứng cần thiết
Yêu cầu kiểm thử và hạ tầng test.

## 15. Giới hạn đã biết
Không có.
