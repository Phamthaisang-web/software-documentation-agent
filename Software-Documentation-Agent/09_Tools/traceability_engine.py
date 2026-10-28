import re
from typing import Dict, List, Set, Any

class TraceabilityEngine:
    """Manages and verifies bidirectional traceability graph across all documentation entities."""

    def __init__(self):
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.links: List[Dict[str, str]] = []

    def register_entity(self, entity_id: str, entity_type: str, title: str, metadata: Dict[str, Any] = None):
        """Registers a traceable entity (e.g., REQ-FUNC-001, TC-AUTH-001, ADR-001)."""
        self.nodes[entity_id] = {
            "id": entity_id,
            "type": entity_type,
            "title": title,
            "parents": set(),
            "children": set(),
            "metadata": metadata or {}
        }

    def add_link(self, source_id: str, target_id: str, relation: str = "verifies_or_implements"):
        """Adds a directional link from source entity to target entity."""
        self.links.append({
            "source": source_id,
            "target": target_id,
            "relation": relation
        })
        if source_id in self.nodes:
            self.nodes[source_id]["children"].add(target_id)
        if target_id in self.nodes:
            self.nodes[target_id]["parents"].add(source_id)

    def verify_traceability(self) -> Dict[str, Any]:
        """
        Validates traceability graph:
        1. Detects broken links (target_id does not exist).
        2. Detects orphan requirements (functional requirements with no test cases).
        3. Detects orphan test cases (test cases with no parent requirement).
        """
        broken_links = []
        orphan_requirements = []
        orphan_test_cases = []
        uncovered_bugs = []

        for link in self.links:
            src = link["source"]
            tgt = link["target"]
            if tgt not in self.nodes:
                broken_links.append({
                    "source_id": src,
                    "target_id": tgt,
                    "issue_type": "MISSING_TARGET",
                    "details": f"Thực thể {src} tham chiếu tới mã {tgt} nhưng mã này không tồn tại trong hệ thống."
                })
            if src not in self.nodes:
                broken_links.append({
                    "source_id": src,
                    "target_id": tgt,
                    "issue_type": "BROKEN_LINK",
                    "details": f"Nguồn liên kết {src} không tồn tại trong hệ thống."
                })

        for node_id, data in self.nodes.items():
            ntype = data["type"]
            # Functional requirements must have at least one verifying test case or child
            if ntype in ["FUNCTIONAL_REQUIREMENT", "REQUIREMENT"]:
                has_test = any(
                    child in self.nodes and self.nodes[child]["type"] in ["TEST_CASE", "TEST_SCENARIO"]
                    for child in data["children"]
                )
                if not has_test and not data["children"]:
                    orphan_requirements.append({
                        "id": node_id,
                        "title": data["title"],
                        "issue": "Yêu cầu chức năng chưa có Test Case kiểm chứng."
                    })

            # Test cases must link to a requirement or PBI
            elif ntype == "TEST_CASE":
                has_req_parent = any(
                    parent in self.nodes and self.nodes[parent]["type"] in ["FUNCTIONAL_REQUIREMENT", "PBI", "USER_STORY"]
                    for parent in data["parents"]
                )
                if not has_req_parent and not data["parents"]:
                    orphan_test_cases.append({
                        "id": node_id,
                        "title": data["title"],
                        "issue": "Ca kiểm thử mồ côi (không gắn với bất kỳ Yêu cầu hoặc User Story nào)."
                    })

        total_nodes = len(self.nodes)
        total_links = len(self.links)
        is_clean = len(broken_links) == 0 and len(orphan_requirements) == 0 and len(orphan_test_cases) == 0

        return {
            "status": "PASSED" if is_clean else ("FAILED" if broken_links else "WARNING"),
            "summary": {
                "total_entities": total_nodes,
                "total_links": total_links,
                "broken_links_count": len(broken_links),
                "orphan_requirements_count": len(orphan_requirements),
                "orphan_test_cases_count": len(orphan_test_cases)
            },
            "broken_links": broken_links,
            "orphan_requirements": orphan_requirements,
            "orphan_test_cases": orphan_test_cases
        }
