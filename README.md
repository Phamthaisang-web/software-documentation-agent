# Hệ Thống Quản Lý & Tự Động Hóa 59 Tài Liệu Phần Mềm Tiêu Chuẩn

> **Tổng hợp và giải nghĩa chi tiết 59 loại tài liệu kỹ thuật phần mềm tiêu chuẩn quốc tế (ISO 29148, ISO 42010, ISO 29119, Scrum Guide 2020) được AI Agent tự động hóa, phân tích mã nguồn và bảo tồn mẫu biểu.**

---

## 1. Điểm Cốt Lõi Của Hệ Thống

* **Chống giả mạo số liệu (Zero Hallucination)**: Tài liệu được sinh hoàn toàn dựa trên bằng chứng thu thập thực tế từ mã nguồn (routes, endpoints, database schemas, docker, package manifests, unit tests); không tự bịa đặt tính năng hay kết quả kiểm thử.
* **Bảo tồn mẫu biểu thực tế (Template Preservation)**: Giữ nguyên định dạng Word (`.docx`), bảng tính Excel (`.xlsx`), kiểu dáng bảng biểu, công thức tính toán và cấu trúc mẫu ban đầu.
* **Mạng lưới truy xuất nguồn gốc 2 chiều (Traceability)**: Tự động kết nối và đối soát liên kết logic giữa *Mục tiêu sản phẩm $\leftrightarrow$ Yêu cầu người dùng (User Story) $\leftrightarrow$ Kiến trúc hệ thống $\leftrightarrow$ API & Database $\leftrightarrow$ Kịch bản kiểm thử (Test Case)*.
* **Chuẩn hóa quy trình Scrum**: Thực thi đúng các quy định cốt lõi của Scrum Guide 2020 (Timebox sự kiện, vai trò, cam kết chất lượng DoD, Sprint Goal) và các thông lệ bổ trợ (DoR, Story Points, Bảng theo dõi số giờ LET, Biểu đồ Burndown).

---

## 2. Giải Nghĩa Chi Tiết 59 Loại Tài Liệu Kỹ Thuật

Dưới đây là mô tả chi tiết từng loại tài liệu, mục đích sử dụng và ý nghĩa thực tế trong các dự án công nghệ và đồ án phần mềm:

---

### NHÓM A: Khởi Động Dự Án & Quản Lý Yêu Cầu (11 Loại Tài Liệu)
*Tham chiếu tiêu chuẩn: **ISO/IEC/IEEE 29148:2018** (Kỹ thuật yêu cầu phần mềm) & **ISO 21500**.*

| Mã Tài Liệu | Tên Tài Liệu | Định Dạng | Tài Liệu Này Là Gì & Dùng Để Làm Gì? |
| :--- | :--- | :---: | :--- |
| `DOC-PM-001` | **Project Charter** *(Hiến chương dự án)* | `.docx` | Văn bản khởi động dự án chính thức; xác nhận sự tồn tại của dự án, mục tiêu kinh doanh, ngân sách dự kiến, thời hạn và trao quyền quản lý cho Project Manager (PM). |
| `DOC-PM-002` | **Project Scope Statement** *(Tuyên bố phạm vi)* | `.docx` | Định rõ ranh giới dự án: những gì **sẽ làm (In-scope)** và những gì **tuyệt đối không làm (Out-of-scope)** để tránh phát sinh chi phí và trễ tiến độ. |
| `DOC-PM-003` | **Stakeholder Register** *(Sổ đăng ký bên liên quan)* | `.xlsx` | Bảng quản lý danh sách các bên liên quan (khách hàng, ban giám đốc, dev, end-user), vai trò, mức độ ảnh hưởng và mức độ quan tâm đối với dự án. |
| `DOC-REQ-001`| **Software Requirements Specification (SRS)** | `.docx` | **Xương sống của dự án**: Văn bản đặc tả toàn bộ yêu cầu phần mềm chi tiết (chức năng, phi chức năng, giao diện, bảo mật) theo chuẩn ISO 29148. |
| `DOC-REQ-002`| **Product Vision Document** *(Tầm nhìn sản phẩm)* | `.docx` | Trình bày lý do sản phẩm ra đời, bài toán cốt lõi cần giải quyết, định vị thị trường và giá trị đem lại cho khách hàng mục tiêu. |
| `DOC-REQ-003`| **Functional Requirements Document (FRD)** | `.docx` | Danh mục mô tả chi tiết tất cả các tính năng, hành vi mà phần mềm bắt buộc phải thực hiện khi người dùng thao tác. |
| `DOC-REQ-004`| **Non-Functional Requirements Document (NFRD)** | `.docx` | Các ràng buộc kỹ thuật chất lượng: tốc độ phản hồi (Response time), khả năng tải đồng thời (Concurrency), độ sẵn sàng (Uptime), mã hóa và bảo mật. |
| `DOC-REQ-005`| **Use Case Specification** *(Đặc tả ca sử dụng)* | `.docx` | Mô tả các kịch bản tương tác giữa Tác nhân (Actor) và Hệ thống, gồm luồng chính (Main flow), luồng phụ (Alternative flow) và ngoại lệ (Exception flow). |
| `DOC-REQ-006`| **User Story Mapping** *(Sơ đồ hành trình người dùng)* | `.docx` | Sắp xếp trực quan các hành vi của người dùng từ lúc bắt đầu đến khi kết thúc, giúp phân chia lộ trình phát hành các phiên bản (Release Slices). |
| `DOC-REQ-007`| **User Stories Catalog** *(Danh mục User Story)* | `.docx` | Tập hợp các câu chuyện người dùng viết theo mẫu: *"Là [vai trò], tôi muốn [tính năng] để [lợi ích/mục tiêu]"*. |
| `DOC-REQ-008`| **Traceability Matrix & Acceptance Criteria (RTM)** | `.xlsx` | **Ma trận truy vết 2 chiều**: Liên kết từng User Story với Tiêu chí nghiệm thu (Given-When-Then) và mã Test Case tương ứng, đảm bảo không bỏ sót yêu cầu nào. |

---

### NHÓM B: Khung Làm Việc Scrum & Quản Trị Sprint (17 Loại Tài Liệu)
*Tham chiếu: **Scrum Guide 2020** (Ken Schwaber & Jeff Sutherland).*

| Mã Tài Liệu | Tên Tài Liệu | Định Dạng | Tài Liệu Này Là Gì & Dùng Để Làm Gì? |
| :--- | :--- | :---: | :--- |
| `DOC-SCRUM-001` | **Product Goal Document** *(Mục tiêu sản phẩm)* | `.md` | Cam kết dài hạn của Product Owner; là kim chỉ nam định hướng cho toàn bộ các hạng mục công việc trong Product Backlog. |
| `DOC-SCRUM-002` | **Product Roadmap** *(Lộ trình sản phẩm)* | `.docx` | Bản đồ chiến lược thể hiện các mốc phát triển lớn của sản phẩm theo thời gian (quý/năm) cho các bên liên quan theo dõi. |
| `DOC-SCRUM-003` | **Product Backlog** *(Danh sách hạng mục sản phẩm)* | `.xlsx` | Danh sách toàn bộ các tính năng, yêu cầu, cải tiến và sửa lỗi được sắp xếp theo thứ tự ưu tiên từ cao xuống thấp. |
| `DOC-SCRUM-004` | **Product Backlog Item (PBI) Specification** | `.docx` | Bản mô tả chi tiết của một hạng mục PBI cụ thể: giải thích bối cảnh, giá trị nghiệp vụ, điều kiện chấp nhận và độ phức tạp. |
| `DOC-SCRUM-005` | **Backlog Refinement Record** *(Biên bản làm mịn)* | `.docx` | Ghi nhận kết quả cuộc họp định kỳ giữa PO và Dev team để làm rõ yêu cầu, chẻ nhỏ PBI to và ước lượng khối lượng công việc. |
| `DOC-SCRUM-006` | **Release Plan** *(Kế hoạch phát hành)* | `.docx` | Kế hoạch dự kiến các Sprint nào sẽ được đóng gói để phát hành phiên bản Increment chính thức ra môi trường thực tế. |
| `DOC-SCRUM-007` | **Sprint Planning Record** *(Biên bản lập kế hoạch Sprint)* | `.docx` | Ghi lại cam kết của nhóm trong buổi đầu Sprint: chọn PBI nào vào Sprint, xác lập Sprint Goal và thống nhất kế hoạch thực hiện. |
| `DOC-SCRUM-008` | **Sprint Goal Document** *(Mục tiêu Sprint)* | `.md` | Cam kết duy nhất và bất biến của nhóm phát triển trong một Sprint; mô tả giá trị cốt lõi cần đạt được trước khi hết Sprint. |
| `DOC-SCRUM-009` | **Sprint Backlog** *(Danh sách công việc Sprint)* | `.xlsx` | Tập hợp các PBI đã chọn cho Sprint kèm theo danh sách các nhiệm vụ kỹ thuật cụ thể của nhóm để hoàn thành mục tiêu. |
| `DOC-SCRUM-010` | **Task Breakdown Sheet** *(Bảng phân rã nhiệm vụ)* | `.docx` | Phân nhỏ từng PBI/User Story thành các đầu việc kỹ thuật chi tiết (Front-end, Back-end, DB, Test) có khối lượng dưới 8 giờ làm việc. |
| `DOC-SCRUM-011` | **Sprint Schedule** *(Lịch trình sự kiện Sprint)* | `.docx` | Lịch phân bổ khung thời gian (Timebox) cho 4 sự kiện chính thức: Sprint Planning, Daily Scrum, Sprint Review và Sprint Retrospective. |
| `DOC-SCRUM-012` | **Daily Scrum Log** *(Nhật ký họp đứng hàng ngày)* | `.md` | Biên bản tóm tắt buổi họp 15 phút mỗi ngày: việc đã hoàn thành hôm qua, việc sẽ làm hôm nay và các trở ngại (Impediments) đang gặp. |
| `DOC-SCRUM-013` | **Sprint Review Record** *(Biên bản sơ kết Sprint)* | `.docx` | Ghi nhận buổi demo sản phẩm tăng dần (Increment) cho khách hàng/PO xem, thảo luận những gì đã làm xong và nhận phản hồi góp ý. |
| `DOC-SCRUM-014` | **Sprint Retrospective Record** *(Biên bản cải tiến)* | `.md` | Buổi họp nội bộ sau mỗi Sprint để nhóm nhìn nhận lại: điều gì làm tốt, điều gì chưa tốt và đưa ra hành động cải tiến cụ thể cho Sprint sau. |
| `DOC-SCRUM-015` | **Definition of Done (DoD)** *(Định nghĩa hoàn thành)* | `.docx` | **Bản cam kết chất lượng**: Danh sách các tiêu chí kỹ thuật bắt buộc (đã code, đã review, đã unit test, pass test, deploy staging) để một tính năng được coi là "Xong". |
| `DOC-SCRUM-016` | **Definition of Ready (DoR)** *(Định nghĩa sẵn sàng)* | `.docx` | Bộ tiêu chuẩn để một User Story đủ độ rõ ràng, khả thi và có tiêu chí nghiệm thu trước khi được bốc vào làm trong Sprint. |
| `DOC-SCRUM-017` | **Sprint Metrics & Burndown Tracking** | `.xlsx` | Bảng theo dõi số giờ còn lại hàng ngày (LET) và biểu đồ Burndown Chart thể hiện khối lượng công việc giảm dần về 0. |

---

### NHÓM C: Kiến Trúc & Thiết Kế Kỹ Thuật (10 Loại Tài Liệu)
*Tham chiếu tiêu chuẩn: **ISO/IEC/IEEE 42010:2022** (Mô tả kiến trúc phần mềm) & **OpenAPI 3.1**.*

| Mã Tài Liệu | Tên Tài Liệu | Định Dạng | Tài Liệu Này Là Gì & Dùng Để Làm Gì? |
| :--- | :--- | :---: | :--- |
| `DOC-ARCH-001` | **Software Architecture Document (SAD)** | `.docx` | **Bản vẽ tổng thể của phần mềm**: Mô tả kiến trúc hệ thống theo mô hình 4+1 Views (Góc nhìn logic, tiến trình, triển khai, dữ liệu và ca sử dụng). |
| `DOC-ARCH-002` | **System Design Document (SDD)** | `.docx` | Thiết kế kỹ thuật chi tiết: các module, cách các tầng (Controller, Service, Repository) giao tiếp với nhau và xử lý nghiệp vụ. |
| `DOC-ARCH-003` | **Database Design Document (DBDD)** | `.docx` | Thiết kế cơ sở dữ liệu chi tiết: danh sách bảng, kiểu dữ liệu từng cột, khóa chính, khóa ngoại, chỉ mục (Index) và ràng buộc toàn vẹn. |
| `DOC-ARCH-004` | **Entity Relationship Diagram (ERD)** | `.mmd` | Sơ đồ quan hệ thực thể biểu diễn trực quan mối liên kết $1-1$, $1-N$, $N-N$ giữa các bảng bằng mã nguồn Mermaid. |
| `DOC-ARCH-005` | **REST API Specification** | `.yaml` | Tài liệu đặc tả toàn bộ các API endpoint theo chuẩn OpenAPI 3.1: URL, phương thức HTTP, headers, tham số request và cấu trúc JSON response. |
| `DOC-ARCH-006` | **UI/UX Design Specification** | `.docx` | Quy định chuẩn giao diện người dùng: bảng màu nhận diện, font chữ, quy chuẩn layout, component dùng chung và luồng thao tác màn hình. |
| `DOC-ARCH-007` | **Component & Package Diagram** | `.docx` | Sơ đồ tổ chức các thư mục mã nguồn, module nội bộ và các thư viện bên thứ ba mà dự án phụ thuộc. |
| `DOC-ARCH-008` | **Deployment & Infrastructure Architecture** | `.mmd` | Sơ đồ mạng hạ tầng: mô tả vị trí máy chủ Client, Web Server, App Server, CSDL, Load Balancer, Cache Redis và tường lửa. |
| `DOC-ARCH-009` | **Technical Design Specification (TDS)** | `.docx` | Đặc tả chi tiết các thuật toán phức tạp, cơ chế bảo mật (JWT, OAuth2, RBAC), cơ chế mã hóa mật khẩu và chiến lược xử lý dữ liệu lớn. |
| `DOC-ARCH-010` | **Architecture Decision Records (ADR)** | `.md` | Nhật ký ghi nhận các quyết định công nghệ quan trọng (tại sao chọn PostgreSQL thay vì MongoDB, tại sao dùng microservices...), bối cảnh và hệ quả. |

---

### NHÓM D: Kiểm Thử & Đảm Bảo Chất Lượng (8 Loại Tài Liệu)
*Tham chiếu tiêu chuẩn: **ISO/IEC/IEEE 29119** (Phần 1, 2, 3, 4 - Quy trình & Tài liệu kiểm thử phần mềm).*

| Mã Tài Liệu | Tên Tài Liệu | Định Dạng | Tài Liệu Này Là Gì & Dùng Để Làm Gì? |
| :--- | :--- | :---: | :--- |
| `DOC-TEST-001` | **Master Test Plan** *(Kế hoạch kiểm thử tổng thể)* | `.docx` | Chiến lược kiểm thử toàn dự án: mục tiêu, phạm vi test (những gì test, những gì không test), môi trường test, nhân sự, công cụ và tiêu chí dừng test. |
| `DOC-TEST-002` | **Test Scenario Specification** *(Kịch bản kiểm thử)* | `.docx` | Danh sách tập hợp các luồng kiểm thử lớn (End-to-End Scenarios) kiểm tra xem hệ thống có chạy thông suốt từ đầu đến cuối không. |
| `DOC-TEST-003` | **Test Case Specification** *(Bảng đặc tả ca kiểm thử)* | `.xlsx` | Bảng chi tiết từng ca kiểm thử: Tiền điều kiện, các bước thực hiện từng bước (Steps), Dữ liệu kiểm thử (Test Data) và Kết quả mong đợi (Expected Result). |
| `DOC-TEST-004` | **Test Execution & Summary Report** | `.docx` | Báo cáo nghiệm thu kiểm thử: tỷ lệ Pass/Fail, danh sách các ca test đã chạy, độ bao phủ mã nguồn và đánh giá phần mềm đã đủ chất lượng để release chưa. |
| `DOC-TEST-005` | **Bug / Defect Report Sheet** *(Bảng theo dõi lỗi)* | `.xlsx` | Bảng quản lý tất cả các lỗi tìm thấy: mô tả lỗi, mức độ nghiêm trọng (Blocker/Major/Minor), độ ưu tiên sửa, hình ảnh bằng chứng và người chịu trách nhiệm. |
| `DOC-TEST-006` | **User Acceptance Testing (UAT) Plan** | `.docx` | Kế hoạch để khách hàng hoặc người dùng thực tế trực tiếp vào trải nghiệm và xác nhận nghiệm thu phần mềm trước khi bàn giao. |
| `DOC-TEST-007` | **Code Review Checklist & Guidelines** | `.docx` | Bảng tiêu chí kiểm tra chéo mã nguồn giữa các lập trình viên: cú pháp, logic xử lý, chống tràn bộ nhớ, lỗ hổng bảo mật (SQL Injection, XSS). |
| `DOC-TEST-008` | **Quality Assurance Metrics Report** | `.docx` | Báo cáo các chỉ số chất lượng định lượng: mật độ lỗi/KLOC, tỷ lệ lỗi phát hiện sớm, nợ kỹ thuật (Technical Debt) và thời gian trung bình sửa một lỗi (MTTR). |

---

### NHÓM E: Vận Hành, Bàn Giao & Triển Khai (13 Loại Tài Liệu)
*Tham chiếu: **ISO 21500** (Tiêu chuẩn quản lý dự án quốc tế).*

| Mã Tài Liệu | Tên Tài Liệu | Định Dạng | Tài Liệu Này Là Gì & Dùng Để Làm Gì? |
| :--- | :--- | :---: | :--- |
| `DOC-DEL-001` | **Project Master Schedule** *(Lịch trình tổng thể)* | `.xlsx` | Bảng tiến độ tổng thể của dự án biểu diễn dưới dạng biểu đồ Gantt, mốc bàn giao (Milestones) và đường găng (Critical Path). |
| `DOC-DEL-002` | **Work Breakdown Structure (WBS)** | `.xlsx` | Cấu trúc phân tách toàn bộ khối lượng công việc của dự án thành các gói công việc (Work Packages) nhỏ theo dạng phân cấp hình cây. |
| `DOC-DEL-003` | **Risk Register & Management Plan** | `.xlsx` | Bảng nhận diện và theo dõi các rủi ro có thể xảy ra trong dự án, chấm điểm mức độ thiệt hại/xác suất và lập phương án phòng ngừa/xử lý. |
| `DOC-DEL-004` | **Project Issue Log** *(Nhật ký vấn đề phát sinh)* | `.xlsx` | Sổ theo dõi các sự cố đã thực sự xảy ra trong dự án, người chịu trách nhiệm giải quyết và thời hạn phải khắc phục xong. |
| `DOC-DEL-005` | **Project Decision Log** *(Nhật ký quyết định)* | `.docx` | Lưu lại mọi quyết định quan trọng đã được thống nhất giữa Khách hàng, PM và Team kỹ thuật (tránh việc sau này tranh cãi hoặc quên mất lý do). |
| `DOC-DEL-006` | **Change Request Form & Log** *(Phiếu yêu cầu thay đổi)* | `.docx` | Quy trình quản lý thay đổi phạm vi: biểu mẫu ghi nhận yêu cầu thay đổi của khách hàng, đánh giá tác động đến chi phí và thời gian giao hàng. |
| `DOC-DEL-007` | **Meeting Minutes** *(Biên bản cuộc họp)* | `.docx` | Mẫu biên bản họp chuẩn: ghi rõ thời gian, địa điểm, thành phần tham gia, nội dung thảo luận chính, kết luận và danh sách việc cần làm (Action Items). |
| `DOC-DEL-008` | **Project Progress & Status Report** | `.docx` | Báo cáo tình hình sức khỏe dự án định kỳ (tuần/tháng) gửi cấp quản lý: tiến độ thực tế, chi phí đã tiêu, rủi ro mới và kế hoạch giai đoạn kế tiếp. |
| `DOC-DEL-009` | **Software Release Notes** *(Thông cáo phát hành)* | `.md` | Văn bản gửi kèm theo mỗi phiên bản cập nhật: thông báo các tính năng mới được bổ sung, danh sách lỗi đã được sửa và các vấn đề còn tồn tại. |
| `DOC-DEL-010` | **User Manual** *(Sách hướng dẫn sử dụng)* | `.docx` | Cẩm nang hướng dẫn người dùng cuối cách sử dụng từng tính năng của phần mềm, có hình ảnh minh họa màn hình từng bước. |
| `DOC-DEL-011` | **Installation & Operation Guide** | `.docx` | Hướng dẫn dành cho kỹ sư vận hành: các bước cài đặt hệ thống từ đầu, cấu hình biến môi trường, khởi động dịch vụ và sao lưu dự phòng. |
| `DOC-DEL-012` | **Project Handover & Sign-off Record** | `.docx` | Biên bản bàn giao chính thức: nghiệm thu toàn bộ mã nguồn, tài liệu, tài khoản hệ thống và đại diện các bên ký tên đóng dấu bàn giao. |
| `DOC-DEL-013` | **Deployment & DevOps Runbook** | `.docx` | Cẩm nang triển khai thực tế: quy trình CI/CD tự động, lệnh deploy production, quy trình khôi phục sự cố khẩn cấp (Rollback Runbook) và giám sát log. |

---

*Hệ thống tài liệu chuẩn được thiết kế để áp dụng cho mọi dự án phần mềm chuyên nghiệp, bài tập lớn và đồ án tốt nghiệp Capstone.*
