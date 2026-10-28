# Workspace: Software Documentation Agent System

Hệ thống **Software Documentation Agent** được triển khai hoàn chỉnh trong workspace này theo tiêu chuẩn của nền tảng **Google Antigravity**.

- **Thư mục hệ thống chính**: [`Software-Documentation-Agent/`](file:///d:/agenttl1/Software-Documentation-Agent/)
- **Điểm khởi chạy Antigravity Skill**: [`.agents/skills/software-documentation-agent/SKILL.md`](file:///d:/agenttl1/.agents/skills/software-documentation-agent/SKILL.md)
- **Hướng dẫn sử dụng chi tiết**: [`Software-Documentation-Agent/HUONG_DAN_SU_DUNG.md`](file:///d:/agenttl1/Software-Documentation-Agent/HUONG_DAN_SU_DUNG.md)

---

## Lệnh Kiểm Tra Nhanh
```powershell
# Chạy bộ 40 bài kiểm thử tự động
python -m pytest Software-Documentation-Agent/10_Tests -v

# Chạy thẩm định hệ thống tài liệu
python Software-Documentation-Agent/09_Tools/cli.py validate
```
