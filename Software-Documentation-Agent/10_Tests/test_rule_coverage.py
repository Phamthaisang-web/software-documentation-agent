import os
import yaml
import pytest

AGENT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_DIR = os.path.join(AGENT_ROOT, "01_Rules")
CONFIG_DIR = os.path.join(AGENT_ROOT, "config")

@pytest.fixture
def doc_registry():
    path = os.path.join(CONFIG_DIR, "document_registry.yaml")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["documents"]

def test_all_referenced_rules_exist(doc_registry):
    """Test: All rules referenced by the 59 documents exist on disk."""
    rule_subdirs = [
        "Global", "Project_Management", "Requirements", "Scrum",
        "Architecture_Design", "Testing_Quality", "Delivery"
    ]
    missing_rules = []
    for doc in doc_registry:
        for rule_file in doc.get("rule_references", []):
            found = False
            for subdir in rule_subdirs:
                rule_path = os.path.join(RULES_DIR, subdir, rule_file)
                if os.path.exists(rule_path):
                    found = True
                    break
            if not found:
                missing_rules.append((doc["document_id"], rule_file))
    assert not missing_rules, f"Missing referenced rule files: {missing_rules}"

def test_rule_files_have_substantive_content():
    """Test: Rule files are not empty and contain required structured sections."""
    rule_files = []
    for root, _, files in os.walk(RULES_DIR):
        for f in files:
            if f.endswith(".md"):
                rule_files.append(os.path.join(root, f))

    assert len(rule_files) >= 50, f"Expected at least 50 rule files, found {len(rule_files)}"
    for rpath in rule_files:
        with open(rpath, "r", encoding="utf-8") as f:
            content = f.read()
        assert len(content) > 300, f"Rule file {rpath} is too short / hollow"
        assert "Mục đích" in content, f"{rpath} missing Mục đích"
        assert "Phạm vi áp dụng" in content, f"{rpath} missing Phạm vi áp dụng"

def test_rules_distinguish_official_requirement_vs_recommendation():
    """Test: Rule files clearly distinguish official requirements from recommendations."""
    scrum_rules_path = os.path.join(RULES_DIR, "Scrum", "Scrum_Rules.md")
    with open(scrum_rules_path, "r", encoding="utf-8") as f:
        scrum_content = f.read()
    assert "- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`" in scrum_content

    dor_rules_path = os.path.join(RULES_DIR, "Scrum", "Definition_of_Ready_Rules.md")
    with open(dor_rules_path, "r", encoding="utf-8") as f:
        dor_content = f.read()
    assert ("- **Loại quy tắc**: `RECOMMENDATION`" in dor_content or "- **Loại quy tắc**: `INTERNAL_POLICY`" in dor_content)
    assert "- **Loại quy tắc**: `OFFICIAL_REQUIREMENT`" not in dor_content, "Definition of Ready header must NOT declare OFFICIAL_REQUIREMENT"

def test_timebox_rules_contain_official_limits():
    """Test: Timebox rules contain exact Scrum Guide maximum limits."""
    timebox_path = os.path.join(RULES_DIR, "Scrum", "Timebox_Rules.md")
    with open(timebox_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "1 tháng" in content or "một tháng" in content
    assert "8 giờ" in content or "8h" in content
    assert "15 phút" in content
    assert "4 giờ" in content or "4h" in content
    assert "3 giờ" in content or "3h" in content
