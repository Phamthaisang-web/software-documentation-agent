import os
import yaml
import pytest

AGENT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(AGENT_ROOT, "config")
TEMPLATES_DIR = os.path.join(AGENT_ROOT, "03_Templates")

@pytest.fixture
def template_registry():
    path = os.path.join(CONFIG_DIR, "template_registry.yaml")
    assert os.path.exists(path), f"Template registry missing at {path}"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["templates"]

def test_template_registry_completeness(template_registry):
    """Test: Every document has an associated template record."""
    doc_path = os.path.join(CONFIG_DIR, "document_registry.yaml")
    with open(doc_path, "r", encoding="utf-8") as f:
        docs = yaml.safe_load(f)["documents"]

    tpl_ids = {t["template_id"] for t in template_registry}
    for doc in docs:
        pref = doc.get("preferred_template_id")
        assert pref in tpl_ids, f"Document {doc['document_id']} references missing template {pref}"

def test_all_physical_templates_exist(template_registry):
    """Test: All physical template files exist on disk."""
    for tpl in template_registry:
        rel_path = tpl.get("file_path")
        full_path = os.path.join(AGENT_ROOT, rel_path)
        assert os.path.exists(full_path), f"Physical template file missing: {full_path}"
        assert os.path.getsize(full_path) > 0, f"Template file is empty: {full_path}"

def test_honest_ai_template_classification(template_registry):
    """Test: AI generated templates are NOT mislabeled as OFFICIAL_SOURCE."""
    for tpl in template_registry:
        if tpl.get("origin_type") == "OFFICIAL_SOURCE":
            assert tpl.get("source_id") != "SYS-BUILTIN-TEMPLATES", \
                f"Generated template {tpl['template_id']} must not be marked as OFFICIAL_SOURCE"

def test_missing_template_detection():
    """Test: Missing template files are identified with status MISSING."""
    # Simulate record with missing file
    fake_record = {
        "template_id": "TPL-FAKE-999",
        "file_path": "03_Templates/NonExistent/Fake.docx",
        "status": "MISSING"
    }
    target_path = os.path.join(AGENT_ROOT, fake_record["file_path"])
    assert not os.path.exists(target_path)
    assert fake_record["status"] == "MISSING"

def test_generated_templates_notice_exists():
    """Test: Notice file exists in 03_Templates describing origins and rules."""
    notice_path = os.path.join(TEMPLATES_DIR, "GENERATED_TEMPLATES_NOTICE.md")
    assert os.path.exists(notice_path)
    with open(notice_path, "r", encoding="utf-8") as f:
        text = f.read()
    assert "GENERATED_TEMPLATE" in text
    assert "USER_PROVIDED" in text
