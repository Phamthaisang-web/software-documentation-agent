import os
import sys
import pytest

AGENT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(AGENT_ROOT, "09_Tools")
sys.path.insert(0, TOOLS_DIR)

from sprint_validator import SprintValidator

def test_sprint_duration_under_or_equal_one_month():
    """Test: Sprints of 7, 14, 21, and 30 days are valid."""
    for days in [7, 14, 21, 28, 30, 31]:
        res = SprintValidator.validate_sprint_duration(days)
        assert res["valid"] is True, f"Sprint {days} days should be valid"

def test_sprint_duration_over_one_month_fails():
    """Test: Sprint longer than one month (> 31 days) fails."""
    for days in [32, 45, 60]:
        res = SprintValidator.validate_sprint_duration(days)
        assert res["valid"] is False, f"Sprint {days} days must violate Scrum Guide"
        assert "tối đa 1 tháng" in res["message"]

def test_sprint_planning_timebox_limits():
    """Test: Sprint Planning <= 8h for 1-month Sprint; excess fails."""
    # 1 month sprint (30 days)
    assert SprintValidator.validate_planning_timebox(8.0, 30)["valid"] is True
    assert SprintValidator.validate_planning_timebox(6.0, 30)["valid"] is True
    assert SprintValidator.validate_planning_timebox(9.0, 30)["valid"] is False

    # 2 weeks sprint (14 days)
    assert SprintValidator.validate_planning_timebox(4.0, 14)["valid"] is True
    assert SprintValidator.validate_planning_timebox(5.0, 14)["valid"] is False

def test_daily_scrum_15_minutes():
    """Test: Daily Scrum must be strictly 15 minutes."""
    assert SprintValidator.validate_daily_scrum(15)["valid"] is True
    assert SprintValidator.validate_daily_scrum(10)["valid"] is True
    assert SprintValidator.validate_daily_scrum(20)["valid"] is False
    assert SprintValidator.validate_daily_scrum(30)["valid"] is False

def test_sprint_review_and_retro_timebox():
    """Test: Sprint Review <= 4h, Retro <= 3h for 1-month Sprint."""
    assert SprintValidator.validate_review_timebox(4.0, 30)["valid"] is True
    assert SprintValidator.validate_review_timebox(4.5, 30)["valid"] is False

    assert SprintValidator.validate_retro_timebox(3.0, 30)["valid"] is True
    assert SprintValidator.validate_retro_timebox(3.5, 30)["valid"] is False

def test_scrum_myths_detection():
    """Test: Reject myths that 8h workday or 2-week Sprint are mandatory Scrum Guide rules."""
    myth1 = "Theo quy định của Scrum Guide, 8 giờ làm việc mỗi ngày là quy định của Scrum bắt buộc."
    issues = SprintValidator.validate_scrum_myths(myth1)
    assert len(issues) >= 1
    assert issues[0]["rule"] == "RULE-SCRUM-001"

    myth2 = "Quy định bắt buộc mọi Sprint phải dài 2 tuần cho tất cả các nhóm."
    issues2 = SprintValidator.validate_scrum_myths(myth2)
    assert len(issues2) >= 1
    assert issues2[0]["rule"] == "RULE-SCRUM-011"

def test_definition_of_ready_not_mandatory_scrum_rule():
    """Test: Definition of Ready cannot be labeled as OFFICIAL_REQUIREMENT of Scrum Guide."""
    fail_res = SprintValidator.validate_definition_of_ready_classification("OFFICIAL_REQUIREMENT")
    assert fail_res["valid"] is False
    assert "Scrum Guide 2020 không có DoR bắt buộc" in fail_res["message"]

    pass_res = SprintValidator.validate_definition_of_ready_classification("RECOMMENDATION")
    assert pass_res["valid"] is True
