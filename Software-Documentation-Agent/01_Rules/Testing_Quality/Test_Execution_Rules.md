# RULE-TEST-004: Test Execution Report Rules

- **Mã quy tắc**: `RULE-TEST-004`
- **Tên quy tắc**: Test Execution Authenticity and Zero-Fake-Pass Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định nguyên tắc ghi nhận kết quả thực thi kiểm thử thực tế và nghiêm cấm tuyệt đối việc tạo kết quả kiểm thử giả.

## 2. Phạm vi áp dụng
Tài liệu `DOC-TEST-004`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29119-2:2021 & ISO/IEC/IEEE 29119-3:2021 (Test Execution Log & Report)

## 4. Đầu vào bắt buộc
Ngày thực thi thực tế, kết quả thực tế quan sát được, trạng thái thực thi (`PASS`, `FAIL`, `BLOCKED`, `NOT_EXECUTED`), tệp log/bằng chứng.

## 5. Cấu trúc trường bắt buộc
Run ID, Ngày thực thi, Cấu hình môi trường, Test Case ID, Kết quả thực tế quan sát được (Actual Result Observed), Trạng thái thực thi, Bằng chứng thực thi (Log/Screenshot), Tham chiếu Bug ID (nếu Fail).

## 6. Quy tắc nội dung BẮT BUỘC
1. **NGUYÊN TẮC ZERO-FAKE-PASS**:
   - Tuyệt đối KHÔNG tự sao chép "Kết quả mong đợi" thành "Kết quả thực tế".
   - Chỉ được ghi trạng thái `PASS` khi có tệp log thực thi thật (JUnit XML, Playwright trace, Jest report, console output thực) chứng minh test case đã chạy và thành công.
   - Nếu test case chưa được chạy trong phiên làm việc, BẮT BUỘC ghi trạng thái là `NOT_EXECUTED`.
2. Mọi ca kiểm thử bị `FAIL` phải liên kết trực tiếp tới một mã lỗi trong `DOC-TEST-005` (Bug Report).
3. Không tự tạo ngày chạy kiểm thử, tên người chạy test hoặc số liệu pass rate ảo.

## 7. Tiêu chí chất lượng
100% kết quả PASS có bằng chứng log đi kèm.

## 8. Quy tắc đặt tên
`DOC-TEST-004_Test_Execution_Report.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết giữa `DOC-TEST-003` (Test Case) và `DOC-TEST-005` (Bug Report).

## 10. Cách kiểm tra
Bài kiểm thử `test_validation.py` quét kiểm tra cấm kết quả giả mạo.

## 11. Ngoại lệ
Không có ngoại lệ đối với việc cấm tạo test pass giả.

## 12. Ví dụ
- Hợp lệ: "Test Case `TC-AUTH-001`: Trạng thái `NOT_EXECUTED` (Chưa chạy kiểm thử tự động trong môi trường này)."
- Không hợp lệ: Tự ý ghi "Trạng thái PASS 100/100 ca" trong khi chưa chạy bất kỳ lệnh test nào.

## 13. Tài liệu liên quan
`DOC-TEST-003`, `DOC-TEST-005`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Tệp test results XML/JSON hoặc console log từ runner.

## 15. Giới hạn đã biết
Nếu workspace không có công cụ chạy test (ví dụ thiếu browser cho e2e), phải ghi nhận `NOT_EXECUTED`.
