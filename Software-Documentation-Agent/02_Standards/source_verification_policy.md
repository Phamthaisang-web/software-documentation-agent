# Source Verification Policy — Chính Sách Thẩm Định Nguồn

Chính sách này quy định các nguyên tắc bắt buộc đối với AI Agent trong việc xác minh, trích dẫn và sử dụng các nguồn tài liệu, tiêu chuẩn kỹ thuật và quy định dự án.

---

## 1. Phân Loại Trạng Thái Xác Minh (Verification Statuses)

| Trạng Thái | Định Nghĩa | Quyền Hạn Trong Sinh Tài Liệu |
| :--- | :--- | :--- |
| `VERIFIED_OFFICIAL` | Nguồn chính thức do tổ chức tiêu chuẩn hoặc tác giả gốc ban hành, đã kiểm tra trực tiếp URL/văn bản. | Được dùng làm căn cứ bắt buộc cho các quy tắc `OFFICIAL_REQUIREMENT`. |
| `VERIFIED_AUTHORITATIVE` | Nguồn từ các tổ chức uy tín cao trong ngành (ví dụ: W3C, RFC, CNCF, Cloud providers) đã thẩm định. | Được dùng làm cơ sở tham chiếu thiết kế và kiến trúc. |
| `USER_PROVIDED` | Tài liệu, mẫu biểu hoặc yêu cầu do chính người dùng cung cấp trong workspace. | Có quyền ưu tiên cao trong việc áp dụng cho dự án cụ thể, nhưng không thay đổi được nguyên tắc logic cốt lõi. |
| `INTERNAL_POLICY` | Quy chế, quy định riêng của tổ chức, doanh nghiệp hoặc nhóm phát triển. | Áp dụng trong phạm vi dự án; phải ghi chú rõ là quy định nội bộ, không gán nhãn thành tiêu chuẩn quốc tế. |
| `UNVERIFIED` | Nguồn thứ cấp, bài viết blog, tổng hợp chưa được đối chiếu văn bản gốc. | Chỉ dùng mang tính gợi ý, không dùng làm ràng buộc kiểm tra tự động. |
| `UNAVAILABLE` | Nguồn không thể truy cập, link hỏng hoặc tài liệu mật không thể mở. | Phải ghi nhận rõ ràng lý do không truy cập được; không giả lập nội dung. |
| `SUPERSEDED` | Phiên bản cũ đã bị thay thế bởi phiên bản mới hơn của tiêu chuẩn. | Cảnh báo cho người dùng và chuyển hướng sang phiên bản hiệu lực. |

---

## 2. 7 Quy Tắc Thẩm Định Bắt Buộc

1. **Ưu tiên trang chính thức**: Luôn truy cập tên miền gốc của tổ chức ban hành tiêu chuẩn (scrumguides.org, iso.org, spec.openapis.org, owasp.org).
2. **Kiểm tra phiên bản và hiệu lực**: Ghi rõ năm phát hành, số hiệu ấn bản và tình trạng hiệu lực.
3. **Cấm bịa đặt thông tin nguồn**: Tuyệt đối không tự bịa đặt URL, mã điều khoản, số trang hoặc trích dẫn giả mạo.
4. **Minh bạch phạm vi kiểm tra**: Nếu chỉ truy cập được phần tóm tắt/giới thiệu (do bản quyền trả phí), phải ghi rõ chỉ xác minh được mục tiêu và cấu trúc, không tuyên bố đã đọc toàn văn tiêu chuẩn.
5. **Tách biệt bắt buộc và hướng dẫn**: Không được biến các ví dụ minh họa hoặc hướng dẫn bổ trợ thành điều khoản bắt buộc.
6. **Bảo vệ bản quyền**: Không sao chép nguyên văn các tiêu chuẩn thương mại có bản quyền vào tài liệu.
7. **Công khai hạn chế**: Bất kỳ khi nào không thể kiểm chứng nguồn mới nhất, phải thông báo rõ trong báo cáo thẩm định.
