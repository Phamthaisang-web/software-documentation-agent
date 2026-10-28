import os
import re
import json
from datetime import datetime, timezone
import yaml
import jsonschema

class ProjectAnalyzer:
    """Analyzes software repository structure, manifests, databases, APIs, and tests."""

    def __init__(self, agent_root):
        self.agent_root = agent_root
        self.config_dir = os.path.join(agent_root, "config")
        self.schema_path = os.path.join(self.config_dir, "project_profile.schema.json")
        with open(self.schema_path, "r", encoding="utf-8") as f:
            self.profile_schema = json.load(f)

    def analyze(self, target_dir):
        """Scans the target directory and constructs a structured ProjectProfile dictionary."""
        abs_target = os.path.abspath(target_dir)
        project_name = os.path.basename(abs_target) or "Software-Project"
        
        technologies = {
            "languages": [],
            "frameworks": [],
            "databases": [],
            "libraries": [],
            "evidence_refs": []
        }
        apis = []
        data_models = {"entities": [], "status": "UNKNOWN"}
        testing_strategy = {
            "automated_tests_found": False,
            "frameworks": [],
            "execution_evidence": "NOT_EXECUTED",
            "status": "UNKNOWN"
        }
        evidence_references = []
        functional_requirements = []
        non_functional_requirements = []
        missing_information = []
        conflicting_information = []

        ref_counter = 1

        # 1. Scan for manifest files
        files_found = []
        for root, dirs, files in os.walk(abs_target):
            # Ignore common bulky folders
            dirs[:] = [d for d in dirs if d not in [
                ".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build", ".next", ".nuxt"
            ]]
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), abs_target).replace("\\", "/")
                files_found.append((rel_path, os.path.join(root, file)))

        # Detect tech stack from manifests
        for rel_path, full_path in files_found:
            fname = os.path.basename(rel_path)
            
            # NodeJS / TypeScript
            if fname == "package.json":
                if "JavaScript" not in technologies["languages"]:
                    technologies["languages"].append("JavaScript")
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        pkg = json.load(f)
                    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
                    if "typescript" in deps and "TypeScript" not in technologies["languages"]:
                        technologies["languages"].append("TypeScript")
                    if "react" in deps and "React" not in technologies["frameworks"]:
                        technologies["frameworks"].append("React")
                    if "express" in deps and "Express" not in technologies["frameworks"]:
                        technologies["frameworks"].append("Express")
                    if "next" in deps and "Next.js" not in technologies["frameworks"]:
                        technologies["frameworks"].append("Next.js")
                    if "prisma" in deps and "Prisma ORM" not in technologies["frameworks"]:
                        technologies["frameworks"].append("Prisma ORM")
                    if "jest" in deps or "vitest" in deps:
                        testing_strategy["automated_tests_found"] = True
                        testing_strategy["frameworks"].append("Jest/Vitest")
                    
                    ref_id = f"EVID-{ref_counter:03d}"
                    ref_counter += 1
                    evidence_references.append({
                        "ref_id": ref_id,
                        "source_path": rel_path,
                        "source_type": "PACKAGE_MANIFEST"
                    })
                    technologies["evidence_refs"].append(rel_path)
                except Exception:
                    pass

            # Python
            elif fname in ["requirements.txt", "pyproject.toml"]:
                if "Python" not in technologies["languages"]:
                    technologies["languages"].append("Python")
                ref_id = f"EVID-{ref_counter:03d}"
                ref_counter += 1
                evidence_references.append({
                    "ref_id": ref_id,
                    "source_path": rel_path,
                    "source_type": "PACKAGE_MANIFEST"
                })
                technologies["evidence_refs"].append(rel_path)

            # Database / Schema files
            elif fname in ["schema.prisma", "models.py", "schema.sql"] or "migration" in rel_path.lower():
                data_models["status"] = "VERIFIED"
                ref_id = f"EVID-{ref_counter:03d}"
                ref_counter += 1
                evidence_references.append({
                    "ref_id": ref_id,
                    "source_path": rel_path,
                    "source_type": "DATABASE_SCHEMA"
                })
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    # simple extraction of model names
                    models = re.findall(r"(?:model|class|CREATE TABLE)\s+([A-Za-z0-9_]+)", content)
                    for m in set(models):
                        if not any(e["name"] == m for e in data_models["entities"]):
                            data_models["entities"].append({
                                "name": m,
                                "attributes": ["id", "created_at"],
                                "relationships": [],
                                "status": "VERIFIED",
                                "evidence_refs": [rel_path]
                            })
                except Exception:
                    pass

            # API routes detection
            elif ("routes" in rel_path.lower() or "controller" in rel_path.lower() or "api" in rel_path.lower()) and fname.endswith((".ts", ".js", ".py", ".go")):
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    # Regex for express/fastapi routes
                    matches = re.findall(r"\.(get|post|put|delete|patch)\s*\(\s*['\"]([^'\"]+)['\"]", content, re.IGNORECASE)
                    for method, path in matches:
                        api_id = f"API-{len(apis)+1:03d}"
                        apis.append({
                            "id": api_id,
                            "method": method.upper(),
                            "path": path,
                            "auth_required": "auth" in content.lower() or "token" in content.lower(),
                            "status": "VERIFIED",
                            "evidence_refs": [rel_path]
                        })
                except Exception:
                    pass

            # Test files
            elif ("test" in fname.lower() or "spec" in fname.lower()) and not fname.endswith(".json"):
                testing_strategy["automated_tests_found"] = True
                testing_strategy["status"] = "VERIFIED"
                ref_id = f"EVID-{ref_counter:03d}"
                ref_counter += 1
                evidence_references.append({
                    "ref_id": ref_id,
                    "source_path": rel_path,
                    "source_type": "TEST_SUITE"
                })

        # Ensure default fallbacks if empty
        if not technologies["languages"]:
            technologies["languages"].append("TypeScript")
            technologies["frameworks"].append("NodeJS")
            missing_information.append({
                "item": "Ngôn ngữ lập trình chính chưa xác định rõ qua manifest",
                "impact": "MEDIUM",
                "recommended_action": "Xác nhận ngôn ngữ và framework chính của dự án"
            })

        # Generate sample functional requirements if detected from APIs or defaults
        if apis:
            for i, api in enumerate(apis[:10]):
                functional_requirements.append({
                    "id": f"REQ-FUNC-{i+1:03d}",
                    "title": f"Cung cấp giao diện {api['method']} {api['path']}",
                    "description": f"Xử lý yêu cầu API {api['method']} tại đường dẫn {api['path']}",
                    "status": "VERIFIED",
                    "evidence_refs": api.get("evidence_refs", [])
                })
        else:
            functional_requirements.append({
                "id": "REQ-FUNC-001",
                "title": "Xác thực và phân quyền người dùng",
                "description": "Cho phép người dùng đăng nhập an toàn và truy cập tính năng theo vai trò",
                "status": "INFERRED",
                "evidence_refs": []
            })
            missing_information.append({
                "item": "Danh sách tính năng chi tiết chưa có tài liệu đặc tả",
                "impact": "HIGH",
                "recommended_action": "Cung cấp đặc tả nghiệp vụ hoặc xác nhận danh sách API routes"
            })

        # Non functional requirements
        non_functional_requirements.append({
            "id": "REQ-NF-PERF-001",
            "category": "Performance",
            "target_metric": "Response time <= 500ms for 95th percentile under normal load",
            "status": "INFERRED",
            "evidence_refs": []
        })
        non_functional_requirements.append({
            "id": "REQ-NF-SEC-001",
            "category": "Security",
            "target_metric": "OWASP Top 10 compliance with JWT authentication and HTTPS transmission",
            "status": "INFERRED",
            "evidence_refs": []
        })

        if not data_models["entities"]:
            data_models["entities"].append({
                "name": "User",
                "attributes": ["id", "email", "password_hash", "role", "created_at"],
                "relationships": [],
                "status": "INFERRED",
                "evidence_refs": []
            })

        profile = {
            "project_id": re.sub(r"[^a-zA-Z0-9_-]", "_", project_name.lower()),
            "project_name": project_name,
            "project_goal": f"Hệ thống phần mềm {project_name} phục vụ chuyển đổi số và tự động hóa quy trình nghiệp vụ.",
            "analysis_timestamp": datetime.now(timezone.utc).isoformat(),
            "status": "VERIFIED" if technologies["evidence_refs"] else "INFERRED",
            "business_problem": {
                "description": f"Giải quyết bài toán quản trị và tối ưu hóa vận hành cho hệ thống {project_name}.",
                "status": "INFERRED",
                "evidence_refs": [ref["source_path"] for ref in evidence_references[:2]]
            },
            "users_and_stakeholders": [
                {
                    "id": "STK-001",
                    "name": "Product Owner",
                    "role": "Product Owner",
                    "influence": "HIGH",
                    "status": "INFERRED",
                    "evidence_refs": []
                },
                {
                    "id": "STK-002",
                    "name": "Development Team",
                    "role": "Developers",
                    "influence": "HIGH",
                    "status": "VERIFIED" if technologies["evidence_refs"] else "INFERRED",
                    "evidence_refs": [ref["source_path"] for ref in evidence_references[:1]]
                },
                {
                    "id": "STK-003",
                    "name": "End User",
                    "role": "Customer / User",
                    "influence": "MEDIUM",
                    "status": "INFERRED",
                    "evidence_refs": []
                }
            ],
            "scope": {
                "in_scope": [
                    "Các tính năng được khai báo trong API và giao diện mã nguồn",
                    "Xác thực và bảo mật cơ bản"
                ],
                "out_of_scope": [
                    "Các module ngoài phạm vi repository hiện tại",
                    "Tích hợp hệ thống legacy không có tài liệu kỹ thuật"
                ]
            },
            "technologies": technologies,
            "system_architecture": {
                "style": "Layered Modular Architecture",
                "components": [
                    {"name": "API Gateway / Controllers", "purpose": "Tiếp nhận và xử lý request HTTP", "status": "VERIFIED" if apis else "INFERRED", "evidence_refs": []},
                    {"name": "Business Service Layer", "purpose": "Xử lý logic nghiệp vụ và ràng buộc hệ thống", "status": "INFERRED", "evidence_refs": []},
                    {"name": "Data Access Layer", "purpose": "Giao tiếp và quản trị dữ liệu CSDL", "status": data_models["status"], "evidence_refs": []}
                ],
                "dependencies": technologies["libraries"][:5],
                "status": "VERIFIED" if technologies["evidence_refs"] else "INFERRED",
                "evidence_refs": technologies["evidence_refs"][:2]
            },
            "functional_requirements": functional_requirements,
            "non_functional_requirements": non_functional_requirements,
            "data_models": data_models,
            "apis": apis if apis else [
                {
                    "id": "API-001",
                    "method": "GET",
                    "path": "/health",
                    "auth_required": False,
                    "status": "INFERRED",
                    "evidence_refs": []
                }
            ],
            "roles_and_permissions": [
                {
                    "role": "Administrator",
                    "permissions": ["system:read", "system:write", "users:manage"],
                    "status": "INFERRED",
                    "evidence_refs": []
                },
                {
                    "role": "User",
                    "permissions": ["profile:read", "profile:write"],
                    "status": "INFERRED",
                    "evidence_refs": []
                }
            ],
            "external_integrations": [],
            "deployment_environments": {
                "containerized": any("docker" in f[0].lower() for f in files_found),
                "orchestration": "Docker Compose" if any("docker-compose" in f[0].lower() for f in files_found) else "UNKNOWN",
                "ci_cd_pipelines": [f[0] for f in files_found if ".github" in f[0] or "gitlab" in f[0]],
                "status": "VERIFIED" if any("docker" in f[0].lower() for f in files_found) else "INFERRED"
            },
            "security": {
                "auth_methods": ["JWT", "Session"] if any("jwt" in str(f) for f in files_found) else ["Standard Auth"],
                "encryption": "TLS/HTTPS in transit",
                "status": "INFERRED"
            },
            "testing_strategy": testing_strategy,
            "project_management": {
                "methodology": "Scrum",
                "sprint_length_weeks": 2.0,
                "status": "INFERRED"
            },
            "known_risks_and_limitations": [
                {
                    "id": "RISK-001",
                    "description": "Tài liệu kiểm thử tự động chưa có báo cáo thực thi gần nhất",
                    "severity": "MEDIUM",
                    "mitigation": "Thiết lập pipeline CI tự động chạy test và lưu log báo cáo"
                }
            ],
            "missing_information": missing_information,
            "conflicting_information": conflicting_information,
            "evidence_references": evidence_references
        }

        # Validate against schema
        jsonschema.validate(instance=profile, schema=self.profile_schema)
        return profile

    def save_profile(self, profile, output_path):
        """Saves profile to YAML file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            yaml.dump(profile, f, allow_unicode=True, sort_keys=False)
        print(f"[OK] Project profile saved to: {output_path}")
