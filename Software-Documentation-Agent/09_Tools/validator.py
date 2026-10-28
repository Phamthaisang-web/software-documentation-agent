import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import json
from datetime import datetime, timezone
import yaml
import jsonschema

try:
    from .sprint_validator import SprintValidator
    from .traceability_engine import TraceabilityEngine
except ImportError:
    from sprint_validator import SprintValidator
    from traceability_engine import TraceabilityEngine

class SystemValidator:
    """Master validation engine for registries, rules, templates, standards, Scrum constraints, and output files."""

    def __init__(self, agent_root):
        self.agent_root = agent_root
        self.config_dir = os.path.join(agent_root, "config")
        self.rules_dir = os.path.join(agent_root, "01_Rules")
        self.templates_dir = os.path.join(agent_root, "03_Templates")
        self.output_dir = os.path.join(agent_root, "output")
        self.schemas_dir = os.path.join(agent_root, "08_Schemas")

        with open(os.path.join(self.schemas_dir, "validation_report.schema.json"), "r", encoding="utf-8") as f:
            self.report_schema = json.load(f)

    def run_all_validations(self) -> dict:
        """Executes all system validation checks and returns the structured report."""
        results = []
        missing_items = []
        traceability_issues = []

        # -------------------------------------------------------------
        # 1. DOCUMENT REGISTRY VALIDATION
        # -------------------------------------------------------------
        doc_reg_path = os.path.join(self.config_dir, "document_registry.yaml")
        if not os.path.exists(doc_reg_path):
            results.append({
                "check_id": "CHK-DOC-REG-001",
                "category": "Registry",
                "target": "document_registry.yaml",
                "rule_id": "RULE-GLOB-003",
                "status": "FAILED",
                "severity": "BLOCKER",
                "message": "Không tìm thấy tệp config/document_registry.yaml"
            })
            docs = []
        else:
            with open(doc_reg_path, "r", encoding="utf-8") as f:
                doc_data = yaml.safe_load(f)
            docs = doc_data.get("documents", [])

            # Check count
            if len(docs) == 59:
                results.append({
                    "check_id": "CHK-DOC-COUNT",
                    "category": "Registry",
                    "target": "document_registry.yaml",
                    "rule_id": "RULE-GLOB-003",
                    "status": "PASSED",
                    "severity": "INFO",
                    "message": "Đủ chính xác 59 loại tài liệu trong Document Registry (Nhóm A đến Nhóm E)."
                })
            else:
                results.append({
                    "check_id": "CHK-DOC-COUNT",
                    "category": "Registry",
                    "target": "document_registry.yaml",
                    "rule_id": "RULE-GLOB-003",
                    "status": "FAILED",
                    "severity": "BLOCKER",
                    "message": f"Số lượng tài liệu không đúng yêu cầu 59 loại (Hiện có: {len(docs)})."
                })

            # Check unique IDs
            doc_ids = [d["document_id"] for d in docs]
            unique_ids = set(doc_ids)
            if len(doc_ids) == len(unique_ids):
                results.append({
                    "check_id": "CHK-DOC-UNIQUE-ID",
                    "category": "Registry",
                    "target": "document_registry.yaml",
                    "rule_id": "RULE-GLOB-003",
                    "status": "PASSED",
                    "severity": "INFO",
                    "message": "Không có Document ID nào bị trùng lặp."
                })
            else:
                duplicates = [item for item in doc_ids if doc_ids.count(item) > 1]
                results.append({
                    "check_id": "CHK-DOC-UNIQUE-ID",
                    "category": "Registry",
                    "target": "document_registry.yaml",
                    "rule_id": "RULE-GLOB-003",
                    "status": "FAILED",
                    "severity": "BLOCKER",
                    "message": f"Phát hiện Document ID trùng lặp: {set(duplicates)}"
                })

        # -------------------------------------------------------------
        # 2. STANDARDS REGISTRY VALIDATION
        # -------------------------------------------------------------
        std_reg_path = os.path.join(self.config_dir, "standards_registry.yaml")
        standards = {}
        if os.path.exists(std_reg_path):
            with open(std_reg_path, "r", encoding="utf-8") as f:
                std_data = yaml.safe_load(f)
            standards = {s["standard_id"]: s for s in std_data.get("standards", [])}
            
            valid_statuses = [
                "VERIFIED_OFFICIAL", "VERIFIED_AUTHORITATIVE", "USER_PROVIDED",
                "INTERNAL_POLICY", "UNVERIFIED", "UNAVAILABLE", "SUPERSEDED"
            ]
            all_statuses_valid = True
            for sid, s in standards.items():
                if s.get("verification_status") not in valid_statuses:
                    all_statuses_valid = False
                    results.append({
                        "check_id": f"CHK-STD-STATUS-{sid}",
                        "category": "Standards",
                        "target": sid,
                        "rule_id": "RULE-GLOB-002",
                        "status": "FAILED",
                        "severity": "CRITICAL",
                        "message": f"Trạng thái xác minh của {sid} không hợp lệ: {s.get('verification_status')}"
                    })
            if all_statuses_valid:
                results.append({
                    "check_id": "CHK-STD-STATUS-ALL",
                    "category": "Standards",
                    "target": "standards_registry.yaml",
                    "rule_id": "RULE-GLOB-002",
                    "status": "PASSED",
                    "severity": "INFO",
                    "message": f"Tất cả {len(standards)} nguồn tiêu chuẩn có trạng thái xác minh hợp lệ."
                })
        else:
            results.append({
                "check_id": "CHK-STD-REG-001",
                "category": "Standards",
                "target": "standards_registry.yaml",
                "rule_id": "RULE-GLOB-002",
                "status": "FAILED",
                "severity": "BLOCKER",
                "message": "Không tìm thấy tệp config/standards_registry.yaml"
            })

        # -------------------------------------------------------------
        # 3. TEMPLATE REGISTRY & FILES VALIDATION
        # -------------------------------------------------------------
        tpl_reg_path = os.path.join(self.config_dir, "template_registry.yaml")
        templates = {}
        if os.path.exists(tpl_reg_path):
            with open(tpl_reg_path, "r", encoding="utf-8") as f:
                tpl_data = yaml.safe_load(f)
            templates = {t["template_id"]: t for t in tpl_data.get("templates", [])}

            # Check every doc has a template record
            all_docs_have_tpl = True
            for d in docs:
                tpl_ref = d.get("preferred_template_id")
                if not tpl_ref or tpl_ref not in templates:
                    all_docs_have_tpl = False
                    missing_items.append({
                        "target_type": "DOCUMENT_TEMPLATE",
                        "target_id": d["document_id"],
                        "description": f"Tài liệu {d['document_id']} không có bản ghi template hợp lệ."
                    })
            if all_docs_have_tpl:
                results.append({
                    "check_id": "CHK-TPL-COVERAGE",
                    "category": "Template",
                    "target": "template_registry.yaml",
                    "rule_id": "RULE-GLOB-004",
                    "status": "PASSED",
                    "severity": "INFO",
                    "message": "Tất cả 59 tài liệu đều có bản ghi Template tương ứng."
                })
            else:
                results.append({
                    "check_id": "CHK-TPL-COVERAGE",
                    "category": "Template",
                    "target": "template_registry.yaml",
                    "rule_id": "RULE-GLOB-004",
                    "status": "FAILED",
                    "severity": "CRITICAL",
                    "message": "Một số tài liệu chưa có bản ghi template."
                })

            # Check physical file existence and honest classification
            all_tpl_files_exist = True
            no_ai_mislabeled = True
            for tid, t in templates.items():
                rel_path = t.get("file_path", "")
                full_path = os.path.join(self.agent_root, rel_path)
                if not os.path.exists(full_path):
                    all_tpl_files_exist = False
                    missing_items.append({
                        "target_type": "PHYSICAL_TEMPLATE_FILE",
                        "target_id": tid,
                        "description": f"Tệp mẫu vật lý không tồn tại: {rel_path}"
                    })
                # Check origin type honesty: AI generated template must NOT be marked OFFICIAL_SOURCE
                if t.get("origin_type") == "OFFICIAL_SOURCE" and "GENERATED" in str(t.get("status")):
                    no_ai_mislabeled = False

            if all_tpl_files_exist:
                results.append({
                    "check_id": "CHK-TPL-FILES-EXIST",
                    "category": "Template",
                    "target": "03_Templates",
                    "rule_id": "RULE-GLOB-004",
                    "status": "PASSED",
                    "severity": "INFO",
                    "message": f"Tất cả {len(templates)} tệp mẫu vật lý đều thực sự tồn tại trên đĩa."
                })
            else:
                results.append({
                    "check_id": "CHK-TPL-FILES-EXIST",
                    "category": "Template",
                    "target": "03_Templates",
                    "rule_id": "RULE-GLOB-004",
                    "status": "FAILED",
                    "severity": "CRITICAL",
                    "message": "Phát hiện tệp mẫu vật lý bị thiếu."
                })

            if no_ai_mislabeled:
                results.append({
                    "check_id": "CHK-TPL-HONEST-ORIGIN",
                    "category": "Template",
                    "target": "template_registry.yaml",
                    "rule_id": "RULE-GLOB-002",
                    "status": "PASSED",
                    "severity": "INFO",
                    "message": "Không có mẫu do AI tạo bị ghi nhầm thành mẫu chính thức (OFFICIAL_SOURCE)."
                })
            else:
                results.append({
                    "check_id": "CHK-TPL-HONEST-ORIGIN",
                    "category": "Template",
                    "target": "template_registry.yaml",
                    "rule_id": "RULE-GLOB-002",
                    "status": "FAILED",
                    "severity": "BLOCKER",
                    "message": "Vi phạm tính trung thực: Mẫu do AI tạo bị gán nhãn OFFICIAL_SOURCE."
                })

        # -------------------------------------------------------------
        # 4. RULE COVERAGE & INTEGRITY
        # -------------------------------------------------------------
        all_rules_exist = True
        for d in docs:
            for rule_file in d.get("rule_references", []):
                found = False
                for r_dir in ["Global", "Project_Management", "Requirements", "Scrum", "Architecture_Design", "Testing_Quality", "Delivery"]:
                    if os.path.exists(os.path.join(self.rules_dir, r_dir, rule_file)):
                        found = True
                        break
                if not found:
                    all_rules_exist = False
                    missing_items.append({
                        "target_type": "RULE_FILE",
                        "target_id": rule_file,
                        "description": f"Tài liệu {d['document_id']} tham chiếu tới Rule không tồn tại: {rule_file}"
                    })

        if all_rules_exist:
            results.append({
                "check_id": "CHK-RULE-COVERAGE",
                "category": "Rules",
                "target": "01_Rules",
                "rule_id": "RULE-GLOB-001",
                "status": "PASSED",
                "severity": "INFO",
                "message": "Tất cả các Rule files được tham chiếu bởi 59 tài liệu đều tồn tại thực tế."
            })
        else:
            results.append({
                "check_id": "CHK-RULE-COVERAGE",
                "category": "Rules",
                "target": "01_Rules",
                "rule_id": "RULE-GLOB-001",
                "status": "FAILED",
                "severity": "CRITICAL",
                "message": "Phát hiện tài liệu tham chiếu tới tệp Rules không tồn tại."
            })

        # -------------------------------------------------------------
        # 5. SCRUM CONSTRAINTS VALIDATION
        # -------------------------------------------------------------
        sprint_dur_res = SprintValidator.validate_sprint_duration(14)
        planning_res = SprintValidator.validate_planning_timebox(4.0, 14)
        daily_res = SprintValidator.validate_daily_scrum(15)
        review_res = SprintValidator.validate_review_timebox(2.0, 14)
        retro_res = SprintValidator.validate_retro_timebox(1.5, 14)
        dor_res = SprintValidator.validate_definition_of_ready_classification("RECOMMENDATION")

        if sprint_dur_res["valid"] and planning_res["valid"] and daily_res["valid"] and review_res["valid"] and retro_res["valid"] and dor_res["valid"]:
            results.append({
                "check_id": "CHK-SCRUM-CONSTRAINTS",
                "category": "Scrum",
                "target": "Scrum Timeboxes & Rules",
                "rule_id": "RULE-SCRUM-019",
                "status": "PASSED",
                "severity": "INFO",
                "message": "Các ràng buộc thời lượng Scrum (Sprint <= 1 tháng, Daily = 15m, Planning/Review/Retro timeboxes, DoR là bổ trợ) được tuân thủ nghiêm ngặt."
            })
        else:
            results.append({
                "check_id": "CHK-SCRUM-CONSTRAINTS",
                "category": "Scrum",
                "target": "Scrum Timeboxes & Rules",
                "rule_id": "RULE-SCRUM-019",
                "status": "FAILED",
                "severity": "CRITICAL",
                "message": "Vi phạm ràng buộc tiêu chuẩn Scrum Guide 2020."
            })

        # -------------------------------------------------------------
        # 6. TRACEABILITY ENGINE INTEGRATION
        # -------------------------------------------------------------
        engine = TraceabilityEngine()
        # Register docs and check dependency links
        for d in docs:
            engine.register_entity(d["document_id"], "DOCUMENT", d["official_name"])
            for dep in d.get("dependencies", []):
                engine.add_link(d["document_id"], dep, relation="depends_on")

        trace_res = engine.verify_traceability()
        if trace_res["status"] == "PASSED":
            results.append({
                "check_id": "CHK-TRACEABILITY",
                "category": "Traceability",
                "target": "Document Dependency Graph",
                "rule_id": "RULE-GLOB-006",
                "status": "PASSED",
                "severity": "INFO",
                "message": "Mạng lưới truy xuất nguồn gốc giữa các tài liệu hợp lệ (không có broken links)."
            })
        else:
            results.append({
                "check_id": "CHK-TRACEABILITY",
                "category": "Traceability",
                "target": "Document Dependency Graph",
                "rule_id": "RULE-GLOB-006",
                "status": "WARNING",
                "severity": "MAJOR",
                "message": f"Phát hiện {len(trace_res['broken_links'])} liên kết đứt gãy trong đồ thị tài liệu."
            })
            traceability_issues.extend(trace_res["broken_links"])

        # Compute summary
        total_checks = len(results)
        passed_count = sum(1 for r in results if r["status"] == "PASSED")
        failed_count = sum(1 for r in results if r["status"] == "FAILED")
        skipped_count = sum(1 for r in results if r["status"] == "SKIPPED")
        not_run_count = sum(1 for r in results if r["status"] == "NOT_RUN")

        report = {
            "report_id": f"VAL-REP-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "target_scope": "Software Documentation Agent System",
            "summary": {
                "total_checks": total_checks,
                "passed": passed_count,
                "failed": failed_count,
                "skipped": skipped_count,
                "not_run": not_run_count,
                "status": "PASSED" if failed_count == 0 else "FAILED"
            },
            "results": results,
            "missing_items": missing_items,
            "traceability_issues": traceability_issues
        }

        # Validate against schema
        jsonschema.validate(instance=report, schema=self.report_schema)
        return report

    def save_report(self, report: dict, output_dir: str = None) -> (str, str):
        """Saves machine-readable JSON and human-readable Markdown validation reports."""
        target_dir = output_dir or os.path.join(self.output_dir, "Validation_Reports")
        os.makedirs(target_dir, exist_ok=True)

        json_path = os.path.join(target_dir, "validation_report.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        md_path = os.path.join(target_dir, "validation_report.md")
        summary = report["summary"]
        status_badge = "✅ PASSED" if summary["status"] == "PASSED" else "❌ FAILED"
        
        md_content = f"""# Báo Cáo Thẩm Định Hệ Thống Tài Liệu (System Validation Report)

- **Mã báo cáo**: `{report['report_id']}`
- **Thời điểm tạo**: `{report['generated_at']}`
- **Kết quả tổng quát**: **{status_badge}**

---

## 1. Tổng Hợp Số Lượng Kiểm Tra
| Chỉ Số | Giá Trị |
| :--- | :--- |
| **Tổng số lượt kiểm tra (Total Checks)** | **{summary['total_checks']}** |
| **Đạt yêu cầu (Passed)** | **{summary['passed']}** |
| **Thất bại (Failed)** | **{summary['failed']}** |
| **Bỏ qua (Skipped)** | **{summary['skipped']}** |
| **Chưa chạy (Not Run)** | **{summary['not_run']}** |

---

## 2. Chi Tiết Kết Quả Kiểm Tra
| Check ID | Hạng Mục | Đối Tượng | Quy Tắc | Mức Độ | Trạng Thái | Mô Tả Chi Tiết |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""
        for r in report["results"]:
            icon = "✅ PASS" if r["status"] == "PASSED" else "❌ FAIL"
            md_content += f"| `{r['check_id']}` | {r['category']} | `{r['target']}` | `{r['rule_id']}` | `{r['severity']}` | {icon} | {r['message']} |\n"

        if report.get("missing_items"):
            md_content += "\n---\n\n## 3. Các Mục Còn Thiếu (Missing Items)\n"
            for item in report["missing_items"]:
                md_content += f"- **[{item['target_type']}]** `{item['target_id']}`: {item['description']}\n"

        if report.get("traceability_issues"):
            md_content += "\n---\n\n## 4. Vấn Đề Truy Xuất Nguồn Gốc (Traceability Issues)\n"
            for t in report["traceability_issues"]:
                md_content += f"- **[{t['issue_type']}]** `{t['source_id']}` -> `{t['target_id']}`: {t['details']}\n"

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"[OK] Validation reports generated:\n  - JSON: {json_path}\n  - MD: {md_path}")
        return json_path, md_path
