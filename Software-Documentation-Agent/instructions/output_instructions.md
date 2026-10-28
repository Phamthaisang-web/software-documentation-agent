# Output Instructions — Hướng Dẫn Định Dạng và Xuất Bản Tài Liệu

Tài liệu này quy định cấu trúc thư mục, quy ước đặt tên và tiêu chuẩn kỹ thuật cho các tệp tài liệu được tạo ra.

---

## 1. Quy Định Cấu Trúc Xuất Bản (`output/`)
Các tài liệu sinh ra được tổ chức thành cấu trúc rõ ràng:
```text
output/
├── Project_Profile/
│   └── project_profile.yaml
├── Nhóm_A_Project_Management_Requirements/
│   ├── DOC-PM-001_Project_Charter.docx
│   ├── DOC-REQ-001_SRS.docx
│   └── ...
├── Nhóm_B_Scrum/
│   ├── DOC-SCRUM-001_Product_Backlog.xlsx
│   ├── DOC-SCRUM-007_Sprint_Backlog.xlsx
│   └── ...
├── Nhóm_C_Architecture_Design/
│   ├── DOC-ARCH-001_SAD.docx
│   ├── DOC-ARCH-004_ERD.mmd
│   ├── DOC-ARCH-005_API_Specification.yaml
│   └── ...
├── Nhóm_D_Testing_Quality/
│   ├── DOC-TEST-001_Test_Plan.docx
│   ├── DOC-TEST-003_Test_Cases.xlsx
│   └── ...
├── Nhóm_E_Delivery_Tracking/
│   ├── DOC-DEL-009_Release_Notes.md
│   ├── DOC-DEL-011_Installation_Guide.md
│   └── ...
├── Metadata/
│   ├── {DOC_ID}.meta.yaml
│   └── ...
└── Validation_Reports/
    ├── validation_report.json
    └── validation_report.md
```

---

## 2. Quy Tắc Đặt Tên Tệp (Naming Conventions)
- Mẫu tên chuẩn: `{DOC_ID}_{Ten_Tai_Lieu_Khong_Dau}.{ext}`
  - Ví dụ: `DOC-PM-001_Project_Charter.docx`
  - Ví dụ: `DOC-ARCH-005_API_Specification.yaml`
  - Ví dụ: `DOC-SCRUM-001_Product_Backlog.xlsx`
- Tệp metadata đồng hành: `{DOC_ID}_{Ten_Tai_Lieu_Khong_Dau}.meta.yaml`

---

## 3. Tiêu Chuẩn Kỹ Thuật Định Dạng
- **DOCX**: Định dạng Microsoft Word OpenXML (.docx) chuẩn. Bảng có viền đầy đủ, tiêu đề in đậm, canh lề nhất quán, không có bảng biểu bị tràn trang.
- **XLSX**: Định dạng Microsoft Excel OpenXML (.xlsx). Header có màu nền xanh navy (#1F497D), chữ trắng in đậm, có border mỏng, tự động co giãn độ rộng cột, giữ nguyên các công thức tính toán.
- **Markdown (.md)**: Tuân thủ CommonMark và GitHub Flavored Markdown (GFM). Tiêu đề cấp 1 đến 3 rõ ràng, bảng biểu định dạng chuẩn, trích dẫn code có syntax highlighting.
- **Mermaid (.mmd)**: Cú pháp hợp lệ (`flowchart TD`, `erDiagram`, `sequenceDiagram`), luôn lưu tệp nguồn để người dùng có thể mở và hiệu chỉnh trên Mermaid Live Editor hoặc IDE plugin.
- **OpenAPI (.yaml)**: Hợp lệ theo chuẩn OpenAPI 3.1.0, có thể mở trực tiếp bằng Swagger Editor.
