# Cross-Document Validation Rules — Quy Tắc Thẩm Định Nhất Quán Chéo

Tài liệu này quy định việc kiểm tra tính logic và truy xuất chéo giữa tất cả các tài liệu trong bộ tài liệu dự án.

---

## 1. Các Kiểm Tra Liên Kết Chéo
1. **Kiểm tra Ma trận Truy xuất (Traceability Matrix Check)**:
   - Tất cả các Functional Requirements (`REQ-FUNC-xxx`) trong `DOC-REQ-003` phải xuất hiện trong bảng RTM (`DOC-REQ-007`).
   - Mọi Test Case (`TC-xxx`) trong `DOC-TEST-003` phải liên kết tới một Requirement ID tồn tại.
   - Bất kỳ liên kết nào trỏ vào ID không tồn tại sẽ bị đánh dấu `FAILED (CRITICAL)`.
2. **Kiểm tra Nhất quán Trạng thái**:
   - Nếu một chức năng được đánh dấu là `DONE` trong `DOC-SCRUM-012` (Sprint Review) hoặc `DOC-DEL-009` (Release Notes), nó bắt buộc phải thỏa mãn Definition of Done trong `DOC-SCRUM-014` và có test case kết quả `PASS` trong `DOC-TEST-004`.
3. **Kiểm tra Đồng bộ Schema CSDL & API**:
   - Tên bảng và tên trường trong `DOC-ARCH-003` (DB Spec) phải khớp với các entity trong `DOC-ARCH-004` (ERD).
