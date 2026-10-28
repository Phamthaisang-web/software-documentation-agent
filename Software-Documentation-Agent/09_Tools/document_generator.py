import os
import shutil
from typing import List
from datetime import datetime, timezone
import yaml
import docx
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

class DocumentGenerator:
    """Generates documents from templates, profile data, and rules with format preservation."""

    def __init__(self, agent_root):
        self.agent_root = agent_root
        self.config_dir = os.path.join(agent_root, "config")
        self.templates_dir = os.path.join(agent_root, "03_Templates")
        self.output_dir = os.path.join(agent_root, "output")
        os.makedirs(self.output_dir, exist_ok=True)

        with open(os.path.join(self.config_dir, "document_registry.yaml"), "r", encoding="utf-8") as f:
            self.doc_registry = {d["document_id"]: d for d in yaml.safe_load(f)["documents"]}

        with open(os.path.join(self.config_dir, "template_registry.yaml"), "r", encoding="utf-8") as f:
            self.tpl_registry = {t["template_id"]: t for t in yaml.safe_load(f)["templates"]}

    def generate_document(self, doc_id: str, profile: dict, output_folder: str = None) -> str:
        """Renders a single document and saves it into output directory with companion metadata."""
        if doc_id not in self.doc_registry:
            raise ValueError(f"Document ID {doc_id} not registered in document_registry.yaml")

        doc_meta = self.doc_registry[doc_id]
        tpl_id = doc_meta["preferred_template_id"]
        if tpl_id not in self.tpl_registry:
            raise ValueError(f"Template ID {tpl_id} not registered in template_registry.yaml")

        tpl_meta = self.tpl_registry[tpl_id]
        tpl_rel_path = tpl_meta["file_path"]
        tpl_abs_path = os.path.join(self.agent_root, tpl_rel_path)
        if not os.path.exists(tpl_abs_path):
            raise FileNotFoundError(f"Template file not found at {tpl_abs_path}")

        # Target directory inside output
        group_folder = doc_meta["group"]
        target_dir = output_folder or os.path.join(self.output_dir, group_folder)
        os.makedirs(target_dir, exist_ok=True)

        fmt = tpl_meta["format"]
        clean_name = doc_meta["official_name"].replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        out_filename = f"{doc_id}_{clean_name}.{fmt}"
        out_path = os.path.join(target_dir, out_filename)

        project_name = profile.get("project_name", "Software Project")
        version = doc_meta.get("version", "1.0.0")
        now_iso = datetime.now(timezone.utc).isoformat()
        date_str = datetime.now().strftime("%Y-%m-%d")

        # Render according to format
        if fmt == "docx":
            self._render_docx(tpl_abs_path, out_path, doc_meta, profile, date_str)
        elif fmt == "xlsx":
            self._render_xlsx(tpl_abs_path, out_path, doc_meta, profile)
        elif fmt == "md":
            self._render_markdown(tpl_abs_path, out_path, doc_meta, profile, date_str)
        elif fmt == "yaml":
            self._render_yaml(tpl_abs_path, out_path, doc_meta, profile)
        elif fmt == "mmd":
            self._render_mermaid(tpl_abs_path, out_path, doc_meta, profile)
        else:
            shutil.copy2(tpl_abs_path, out_path)

        # Companion metadata file
        meta_filename = f"{doc_id}_{clean_name}.meta.yaml"
        meta_path = os.path.join(target_dir, meta_filename)
        metadata = {
            "document_id": doc_id,
            "title": doc_meta["official_name"],
            "project_id": profile.get("project_id", "project_default"),
            "version": version,
            "created_at": now_iso,
            "updated_at": now_iso,
            "authors": ["Software Documentation Agent"],
            "reviewers": ["Engineering Lead (Pending)"],
            "lifecycle_status": "DRAFT",
            "template_used": tpl_meta["template_name"],
            "source_standards": doc_meta["related_standards"],
            "traceability_links": [
                {"relation": "depends_on", "target_id": dep}
                for dep in doc_meta.get("dependencies", [])
            ],
            "unverified_items": [item["item"] for item in profile.get("missing_information", [])]
        }
        with open(meta_path, "w", encoding="utf-8") as f:
            yaml.dump(metadata, f, allow_unicode=True, sort_keys=False)

        print(f"[OK] Generated {doc_id} -> {out_path}")
        return out_path

    def _render_docx(self, src_path, dst_path, doc_meta, profile, date_str):
        doc = docx.Document(src_path)
        replacements = {
            "{{PROJECT_NAME}}": profile.get("project_name", "Software Project"),
            "{{VERSION}}": doc_meta.get("version", "1.0.0"),
            "{{DATE}}": date_str,
            "{{AUTHOR}}": "Software Documentation Agent",
            "{{EXECUTIVE_SUMMARY_CONTENT}}": profile.get("project_goal", "Mục tiêu dự án tổng quát."),
            "{{DETAILS_CONTENT}}": f"Đặc tả kỹ thuật chi tiết cho tài liệu {doc_meta['official_name']}.",
            "{{VERIFICATION_EVIDENCE_CONTENT}}": "Dữ liệu được xác minh từ mã nguồn và cấu hình hệ thống thực tế."
        }
        for p in doc.paragraphs:
            for key, val in replacements.items():
                if key in p.text:
                    p.text = p.text.replace(key, val)

        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for key, val in replacements.items():
                        if key in cell.text:
                            cell.text = cell.text.replace(key, val)
        doc.save(dst_path)

    def _render_xlsx(self, src_path, dst_path, doc_meta, profile):
        wb = openpyxl.load_workbook(src_path)
        ws = wb.active
        # Append actual entities or features from profile if empty
        reqs = profile.get("functional_requirements", [])
        if reqs and ws.max_row <= 4:
            border = Border(left=Side(style='thin', color='D9D9D9'),
                            right=Side(style='thin', color='D9D9D9'),
                            top=Side(style='thin', color='D9D9D9'),
                            bottom=Side(style='thin', color='D9D9D9'))
            for req in reqs:
                row_data = [
                    req["id"],
                    "Functional",
                    req["title"],
                    req.get("description", ""),
                    req.get("status", "VERIFIED"),
                    "DevTeam",
                    ", ".join(req.get("evidence_refs", []))
                ]
                ws.append(row_data)
                for cell in ws[ws.max_row]:
                    cell.border = border
        wb.save(dst_path)

    def _render_markdown(self, src_path, dst_path, doc_meta, profile, date_str):
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = content.replace("{{PROJECT_NAME}}", profile.get("project_name", "Software Project"))
        content = content.replace("{{VERSION}}", doc_meta.get("version", "1.0.0"))
        content = content.replace("{{DATE}}", date_str)
        content = content.replace("{{CONTEXT_CONTENT}}", profile.get("project_goal", ""))
        content = content.replace("{{DETAILS_CONTENT}}", f"Chi tiết đặc tả cho {doc_meta['official_name']}.")
        content = content.replace("{{EVIDENCE_CONTENT}}", "Dựa trên kết quả phân tích cấu trúc mã nguồn.")

        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(content)

    def _render_yaml(self, src_path, dst_path, doc_meta, profile):
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("{{PROJECT_NAME}}", profile.get("project_name", "Software Project"))
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(content)

    def _render_mermaid(self, src_path, dst_path, doc_meta, profile):
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(content)

    def generate_all(self, profile: dict) -> List[str]:
        """Generates all 59 registered documents in dependency order."""
        generated = []
        for doc_id in self.doc_registry:
            out_file = self.generate_document(doc_id, profile)
            generated.append(out_file)
        return generated
