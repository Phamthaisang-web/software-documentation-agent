# Traceability Rules — Quy Tắc Xây Dựng Mạng Lưới Truy Xuất

Tài liệu này quy định cách thức thiết lập và duy trì liên kết truy xuất nguồn gốc hai chiều (Forward & Backward Traceability) trong quá trình sinh tài liệu.

---

## 1. Mạng Lưới Truy Xuất Cốt Lõi
Hệ thống duy trì các chuỗi truy xuất bắt buộc:
1. **Chuỗi Giá Trị Sản Phẩm**:
   `Product Vision (DOC-REQ-002)`
   ↳ `Product Goal (DOC-SCRUM-002)`
   ↳ `Product Backlog (DOC-SCRUM-001)`
   ↳ `PBI / User Story (DOC-SCRUM-003)`
   ↳ `Acceptance Criteria (DOC-REQ-008)`
   ↳ `Test Case Specification (DOC-TEST-003)`
   ↳ `Test Execution Report (DOC-TEST-004)`
   ↳ `Increment Deliverables (DOC-SCRUM-015)`
   ↳ `Release Notes (DOC-DEL-009)`

2. **Chuỗi Kỹ Nghệ Yêu Cầu & Thiết Kế**:
   `Functional Requirements (DOC-REQ-003)`
   ↳ `Use Case Specification (DOC-REQ-005)`
   ↳ `API Specification (DOC-ARCH-005) & Detailed Design (DOC-ARCH-002)`
   ↳ `Test Case Specification (DOC-TEST-003)`

3. **Chuỗi Phi Chức Năng & Quyết Định**:
   `Non-Functional Requirements (DOC-REQ-004)`
   ↳ `Architecture Decision Records (DOC-ARCH-010)`
   ↳ `Performance & Security Test Cases`
   ↳ `Evidence in Quality Metrics (DOC-TEST-008)`

4. **Chuỗi Quản Trị Rủi Ro & Thay Đổi**:
   `Risk Register (DOC-DEL-003)`
   ↳ `Mitigation Actions / Issue Log (DOC-DEL-004)`
   ↳ `Decision Log (DOC-DEL-005)`
   ↳ `Progress Report (DOC-DEL-008)`

## 2. Quy Tắc Ràng Buộc Kỹ Thuật
- Mọi ID trong bảng truy xuất phải tồn tại thật trong bộ tài liệu.
- Bất kỳ mắt xích nào bị đứt (ví dụ: Yêu cầu không có Test Case, hoặc Test Case trỏ vào ID ảo) sẽ bị `traceability_engine.py` gắn cờ lỗi `BROKEN_LINK` hoặc `ORPHAN_ITEM`.
