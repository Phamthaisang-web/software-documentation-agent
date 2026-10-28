import os
import yaml
import pytest

AGENT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(AGENT_ROOT, "config")

@pytest.fixture
def standards():
    path = os.path.join(CONFIG_DIR, "standards_registry.yaml")
    assert os.path.exists(path), f"Standards registry missing at {path}"
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["standards"]

def test_standards_registry_contains_core_standards(standards):
    """Test: Standards registry contains all required core standards."""
    std_ids = {s["standard_id"] for s in standards}
    required_standards = {
        "STD-SCRUM-2020",
        "STD-REQ-29148",
        "STD-ARCH-42010",
        "STD-TEST-29119-1",
        "STD-TEST-29119-2",
        "STD-TEST-29119-3",
        "STD-TEST-29119-4",
        "STD-PM-21500",
        "STD-API-OAS31",
        "STD-SEC-OWASP2021"
    }
    assert required_standards.issubset(std_ids), f"Missing core standards: {required_standards - std_ids}"

def test_verification_status_validity(standards):
    """Test: All standards have valid verification status enums."""
    valid_statuses = {
        "VERIFIED_OFFICIAL", "VERIFIED_AUTHORITATIVE", "USER_PROVIDED",
        "INTERNAL_POLICY", "UNVERIFIED", "UNAVAILABLE", "SUPERSEDED"
    }
    for s in standards:
        status = s.get("verification_status")
        assert status in valid_statuses, f"Standard {s['standard_id']} has invalid status '{status}'"

def test_official_domains_correctness(standards):
    """Test: Official URLs point to verified official domains."""
    for s in standards:
        url = s.get("url", "")
        if s["standard_id"] == "STD-SCRUM-2020":
            assert "scrumguides.org" in url
        elif "ISO" in s["standard_id"] or s["standard_id"].startswith("STD-TEST-") or s["standard_id"] == "STD-REQ-29148" or s["standard_id"] == "STD-ARCH-42010":
            assert "iso.org" in url
        elif s["standard_id"] == "STD-API-OAS31":
            assert "openapis.org" in url
        elif s["standard_id"] == "STD-SEC-OWASP2021":
            assert "owasp.org" in url

def test_specific_iso_test_standard_urls(standards):
    """Test: Each part of ISO 29119 has a specific ISO catalogue URL, not generic homepage."""
    test_stds = [s for s in standards if s["standard_id"].startswith("STD-TEST-29119-")]
    assert len(test_stds) >= 4
    for ts in test_stds:
        url = ts.get("url", "")
        assert "/standard/" in url, f"Standard {ts['standard_id']} must have specific catalogue URL, got {url}"
