# Template Preservation Rules — Quy Tắc Giữ Nguyên Định Dạng Mẫu

Tài liệu này quy định chi tiết các biện pháp kỹ thuật nhằm bảo toàn định dạng gốc của các mẫu tài liệu Word (.docx), Excel (.xlsx), PowerPoint (.pptx), Markdown, YAML và Mermaid.

---

## 1. Đối Với Microsoft Word (.docx)
1. **Bảo tồn Style & Heading Hierarchy**: Sử dụng các style có sẵn trong mẫu (`Heading 1`, `Heading 2`, `Normal`, `Title`). Không tự ý ghi đè màu sắc hoặc font chữ của template.
2. **Bảo tồn Cấu trúc Bảng (Tables)**:
   - Điền dữ liệu vào các hàng của bảng có sẵn.
   - Nếu cần thêm hàng, nhân bản định dạng của hàng mẫu trước đó (borders, cell shading, font).
   - Không xóa bảng hoặc làm lệch độ rộng cột đã được căn chỉnh.
3. **Bảo tồn Header & Footer & Logo**:
   - Giữ nguyên toàn bộ phần Header, Footer, số trang tự động và logo thương hiệu của tổ chức.
4. **Thay thế Placeholder**: Chỉ tìm kiếm và thay thế chuỗi placeholder, không xóa trắng toàn bộ văn bản.

---

## 2. Đối Với Microsoft Excel (.xlsx)
1. **Bảo tồn Công thức (Formulas)**:
   - Tuyệt đối không thay thế các ô chứa công thức (ví dụ: `=SUM(C2:C20)`, `=AVERAGE(D2:D10)`) bằng các số tĩnh.
   - Thêm dòng dữ liệu mới vào đúng vùng dữ liệu mà công thức đang tham chiếu tới.
2. **Bảo tồn Định dạng & Màu sắc (Styles & Colors)**:
   - Giữ nguyên màu nền header (`PatternFill`), viền ô (`Border`), canh lề (`Alignment`) và kiểu dữ liệu (Date, Currency, Number).
3. **Bảo tồn Cấu trúc Sheet**:
   - Giữ nguyên tên các worksheet, thứ tự các sheet và các chế độ xem (Freeze Panes, Filter).

---

## 3. Đối Với Mermaid, YAML, Markdown
1. **Mermaid (.mmd)**:
   - Giữ mã nguồn sơ đồ để người dùng có thể mở và hiệu chỉnh trên Mermaid Live Editor hoặc IDE.
2. **OpenAPI / YAML**:
   - Cú pháp thụt lề 2 spaces chuẩn, kiểm tra schema hợp lệ bằng PyYAML.
