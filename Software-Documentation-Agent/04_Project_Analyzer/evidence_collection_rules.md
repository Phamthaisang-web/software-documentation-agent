# Evidence Collection Rules — Quy Tắc Thu Thập Bằng Chứng

Tài liệu này quy định cách thức trích xuất, định dạng và lưu trữ bằng chứng từ codebase để hậu thuẫn cho nội dung tài liệu.

---

## 1. Định Dạng Tham Chiếu Bằng Chứng (`evidence_refs`)
Mỗi bằng chứng thu thập được phải được lưu trữ dưới dạng:
```yaml
ref_id: "EVID-001"
source_path: "src/controllers/payment.controller.ts#L45-L68"
source_type: "CODE" # [CODE, CONFIG, DATABASE, TEST, DOC, GIT]
description: "Khai báo endpoint POST /api/v1/payments với Stripe SDK"
extracted_at: "2026-10-29T03:00:00Z"
```

## 2. Quy Tắc Thu Thập Theo Loại Bằng Chứng
- **Mã nguồn (Code)**: Ghi rõ đường dẫn tệp tương đối từ thư mục gốc, kèm tên hàm/lớp hoặc dải số dòng.
- **Cấu hình (Config)**: Trích xuất các key cấu hình không nhạy cảm (ví dụ `PORT: 3000`, `DATABASE_ENGINE: postgresql`).
- **Cơ sở dữ liệu (Database)**: Trích xuất tên bảng, tên cột và ràng buộc khóa chính/ngoại từ tệp migration/schema.
- **Kiểm thử (Test)**: Trích xuất tên hàm test (`test_user_can_login`), framework kiểm thử (`jest`, `pytest`, `junit`), và file log kết quả thực thi (nếu có).

## 3. Cấm Trích Xuất Dữ Liệu Nhạy Cảm
Bằng chứng tuyệt đối không chứa:
- Chuỗi mật khẩu thật.
- Khóa bí mật (Private keys), Access tokens.
- Dữ liệu người dùng thật (PII).
- Tất cả phải được che giấu: `[REDACTED]`.
