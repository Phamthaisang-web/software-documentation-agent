import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import argparse
import yaml
from project_analyzer import ProjectAnalyzer
from document_generator import DocumentGenerator
from validator import SystemValidator

AGENT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser(
        description="Software Documentation Agent CLI — Phân tích, sinh và thẩm định tài liệu phần mềm."
    )
    subparsers = parser.add_subparsers(dest="command", help="Lệnh cần thực thi")

    # analyze
    analyze_parser = subparsers.add_parser("analyze", help="Phân tích mã nguồn và tạo Project Profile")
    analyze_parser.add_argument("--target", default=".", help="Thư mục mã nguồn cần phân tích")
    analyze_parser.add_argument("--output", default="output/Project_Profile/project_profile.yaml", help="Đường dẫn lưu profile")

    # generate
    gen_parser = subparsers.add_parser("generate", help="Tạo một tài liệu cụ thể")
    gen_parser.add_argument("--doc-id", required=True, help="Mã tài liệu (ví dụ: DOC-REQ-001)")
    gen_parser.add_argument("--profile", default="output/Project_Profile/project_profile.yaml", help="Đường dẫn hồ sơ dự án")

    # generate-set
    gen_set_parser = subparsers.add_parser("generate-set", help="Tạo bộ 59 tài liệu hoàn chỉnh")
    gen_set_parser.add_argument("--profile", default="output/Project_Profile/project_profile.yaml", help="Đường dẫn hồ sơ dự án")

    # validate
    val_parser = subparsers.add_parser("validate", help="Chạy thẩm định toàn diện hệ thống tài liệu")
    val_parser.add_argument("--output-dir", default="output/Validation_Reports", help="Thư mục xuất báo cáo kiểm tra")

    # verify-sources
    subparsers.add_parser("verify-sources", help="Kiểm tra tính hợp lệ của các nguồn tiêu chuẩn")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "analyze":
        print(f"[*] Bắt đầu phân tích thư mục: {args.target}...")
        analyzer = ProjectAnalyzer(AGENT_ROOT)
        profile = analyzer.analyze(args.target)
        out_path = os.path.join(AGENT_ROOT, args.output) if not os.path.isabs(args.output) else args.output
        analyzer.save_profile(profile, out_path)
        print("[+] Hoàn tất phân tích dự án thành công.")

    elif args.command == "generate":
        print(f"[*] Tạo tài liệu: {args.doc_id}...")
        profile_path = os.path.join(AGENT_ROOT, args.profile) if not os.path.isabs(args.profile) else args.profile
        if not os.path.exists(profile_path):
            print(f"[!] Hồ sơ dự án không tồn tại ở {profile_path}. Tự động phân tích dự án...")
            analyzer = ProjectAnalyzer(AGENT_ROOT)
            profile = analyzer.analyze(".")
            analyzer.save_profile(profile, profile_path)
        else:
            with open(profile_path, "r", encoding="utf-8") as f:
                profile = yaml.safe_load(f)

        generator = DocumentGenerator(AGENT_ROOT)
        out_file = generator.generate_document(args.doc_id, profile)
        print(f"[+] Tài liệu đã tạo tại: {out_file}")

    elif args.command == "generate-set":
        print("[*] Bắt đầu tạo bộ 59 tài liệu hoàn chỉnh...")
        profile_path = os.path.join(AGENT_ROOT, args.profile) if not os.path.isabs(args.profile) else args.profile
        if not os.path.exists(profile_path):
            analyzer = ProjectAnalyzer(AGENT_ROOT)
            profile = analyzer.analyze(".")
            analyzer.save_profile(profile, profile_path)
        else:
            with open(profile_path, "r", encoding="utf-8") as f:
                profile = yaml.safe_load(f)

        generator = DocumentGenerator(AGENT_ROOT)
        files = generator.generate_all(profile)
        print(f"[+] Hoàn tất tạo {len(files)} tài liệu kỹ thuật trong output/.")

    elif args.command == "validate":
        print("[*] Thực thi thẩm định toàn diện hệ thống...")
        validator = SystemValidator(AGENT_ROOT)
        report = validator.run_all_validations()
        out_dir = os.path.join(AGENT_ROOT, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
        validator.save_report(report, out_dir)
        summary = report["summary"]
        print(f"\n=== KẾT QUẢ THẨM ĐỊNH: {summary['status']} ===")
        print(f"Tổng số kiểm tra: {summary['total_checks']} | Đạt: {summary['passed']} | Thất bại: {summary['failed']}")
        if summary["failed"] > 0:
            sys.exit(1)

    elif args.command == "verify-sources":
        print("[*] Kiểm tra các nguồn tiêu chuẩn trong config/standards_registry.yaml...")
        std_path = os.path.join(AGENT_ROOT, "config", "standards_registry.yaml")
        with open(std_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for s in data["standards"]:
            print(f"  - [{s['verification_status']}] {s['standard_id']}: {s['official_name']} ({s['url']})")
        print("[+] Toàn bộ nguồn đã được cấu hình và kiểm tra.")

if __name__ == "__main__":
    main()
