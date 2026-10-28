# Project Profile Rules — Quy Tắc Xây Dựng Hồ Sơ Dự Án

Tài liệu này quy định cấu trúc và cách hình thành tệp Hồ sơ Dự án (`project_profile.yaml`) sau khi Analyzer hoàn thành việc quét mã nguồn.

---

## 1. Mục Đích Hồ Sơ Dự Án
`project_profile.yaml` đóng vai trò là "nguồn chân lý kỹ thuật" (Single Source of Truth) đại diện cho toàn bộ hiện trạng của phần mềm. Mọi tài liệu kỹ thuật sau đó đều lấy dữ liệu từ tệp này để sinh nội dung.

## 2. Tiêu Chuẩn Schema
Hồ sơ dự án BẮT BUỘC phải tuân thủ nghiêm ngặt schema JSON:
`08_Schemas/project_profile.schema.json`.

## 3. Các Phần Bắt Buộc Trong Hồ Sơ
1. `project_id` & `project_name`: Mã và tên dự án.
2. `analysis_timestamp`: Thời điểm hoàn thành quét.
3. `status`: Trạng thái tổng thể (`VERIFIED`, `INFERRED`, `PARTIALLY_VERIFIED`, `UNKNOWN`, `CONFLICT`).
4. `business_problem`: Bài toán nghiệp vụ & mục tiêu.
5. `technologies`: Ngôn ngữ, Framework, CSDL, Thư viện kèm bằng chứng.
6. `functional_requirements`: Danh mục yêu cầu chức năng trích xuất được.
7. `non_functional_requirements`: Danh mục yêu cầu phi chức năng.
8. `system_architecture`: Kiến trúc, components, dependencies.
9. `data_models`: Bảng, thực thể, quan hệ.
10. `apis`: Danh sách endpoint, method, auth.
11. `roles_and_permissions`: Danh mục vai trò và quyền hạn.
12. `testing_strategy`: Trạng thái kiểm thử tự động và bằng chứng chạy test.
13. `missing_information`: Danh mục các phần còn thiếu cần hỏi người dùng.
14. `conflicting_information`: Danh mục các điểm mâu thuẫn cần giải quyết.
15. `evidence_references`: Bảng tham chiếu bằng chứng toàn cục.
