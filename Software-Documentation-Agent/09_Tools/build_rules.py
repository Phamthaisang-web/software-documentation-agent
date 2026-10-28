import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_DIR = os.path.join(BASE_DIR, "01_Rules")

def write_rule_file(rel_dir, filename, content):
    target_dir = os.path.join(RULES_DIR, rel_dir)
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, filename)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {rel_dir}/{filename}")

# ==============================================================================
# GLOBAL RULES (11 files)
# ==============================================================================

write_rule_file("Global", "Global_Rules.md", """# RULE-GLOB-001: General Operating Principles (Nguyên Tắc Hoạt Động Chung)

- **Mã quy tắc**: `RULE-GLOB-001`
- **Tên quy tắc**: General Operating Principles for Software Documentation
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định các nguyên tắc hoạt động tối cao, bắt buộc áp dụng xuyên suốt hệ thống Software Documentation Agent nhằm đảm bảo tính chân thực, chính xác và có thể kiểm chứng của mọi tài liệu kỹ thuật.

## 2. Phạm vi áp dụng
Áp dụng cho toàn bộ các module phân tích dự án, tạo tài liệu, cập nhật tài liệu và kiểm thử chất lượng trong hệ thống.

## 3. Nguồn tiêu chuẩn hoặc chính sách
- ISO/IEC/IEEE 29148:2018 (Requirements engineering processes)
- ISO/IEC/IEEE 42010:2022 (Architecture description)
- The Scrum Guide (Nov 2020)
- ISO/IEC/IEEE 29119 (Software testing series)

## 4. Đầu vào bắt buộc
- Bằng chứng thực tế từ mã nguồn (source code files)
- Cấu hình dự án (package manifests, environment configs, dockerfiles)
- Lược đồ cơ sở dữ liệu (migrations, schemas, models)
- Báo cáo và log thực thi kiểm thử thực tế

## 5. Cấu trúc tài liệu hoặc trường dữ liệu bắt buộc
Mỗi tài liệu sinh ra phải có:
- Định danh tài liệu chuẩn `document_id`
- Phiên bản (`version`) và ngày cập nhật (`updated_at`)
- Trạng thái xác minh của từng mục (`VERIFIED`, `INFERRED`, `UNKNOWN`, `CONFLICT`)
- Tham chiếu bằng chứng cụ thể (`evidence_refs`)

## 6. Quy tắc nội dung
1. Luôn phân tích dự án kỹ lưỡng trước khi sinh bất kỳ tài liệu nào.
2. Ưu tiên tuyệt đối bằng chứng từ mã nguồn, tệp cấu hình, cơ sở dữ liệu, API route và kết quả kiểm thử.
3. Không tự bịa đặt tính năng, yêu cầu, vai trò, kiến trúc, công nghệ, số liệu đo lường hoặc kết quả kiểm thử.
4. Không tự xác nhận một tính năng là hoàn thành (Done) chỉ vì tìm thấy một đoạn mã nguồn liên quan.
5. Không tự xác nhận phần mềm hoạt động tốt chỉ vì mã nguồn biên dịch thành công.
6. Không tự tạo thông tin phê duyệt, chữ ký, ngày họp, thành phần tham dự khi chưa có biên bản thực tế.
7. Không nhầm lẫn giữa tiêu chuẩn chính thức (Official Standard), quy định nội bộ (Internal Policy) và đề xuất của AI (Recommendation).
8. Không tự ý sửa đổi các quyết định đã được người dùng phê duyệt trước đó.
9. Không ghi đè trực tiếp lên mẫu gốc (original template) do người dùng cung cấp.
10. Đánh dấu rõ các mục thiếu thông tin là `UNKNOWN` hoặc `TBD`.

## 7. Tiêu chí chất lượng
- Tính xác thực (Authenticity): 100% dữ liệu quan trọng có nguồn gốc rõ ràng.
- Tính nhất quán (Consistency): Không mâu thuẫn giữa các tài liệu trong cùng một bộ.
- Tính đầy đủ (Completeness): Đầy đủ các mục bắt buộc theo registry.

## 8. Quy tắc mã định danh và đặt tên
- Mã tài liệu: `DOC-{NHOM}-{SO}` (ví dụ: `DOC-REQ-001`)
- Mã yêu cầu: `REQ-{LOAI}-{SO}` (ví dụ: `REQ-FUNC-001`)
- Mã ca kiểm thử: `TC-{MODULE}-{SO}` (ví dụ: `TC-AUTH-001`)

## 9. Quy tắc truy xuất nguồn gốc
Mọi yêu cầu phải liên kết hai chiều từ Vision -> Backlog -> Design -> Test Case -> Release Note.

## 10. Cách kiểm tra
- Chạy công cụ kiểm tra tự động `validator.py` kiểm tra `evidence_refs`.
- Kiểm tra tính hợp lệ của schema `document_metadata.schema.json`.

## 11. Ngoại lệ và điều kiện áp dụng
Không có ngoại lệ đối với việc cấm bịa đặt thông tin.

## 12. Ví dụ hợp lệ và không hợp lệ
- **Hợp lệ**: "Hệ thống sử dụng JWT token cho xác thực API dựa trên khai báo trong `src/middleware/auth.ts:25`."
- **Không hợp lệ**: "Hệ thống đạt 99.99% uptime và chịu tải 10,000 req/s" (trong khi mã nguồn không có bất kỳ cấu hình cluster, benchmark hay cam kết SLA nào).

## 13. Tài liệu liên quan
Tất cả 59 tài liệu trong danh mục.

## 14. Bằng chứng cần thiết
Đường dẫn tệp, số dòng, commit hash hoặc cấu hình hệ thống.

## 15. Giới hạn đã biết
Agent không thể suy đoán các thỏa thuận miệng của ban lãnh đạo nếu không có ghi chép bằng văn bản.
""")

write_rule_file("Global", "Source_Verification_Rules.md", """# RULE-GLOB-002: Source Verification Rules (Quy Tắc Xác Minh Nguồn Tham Chiếu)

- **Mã quy tắc**: `RULE-GLOB-002`
- **Tên quy tắc**: Source Verification and Integrity Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Quy định quy chuẩn xác minh nguồn tham khảo, phân loại thẩm quyền của nguồn và ngăn chặn trích dẫn giả mạo.

## 2. Phạm vi áp dụng
Mọi tài liệu, chuẩn kỹ thuật, đường dẫn URL hoặc chính sách được tham chiếu trong tài liệu dự án.

## 3. Nguồn tiêu chuẩn hoặc chính sách
- Chính sách kiểm tra nguồn: `02_Standards/source_verification_policy.md`
- Danh mục chuẩn: `config/standards_registry.yaml`

## 4. Đầu vào bắt buộc
- Bản ghi nguồn (`source_reference`) gồm: `source_id`, `source_name`, `url`, `version`, `verification_status`.

## 5. Cấu trúc trường dữ liệu bắt buộc
- `verification_status` bắt buộc phải là một trong các giá trị:
  - `VERIFIED_OFFICIAL`
  - `VERIFIED_AUTHORITATIVE`
  - `USER_PROVIDED`
  - `INTERNAL_POLICY`
  - `UNVERIFIED`
  - `UNAVAILABLE`
  - `SUPERSEDED`

## 6. Quy tắc nội dung
1. Luôn ưu tiên trang chính thức của tổ chức ban hành tiêu chuẩn hoặc tác giả gốc.
2. Kiểm tra phiên bản, phạm vi áp dụng và tình trạng hiệu lực trước khi gán nhãn `VERIFIED_OFFICIAL`.
3. Không tự bịa đặt URL, mã điều khoản, số trang hoặc nội dung trích dẫn.
4. Nếu chỉ tiếp cận được phần tóm tắt của tiêu chuẩn có bản quyền trả phí, phải ghi rõ giới hạn đó, không tuyên bố đã đọc toàn văn.
5. Phân biệt nội dung bắt buộc của tiêu chuẩn với tài liệu hướng dẫn triển khai phụ trợ.
6. Không sao chép trái phép toàn bộ nội dung tiêu chuẩn thương mại có bản quyền.
7. Nếu không kiểm tra được nguồn mới nhất, phải công khai hạn chế trong báo cáo.

## 7. Tiêu chí chất lượng
100% các tiêu chuẩn chính thức có URL hợp lệ trỏ tới tên miền của tổ chức ban hành.

## 8. Quy tắc mã định danh
Định danh nguồn: `STD-{LINH_VUC}-{MA}` (ví dụ: `STD-SCRUM-2020`, `STD-REQ-29148`).

## 9. Quy tắc truy xuất nguồn gốc
Mỗi `document_record` trong `document_registry.yaml` phải trỏ đến các `source_id` hợp lệ trong `standards_registry.yaml`.

## 10. Cách kiểm tra
Chạy bài kiểm thử tự động `test_source_registry.py` để quét trạng thái và định dạng nguồn.

## 11. Ngoại lệ và điều kiện áp dụng
Tài liệu nội bộ dự án không có URL công khai thì ghi nhận đường dẫn tệp trong workspace.

## 12. Ví dụ hợp lệ và không hợp lệ
- **Hợp lệ**: `STD-SCRUM-2020` trỏ tới `https://scrumguides.org/scrum-guide.html` (VERIFIED_OFFICIAL).
- **Không hợp lệ**: Trỏ tới blog cá nhân nhưng gán nhãn `VERIFIED_OFFICIAL` cho Scrum Guide.

## 13. Tài liệu liên quan
Tất cả các tài liệu thuộc Nhóm A, B, C, D, E.

## 14. Bằng chứng cần thiết
URL hợp lệ hoặc tệp nội bộ đã xác minh.

## 15. Giới hạn đã biết
Một số tiêu chuẩn ISO cần tài khoản trả phí để tải toàn văn; hệ thống chỉ thẩm định qua danh mục chính thức của ISO.org.
""")

write_rule_file("Global", "Document_Registry_Rules.md", """# RULE-GLOB-003: Document Registry Rules (Quy Tắc Quản Lý Danh Mục Tài Liệu)

- **Mã quy tắc**: `RULE-GLOB-003`
- **Tên quy tắc**: Document Registry Management and Integrity Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Đảm bảo toàn bộ 59 loại tài liệu phần mềm được khai báo đầy đủ, chuẩn xác, không trùng lặp và có cấu trúc liên kết hoàn chỉnh.

## 2. Phạm vi áp dụng
Áp dụng cho tệp trung tâm `config/document_registry.yaml`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Project Governance)
- ISO/IEC/IEEE 29148:2018 (Information Items)

## 4. Đầu vào bắt buộc
Tệp cấu hình `config/document_registry.yaml`.

## 5. Cấu trúc trường bắt buộc
Mỗi bản ghi tài liệu phải có: `document_id`, `official_name`, `group`, `purpose`, `applicability`, `required_inputs`, `output_formats`, `rule_references`, `preferred_template_id`, `related_standards`, `required_sections`, `validation_profile`.

## 6. Quy tắc nội dung
1. Tuyệt đối không trùng lặp `document_id`.
2. Đầy đủ cả 5 nhóm tài liệu (Nhóm A: Quản lý & Yêu cầu, Nhóm B: Scrum, Nhóm C: Kiến trúc & Thiết kế, Nhóm D: Kiểm thử & Chất lượng, Nhóm E: Bàn giao & Theo dõi).
3. Đủ tối thiểu 59 loại tài liệu theo quy định.
4. Mọi `preferred_template_id` phải tồn tại trong `template_registry.yaml`.
5. Mọi `rule_references` phải trỏ tới tệp Rules thực tế tồn tại trong `01_Rules/`.
6. Mọi `related_standards` phải tồn tại trong `standards_registry.yaml`.

## 7. Tiêu chí chất lượng
100% tài liệu vượt qua kiểm tra JSON schema `document_record.schema.json`.

## 8. Quy tắc mã định danh
Mã tài liệu phải tuân thủ regex `^DOC-[A-Z]+-[0-9]{3}$`.

## 9. Quy tắc truy xuất nguồn gốc
Trường `dependencies` và `traceability_requirements` phải trỏ tới các `document_id` hợp lệ.

## 10. Cách kiểm tra
Chạy bài kiểm thử `test_document_registry.py`.

## 11. Ngoại lệ
Không có ngoại lệ.

## 12. Ví dụ hợp lệ và không hợp lệ
- **Hợp lệ**: `DOC-REQ-001` trỏ đến `SRS_Rules.md` và `TPL-REQ-001`.
- **Không hợp lệ**: `DOC-REQ-001` trỏ đến `None` hoặc rule file không tồn tại.

## 13. Tài liệu liên quan
59 tài liệu trong hệ thống.

## 14. Bằng chứng cần thiết
Tệp `config/document_registry.yaml`.

## 15. Giới hạn đã biết
Không có.
""")

write_rule_file("Global", "Document_Formatting_Rules.md", """# RULE-GLOB-004: Document Formatting Rules (Quy Tắc Định Dạng Tài Liệu)

- **Mã quy tắc**: `RULE-GLOB-004`
- **Tên quy tắc**: Document Formatting and Template Preservation Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Đảm bảo khi xuất bản tài liệu trên các mẫu biểu (DOCX, XLSX, PPTX, MD, YAML, MMD), định dạng gốc, thẩm mỹ và tính toàn vẹn kỹ thuật được giữ nguyên vẹn.

## 2. Phạm vi áp dụng
Mọi thao tác render và xuất bản tài liệu ra thư mục `output/`.

## 3. Nguồn tiêu chuẩn
- Microsoft OpenXML Specification (ISO/IEC 29500)
- OpenAPI Specification 3.1.0
- Mermaid.js Syntax Specification

## 4. Đầu vào bắt buộc
Tệp mẫu nguồn từ `03_Templates/` hoặc do người dùng cung cấp.

## 5. Cấu trúc bắt buộc
- **DOCX**: Giữ nguyên Styles, Header, Footer, Table Grid, Font Family.
- **XLSX**: Giữ nguyên Worksheets, Header color (#1F497D), Freeze Panes, AutoFilter, Formulas.
- **Mermaid**: Cú pháp sơ đồ hợp lệ, lưu trữ mã nguồn để người dùng chỉnh sửa được.

## 6. Quy tắc nội dung
1. Với Word (DOCX): Thay thế placeholder (ví dụ `{{PROJECT_NAME}}`), không xóa bảng, không làm lệch trang.
2. Với Excel (XLSX): Không ghi đè công thức tính toán (`SUM`, `AVERAGE`) bằng giá trị tĩnh.
3. Với Markdown / YAML / JSON: Cú pháp hợp lệ, validate được bằng parser tương ứng.
4. Không được tuyên bố giữ nguyên định dạng nếu chưa chạy kiểm tra tệp thực tế.

## 7. Tiêu chí chất lượng
Các tệp sinh ra mở được bằng Microsoft Office / LibreOffice / VS Code mà không có cảnh báo corrupt.

## 8. Quy tắc đặt tên
Tên tệp không dấu, sử dụng dấu gạch dưới: `{DOC_ID}_{Document_Name}.{ext}`.

## 9. Truy xuất nguồn gốc
Lưu kèm tệp `{DOC_ID}.meta.yaml` ghi nhận template gốc được sử dụng.

## 10. Cách kiểm tra
Chạy bài kiểm thử `test_template_preservation.py`.

## 11. Ngoại lệ
Nếu định dạng tệp không được hỗ trợ xử lý sâu (ví dụ binary proprietary), phải ghi nhận rõ hạn chế.

## 12. Ví dụ
- Hợp lệ: Giữ nguyên công thức `=SUM(E2:E20)` trong bảng chấm công / burndown Excel.
- Không hợp lệ: Xóa công thức và gõ cứng số `50`.

## 13. Tài liệu liên quan
Tất cả các tài liệu định dạng `.docx`, `.xlsx`, `.md`, `.yaml`, `.mmd`.

## 14. Bằng chứng cần thiết
Tệp đầu ra có thể mở và đọc thành công.

## 15. Giới hạn đã biết
Không thể kiểm tra trực quan giao diện đồ họa nếu môi trường thiếu Word viewer; kiểm tra cấu trúc XML bên trong.
""")

write_rule_file("Global", "Quality_Rules.md", """# RULE-GLOB-005: Quality Rules (Quy Tắc Chất Lượng Nội Dung)

- **Mã quy tắc**: `RULE-GLOB-005`
- **Tên quy tắc**: Documentation Quality & Precision Criteria
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Xác lập các tiêu chí chất lượng kỹ thuật bắt buộc cho toàn bộ nội dung tài liệu phần mềm.

## 2. Phạm vi áp dụng
Toàn bộ văn bản và dữ liệu được tạo ra trong tài liệu.

## 3. Nguồn tiêu chuẩn
- ISO/IEC 25010:2023 (Systems and software quality models)
- ISO/IEC/IEEE 29148:2018 (Requirements quality criteria)

## 4. Đầu vào bắt buộc
Nội dung tài liệu được sinh ra.

## 5. Cấu trúc bắt buộc
Mỗi mệnh đề yêu cầu kỹ thuật phải rõ ràng, đo lường được, có thể kiểm chứng được.

## 6. Quy tắc nội dung
1. Tính rõ ràng (Unambiguous): Không dùng các từ mơ hồ như "nhanh chóng", "thân thiện", "tối ưu" mà không có chỉ số cụ thể.
2. Tính kiểm chứng được (Verifiable): Mỗi yêu cầu phải có phương pháp kiểm thử hoặc tiêu chí nghiệm thu rõ ràng.
3. Tính nhất quán (Consistent): Không có hai điều khoản mâu thuẫn nhau trong tài liệu.
4. Tính khả thi (Feasible): Phù hợp với năng lực công nghệ và phạm vi dự án.
5. Không gán nhãn PASS cho các mục chưa được kiểm thử thực tế.

## 7. Tiêu chí chất lượng
100% các tiêu chí chất lượng được đánh giá trước khi phát hành.

## 8. Mã định danh
Quy định chất lượng: `RULE-GLOB-005`.

## 9. Truy xuất nguồn gốc
Liên kết với `06_Validation/content_validation_rules.md`.

## 10. Cách kiểm tra
Sử dụng công cụ `validator.py`.

## 11. Ngoại lệ
Tài liệu phác thảo giai đoạn đầu (DRAFT) có thể có một số mục TBD.

## 12. Ví dụ
- Hợp lệ: "Thời gian phản hồi của API `/login` phải <= 200ms với 100 concurrent requests."
- Không hợp lệ: "API đăng nhập phải chạy cực kỳ nhanh."

## 13. Tài liệu liên quan
Tất cả các tài liệu yêu cầu và kiến trúc.

## 14. Bằng chứng cần thiết
Báo cáo kiểm thử hoặc benchmark đo đạc cụ thể.

## 15. Giới hạn đã biết
Không có.
""")

write_rule_file("Global", "Traceability_Rules.md", """# RULE-GLOB-006: Traceability Rules (Quy Tắc Truy Xuất Nguồn Gốc)

- **Mã quy tắc**: `RULE-GLOB-006`
- **Tên quy tắc**: Bidirectional Requirements and Artifacts Traceability
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định cơ chế theo dõi mối liên kết hai chiều giữa các thành phần tài liệu xuyên suốt vòng đời phát triển phần mềm.

## 2. Phạm vi áp dụng
Mọi thực thể: Yêu cầu, Ca sử dụng, Thiết kế, Quyết định kiến trúc, PBI, Ca kiểm thử, Lỗi, Ghi chú phát hành.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 (Requirements Traceability)
- ISO/IEC/IEEE 29119-3:2021 (Test Traceability)

## 4. Đầu vào bắt buộc
Danh sách định danh thực thể: `REQ-*`, `PBI-*`, `ARCH-*`, `TC-*`, `BUG-*`, `REL-*`.

## 5. Cấu trúc trường bắt buộc
Mỗi thực thể phải lưu trữ danh sách `parent_refs` và `child_refs`.

## 6. Quy tắc nội dung
1. Mọi Functional Requirement (`REQ-FUNC-xxx`) phải có ít nhất một Test Case (`TC-xxx`) kiểm chứng.
2. Không cho phép mồ côi (Orphan Item): Không tạo Test Case không gắn với yêu cầu hay PBI nào.
3. Không tham chiếu đến ID không tồn tại (Broken link).
4. Chuỗi truy xuất mẫu:
   `Product Vision -> Product Goal -> Product Backlog -> PBI -> Acceptance Criteria -> Test Case -> Test Execution -> Release Notes`.

## 7. Tiêu chí chất lượng
Độ bao phủ truy xuất đạt 100% đối với các yêu cầu chức năng cốt lõi.

## 8. Quy tắc đặt tên
Định dạng mã: `REQ-[LOAI]-[SO]`, `TC-[MODULE]-[SO]`.

## 9. Truy xuất nguồn gốc
Tài liệu `DOC-REQ-007` (RTM) là trung tâm thể hiện ma trận truy xuất.

## 10. Cách kiểm tra
Chạy bài kiểm thử tự động `test_traceability.py`.

## 11. Ngoại lệ
Các yêu cầu phi chức năng cấp hệ thống (NFR) có thể liên kết trực tiếp tới quyết định kiến trúc (`DOC-ARCH-010`).

## 12. Ví dụ
- Hợp lệ: `TC-AUTH-001` kiểm chứng cho `REQ-FUNC-001` (User Login).
- Không hợp lệ: `TC-MISC-999` kiểm chứng cho `REQ-9999` (ID không tồn tại).

## 13. Tài liệu liên quan
`DOC-REQ-001`, `DOC-REQ-007`, `DOC-TEST-003`, `DOC-DEL-009`.

## 14. Bằng chứng cần thiết
Bảng ma trận truy xuất nguồn gốc RTM.

## 15. Giới hạn đã biết
Không tự động phát hiện được liên kết logic nếu người dùng không gán ID.
""")

write_rule_file("Global", "Version_Control_Rules.md", """# RULE-GLOB-007: Version Control Rules (Quy Tắc Quản Lý Phiên Bản)

- **Mã quy tắc**: `RULE-GLOB-007`
- **Tên quy tắc**: Document Versioning and Change Tracking Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định chuẩn quản lý phiên bản cho toàn bộ tài liệu kỹ thuật nhằm đảm bảo khả năng theo dõi lịch sử và tính nhất quán với mã nguồn.

## 2. Phạm vi áp dụng
Mọi tài liệu được tạo hoặc cập nhật trong hệ thống.

## 3. Nguồn tiêu chuẩn
- Semantic Versioning 2.0.0 (SemVer)
- ISO 21500:2021 (Configuration & Document Management)

## 4. Đầu vào bắt buộc
Trường `version` dạng `MAJOR.MINOR.PATCH`.

## 5. Cấu trúc trường bắt buộc
Bảng lịch sử thay đổi (Changelog / Revision History) ở đầu mỗi tài liệu: `Version`, `Date`, `Author`, `Description of Change`, `Approver`.

## 6. Quy tắc nội dung
1. Phiên bản khởi tạo ban đầu là `1.0.0` (hoặc `0.1.0` nếu là bản nháp).
2. Tăng `MAJOR` khi có thay đổi lớn làm thay đổi cấu trúc hoặc phạm vi cốt lõi.
3. Tăng `MINOR` khi thêm tính năng, phần mới mà không phá vỡ cấu trúc cũ.
4. Tăng `PATCH` khi sửa lỗi chính tả, làm rõ câu từ hoặc sửa định dạng nhỏ.
5. Không sửa đổi nội dung mà giữ nguyên phiên bản cũ.

## 7. Tiêu chí chất lượng
100% tài liệu có lịch sử thay đổi rõ ràng.

## 8. Quy tắc đặt tên
`v{MAJOR}.{MINOR}.{PATCH}`.

## 9. Truy xuất nguồn gốc
Ghi nhận trong metadata `{DOC_ID}.meta.yaml`.

## 10. Cách kiểm tra
Kiểm tra cấu trúc header của tài liệu.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Cập nhật thêm 2 API endpoint -> tăng từ `1.0.0` lên `1.1.0`.
- Không hợp lệ: Thay đổi toàn bộ kiến trúc từ Monolith sang Microservices nhưng vẫn để `1.0.0`.

## 13. Tài liệu liên quan
Tất cả 59 tài liệu.

## 14. Bằng chứng cần thiết
Bảng revision history trong tài liệu.

## 15. Giới hạn đã biết
Không có.
""")

write_rule_file("Global", "Privacy_And_Security_Rules.md", """# RULE-GLOB-008: Privacy and Security Rules (Quy Tắc Bảo Mật và Quyền Riêng Tư)

- **Mã quy tắc**: `RULE-GLOB-008`
- **Tên quy tắc**: Confidentiality, Secret Sanitization and Data Protection Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Ngăn chặn tuyệt đối việc lộ lọt thông tin nhạy cảm, thông tin bí mật, khóa truy cập (API keys, passwords, private keys) trong tài liệu kỹ thuật.

## 2. Phạm vi áp dụng
Toàn bộ mã nguồn, tệp cấu hình và tài liệu được phân tích và tạo ra.

## 3. Nguồn tiêu chuẩn
- OWASP Top 10:2021 (A07: Identification and Authentication Failures)
- ISO/IEC 27001:2022 (Information Security Management)

## 4. Đầu vào bắt buộc
Quá trình quét và lọc văn bản trước khi đưa vào tài liệu.

## 5. Cấu trúc trường bắt buộc
Cơ chế mặt nạ (Masking / Redaction): Các chuỗi nhạy cảm phải được thay bằng `[REDACTED_API_KEY]`, `[REDACTED_SECRET]`, `********`.

## 6. Quy tắc nội dung
1. Tuyệt đối không sao chép API key, secret token, private SSH key, password vào tài liệu.
2. Không lưu trữ thông tin cá nhân (PII) thật của khách hàng vào tài liệu ví dụ (sử dụng dữ liệu giả lập như `user@example.com`).
3. Không thực thi tự động các tệp script lạ hoặc lệnh không đáng tin cậy tìm thấy trong repository.
4. Không gửi dữ liệu mã nguồn độc quyền ra các dịch vụ ngoài khi chưa được phép.

## 7. Tiêu chí chất lượng
Zero secret leakage: Không có bất kỳ credential nào tồn tại trong thư mục `output/`.

## 8. Quy tắc đặt tên
Pattern nhận diện secret: `.*(api[_-]?key|secret|password|token|private[_-]?key).*`.

## 9. Truy xuất nguồn gốc
Ghi nhận trong báo cáo thẩm định an toàn bảo mật.

## 10. Cách kiểm tra
Bộ lọc regex quét credential trong engine kiểm tra.

## 11. Ngoại lệ
Các giá trị giả lập mẫu trong hướng dẫn (ví dụ: `password: "example_password_123"`) phải được đánh dấu rõ là ví dụ minh họa.

## 12. Ví dụ
- Hợp lệ: `Authorization: Bearer <USER_JWT_TOKEN>`
- Không hợp lệ: `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR...` (token thật).

## 13. Tài liệu liên quan
`DOC-ARCH-005` (API Spec), `DOC-DEL-011` (Install Guide), `DOC-DEL-013` (Deployment Guide).

## 14. Bằng chứng cần thiết
Báo cáo kiểm tra secret scanning sạch.

## 15. Giới hạn đã biết
Các khóa mã hóa được obfuscate phức tạp có thể cần cấu hình regex chuyên biệt.
""")

write_rule_file("Global", "Naming_Conventions_Rules.md", """# RULE-GLOB-009: Naming Conventions Rules (Quy Tắc Đặt Tên Chuẩn Hóa)

- **Mã quy tắc**: `RULE-GLOB-009`
- **Tên quy tắc**: Standard Identifier and File Naming Conventions
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Chuẩn hóa toàn diện quy ước đặt tên cho tệp tin, mã định danh yêu cầu, mã kiểm thử và các thành phần kỹ thuật.

## 2. Phạm vi áp dụng
Mọi tệp tin, ID và tiêu đề trong hệ thống tài liệu.

## 3. Nguồn tiêu chuẩn
- ISO 21500 (Project Management Naming)
- POSIX Portable Filename Standards

## 4. Đầu vào bắt buộc
Tên tệp và các định danh.

## 5. Cấu trúc trường bắt buộc
Quy ước định danh:
- Tài liệu: `DOC-{GROUP}-{NUMBER}` (ví dụ: `DOC-PM-001`, `DOC-SCRUM-007`)
- Yêu cầu chức năng: `REQ-FUNC-{NUMBER}`
- Yêu cầu phi chức năng: `REQ-NF-{CATEGORY}-{NUMBER}`
- User Story: `US-{MODULE}-{NUMBER}`
- Ca kiểm thử: `TC-{MODULE}-{NUMBER}`
- Lỗi/Defect: `BUG-{NUMBER}`
- Quyết định kiến trúc: `ADR-{NUMBER}`

## 6. Quy tắc nội dung
1. Tên tệp tin không chứa dấu tiếng Việt, không chứa khoảng trắng, dùng gạch dưới `_` hoặc gạch ngang `-`.
2. Tên tệp đầu ra tuân thủ định dạng: `{DOC_ID}_{Ten_Tai_Lieu}.{ext}`.
3. Không đặt tên tệp tùy tiện như `tailieu1.docx`, `final_final.xlsx`.

## 7. Tiêu chí chất lượng
100% tệp tin và ID tuân thủ quy tắc regex đã định nghĩa.

## 8. Quy tắc đặt tên
Xem mục 5.

## 9. Truy xuất nguồn gốc
Hỗ trợ ánh xạ ID chính xác trên toàn hệ thống.

## 10. Cách kiểm tra
Kiểm tra tự động qua `validator.py`.

## 11. Ngoại lệ
Mẫu do người dùng cung cấp có thể giữ nguyên tên tệp gốc của người dùng.

## 12. Ví dụ
- Hợp lệ: `DOC-ARCH-001_Software_Architecture_Description.docx`
- Không hợp lệ: `Kien truc phan mem final 2.docx`

## 13. Tài liệu liên quan
Toàn bộ hệ thống.

## 14. Bằng chứng cần thiết
Danh sách file trong `output/`.

## 15. Giới hạn đã biết
Không có.
""")

write_rule_file("Global", "Conflict_Resolution_Rules.md", """# RULE-GLOB-010: Conflict Resolution Rules (Quy Tắc Giải Quyết Mâu Thuẫn)

- **Mã quy tắc**: `RULE-GLOB-010`
- **Tên quy tắc**: Information Conflict Detection and Resolution Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `CRITICAL`

## 1. Mục đích
Quy định nguyên tắc phát hiện và thứ tự ưu tiên xử lý khi có sự mâu thuẫn giữa các nguồn thông tin trong dự án.

## 2. Phạm vi áp dụng
Khi phân tích dự án và đối chiếu giữa mã nguồn, tài liệu cũ, cấu hình và phản hồi của người dùng.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 29148:2018 (Conflict Resolution in Requirements)

## 4. Đầu vào bắt buộc
Hai hay nhiều nguồn dữ liệu cung cấp thông tin trái ngược nhau về cùng một tính năng hoặc thông số.

## 5. Cấu trúc trường bắt buộc
Bản ghi mâu thuẫn: `topic`, `source_a`, `source_b`, `conflict_description`, `resolution_status`.

## 6. Quy tắc nội dung (Thứ tự ưu tiên giải quyết)
1. **Xác nhận trực tiếp từ người dùng (User Confirmation)**: Có quyền quyết định cao nhất đối với định hướng nghiệp vụ.
2. **Mã nguồn và cấu hình thực tế đang chạy (Running Code & Config)**: Được ưu tiên hơn tài liệu mô tả cũ chưa cập nhật.
3. **Tiêu chuẩn chính thức (Official Standards)**: Được ưu tiên hơn thông lệ không chính thức khi xác định các ràng buộc quy trình (ví dụ: Timebox Scrum).
4. Khi phát hiện mâu thuẫn không thể tự giải quyết an toàn, hệ thống phải ghi nhãn `CONFLICT` và đưa vào danh sách câu hỏi cần làm rõ, không được tự ý thiên vị một bên.

## 7. Tiêu chí chất lượng
Mọi mâu thuẫn được ghi nhận minh bạch, không âm thầm giấu diếm.

## 8. Quy tắc đặt tên
Mã mâu thuẫn: `CONF-{NUMBER}`.

## 9. Truy xuất nguồn gốc
Liên kết trong `project_profile.yaml` mục `conflicting_information`.

## 10. Cách kiểm tra
Bài kiểm thử `test_validation.py`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Xung đột: README ghi cơ sở dữ liệu là MongoDB, nhưng mã nguồn dùng Prisma với PostgreSQL -> Gắn nhãn `CONFLICT`, ưu tiên schema thực tế và hỏi người dùng.

## 13. Tài liệu liên quan
`project_profile_rules.md`, `validation_rules.md`.

## 14. Bằng chứng cần thiết
Đoạn trích từ 2 nguồn mâu thuẫn.

## 15. Giới hạn đã biết
Không tự động phán đoán được ý định tương lai của khách hàng nếu mã nguồn chưa cập nhật.
""")

write_rule_file("Global", "Document_Lifecycle_Rules.md", """# RULE-GLOB-011: Document Lifecycle Rules (Quy Tắc Vòng Đời Tài Liệu)

- **Mã quy tắc**: `RULE-GLOB-011`
- **Tên quy tắc**: Document Lifecycle and State Transition Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `MAJOR`

## 1. Mục đích
Quy định các trạng thái và điều kiện chuyển đổi trạng thái của tài liệu từ lúc khởi tạo đến khi lưu trữ.

## 2. Phạm vi áp dụng
Tất cả các tài liệu kỹ thuật trong hệ thống.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 (Document and Records Control)

## 4. Đầu vào bắt buộc
Trường `lifecycle_status` trong metadata.

## 5. Cấu trúc trường bắt buộc
Trạng thái hợp lệ: `DRAFT`, `UNDER_REVIEW`, `APPROVED`, `SUPERSEDED`, `DEPRECATED`.

## 6. Quy tắc nội dung
1. Tài liệu mới sinh ra tự động có trạng thái `DRAFT` cho đến khi vượt qua bộ kiểm tra chất lượng.
2. Tài liệu chuyển sang `APPROVED` chỉ khi có xác nhận chính thức hoặc phê duyệt từ người dùng/stakeholder có thẩm quyền.
3. Tuyệt đối không tự động gán nhãn `APPROVED` khi chưa có bằng chứng phê duyệt.
4. Khi tài liệu được cập nhật phiên bản mới, phiên bản cũ chuyển sang trạng thái `SUPERSEDED`.
5. Tài liệu không còn áp dụng chuyển sang `DEPRECATED`.

## 7. Tiêu chí chất lượng
100% tài liệu có trạng thái vòng đời xác định.

## 8. Quy tắc đặt tên
Trạng thái chữ hoa chuẩn enum.

## 9. Truy xuất nguồn gốc
Theo dõi trong metadata `{DOC_ID}.meta.yaml`.

## 10. Cách kiểm tra
Kiểm tra qua schema `document_metadata.schema.json`.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Agent sinh tài liệu xong để trạng thái `DRAFT` và chờ người dùng duyệt.
- Không hợp lệ: Agent tự ý ghi "Approved by CTO John Doe" khi chưa có xác nhận.

## 13. Tài liệu liên quan
Tất cả 59 tài liệu.

## 14. Bằng chứng cần thiết
Biên bản phê duyệt hoặc xác nhận của người dùng.

## 15. Giới hạn đã biết
Không có.
""")

print("Global rules created successfully.")
