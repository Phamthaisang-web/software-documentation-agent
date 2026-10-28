# RULE-DEL-012: Project Handover Rules

- **Mã quy tắc**: `RULE-DEL-012`
- **Tên quy tắc**: Formal Project Handover and Asset Transfer Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Ghi nhận việc bàn giao toàn diện tài sản phần mềm, mã nguồn, tài liệu, tài nguyên hạ tầng và trách nhiệm bảo hành/vận hành giữa các bên.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-012`.

## 3. Nguồn tiêu chuẩn
- ISO 21500:2021 Clause 6.8 (Project Closeout & Asset Transfer)

## 4. Đầu vào bắt buộc
Danh mục tài sản bàn giao, danh sách bên bàn giao và bên nhận, tóm tắt kết quả nghiệm thu, cam kết bảo hành và hỗ trợ.

## 5. Cấu trúc trường bắt buộc
Thông tin bàn giao & Các bên liên quan, Danh mục tài sản bàn giao (Mã nguồn, Tài liệu, Môi trường, Tài khoản quản trị), Tóm tắt nghiệm thu, Các hạng mục tồn đọng & Điều khoản bảo hành, Xác nhận bàn giao chính thức.

## 6. Quy tắc nội dung
1. Tuyệt đối không tự tạo biên bản bàn giao có chữ ký giả khi chưa có sự thống nhất giữa hai bên.
2. Danh mục tài sản phải kiểm kê đầy đủ: Đường dẫn kho mã nguồn (Git repo), các tài liệu kỹ thuật, quyền quản trị cloud/hosting, tên miền.
3. Ghi rõ thời gian bảo hành và cam kết hỗ trợ sau bàn giao (nếu có).

## 7. Tiêu chí chất lượng
Danh mục tài sản kiểm kê đầy đủ, không thiếu sót thành phần cốt lõi.

## 8. Quy tắc đặt tên
`DOC-DEL-012_Project_Handover_Report.docx`.

## 9. Truy xuất nguồn gốc
Dựa trên `DOC-TEST-006` (UAT) và tổng kết toàn bộ dự án.

## 10. Cách kiểm tra
Kiểm tra sự hiện diện của danh mục tài sản và xác nhận giữa hai bên.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ: Bàn giao quyền sở hữu repository `github.com/org/repo` và tài khoản AWS quản trị cho đại diện khách hàng.
- Không hợp lệ: Tự ý tuyên bố bàn giao hoàn tất trong khi khách hàng chưa nhận mã nguồn.

## 13. Tài liệu liên quan
`DOC-PM-001`, `DOC-TEST-006`.

## 14. Bằng chứng cần thiết
Văn bản bàn giao có chữ ký của đại diện có thẩm quyền hai bên.

## 15. Giới hạn đã biết
Không có.
