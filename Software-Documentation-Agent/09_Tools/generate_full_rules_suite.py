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
# REQUIREMENTS RULES (8 files)
# ==============================================================================
write_rule("Requirements", "SRS_Rules.md", """# RULE-REQ-001: Software Requirements Specification Rules

- **Mã quy tắc**: `RULE-REQ-001`
- **Tên quy tắc**: Software Requirements Specification Structure and Quality Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định cấu trúc và tiêu chuẩn chất lượng của tài liệu Đặc tả Yêu cầu Phần mềm (SRS) tuân thủ tiêu chuẩn quốc tế ISO/IEC/IEEE 29148:2018.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-001` (SRS).

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 Clause 9.5 (Software Requirements Specification)

## 4. Đầu vào bắt buộc
- Danh sách yêu cầu chức năng (`functional_requirements`)
- Danh sách yêu cầu phi chức năng (`non_functional_requirements`)
- Giao diện hệ thống bên ngoài (`external_interfaces`)

## 5. Cấu trúc trường bắt buộc
Mục tiêu & Phạm vi, Mô tả tổng quan, Tính năng hệ thống, Yêu cầu phi chức năng, Giao diện ngoài, Tiêu chí kiểm chứng.

## 6. Quy tắc nội dung
1. Mỗi yêu cầu phải có một mã định danh duy nhất không đổi (`REQ-xxx`).
2. Mọi yêu cầu phải đáp ứng 8 tiêu chí ISO 29148: Cần thiết, Rõ ràng, Nhất quán, Hoàn chỉnh, Đơn nhất, Khả thi, Kiểm chứng được, Truy xuất được.
3. Không tự đặt số liệu hiệu năng, SLA mà chưa có cơ sở từ cấu hình hoặc cam kết kỹ thuật; nếu chưa rõ ghi `TBD`.
4. Phân biệt rõ yêu cầu của người dùng (User requirements) và yêu cầu kỹ thuật hệ thống (System requirements).

## 7. Tiêu chí chất lượng
100% yêu cầu có phương pháp kiểm chứng (Test, Inspection, Analysis, Demonstration).

## 8. Quy tắc đặt tên
`DOC-REQ-001_Software_Requirements_Specification.docx`.

## 9. Truy xuất nguồn gốc
Phải trỏ tới `DOC-PM-002` (Scope) và làm cơ sở cho `DOC-ARCH-001` (SAD) và `DOC-TEST-001` (Test Plan).

## 10. Cách kiểm tra
Kiểm tra cấu trúc và tính duy nhất của ID yêu cầu qua `validator.py`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "REQ-FUNC-001: Hệ thống cho phép người dùng đăng nhập bằng email và mật khẩu qua giao thức HTTPS."
- Không hợp lệ: "Hệ thống hỗ trợ đăng nhập tốt và bảo mật."

## 13. Tài liệu liên quan
`DOC-PM-002`, `DOC-REQ-003`, `DOC-REQ-004`, `DOC-REQ-007`.

## 14. Bằng chứng cần thiết
Code router, authentication middleware, controller.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Requirements", "Product_Vision_Rules.md", """# RULE-REQ-002: Product Vision Rules

- **Mã quy tắc**: `RULE-REQ-002`
- **Tên quy tắc**: Product Vision Articulation Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Định hướng tầm nhìn chiến lược dài hạn và định vị giá trị của sản phẩm theo ISO/IEC/IEEE 29148.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-002`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 (Vision Document concepts)

## 4. Đầu vào bắt buộc
- Khách hàng mục tiêu (`target_customer`)
- Vấn đề cần giải quyết (`problem_statement`)
- Đề xuất giá trị cốt lõi (`value_proposition`)

## 5. Cấu trúc trường bắt buộc
Khách hàng mục tiêu, Tuyên bố tầm nhìn, Tính năng cốt lõi, Mục tiêu kinh doanh & Đo lường thành công.

## 6. Quy tắc nội dung
1. Tuyên bố tầm nhìn phải nêu bật sự khác biệt và giá trị độc đáo của sản phẩm.
2. Không viết lan man về giải pháp kỹ thuật chi tiết; tập trung vào bài toán người dùng.

## 7. Tiêu chí chất lượng
Ngắn gọn, truyền cảm hứng và định hướng được mục tiêu sản phẩm.

## 8. Quy tắc đặt tên
`DOC-REQ-002_Product_Vision.docx`.

## 9. Truy xuất nguồn gốc
Làm nguồn gốc cho `DOC-SCRUM-002` (Product Goal) và `DOC-REQ-001` (SRS).

## 10. Cách kiểm tra
Kiểm tra cấu trúc tuyên bố tầm nhìn theo mẫu chuẩn.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Dành cho các lập trình viên cần tạo tài liệu chuẩn, Agent là công cụ tự động phân tích và sinh tài liệu kỹ thuật."
- Không hợp lệ: "Phần mềm để viết tài liệu."

## 13. Tài liệu liên quan
`DOC-SCRUM-002`, `DOC-REQ-001`.

## 14. Bằng chứng cần thiết
Business Case hoặc đề án phát triển sản phẩm.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Requirements", "Functional_Requirements_Rules.md", """# RULE-REQ-003: Functional Requirements Rules

- **Mã quy tắc**: `RULE-REQ-003`
- **Tên quy tắc**: Functional Requirements Specification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Dặc tả chi tiết từng yêu cầu chức năng, logic nghiệp vụ, dữ liệu đầu vào và đầu ra theo ISO 29148.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-003`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018

## 4. Đầu vào bắt buộc
Danh mục chức năng, mô tả chi tiết, quy tắc nghiệp vụ.

## 5. Cấu trúc trường bắt buộc
Bảng: Feature ID, Module, Feature Name, Detailed Description, Business Rules, Verification Method.

## 6. Quy tắc nội dung
1. Mỗi chức năng phải có logic nghiệp vụ rõ ràng, mô tả luồng chính và luồng ngoại lệ.
2. Không gộp nhiều chức năng độc lập vào một ID duy nhất (vi phạm tính đơn nhất).

## 7. Tiêu chí chất lượng
100% chức năng có thể kiểm thử độc lập.

## 8. Quy tắc đặt tên
`DOC-REQ-003_Functional_Requirements.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-REQ-005` (Use Case) và `DOC-TEST-003` (Test Case).

## 10. Cách kiểm tra
Kiểm tra ID dạng `REQ-FUNC-xxx`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `REQ-FUNC-001`: Đăng ký tài khoản với email, xác thực OTP trong vòng 5 phút.
- Không hợp lệ: `REQ-FUNC-001`: Hệ thống quản lý toàn bộ người dùng và thanh toán và báo cáo.

## 13. Tài liệu liên quan
`DOC-REQ-001`, `DOC-REQ-005`, `DOC-TEST-003`.

## 14. Bằng chứng cần thiết
Code controller, service logic trong dự án.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Requirements", "Non_Functional_Requirements_Rules.md", """# RULE-REQ-004: Non-Functional Requirements Rules

- **Mã quy tắc**: `RULE-REQ-004`
- **Tên quy tắc**: Non-Functional Requirements Quantification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Xác định và định lượng các yêu cầu phi chức năng (hiệu năng, bảo mật, độ tin cậy, khả năng bảo trì) theo ISO 29148 và ISO 25010.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-004`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018
- OWASP Top 10:2021

## 4. Đầu vào bắt buộc
Chỉ tiêu đo lường, ngưỡng chấp nhận, phương pháp đo.

## 5. Cấu trúc trường bắt buộc
NFR ID, Category (Performance/Security/Reliability/Usability), Target Metric, Measurement Method, Architecture Impact.

## 6. Quy tắc nội dung
1. Mọi chỉ tiêu phải có con số cụ thể hoặc ngưỡng đo lường được (không dùng từ chung chung).
2. Nếu không có căn cứ từ cấu hình hoặc benchmark, bắt buộc phải đánh dấu `TBD`.
3. Yêu cầu bảo mật phải tham chiếu tới các kiểm soát của OWASP Top 10.

## 7. Tiêu chí chất lượng
100% NFR có đơn vị đo rõ ràng (ms, %, req/s, bits).

## 8. Quy tắc đặt tên
`DOC-REQ-004_Non_Functional_Requirements.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-ARCH-001` (SAD) và `DOC-ARCH-010` (ADR).

## 10. Cách kiểm tra
Kiểm tra sự tồn tại của trường `target_metric`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `REQ-NF-PERF-001`: Thời gian phản hồi trang dashboard <= 1.5s ở tải 500 CCU.
- Không hợp lệ: `REQ-NF-PERF-001`: Trang dashboard phải load nhanh.

## 13. Tài liệu liên quan
`DOC-ARCH-001`, `DOC-TEST-001`.

## 14. Bằng chứng cần thiết
Cấu hình cache, pool kết nối, kết quả load test.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Requirements", "Use_Case_Rules.md", """# RULE-REQ-005: Use Case Specification Rules

- **Mã quy tắc**: `RULE-REQ-005`
- **Tên quy tắc**: Use Case Flow Specification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Đặc tả luồng tương tác giữa tác nhân (Actor) và hệ thống để hoàn thành mục tiêu nghiệp vụ.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-005`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 (Use Case model)

## 4. Đầu vào bắt buộc
Tác nhân, Tiền điều kiện, Luồng cơ bản, Luồng ngoại lệ, Hậu điều kiện.

## 5. Cấu trúc trường bắt buộc
Use Case ID, Use Case Name, Primary Actor, Preconditions, Basic Flow (Step-by-step), Alternative/Exception Flows, Postconditions.

## 6. Quy tắc nội dung
1. Luồng cơ bản (Basic flow) phải thể hiện chuỗi bước thành công lý tưởng.
2. Luồng ngoại lệ phải mô tả cách hệ thống xử lý khi có lỗi hoặc dữ liệu không hợp lệ.
3. Tiền điều kiện và hậu điều kiện phải phản ánh trạng thái dữ liệu chính xác.

## 7. Tiêu chí chất lượng
Các bước tương tác giữa User và System được phân định rõ ràng.

## 8. Quy tắc đặt tên
`DOC-REQ-005_Use_Case_Specification.docx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-REQ-003` và `DOC-TEST-002` (Test Scenario).

## 10. Cách kiểm tra
Kiểm tra cấu trúc step-by-step của Basic flow.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Bước 1: Người dùng nhấn nút Thanh toán. Bước 2: Hệ thống kiểm tra số dư ví..."
- Không hợp lệ: "Người dùng thực hiện thanh toán xong xuôi."

## 13. Tài liệu liên quan
`DOC-REQ-003`, `DOC-TEST-002`.

## 14. Bằng chứng cần thiết
Code luồng xử lý hoặc controller.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Requirements", "User_Story_Rules.md", """# RULE-REQ-006: User Story Rules

- **Mã quy tắc**: `RULE-REQ-006`
- **Tên quy tắc**: Agile User Story Construction Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Đặc tả yêu cầu phần mềm dưới dạng User Story chuẩn Agile theo cấu trúc As a / I want / So that.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-006`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 & Agile Practice Guide

## 4. Đầu vào bắt buộc
Vai trò người dùng, Mong muốn hành động, Giá trị nhận được.

## 5. Cấu trúc trường bắt buộc
Story ID, Title, Persona (As a), Action (I want), Benefit (So that), Priority, Acceptance Criteria Ref.

## 6. Quy tắc nội dung
1. Bắt buộc tuân thủ mẫu 3 thành phần: "Là [vai trò], tôi muốn [hành động], để [giá trị mang lại]".
2. Phải nêu bật được giá trị kinh doanh trong mệnh đề "So that" (không được viết sáo rỗng).
3. Tuân thủ nguyên tắc INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).

## 7. Tiêu chí chất lượng
100% User Stories có tiêu chí chấp nhận đi kèm.

## 8. Quy tắc đặt tên
`DOC-REQ-006_User_Story_Specification.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-REQ-008` (Acceptance Criteria) và `DOC-SCRUM-003` (PBI).

## 10. Cách kiểm tra
Kiểm tra định dạng As a / I want / So that bằng regex.

## 11. Ngoại lệ
Các PBI kỹ thuật nội bộ (Spike, Refactoring) có thể viết dạng Technical Task.

## 12. Ví dụ
- Hợp lệ: "Là Người mua hàng, tôi muốn lọc sản phẩm theo mức giá, để nhanh chóng tìm thấy món đồ phù hợp túi tiền."
- Không hợp lệ: "Tôi muốn làm bộ lọc."

## 13. Tài liệu liên quan
`DOC-REQ-008`, `DOC-SCRUM-003`.

## 14. Bằng chứng cần thiết
Tính năng frontend/backend tương ứng.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Requirements", "Acceptance_Criteria_Rules.md", """# RULE-REQ-007: Acceptance Criteria Rules

- **Mã quy tắc**: `RULE-REQ-007`
- **Tên quy tắc**: Acceptance Criteria Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định tiêu chuẩn viết tiêu chí chấp nhận (Acceptance Criteria) theo định dạng Given-When-Then hoặc Checklist kiểm chứng được.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-008`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 & Agile Standards

## 4. Đầu vào bắt buộc
Story ID, Điều kiện đầu vào, Hành động thực hiện, Kết quả mong đợi.

## 5. Cấu trúc trường bắt buộc
Story ID, Criterion ID, Scenario Title, Given, When, Then, Verification Status.

## 6. Quy tắc nội dung
1. Mỗi tiêu chí phải có thể kiểm chứng được một cách khách quan không thể chối cãi.
2. Bao quát cả trường hợp biên (boundary cases) và trường hợp dữ liệu sai.
3. Không viết tiêu chí chấp nhận một cách chung chung như "hệ thống không bị lỗi".

## 7. Tiêu chí chất lượng
100% tiêu chí có thể chuyển đổi trực tiếp thành Automated Test Case.

## 8. Quy tắc đặt tên
`DOC-REQ-008_Acceptance_Criteria.xlsx`.

## 9. Truy xuất nguồn gốc
Trỏ từ `DOC-REQ-006` tới `DOC-TEST-003` (Test Case).

## 10. Cách kiểm tra
Kiểm tra cấu trúc Given-When-Then.

## 11. Ngoại lệ
Checklist ngắn đối với các thay đổi giao diện đơn giản.

## 12. Ví dụ
- Hợp lệ: "Given người dùng nhập mật khẩu dưới 8 ký tự, When nhấn Đăng ký, Then thông báo lỗi màu đỏ 'Mật khẩu phải từ 8 ký tự trở lên' xuất hiện."
- Không hợp lệ: "Đăng ký phải chạy ngon lành."

## 13. Tài liệu liên quan
`DOC-REQ-006`, `DOC-TEST-003`.

## 14. Bằng chứng cần thiết
Logic validation trên frontend/backend.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Requirements", "RTM_Rules.md", """# RULE-REQ-008: Requirements Traceability Matrix Rules

- **Mã quy tắc**: `RULE-REQ-008`
- **Tên quy tắc**: Traceability Matrix Generation and Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Đảm bảo ma trận truy xuất nguồn gốc (RTM) liên kết toàn diện mọi yêu cầu với thiết kế, ca kiểm thử và lần phát hành.

## 2. Phạm vi áp dụng
Tài liệu `DOC-REQ-007`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 Clause 9.6

## 4. Đầu vào bắt buộc
Danh sách `REQ-*`, `ARCH-*`, `TC-*`, `REL-*`.

## 5. Cấu trúc trường bắt buộc
Bảng RTM: Requirement ID, Description, Architecture ID, Test Case ID, Test Execution Status, Release Tag.

## 6. Quy tắc nội dung
1. Phát hiện ngay các yêu cầu không có ca kiểm thử (Uncovered Requirements).
2. Phát hiện các ca kiểm thử không có yêu cầu liên kết (Orphan Test Cases).
3. Không tự tạo liên kết giả giữa các thành phần không liên quan.

## 7. Tiêu chí chất lượng
Zero broken references: 100% ID được tham chiếu phải tồn tại trong hệ thống.

## 8. Quy tắc đặt tên
`DOC-REQ-007_Requirements_Traceability_Matrix.xlsx`.

## 9. Truy xuất nguồn gốc
Tài liệu trung tâm của toàn bộ mạng lưới liên kết.

## 10. Cách kiểm tra
Chạy `test_traceability.py`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `REQ-FUNC-001` -> `ARCH-API-001` -> `TC-AUTH-001` -> `v1.0.0`.
- Không hợp lệ: `REQ-FUNC-001` -> trỏ tới `TC-999` (không tồn tại).

## 13. Tài liệu liên quan
`DOC-REQ-001`, `DOC-TEST-003`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Tệp RTM hoàn chỉnh.

## 15. Giới hạn đã biết
Không có.
""")

print("Requirements rules created successfully.")
