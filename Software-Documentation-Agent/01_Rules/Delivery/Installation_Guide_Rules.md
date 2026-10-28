# RULE-DEL-011: Installation Guide Rules

- **Mã quy tắc**: `RULE-DEL-011`
- **Tên quy tắc**: Installation Environment and Command Verifiability Rules
- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`
- **Mức độ nghiêm trọng khi vi phạm**: `BLOCKER`

## 1. Mục đích
Hướng dẫn chi tiết, chính xác các bước chuẩn bị môi trường, cài đặt thư viện, cấu hình và khởi chạy ứng dụng từ mã nguồn repository.

## 2. Phạm vi áp dụng
Tài liệu `DOC-DEL-011`.

## 3. Nguồn tiêu chuẩn
- ISO/IEC/IEEE 26514:2022 (Design and development of user documentation)

## 4. Đầu vào bắt buộc
Yêu cầu tiên quyết (Prerequisites), biến môi trường mẫu (`.env.example`), lệnh cài đặt, lệnh khởi chạy, lệnh kiểm tra (smoke test).

## 5. Cấu trúc trường bắt buộc
Yêu cầu hệ thống & Điều kiện tiên quyết (OS, Node/Python/Java version, Docker), Cấu hình biến môi trường, Các bước cài đặt chi tiết từng câu lệnh, Các bước kiểm tra chạy thử (Smoke testing), Xử lý lỗi cài đặt phổ biến.

## 6. Quy tắc nội dung
1. Mọi câu lệnh cài đặt phải phù hợp chính xác với repository thực tế (ví dụ: dùng `npm install` hoặc `pnpm install` hoặc `pip install -r requirements.txt` dựa vào tệp manifest có trong repo).
2. Tuyệt đối không đưa mật khẩu hoặc key thật vào phần biến môi trường mẫu.
3. Phải có câu lệnh chạy thử để người cài đặt kiểm tra hệ thống đã hoạt động bình thường hay chưa.

## 7. Tiêu chí chất lượng
Một lập trình viên mới clone repo về có thể cài đặt và chạy thành công mà không gặp lỗi thiếu bước.

## 8. Quy tắc đặt tên
`DOC-DEL-011_Installation_Guide.md`.

## 9. Truy xuất nguồn gốc
Kế thừa từ `DOC-ARCH-008` (Deployment Architecture).

## 10. Cách kiểm tra
Kiểm tra sự khớp nhau giữa file manifest trong repo và các lệnh cài đặt trong tài liệu.

## 11. Ngoại lệ
Không có.

## 12. Ví dụ
- Hợp lệ:
  ```bash
  git clone <repo-url>
  cd project
  cp .env.example .env
  npm install
  npm run dev
  ```
- Không hợp lệ: Hướng dẫn gõ `pip install` cho một dự án thuần NodeJS / React.

## 13. Tài liệu liên quan
`DOC-ARCH-008`, `DOC-DEL-013`.

## 14. Bằng chứng cần thiết
Tệp package.json, requirements.txt, .env.example trong repository.

## 15. Giới hạn đã biết
Không có.
