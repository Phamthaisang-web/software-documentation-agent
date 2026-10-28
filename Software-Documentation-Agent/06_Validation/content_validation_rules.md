# Content Validation Rules — Quy Tắc Thẩm Định Nội Dung

Tài liệu này quy định các tiêu chí kiểm tra tính đúng đắn, chính xác và không bịa đặt của nội dung tài liệu.

---

## 1. Các Kiểm Tra Bắt Buộc
1. **Kiểm tra Zero-Hallucination**:
   - Xác minh mọi thông tin kỹ thuật (endpoints, database schema, frameworks) đều có tham chiếu bằng chứng (`evidence_refs`).
   - Cấm kết quả kiểm thử PASS giả: Báo cáo thực thi test (`DOC-TEST-004`) chỉ được có PASS khi có tệp log chạy test thực tế chứng minh. Nếu chưa chạy, bắt buộc phải là `NOT_EXECUTED`.
2. **Kiểm tra TBD / UNKNOWN**:
   - Các thông tin chưa xác định phải được đánh dấu rõ ràng là `UNKNOWN` hoặc `TBD`.
3. **Kiểm tra Tính Đo Lường Được của NFR**:
   - Yêu cầu phi chức năng phải có ngưỡng đo lường định lượng hoặc tiêu chí cụ thể.
4. **Kiểm tra Tiêu chuẩn Scrum**:
   - Kiểm tra tuân thủ đúng định nghĩa của Scrum Guide 2020:
     - Sprint timebox <= 31 ngày.
     - Sprint Planning <= 8h (Sprint 1 tháng).
     - Daily Scrum = 15 phút.
     - Sprint Review <= 4h (Sprint 1 tháng).
     - Sprint Retrospective <= 3h (Sprint 1 tháng).
     - Story Points, Velocity, Burndown, DoR được đánh dấu là bổ trợ (`RECOMMENDATION`), không phải luật Scrum bắt buộc.
