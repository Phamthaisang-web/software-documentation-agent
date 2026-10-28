import os
import sys
import pytest

AGENT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(AGENT_ROOT, "09_Tools")
sys.path.insert(0, TOOLS_DIR)

from traceability_engine import TraceabilityEngine

def test_valid_traceability_graph():
    """Test: A fully linked traceability graph passes validation."""
    engine = TraceabilityEngine()
    engine.register_entity("REQ-FUNC-001", "FUNCTIONAL_REQUIREMENT", "User Authentication")
    engine.register_entity("TC-AUTH-001", "TEST_CASE", "Test Valid User Login")
    engine.register_entity("REL-1.0.0", "RELEASE", "Version 1.0.0 Release")

    engine.add_link("REQ-FUNC-001", "TC-AUTH-001", relation="verified_by")
    engine.add_link("TC-AUTH-001", "REL-1.0.0", relation="included_in")

    res = engine.verify_traceability()
    assert res["status"] == "PASSED"
    assert res["summary"]["broken_links_count"] == 0
    assert res["summary"]["orphan_requirements_count"] == 0

def test_detect_broken_link():
    """Test: Referencing a non-existent entity is detected as BROKEN_LINK / MISSING_TARGET."""
    engine = TraceabilityEngine()
    engine.register_entity("REQ-FUNC-001", "FUNCTIONAL_REQUIREMENT", "User Authentication")
    # Link to non-existent TC-999
    engine.add_link("REQ-FUNC-001", "TC-999-NONEXISTENT")

    res = engine.verify_traceability()
    assert res["status"] in ["FAILED", "WARNING"]
    assert res["summary"]["broken_links_count"] >= 1
    assert any(b["target_id"] == "TC-999-NONEXISTENT" for b in res["broken_links"])

def test_detect_orphan_requirement():
    """Test: Functional requirement without test case is detected as orphan."""
    engine = TraceabilityEngine()
    engine.register_entity("REQ-FUNC-002", "FUNCTIONAL_REQUIREMENT", "Payment Processing")
    res = engine.verify_traceability()
    assert res["summary"]["orphan_requirements_count"] >= 1
    assert any(o["id"] == "REQ-FUNC-002" for o in res["orphan_requirements"])

def test_detect_orphan_test_case():
    """Test: Test case not linked to any requirement is detected as orphan."""
    engine = TraceabilityEngine()
    engine.register_entity("TC-ORPHAN-001", "TEST_CASE", "Random Standalone Test")
    res = engine.verify_traceability()
    assert res["summary"]["orphan_test_cases_count"] >= 1
    assert any(o["id"] == "TC-ORPHAN-001" for o in res["orphan_test_cases"])
