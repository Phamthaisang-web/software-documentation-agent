# RULE-GLOB-009: Naming Conventions Rules (Quy Tắc Đặt Tên Chuẩn Hóa)

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
