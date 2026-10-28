# Output Directory — Thư Mục Chứa Tài Liệu Xuất Bản

Thư mục này là nơi lưu trữ toàn bộ các sản phẩm tài liệu kỹ thuật được sinh ra bởi **Software Documentation Agent**.

---

## 1. Cấu Trúc Các Thư Mục Con
```text
output/
├── Project_Profile/
│   └── project_profile.yaml          # Hồ sơ dự án được phân tích từ codebase
├── Project_Management/              # Nhóm A: Project Charter, Scope, Stakeholders
├── Requirements/                    # Nhóm A: SRS, FRS, NFRS, Use Cases, User Stories, RTM
├── Scrum/                           # Nhóm B: Backlogs, Goals, Sprint records, DoD, DoR
├── Architecture_Design/             # Nhóm C: SAD, SDD, DB Spec, ERD, OpenAPI, ADRs
├── Testing_Quality/                 # Nhóm D: Test Plan, Test Cases, Bug Reports, Metrics
├── Delivery/                        # Nhóm E: Schedule, WBS, Risk Register, Release Notes, Guides
└── Validation_Reports/              # Báo cáo thẩm định tự động (JSON & Markdown)
```

---

## 2. Quy Cách Tệp Tin
- Mỗi tài liệu chính luôn có một tệp metadata đồng hành: `{DOC_ID}_{Name}.meta.yaml` chứa thông tin về phiên bản, tác giả, trạng thái vòng đời (`lifecycle_status`) và các liên kết truy xuất nguồn gốc (`traceability_links`).
- Không chỉnh sửa trực tiếp các tệp xuất bản nếu chưa cập nhật nguồn trong `project_profile.yaml` hoặc mẫu biểu gốc.
