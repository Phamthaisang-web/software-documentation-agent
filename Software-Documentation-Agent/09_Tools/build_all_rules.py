import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_DIR = os.path.join(BASE_DIR, "01_Rules")

def write_rule(category, filename, content):
    target_dir = os.path.join(RULES_DIR, category)
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, filename)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated: {category}/{filename}")

# ==============================================================================
# PROJECT MANAGEMENT RULES (3 files)
# ==============================================================================
write_rule("Project_Management", "Project_Charter_Rules.md", """# RULE-PM-001: Project Charter Rules

- **Mã quy tắc**: `RULE-PM-001`
- **Tên quy tắc**: Project Charter Definition and Authority Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định tiêu chuẩn lập tài liệu Khởi tạo Dự án (Project Charter) theo ISO 21500, xác lập sự tồn tại chính thức của dự án và quyền hạn của Giám đốc dự án.

## 2. Phạm vi áp dụng
Tài liệu `DOC-PM-001` (Project Charter).

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6 (Project Governance & Initiation)

## 4. Đầu vào bắt buộc
- Bối cảnh kinh doanh (`business_need`)
- Mục tiêu tổng quát của dự án (`project_objectives`)
- Danh sách các bên liên quan chính (`key_stakeholders`)

## 5. Cấu trúc trường bắt buộc
Bao gồm: Mục tiêu dự án, Trường hợp kinh doanh, Tóm tắt phạm vi, Các mốc ban đầu, Bên liên quan chính, Thẩm quyền và phê duyệt.

## 6. Quy tắc nội dung
1. Phải nêu rõ lý do tại sao dự án cần được thực hiện và bài toán nghiệp vụ giải quyết.
2. Không tự bịa đặt ngân sách, nguồn vốn hoặc tên người tài trợ (Sponsor) nếu chưa có thông tin xác thực; đánh dấu `TBD`.
3. Mục tiêu phải tuân thủ nguyên tắc SMART (Specific, Measurable, Achievable, Relevant, Time-bound).
4. Phân định rõ quyền hạn của Project Manager và ban chỉ đạo.

## 7. Tiêu chí chất lượng
Mục tiêu dự án có chỉ số đo lường thành công định lượng hoặc định tính rõ ràng.

## 8. Quy tắc đặt tên
Tệp xuất bản: `DOC-PM-001_Project_Charter.docx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-PM-002` (Scope Statement) và `DOC-PM-003` (Stakeholder Register).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của các phần bắt buộc qua `validator.py`.

## 11. Ngoại lệ
Dự án nội bộ nhỏ (Pet project/PoC) có thể rút gọn phần phân bổ ngân sách.

## 12. Ví dụ
- Hợp lệ: "Mục tiêu: Xây dựng cổng thanh toán trực tuyến xử lý 10,000 giao dịch/ngày hoàn thành vào Q4/2026."
- Không hợp lệ: "Xây dựng hệ thống tốt nhất thế giới."

## 13. Tài liệu liên quan
`DOC-PM-002`, `DOC-PM-003`.

## 14. Bằng chứng cần thiết
Văn bản yêu cầu dự án hoặc tài liệu đề xuất giải pháp.

## 15. Giới hạn đã biết
Không thể xác minh thông tin tài chính nếu doanh nghiệp bảo mật.
""")

write_rule("Project_Management", "Project_Scope_Rules.md", """# RULE-PM-002: Project Scope Statement Rules

- **Mã quy tắc**: `RULE-PM-002`
- **Tên quy tắc**: Scope Definition and Boundary Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định phương pháp xác định ranh giới phạm vi dự án, phân định rõ những gì thuộc phạm vi và ngoài phạm vi.

## 2. Phạm vi áp dụng
Tài liệu `DOC-PM-002`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6.3 (Scope management)
- ISO/IEC/IEEE 29148:2018

## 4. Đầu vào bắt buộc
- Danh mục công việc trong phạm vi (`in_scope`)
- Danh mục loại trừ ngoài phạm vi (`out_of_scope`)
- Kết quả bàn giao chính (`deliverables`)

## 5. Cấu trúc trường bắt buộc
Mô tả phạm vi, Kết quả bàn giao chính, Tiêu chí chấp nhận, Loại trừ (Out of Scope), Ràng buộc và Giả định.

## 6. Quy tắc nội dung
1. Bắt buộc phải có mục "Ngoài phạm vi" (Out of Scope) để chống phình phạm vi (Scope Creep).
2. Các kết quả bàn giao phải cụ thể, có thể nghiệm thu được.
3. Không ngầm định các tính năng không được liệt kê là nằm trong phạm vi.

## 7. Tiêu chí chất lượng
Ranh giới rõ ràng, không có sự nhập nhằng giữa in-scope và out-of-scope.

## 8. Quy tắc đặt tên
`DOC-PM-002_Project_Scope_Statement.docx`.

## 9. Truy xuất nguồn gốc
Phải trỏ tới `DOC-REQ-001` (SRS) và `DOC-DEL-002` (WBS).

## 10. Cách kiểm tra
Kiểm tra trường `out_of_scope` không được rỗng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Trong phạm vi: Đăng nhập bằng Email/Password. Ngoài phạm vi: Đăng nhập sinh trắc học và SSO Google trong Phase 1."
- Không hợp lệ: "Hệ thống bao gồm mọi chức năng người dùng mong muốn."

## 13. Tài liệu liên quan
`DOC-PM-001`, `DOC-REQ-001`, `DOC-DEL-002`.

## 14. Bằng chứng cần thiết
Biên bản thỏa thuận phạm vi.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Project_Management", "Stakeholder_Register_Rules.md", """# RULE-PM-003: Stakeholder Register Rules

- **Mã quy tắc**: `RULE-PM-003`
- **Tên quy tắc**: Stakeholder Identification and Management Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định việc nhận diện, phân loại và quản lý các bên liên quan của dự án theo ISO 21500.

## 2. Phạm vi áp dụng
Tài liệu `DOC-PM-003`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Stakeholder engagement)

## 4. Đầu vào bắt buộc
Danh sách bên liên quan, vai trò, mức độ ảnh hưởng, kỳ vọng.

## 5. Cấu trúc trường bắt buộc
Bảng: Stakeholder ID, Tên/Tổ chức, Vai trò, Mức độ quan tâm, Mức độ ảnh hưởng, Chiến lược tương tác.

## 6. Quy tắc nội dung
1. Nhận diện đầy đủ cả bên liên quan nội bộ (Dev, QA, PM, PO) và bên ngoài (Khách hàng, Người dùng cuối, Ban pháp chế).
2. Không công khai thông tin liên lạc nhạy cảm của cá nhân nếu không có sự đồng ý.
3. Đánh giá mức độ ảnh hưởng (Cao/Trung bình/Thấp) phải có căn cứ.

## 7. Tiêu chí chất lượng
Đầy đủ các vai trò chủ chốt của dự án.

## 8. Quy tắc đặt tên
`DOC-PM-003_Stakeholder_Register.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết với các yêu cầu do từng bên liên quan đưa ra trong `DOC-REQ-001`.

## 10. Cách kiểm tra
Kiểm tra số lượng vai trò tối thiểu (PO, Dev, Stakeholder).

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Phân loại Product Owner: Mức ảnh hưởng Cao, Mức quan tâm Cao.
- Không hợp lệ: Để trống vai trò người dùng cuối.

## 13. Tài liệu liên quan
`DOC-PM-001`, `DOC-REQ-001`.

## 14. Bằng chứng cần thiết
Sơ đồ tổ chức dự án hoặc danh sách phân công nhiệm vụ.

## 15. Giới hạn đã biết
Không có.
""")

print("Project Management rules created.")
