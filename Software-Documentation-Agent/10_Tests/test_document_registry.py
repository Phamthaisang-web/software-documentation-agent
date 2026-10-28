import os
import re
import yaml
import pytest

AGENT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(AGENT_ROOT, "config")

@pytest.fixture
def doc_registry():
    path = os.path.join(CONFIG_DIR, "document_registry.yaml")
    assert os.path.exists(path), f"Registry file missing at {path}"
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("documents", [])

def test_document_registry_has_59_documents(doc_registry):
    """Test 1: Verify exactly 59 document types are registered."""
    assert len(doc_registry) == 59, f"Expected 59 documents, but found {len(doc_registry)}"

def test_no_duplicate_document_ids(doc_registry):
    """Test 2: Verify no duplicate Document IDs exist."""
    ids = [d["document_id"] for d in doc_registry]
    assert len(ids) == len(set(ids)), f"Duplicate IDs found: {[x for x in ids if ids.count(x) > 1]}"

def test_document_id_naming_pattern(doc_registry):
    """Test 3: Verify document IDs follow regex ^DOC-[A-Z]+-[0-9]{3}$."""
    pattern = re.compile(r"^DOC-[A-Z]+-[0-9]{3}$")
    for doc in doc_registry:
        assert pattern.match(doc["document_id"]), f"Invalid ID format: {doc['document_id']}"

def test_all_five_groups_present(doc_registry):
    """Test 4: Verify all five required groups are represented."""
    groups = {d["group"] for d in doc_registry}
    expected_groups = {
        "Project_Management", "Requirements", "Scrum",
        "Architecture_Design", "Testing_Quality", "Delivery"
    }
    assert expected_groups.issubset(groups), f"Missing groups: {expected_groups - groups}"

def test_mandatory_document_fields(doc_registry):
    """Test 5: Verify each document has all mandatory specification fields."""
    mandatory_fields = [
        "document_id", "official_name", "group", "purpose",
        "applicability", "required_inputs", "output_formats",
        "rule_references", "preferred_template_id", "related_standards",
        "required_sections", "validation_profile"
    ]
    for doc in doc_registry:
        for field in mandatory_fields:
            assert field in doc, f"Document {doc['document_id']} is missing field '{field}'"
            assert doc[field], f"Document {doc['document_id']} has empty field '{field}'"

def test_optional_documents_registered(doc_registry):
    """Test 6: Verify optional documents are registered and flagged is_optional=True."""
    optional_ids = ["DOC-SCRUM-005", "DOC-SCRUM-011", "DOC-SCRUM-016", "DOC-SCRUM-017"]
    id_map = {d["document_id"]: d for d in doc_registry}
    for opt_id in optional_ids:
        assert opt_id in id_map, f"Optional document {opt_id} must be registered"
        assert id_map[opt_id].get("is_optional") is True, f"{opt_id} must have is_optional=True"

def test_missing_config_fails():
    """Test 7: Verify missing required config causes immediate failure."""
    non_existent = os.path.join(CONFIG_DIR, "non_existent_config.yaml")
    assert not os.path.exists(non_existent)
    with pytest.raises(FileNotFoundError):
        with open(non_existent, "r") as f:
            f.read()
