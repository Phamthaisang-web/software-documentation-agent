import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_DIR = os.path.join(BASE_DIR, "01_Rules", "Scrum")
os.makedirs(RULES_DIR, exist_ok=True)

def write_rule(filename, content):
    target_path = os.path.join(RULES_DIR, filename)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated Scrum rule: {filename}")

write_rule("Scrum_Rules.md", """# RULE-SCRUM-001: Foundational Scrum Framework Rules

- **Mã quy tắc**: `RULE-SCRUM-001`
- **Tên quy tắc**: Official Scrum Guide 2020 Core Governance Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định việc áp dụng khuôn khổ Scrum đúng định nghĩa chính thức của The Scrum Guide (Nov 2020), loại bỏ các hiểu lầm và ngăn chặn việc gán nhãn sai các thông lệ tùy chọn thành luật Scrum bắt buộc.

## 2. Phạm vi áp dụng
Toàn bộ quy trình và tài liệu Scrum (`DOC-SCRUM-001` đến `DOC-SCRUM-017`).

## 3. Nguồn tiêu chuẩn
- The Scrum Guide (November 2020), Ken Schwaber & Jeff Sutherland (`STD-SCRUM-2020`).

## 4. Đầu vào bắt buộc
Khai báo cấu hình Scrum Team, độ dài Sprint, các sự kiện và hiện vật Scrum.

## 5. Cấu trúc trường bắt buộc
Các vai trò (Accountabilities: Product Owner, Scrum Master, Developers), Các sự kiện (Events: Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective), Các hiện vật (Artifacts: Product Backlog, Sprint Backlog, Increment) kèm 3 Cam kết (Commitments: Product Goal, Sprint Goal, Definition of Done).

## 6. Quy tắc nội dung
1. Sprint có độ dài cố định từ một tháng trở xuống. Không bắt buộc mọi Sprint phải dài 2 tuần.
2. 3 Hiện vật và 3 Cam kết chính thức:
   - Product Backlog gắn với Cam kết: **Product Goal**.
   - Sprint Backlog gắn với Cam kết: **Sprint Goal**.
   - Increment gắn với Cam kết: **Definition of Done**.
3. Product Owner chịu trách nhiệm tối đa hóa giá trị sản phẩm và quản lý Product Backlog.
4. Developers chịu trách nhiệm tạo ra Increment có thể sử dụng được mỗi Sprint đáp ứng DoD.
5. Không được diễn giải "8 giờ làm việc mỗi ngày" là quy định của Scrum Guide (Scrum Guide chỉ quy định thời lượng timebox cho các sự kiện, không quy định giờ làm việc hành chính).
6. Phân biệt rõ: Story Points, Velocity, Burndown Charts, Definition of Ready (DoR), Daily Scrum Log là các kỹ thuật/thông lệ bổ trợ (Complementary Practices), KHÔNG phải là quy tắc bắt buộc của Scrum Guide.
7. Không tự bịa đặt nhiệm vụ hoàn thành, kết quả họp, người tham dự hoặc dữ liệu Velocity giả.

## 7. Tiêu chí chất lượng
100% tài liệu Scrum tuân thủ đúng định nghĩa thuật ngữ của Scrum Guide 2020.

## 8. Quy tắc đặt tên
`DOC-SCRUM-{NUMBER}_{Name}`.

## 9. Truy xuất nguồn gốc
Liên kết với `02_Standards/official_sources.md`.

## 10. Cách kiểm tra
Chạy bài kiểm thử tự động `test_sprint_constraints.py`.

## 11. Ngoại lệ
Nếu nhóm áp dụng quy định riêng, phải ghi chú rõ là `INTERNAL_POLICY`, không được ghi là Scrum Guide.

## 12. Ví dụ
- Hợp lệ: "Nhóm chọn Sprint 3 tuần; Sprint Planning kéo dài tối đa 6 giờ."
- Không hợp lệ: "Scrum Guide bắt buộc mọi nhóm phải làm việc 8 tiếng/ngày và phải dùng Story Point."

## 13. Tài liệu liên quan
`DOC-SCRUM-001` đến `DOC-SCRUM-017`.

## 14. Bằng chứng cần thiết
Cấu hình dự án và biên bản phiên họp Scrum.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Product_Goal_Rules.md", """# RULE-SCRUM-002: Product Goal Rules

- **Mã quy tắc**: `RULE-SCRUM-002`
- **Tên quy tắc**: Product Goal Commitment Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc thiết lập và quản lý Product Goal — cam kết chính thức cho Product Backlog theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-002`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Artifact Commitment: Product Goal)

## 4. Đầu vào bắt buộc
Tầm nhìn sản phẩm, mục tiêu dài hạn, tiêu chí đánh giá.

## 5. Cấu trúc trường bắt buộc
Tuyên bố Product Goal, Kết quả kỳ vọng, Chỉ số đo lường tiến độ, Cam kết của Scrum Team.

## 6. Quy tắc nội dung
1. Tại một thời điểm, Scrum Team chỉ tập trung vào MỘT Product Goal duy nhất trước khi chuyển sang mục tiêu tiếp theo.
2. Product Goal mô tả trạng thái tương lai của sản phẩm, làm mục tiêu lập kế hoạch cho Product Backlog.
3. Toàn bộ các PBI được đưa vào Backlog phải phục vụ hoặc hướng tới Product Goal hiện tại.

## 7. Tiêu chí chất lượng
Mục tiêu rõ ràng, truyền cảm hứng và có thể xác định được khi nào đã đạt được.

## 8. Quy tắc đặt tên
`DOC-SCRUM-002_Product_Goal.docx`.

## 9. Truy xuất nguồn gốc
Trỏ từ `DOC-REQ-002` (Product Vision) tới `DOC-SCRUM-001` (Product Backlog).

## 10. Cách kiểm tra
Kiểm tra tính đơn nhất của Product Goal đang hoạt động (Active).

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Ra mắt phiên bản MVP thương mại điện tử hỗ trợ thanh toán thẻ và giao hàng trong 24h trước tháng 12/2026."
- Không hợp lệ: Đặt cùng lúc 5 Product Goal độc lập trong một nhóm Scrum.

## 13. Tài liệu liên quan
`DOC-REQ-002`, `DOC-SCRUM-001`.

## 14. Bằng chứng cần thiết
Tuyên bố mục tiêu của Product Owner.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Product_Backlog_Rules.md", """# RULE-SCRUM-003: Product Backlog Rules

- **Mã quy tắc**: `RULE-SCRUM-003`
- **Tên quy tắc**: Product Backlog Management and Ordering Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc xây dựng, sắp xếp và duy trì Product Backlog theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-001`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Product Backlog definition)

## 4. Đầu vào bắt buộc
Danh mục tính năng, sửa lỗi, yêu cầu phi chức năng cần thiết cho sản phẩm.

## 5. Cấu trúc trường bắt buộc
Bảng: Item ID, Title, Description / Acceptance Criteria, Order / Priority, Estimate, Status, Product Goal Alignment.

## 6. Quy tắc nội dung
1. Product Backlog là nguồn duy nhất ghi nhận các công việc cho sản phẩm.
2. Product Owner chịu trách nhiệm sắp xếp thứ tự ưu tiên (Ordering) của Backlog.
3. Các mục ở trên đỉnh Backlog phải chi tiết, rõ ràng và có độ mịn cao hơn các mục ở phía dưới.
4. Mọi PBI phải gắn liền với Product Goal hiện tại.

## 7. Tiêu chí chất lượng
Các PBI ưu tiên cao phải có mô tả rõ ràng và tiêu chí chấp nhận.

## 8. Quy tắc đặt tên
`DOC-SCRUM-001_Product_Backlog.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-SCRUM-003` (PBI detail) và `DOC-SCRUM-007` (Sprint Backlog).

## 10. Cách kiểm tra
Kiểm tra trường `order` hoặc `priority` không bị trùng lặp.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: PBI-001 xếp thứ 1 (High priority), có Acceptance Criteria đầy đủ.
- Không hợp lệ: Danh sách hàng trăm mục không có thứ tự ưu tiên.

## 13. Tài liệu liên quan
`DOC-SCRUM-002`, `DOC-SCRUM-003`, `DOC-SCRUM-004`.

## 14. Bằng chứng cần thiết
Dữ liệu backlog từ Jira, Trello, Git Issues hoặc bảng Excel.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("PBI_Rules.md", """# RULE-SCRUM-004: Product Backlog Item Rules

- **Mã quy tắc**: `RULE-SCRUM-004`
- **Tên quy tắc**: PBI Definition and Attribute Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định các trường thông tin cần thiết của một Product Backlog Item (PBI).

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-003`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020

## 4. Đầu vào bắt buộc
Mô tả PBI, giá trị nghiệp vụ, thứ tự ưu tiên.

## 5. Cấu trúc trường bắt buộc
PBI ID, Tiêu đề, Mô tả chi tiết, Tiêu chí chấp nhận, Thứ tự (Order), Ước lượng (nếu có).

## 6. Quy tắc nội dung
1. PBI có thể là User Story, Bug, Spike hoặc Technical Improvement.
2. Các PBI được chọn vào Sprint phải đủ nhỏ để hoàn thành trong một Sprint.

## 7. Tiêu chí chất lượng
PBI rõ ràng, độc lập và kiểm chứng được.

## 8. Quy tắc đặt tên
`DOC-SCRUM-003_PBI_User_Story.docx`.

## 9. Truy xuất nguồn gốc
Thuộc `DOC-SCRUM-001`.

## 10. Cách kiểm tra
Kiểm tra ID dạng `PBI-xxx`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: PBI-001: Nâng cấp thư viện OpenSSL lên phiên bản mới nhất để vá lỗ hổng bảo mật.
- Không hợp lệ: PBI không có mô tả nội dung.

## 13. Tài liệu liên quan
`DOC-SCRUM-001`, `DOC-SCRUM-007`.

## 14. Bằng chứng cần thiết
Ticket hoặc tài liệu mô tả task.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Backlog_Refinement_Rules.md", """# RULE-SCRUM-005: Backlog Refinement Rules

- **Mã quy tắc**: `RULE-SCRUM-005`
- **Tên quy tắc**: Backlog Refinement Activity Documentation Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Ghi nhận hoạt động làm mịn Backlog (làm rõ, chia nhỏ, ước lượng) giữa PO và Developers.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-004`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Product Backlog Refinement)

## 4. Đầu vào bắt buộc
Danh sách PBI được xem xét, các nội dung làm rõ, kết quả chia nhỏ.

## 5. Cấu trúc trường bắt buộc
Ngày họp, Danh sách PBI được review, PBI được chia nhỏ, PBI sẵn sàng cho Sprint Planning tiếp theo.

## 6. Quy tắc nội dung
1. Làm mịn là một hoạt động diễn ra liên tục trong suốt Sprint, không phải là một sự kiện đóng khung cố định.
2. Chỉ ghi nhận biên bản khi hoạt động làm mịn thực sự đã diễn ra.

## 7. Tiêu chí chất lượng
Ghi rõ các thay đổi về mô tả và tiêu chí chấp nhận sau phiên làm mịn.

## 8. Quy tắc đặt tên
`DOC-SCRUM-004_Backlog_Refinement.docx`.

## 9. Truy xuất nguồn gốc
Cập nhật trực tiếp vào `DOC-SCRUM-001`.

## 10. Cách kiểm tra
Kiểm tra ngày họp và danh sách PBI được refine.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: PBI lớn "Quản lý kho" được chia thành 3 PBI nhỏ hơn: Nhập kho, Xuất kho, Kiểm kê.
- Không hợp lệ: Tự tạo biên bản họp giả khi nhóm không tổ chức refinement.

## 13. Tài liệu liên quan
`DOC-SCRUM-001`, `DOC-SCRUM-006`.

## 14. Bằng chứng cần thiết
Lịch sử thay đổi PBI trong công cụ quản lý.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Release_Plan_Rules.md", """# RULE-SCRUM-006: Release Plan Rules

- **Mã quy tắc**: `RULE-SCRUM-006`
- **Tên quy tắc**: Release Planning & Optional Forecast Rules
- **Loại quy tắc**: `RECOMMENDATION`
- **Mức độ nghiêm trọng khi vi phạm**: `MINOR`

## 1. Mục đích
Định hướng kế hoạch bàn giao các phiên bản phát hành qua các Sprint (được đánh dấu rõ là thông lệ bổ trợ tùy chọn).

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-005`.

## 3. Nguồn tiêu chuẩn
- Agile Practice Guide & Scrum Complementary Practices (NOT mandatory in Scrum Guide).

## 4. Đầu vào bắt buộc
Ngày phát hành dự kiến, danh sách PBI ứng viên.

## 5. Cấu trúc trường bắt buộc
Phiên bản phát hành, Ngày mục tiêu, Mục tiêu phát hành, Danh sách PBIs dự kiến, Rủi ro phát hành.

## 6. Quy tắc nội dung
1. Phải ghi rõ: Kế hoạch phát hành là dự báo (Forecast), không phải là cam kết hợp đồng cố định.
2. Đánh dấu rõ là thực hành bổ trợ tùy chọn (`RECOMMENDATION`), không phải quy định bắt buộc của Scrum Guide.

## 7. Tiêu chí chất lượng
Rõ ràng về phạm vi dự kiến của từng release.

## 8. Quy tắc đặt tên
`DOC-SCRUM-005_Release_Plan.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-DEL-009` (Release Notes).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của thông báo "Optional Complementary Practice".

## 11. Ngoại lệ
Dự án Continuous Deployment (CD) có thể không cần tài liệu này.

## 12. Ví dụ
- Hợp lệ: Dự báo Release v1.0 sau Sprint 3 với 10 PBIs cốt lõi.
- Không hợp lệ: Khẳng định Scrum Guide bắt buộc phải có Release Plan cố định.

## 13. Tài liệu liên quan
`DOC-SCRUM-001`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Roadmap hoặc kế hoạch bàn giao.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Sprint_Planning_Rules.md", """# RULE-SCRUM-007: Sprint Planning Rules

- **Mã quy tắc**: `RULE-SCRUM-007`
- **Tên quy tắc**: Sprint Planning Event and Topics Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định nội dung và giới hạn thời lượng (Timebox) của sự kiện Sprint Planning theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-006`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Sprint Planning Event)

## 4. Đầu vào bắt buộc
Product Goal, Product Backlog đã làm mịn, năng lực khả dụng của nhóm (Capacity), Increment gần nhất.

## 5. Cấu trúc trường bắt buộc
Bao gồm đủ 3 chủ đề (Topics) của Scrum Guide 2020:
- Chủ đề 1: Tại sao Sprint này có giá trị? (Why is this Sprint valuable? -> Định hình **Sprint Goal**).
- Chủ đề 2: Những gì có thể Hoàn thành trong Sprint này? (What can be Done this Sprint? -> Chọn các **PBIs**).
- Chủ đề 3: Công việc đã chọn sẽ được hoàn thành như thế nào? (How will the chosen work get done? -> Lập kế hoạch hành động / phân rã tasks).
- Giới hạn thời gian (Timebox Compliance): Tối đa 8 giờ cho Sprint 1 tháng.

## 6. Quy tắc nội dung
1. Thời lượng sự kiện Sprint Planning tối đa là 8 giờ đối với Sprint 1 tháng; Sprint ngắn hơn thường có thời lượng ngắn hơn (ví dụ: Sprint 2 tuần thường tối đa 4 giờ).
2. Sprint Goal phải được thống nhất trong sự kiện này trước khi kết thúc phiên họp.
3. Chỉ Developers mới có quyền quyết định lượng công việc có thể hoàn thành trong Sprint.
4. Không tự bịa đặt nội dung phiên họp nếu Sprint chưa diễn ra.

## 7. Tiêu chí chất lượng
Trả lời trọn vẹn cả 3 câu hỏi Chủ đề 1, 2, 3 của Scrum Guide.

## 8. Quy tắc đặt tên
`DOC-SCRUM-006_Sprint_Planning.docx`.

## 9. Truy xuất nguồn gốc
Tạo ra `DOC-SCRUM-007` (Sprint Backlog) và `DOC-SCRUM-008` (Sprint Goal).

## 10. Cách kiểm tra
Kiểm tra Timebox <= 8h và sự hiện diện của cả 3 Topics trong `test_sprint_constraints.py`.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn timebox.

## 12. Ví dụ
- Hợp lệ: Sprint 2 tuần, thời lượng Planning 3.5 giờ, xác lập Sprint Goal và chọn 5 PBIs.
- Không hợp lệ: Sprint Planning kéo dài 12 giờ cho Sprint 2 tuần (vi phạm nghiêm trọng timebox).

## 13. Tài liệu liên quan
`DOC-SCRUM-007`, `DOC-SCRUM-008`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Biên bản Sprint Planning thực tế.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Sprint_Goal_Rules.md", """# RULE-SCRUM-008: Sprint Goal Rules

- **Mã quy tắc**: `RULE-SCRUM-008`
- **Tên quy tắc**: Sprint Goal Commitment and Cohesion Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định việc xác lập Sprint Goal — cam kết chính thức duy nhất của Sprint Backlog theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-008`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Artifact Commitment: Sprint Goal)

## 4. Đầu vào bắt buộc
Giá trị cốt lõi cần đạt được trong Sprint, bối cảnh nghiệp vụ.

## 5. Cấu trúc trường bắt buộc
Số thứ tự Sprint, Tuyên bố Sprint Goal, Bối cảnh & Giá trị nghiệp vụ mang lại, Ranh giới linh hoạt, Tiêu chí đánh giá.

## 6. Quy tắc nội dung
1. Sprint Goal phải thể hiện một mục tiêu chung bao trùm mang lại giá trị, KHÔNG PHẢI chỉ là danh sách liệt kê các đầu việc rời rạc.
2. Sprint Goal tạo ra sự tập trung và gắn kết cho Developers; nếu công việc cần làm khác đi so với dự kiến, Developers thương lượng lại phạm vi với PO nhưng không được làm nguy hại tới Sprint Goal.
3. Không được để trống Sprint Goal trong bất kỳ Sprint nào.

## 7. Tiêu chí chất lượng
Tuyên bố mục tiêu rõ ràng, định hướng giá trị cho người dùng hoặc hệ thống.

## 8. Quy tắc đặt tên
`DOC-SCRUM-008_Sprint_Goal.docx`.

## 9. Truy xuất nguồn gốc
Nằm ở đầu `DOC-SCRUM-007` (Sprint Backlog) và được đánh giá trong `DOC-SCRUM-012` (Sprint Review).

## 10. Cách kiểm tra
Kiểm tra sự tồn tại của tuyên bố Sprint Goal không rỗng.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: "Hoàn thiện quy trình thanh toán qua thẻ tín dụng và xuất hóa đơn điện tử an toàn."
- Không hợp lệ: "Làm xong task 1, task 2, task 3, task 4, task 5."

## 13. Tài liệu liên quan
`DOC-SCRUM-006`, `DOC-SCRUM-007`, `DOC-SCRUM-012`.

## 14. Bằng chứng cần thiết
Biên bản Sprint Planning.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Sprint_Backlog_Rules.md", """# RULE-SCRUM-009: Sprint Backlog Rules

- **Mã quy tắc**: `RULE-SCRUM-009`
- **Tên quy tắc**: Sprint Backlog Composition and Ownership Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định cấu trúc và nguyên tắc quản lý Sprint Backlog theo đúng Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-007`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Sprint Backlog definition)

## 4. Đầu vào bắt buộc
Sprint Goal, danh sách PBIs được chọn, kế hoạch phân rã công việc.

## 5. Cấu trúc trường bắt buộc
Sprint Backlog bắt buộc bao gồm đủ 3 thành phần:
1. **Sprint Goal** (Tại sao).
2. **Tập hợp Product Backlog Items được chọn cho Sprint** (Cái gì).
3. **Kế hoạch hành động chi tiết để tạo ra Increment** (Làm thế nào / Phân rã Tasks).

## 6. Quy tắc nội dung
1. Sprint Backlog là kế hoạch do chính Developers lập ra và thuộc quyền sở hữu của Developers.
2. Phạm vi Sprint có thể được làm rõ và thương lượng lại giữa Product Owner và Developers trong suốt Sprint khi hiểu biết tăng lên, nhưng không được gây nguy hiểm cho Sprint Goal.
3. Chỉ Developers mới có quyền thay đổi Sprint Backlog trong quá trình thực hiện Sprint.
4. Trạng thái công việc được cập nhật liên tục (To Do, In Progress, Done).

## 7. Tiêu chí chất lượng
Đầy đủ cả 3 thành phần: Goal, Selected PBIs, Actionable Plan.

## 8. Quy tắc đặt tên
`DOC-SCRUM-007_Sprint_Backlog.xlsx`.

## 9. Truy xuất nguồn gốc
Trỏ tới `DOC-SCRUM-015` (Increment Deliverables).

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của Sprint Goal và danh sách tasks liên kết với PBIs.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Sprint Backlog có Sprint Goal rõ ràng, 4 PBIs được chọn, mỗi PBI có 2-5 technical tasks cụ thể.
- Không hợp lệ: Sprint Backlog chỉ có danh sách công việc mà không có Sprint Goal.

## 13. Tài liệu liên quan
`DOC-SCRUM-006`, `DOC-SCRUM-008`, `DOC-SCRUM-009`, `DOC-SCRUM-015`.

## 14. Bằng chứng cần thiết
Sprint Board thực tế (Jira/Trello/GitHub Projects).

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Task_Breakdown_Rules.md", """# RULE-SCRUM-010: Task Breakdown Rules

- **Mã quy tắc**: `RULE-SCRUM-010`
- **Tên quy tắc**: Work Decomposition and Task Sizing Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định kỹ thuật phân rã PBI thành các tác vụ kỹ thuật cụ thể cho Developers.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-009`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020

## 4. Đầu vào bắt buộc
Parent PBI ID, mô tả công việc kỹ thuật.

## 5. Cấu trúc trường bắt buộc
Task ID, Parent PBI ID, Task Description, Task Type (Frontend/Backend/DB/Testing), Estimate (giờ/points), Status, Assignee.

## 6. Quy tắc nội dung
1. Mỗi tác vụ kỹ thuật phải đủ nhỏ để có thể hoàn thành trong vòng một ngày hoặc vài ngày làm việc.
2. Các task phải gắn trực tiếp với một PBI cha; không tạo task vô định hướng.

## 7. Tiêu chí chất lượng
Mô tả hành động cụ thể (ví dụ: "Viết migration bảng users", không viết "làm database").

## 8. Quy tắc đặt tên
`DOC-SCRUM-009_Task_Breakdown.xlsx`.

## 9. Truy xuất nguồn gốc
Thuộc `DOC-SCRUM-007` (Sprint Backlog).

## 10. Cách kiểm tra
Kiểm tra `parent_pbi_id` phải tồn tại trong danh sách PBIs của Sprint.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: `TASK-001` (thuộc `PBI-001`): Tạo endpoint `/api/v1/auth/login` với validation express-validator.
- Không hợp lệ: `TASK-999`: Làm việc chung chung.

## 13. Tài liệu liên quan
`DOC-SCRUM-007`, `DOC-SCRUM-003`.

## 14. Bằng chứng cần thiết
Danh sách task kỹ thuật của nhóm.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Sprint_Schedule_Rules.md", """# RULE-SCRUM-011: Sprint Schedule Rules

- **Mã quy tắc**: `RULE-SCRUM-011`
- **Tên quy tắc**: Sprint Duration and Events Calendar Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định giới hạn độ dài của Sprint và lịch trình các sự kiện Scrum theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-010`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (The Sprint definition & timeboxes)

## 4. Đầu vào bắt buộc
Ngày bắt đầu Sprint (`start_date`), Ngày kết thúc Sprint (`end_date`).

## 5. Cấu trúc trường bắt buộc
Sprint ID, Ngày bắt đầu, Ngày kết thúc, Độ dài (tuần/ngày), Lịch các sự kiện Scrum, Kiểm tra giới hạn Timebox.

## 6. Quy tắc nội dung
1. **Độ dài Sprint**: Bắt buộc là một tháng hoặc ngắn hơn (thường từ 1 đến 4 tuần). Tuyệt đối không được vượt quá 1 tháng (tối đa 31 ngày).
2. Một Sprint mới bắt đầu ngay lập tức sau khi Sprint trước đó kết thúc; không có khoảng trống (Sprint 0, hardening sprint, v.v. không thuộc Scrum chính thức).
3. Lịch các sự kiện phải thể hiện rõ: Sprint Planning ở đầu Sprint, Daily Scrum hàng ngày, Sprint Review và Sprint Retrospective ở cuối Sprint.

## 7. Tiêu chí chất lượng
Ngày kết thúc phải lớn hơn ngày bắt đầu và hiệu số ngày <= 31 ngày.

## 8. Quy tắc đặt tên
`DOC-SCRUM-010_Sprint_Schedule.xlsx`.

## 9. Truy xuất nguồn gốc
Liên kết tới `DOC-DEL-001` (Project Schedule).

## 10. Cách kiểm tra
Chạy bài kiểm thử `test_sprint_constraints.py` kiểm tra `end_date - start_date <= 31 days`.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn tối đa một tháng của Sprint.

## 12. Ví dụ
- Hợp lệ: Sprint 1 từ 01/11/2026 đến 14/11/2026 (14 ngày).
- Không hợp lệ: Sprint kéo dài 45 ngày hoặc 2 tháng (vi phạm nguyên tắc cốt lõi của Scrum).

## 13. Tài liệu liên quan
`DOC-SCRUM-006`, `DOC-SCRUM-012`, `DOC-SCRUM-013`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Lịch Sprint của dự án.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Daily_Scrum_Log_Rules.md", """# RULE-SCRUM-012: Daily Scrum Log Rules

- **Mã quy tắc**: `RULE-SCRUM-012`
- **Tên quy tắc**: Daily Scrum Timebox and Optional Log Rules
- **Loại quy tắc**: `RECOMMENDATION`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định nguyên tắc thời lượng bắt buộc của sự kiện Daily Scrum (15 phút) và ghi nhận nhật ký (thông lệ tùy chọn).

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-011`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Daily Scrum Event)

## 4. Đầu vào bắt buộc
Ngày họp, tiến độ hướng tới Sprint Goal, các trở ngại (Impediments).

## 5. Cấu trúc trường bắt buộc
Ngày, Tiến độ hướng tới Sprint Goal, Trở ngại / Blockers, Kế hoạch điều chỉnh trong 24h tới, Cam kết tuân thủ timebox 15 phút.

## 6. Quy tắc nội dung
1. **Timebox bắt buộc**: Daily Scrum là sự kiện kéo dài đúng **15 phút** dành cho Developers của Scrum Team. Không được kéo dài quá 15 phút.
2. **Tính chất tùy chọn của Log**: Việc ghi chép thành văn bản Daily Scrum Log là thông lệ tùy chọn của nhóm, Scrum Guide KHÔNG bắt buộc phải ghi log hàng ngày.
3. Mục đích là để Developers tự quản lý, kiểm tra tiến độ hướng tới Sprint Goal và điều chỉnh kế hoạch ngày làm việc tiếp theo, không phải buổi báo cáo trạng thái cho quản lý.

## 7. Tiêu chí chất lượng
Nêu bật được trở ngại và hành động tháo gỡ.

## 8. Quy tắc đặt tên
`DOC-SCRUM-011_Daily_Scrum_Log.xlsx`.

## 9. Truy xuất nguồn gốc
Trở ngại liên kết tới `DOC-DEL-004` (Issue Log).

## 10. Cách kiểm tra
Kiểm tra giới hạn timebox 15 phút.

## 11. Ngoại lệ
Nếu nhóm không có nhu cầu lưu log bằng văn bản, tài liệu này có thể bỏ qua (`is_optional: true`).

## 12. Ví dụ
- Hợp lệ: Phiên Daily Scrum diễn ra trong 15 phút, Developers phát hiện API Gateway bị nghẽn và cử 2 người xử lý.
- Không hợp lệ: Daily Scrum kéo dài 60 phút biến thành buổi tranh luận giải pháp kỹ thuật sâu.

## 13. Tài liệu liên quan
`DOC-SCRUM-007`, `DOC-DEL-004`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Ghi chép standup thực tế của nhóm.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Sprint_Review_Rules.md", """# RULE-SCRUM-013: Sprint Review Rules

- **Mã quy tắc**: `RULE-SCRUM-013`
- **Tên quy tắc**: Sprint Review Event and Timebox Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định nội dung và thời lượng của sự kiện Sprint Review theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-012`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Sprint Review Event)

## 4. Đầu vào bắt buộc
Increment thực tế hoàn thành đáp ứng DoD, phản hồi của bên liên quan (Stakeholders).

## 5. Cấu trúc trường bắt buộc
Sprint ID, Đánh giá mức độ đạt được Sprint Goal, Các mục Done (đáp ứng DoD), Các mục Chưa Done (trả về Product Backlog), Trình diễn Increment, Phản hồi của Stakeholders & Điều chỉnh Backlog tiếp theo.

## 6. Quy tắc nội dung
1. **Timebox bắt buộc**: Sprint Review có thời lượng tối đa **4 giờ** đối với Sprint một tháng; Sprint ngắn hơn thường có sự kiện ngắn hơn (ví dụ Sprint 2 tuần thường tối đa 2 giờ).
2. Sprint Review là một buổi làm việc cộng tác (working session) để kiểm tra kết quả và xác định các điều chỉnh tiếp theo, KHÔNG chỉ đơn thuần là buổi thuyết trình (demo/presentation).
3. Chỉ những PBI đáp ứng trọn vẹn Definition of Done mới được trình diễn và coi là hoàn thành.
4. Những mục chưa hoàn thành không được coi là Increment và phải được chuyển lại về Product Backlog.
5. Không tự bịa đặt người tham dự hoặc biên bản review nếu sự kiện chưa diễn ra.

## 7. Tiêu chí chất lượng
Có phản hồi thực chất từ các bên liên quan và điều chỉnh Backlog cụ thể.

## 8. Quy tắc đặt tên
`DOC-SCRUM-012_Sprint_Review_Report.docx`.

## 9. Truy xuất nguồn gốc
Cập nhật lại `DOC-SCRUM-001` (Product Backlog).

## 10. Cách kiểm tra
Kiểm tra Timebox <= 4h trong `test_sprint_constraints.py`.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn 4 giờ.

## 12. Ví dụ
- Hợp lệ: Sprint 2 tuần, Review 1.5 giờ, PO và khách hàng dùng thử tính năng tìm kiếm và gợi ý thêm bộ lọc.
- Không hợp lệ: Họp Sprint Review 6 giờ hoặc tự nhận các PBI lỗi là Done.

## 13. Tài liệu liên quan
`DOC-SCRUM-008`, `DOC-SCRUM-014`, `DOC-SCRUM-015`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Biên bản Sprint Review thực tế.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Sprint_Retrospective_Rules.md", """# RULE-SCRUM-014: Sprint Retrospective Rules

- **Mã quy tắc**: `RULE-SCRUM-014`
- **Tên quy tắc**: Sprint Retrospective Event and Continuous Improvement Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định nội dung và thời lượng của sự kiện Sprint Retrospective theo Scrum Guide 2020 nhằm cải tiến liên tục.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-013`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Sprint Retrospective Event)

## 4. Đầu vào bắt buộc
Những điều làm tốt, những khó khăn vướng mắc, các hành động cải tiến cụ thể.

## 5. Cấu trúc trường bắt buộc
Sprint ID, Thành phần tham dự (Scrum Team), Điểm tích cực / Thành công, Khó khăn / Trở ngại, Kế hoạch hành động cải tiến cho Sprint tới (có Người phụ trách), Cải tiến Definition of Done (nếu có).

## 6. Quy tắc nội dung
1. **Timebox bắt buộc**: Sprint Retrospective có thời lượng tối đa **3 giờ** đối với Sprint một tháng; Sprint ngắn hơn thường ngắn hơn (ví dụ Sprint 2 tuần thường tối đa 1.5 giờ).
2. Sự kiện tập trung vào con người, mối quan hệ, quy trình và công cụ để nâng cao chất lượng và hiệu quả.
3. Nhóm xác định các thay đổi hữu ích nhất và đưa ít nhất một hành động cải tiến có tác động cao vào Sprint Backlog của Sprint tiếp theo.
4. Không tự bịa đặt nội dung họp nếu sự kiện chưa diễn ra.

## 7. Tiêu chí chất lượng
Mỗi hành động cải tiến phải có người phụ trách và cách đo lường kết quả.

## 8. Quy tắc đặt tên
`DOC-SCRUM-013_Sprint_Retrospective.docx`.

## 9. Truy xuất nguồn gốc
Hành động cải tiến chuyển vào `DOC-SCRUM-006` của Sprint kế tiếp.

## 10. Cách kiểm tra
Kiểm tra Timebox <= 3h trong `test_sprint_constraints.py`.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn 3 giờ.

## 12. Ví dụ
- Hợp lệ: Sprint 2 tuần, Retro 1 giờ, thống nhất hành động: "Tự động hóa linting trước khi commit để giảm lỗi code review."
- Không hợp lệ: Retrospective kéo dài 5 giờ.

## 13. Tài liệu liên quan
`DOC-SCRUM-006`, `DOC-SCRUM-014`, `Timebox_Rules.md`.

## 14. Bằng chứng cần thiết
Biên bản Sprint Retrospective thực tế.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Definition_of_Done_Rules.md", """# RULE-SCRUM-015: Definition of Done Rules

- **Mã quy tắc**: `RULE-SCRUM-015`
- **Tên quy tắc**: Definition of Done Commitment and Quality Standard Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định tiêu chuẩn chất lượng bắt buộc của Definition of Done (DoD) — cam kết chính thức của Increment theo Scrum Guide 2020.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-014`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Artifact Commitment: Definition of Done)

## 4. Đầu vào bắt buộc
Tiêu chuẩn chất lượng tổ chức, yêu cầu kiểm thử tự động, chuẩn code review.

## 5. Cấu trúc trường bắt buộc
Phạm vi áp dụng DoD, Chuẩn mã nguồn & phong cách code, Yêu cầu kiểm thử tự động (Unit/Integration Test Coverage), Tiêu chuẩn Code Review, Tài liệu hóa đầy đủ, Tiêu chuẩn triển khai và xác minh.

## 6. Quy tắc nội dung
1. Definition of Done là mô tả hình thức về trạng thái của Increment khi nó đáp ứng đầy đủ các biện pháp chất lượng cần thiết cho sản phẩm.
2. Thời điểm một PBI đáp ứng Definition of Done, một **Increment** được sinh ra.
3. Nếu một PBI không đáp ứng Definition of Done, nó KHÔNG ĐƯỢC coi là một phần của Increment, không được phát hành và không được trình diễn tại Sprint Review (phải đưa lại về Product Backlog).
4. Nếu tổ chức đã có DoD cấp doanh nghiệp, Scrum Team phải kế thừa và có thể làm cho nó nghiêm ngặt hơn.
5. Không hạ thấp tiêu chuẩn DoD trong quá trình chạy Sprint để cố tình "hoàn thành" công việc.

## 7. Tiêu chí chất lượng
Các tiêu chí trong DoD phải đo đếm và kiểm tra được (Automated checks).

## 8. Quy tắc đặt tên
`DOC-SCRUM-014_Definition_of_Done.docx`.

## 9. Truy xuất nguồn gốc
Kiểm chứng trực tiếp cho `DOC-SCRUM-015` (Increment) và `DOC-TEST-007` (Code Review Checklist).

## 10. Cách kiểm tra
Kiểm tra sự tồn tại của tiêu chuẩn kiểm thử và tiêu chuẩn mã nguồn trong DoD.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: DoD quy định: Mã nguồn được review bởi ít nhất 1 peer, Unit test pass 100%, Code coverage >= 80%, Deploy thành công lên Staging.
- Không hợp lệ: Tính năng còn bug nghiêm trọng nhưng vẫn đánh dấu Done.

## 13. Tài liệu liên quan
`DOC-SCRUM-015`, `DOC-TEST-007`.

## 14. Bằng chứng cần thiết
Văn bản DoD được thống nhất bởi Scrum Team.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Definition_of_Ready_Rules.md", """# RULE-SCRUM-016: Definition of Ready Rules

- **Mã quy tắc**: `RULE-SCRUM-016`
- **Tên quy tắc**: Definition of Ready (Optional Practice) Rules
- **Loại quy tắc**: `RECOMMENDATION`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định tiêu chuẩn đánh giá PBI sẵn sàng đưa vào Sprint Planning (thông lệ tùy chọn của nhóm).

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-017`.

## 3. Nguồn tiêu chuẩn
- Agile Complementary Practices (Scrum Alliance / Scrum.org community practice).
- **LƯU Ý QUAN TRỌNG**: Definition of Ready KHÔNG PHẢI là một khái niệm hay quy tắc bắt buộc trong The Scrum Guide 2020.

## 4. Đầu vào bắt buộc
Checklist kiểm tra PBI trước khi đưa vào Sprint Planning.

## 5. Cấu trúc trường bắt buộc
Thông báo trạng thái tùy chọn (Optional Status Notice), Tiêu chuẩn độ rõ ràng của PBI, Độ rõ ràng của Acceptance Criteria, Đã được ước lượng, Sự phụ thuộc đã được giải quyết.

## 6. Quy tắc nội dung
1. **Bắt buộc phân loại đúng**: Phải đánh dấu rõ ràng Definition of Ready là `RECOMMENDATION` hoặc `INTERNAL_POLICY` của nhóm. Tuyệt đối không được gán nhãn DoR là quy tắc chính thức của Scrum Guide.
2. DoR không được dùng như một cánh cổng kiểm soát cứng nhắc (Stage-gate) ngăn cản sự cộng tác giữa PO và Developers.

## 7. Tiêu chí chất lượng
Có tuyên bố minh bạch về tính chất bổ trợ của DoR.

## 8. Quy tắc đặt tên
`DOC-SCRUM-017_Definition_of_Ready.docx`.

## 9. Truy xuất nguồn gốc
Hỗ trợ sàng lọc PBI trong `DOC-SCRUM-003`.

## 10. Cách kiểm tra
Chạy bài kiểm thử `test_sprint_constraints.py` để xác nhận DoR không bị ghi nhầm là `OFFICIAL_REQUIREMENT`.

## 11. Ngoại lệ
Nhóm hoàn toàn có quyền không sử dụng DoR nếu thấy không cần thiết.

## 12. Ví dụ
- Hợp lệ: DoR là checklist nội bộ của nhóm để hỗ trợ PO chuẩn bị story tốt hơn.
- Không hợp lệ: Khẳng định "Theo quy định Scrum Guide bắt buộc phải có Definition of Ready mới được Planning".

## 13. Tài liệu liên quan
`DOC-SCRUM-003`, `DOC-SCRUM-006`.

## 14. Bằng chứng cần thiết
Thỏa thuận nội bộ của nhóm phát triển.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Sprint_Deliverables_Rules.md", """# RULE-SCRUM-017: Sprint Deliverables Rules

- **Mã quy tắc**: `RULE-SCRUM-017`
- **Tên quy tắc**: Increment Deliverables Verification Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Ghi nhận và kiểm chứng Increment thực tế hoàn thành sau Sprint đáp ứng Definition of Done.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-015`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (Increment definition)

## 4. Đầu vào bắt buộc
Phiên bản build/package có thể chạy được, danh sách PBIs đã xác minh đạt DoD.

## 5. Cấu trúc trường bắt buộc
Increment Version/Tag, Danh sách PBIs đạt DoD, Tham chiếu mã nguồn/commit hash, Bằng chứng kiểm thử nghiệm thu, Trạng thái sẵn sàng phát hành.

## 6. Quy tắc nội dung
1. Increment phải ở trạng thái có thể sử dụng được (usable), bất kể Product Owner có quyết định phát hành nó ra thực tế hay không.
2. Mọi phần tính năng trong Increment phải đáp ứng đầy đủ Definition of Done.
3. Không tự tạo thông tin phát hành khi mã nguồn chưa build thành công hoặc test fail.

## 7. Tiêu chí chất lượng
Có commit hash hoặc artifact URL cụ thể.

## 8. Quy tắc đặt tên
`DOC-SCRUM-015_Increment_Deliverables.xlsx`.

## 9. Truy xuất nguồn gốc
Cơ sở để lập `DOC-DEL-009` (Release Notes).

## 10. Cách kiểm tra
Kiểm tra đối chiếu với `DOC-SCRUM-014` (DoD).

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Increment `v1.2.0` (commit `a1b2c3d`) hoàn thành 4 PBIs và pass toàn bộ test suite.
- Không hợp lệ: Ghi nhận bàn giao trong khi mã nguồn đang bị lỗi cú pháp không build được.

## 13. Tài liệu liên quan
`DOC-SCRUM-014`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Docker image tag, artifact repository hoặc Git release tag.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Sprint_Metrics_Rules.md", """# RULE-SCRUM-018: Sprint Metrics Rules

- **Mã quy tắc**: `RULE-SCRUM-018`
- **Tên quy tắc**: Sprint Metrics and Burndown Tracking Rules
- **Loại quy tắc**: `RECOMMENDATION`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định việc theo dõi các chỉ số Sprint (Velocity, Burndown Chart) dựa trên dữ liệu thực tế (thông lệ tùy chọn).

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-016`.

## 3. Nguồn tiêu chuẩn
- Agile Practice Guide (Complementary practice, NOT mandatory in Scrum Guide).

## 4. Đầu vào bắt buộc
Dữ liệu công việc còn lại thực tế qua các ngày của Sprint.

## 5. Cấu trúc trường bắt buộc
Sprint ID, Điểm kế hoạch vs Điểm thực tế hoàn thành, Bảng số liệu Burndown hàng ngày, Phân tích Velocity, Thông báo tính chất bổ trợ.

## 6. Quy tắc nội dung
1. **Tính chất bổ trợ**: Phải nêu rõ Burndown chart và Velocity là công cụ bổ trợ, KHÔNG PHẢI quy định bắt buộc của Scrum Guide.
2. **Cấm bịa đặt số liệu**: Tuyệt đối không tự bịa đặt dữ liệu burndown giả nếu không có log theo dõi công việc thực tế từ nhóm.
3. Velocity chỉ mang tính tham khảo nội bộ nhóm để hỗ trợ lập kế hoạch, không dùng để so sánh năng suất giữa các nhóm khác nhau.

## 7. Tiêu chí chất lượng
Biểu đồ và bảng số liệu khớp nhau 100%.

## 8. Quy tắc đặt tên
`DOC-SCRUM-016_Sprint_Metrics_Burndown.xlsx`.

## 9. Truy xuất nguồn gốc
Hỗ trợ dữ liệu cho `DOC-DEL-008` (Progress Report).

## 10. Cách kiểm tra
Kiểm tra cấm số liệu bịa đặt và nhãn `RECOMMENDATION`.

## 11. Ngoại lệ
Nhóm làm theo Kanban/Flow metrics có thể dùng CFD (Cumulative Flow Diagram) thay thế.

## 12. Ví dụ
- Hợp lệ: Nhóm ghi nhận điểm hoàn thành thực tế của Sprint 1 là 24 story points.
- Không hợp lệ: Tự vẽ đường burndown thẳng tắp hoàn hảo trong khi dự án chưa từng chạy Sprint.

## 13. Tài liệu liên quan
`DOC-SCRUM-007`, `DOC-DEL-008`.

## 14. Bằng chứng cần thiết
Dữ liệu log từ issue tracker.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Timebox_Rules.md", """# RULE-SCRUM-019: Scrum Timebox Rules

- **Mã quy tắc**: `RULE-SCRUM-019`
- **Tên quy tắc**: Strict Scrum Events Timeboxing Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định chặt chẽ và chính xác giới hạn thời gian (Timebox) cho tất cả các sự kiện Scrum theo đúng quy định của The Scrum Guide (Nov 2020).

## 2. Phạm vi áp dụng
Tất cả các tài liệu về sự kiện và lịch trình Scrum (`DOC-SCRUM-006`, `DOC-SCRUM-010`, `DOC-SCRUM-011`, `DOC-SCRUM-012`, `DOC-SCRUM-013`).

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 (The Events of Scrum)

## 4. Đầu vào bắt buộc
Độ dài Sprint (`sprint_duration`), thời lượng dự kiến của từng sự kiện.

## 5. Cấu trúc trường bắt buộc
Bảng kiểm tra tuân thủ Timebox cho từng sự kiện.

## 6. Quy tắc nội dung bắt buộc
1. **The Sprint**: Tối đa 1 tháng (<= 31 ngày).
2. **Sprint Planning**: Tối đa **8 giờ** cho Sprint 1 tháng. Đối với Sprint ngắn hơn (ví dụ Sprint 2 tuần), sự kiện thường ngắn hơn (thường tối đa 4 giờ).
3. **Daily Scrum**: Đúng **15 phút** cho Developers.
4. **Sprint Review**: Tối đa **4 giờ** cho Sprint 1 tháng. Đối với Sprint ngắn hơn, sự kiện thường ngắn hơn (thường tối đa 2 giờ).
5. **Sprint Retrospective**: Tối đa **3 giờ** cho Sprint 1 tháng. Đối với Sprint ngắn hơn, sự kiện thường ngắn hơn (thường tối đa 1.5 giờ).
6. **LÀM RÕ CÁC HIỂU LẦM**:
   - Scrum Guide **KHÔNG** quy định ngày làm việc phải là 8 giờ (đây là luật lao động hành chính, không phải quy tắc Scrum).
   - Scrum Guide **KHÔNG** bắt buộc mọi Sprint phải dài 2 tuần.
   - Khi hết thời lượng timebox quy định, sự kiện kết thúc ngay lập tức.

## 7. Tiêu chí chất lượng
100% thời lượng sự kiện khai báo trong tài liệu không vượt quá ngưỡng tối đa của Scrum Guide.

## 8. Quy tắc đặt tên
`RULE-SCRUM-019`.

## 9. Truy xuất nguồn gốc
Được kiểm tra tự động qua bộ test suite `test_sprint_constraints.py`.

## 10. Cách kiểm tra
Hàm kiểm tra `validate_sprint_timeboxes()` kiểm tra các giá trị giờ.

## 11. Ngoại lệ
Không có ngoại lệ đối với giới hạn trần của timebox.

## 12. Ví dụ
- Hợp lệ: Sprint 1 tháng có Sprint Planning 7 giờ, Review 3.5 giờ, Retro 2.5 giờ, Daily Scrum 15 phút.
- Không hợp lệ: Sprint 2 tuần mà xếp lịch Sprint Planning 10 giờ (vi phạm nghiêm trọng).

## 13. Tài liệu liên quan
`DOC-SCRUM-006`, `DOC-SCRUM-010`, `DOC-SCRUM-011`, `DOC-SCRUM-012`, `DOC-SCRUM-013`.

## 14. Bằng chứng cần thiết
Lịch biểu sự kiện Scrum trong dự án.

## 15. Giới hạn đã biết
Không có.
""")

write_rule("Estimation_Rules.md", """# RULE-SCRUM-020: Estimation Rules

- **Mã quy tắc**: `RULE-SCRUM-020`
- **Tên quy tắc**: Estimation Techniques and Optional Complementary Practice Rules
- **Loại quy tắc**: `RECOMMENDATION`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định phương pháp ước lượng công việc trong Scrum và làm rõ tính chất bổ trợ của Story Points.

## 2. Phạm vi áp dụng
Tài liệu `DOC-SCRUM-001`, `DOC-SCRUM-003`, `DOC-SCRUM-007`.

## 3. Nguồn tiêu chuẩn
- The Scrum Guide 2020 & Agile Practice Guide

## 4. Đầu vào bắt buộc
Kỹ thuật ước lượng được nhóm lựa chọn (Story Points, T-shirt sizing, Hours).

## 5. Cấu trúc trường bắt buộc
PBI ID, Ước lượng độ phức tạp, Kỹ thuật sử dụng, Người ước lượng (Developers).

## 6. Quy tắc nội dung
1. **Quyền ước lượng**: Những người thực hiện công việc (Developers) là người duy nhất chịu trách nhiệm đưa ra ước lượng. Product Owner có thể gây ảnh hưởng bằng cách làm rõ nghiệp vụ, nhưng không được áp đặt con số ước lượng.
2. **Tính chất bổ trợ**: Story Points, dãy số Fibonacci, Planning Poker là các thông lệ bổ trợ phổ biến, **KHÔNG PHẢI** là yêu cầu bắt buộc của Scrum Guide 2020.
3. Ước lượng chỉ là dự đoán mang tính tương đối, không phải cam kết bất biến.

## 7. Tiêu chí chất lượng
Các ước lượng được đưa ra trên cơ sở thống nhất của Developers.

## 8. Quy tắc đặt tên
`RULE-SCRUM-020`.

## 9. Truy xuất nguồn gốc
Liên kết với `DOC-SCRUM-001`.

## 10. Cách kiểm tra
Kiểm tra trường `estimate` trong bảng Backlog.

## 11. Ngoại lệ
Nhóm có thể không ước lượng điểm nếu áp dụng kỹ thuật chia nhỏ đều (NoEstimates / Right-sizing).

## 12. Ví dụ
- Hợp lệ: Developers cùng thảo luận và gán 5 Story Points cho PBI-002.
- Không hợp lệ: Product Owner ép Developers phải nhận task trong 2 ngày.

## 13. Tài liệu liên quan
`DOC-SCRUM-001`, `DOC-SCRUM-007`.

## 14. Bằng chứng cần thiết
Biên bản phiên Planning Poker hoặc ước lượng.

## 15. Giới hạn đã biết
Không có.
""")

print("All 20 Scrum rules created successfully.")
