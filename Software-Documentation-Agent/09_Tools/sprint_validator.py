from typing import Dict, Any, List

class SprintValidator:
    """Validates Sprint parameters and documents against the official Scrum Guide (Nov 2020)."""

    MAX_SPRINT_DAYS = 31
    MAX_DAILY_SCRUM_MINUTES = 15
    MAX_PLANNING_HOURS_ONE_MONTH = 8.0
    MAX_REVIEW_HOURS_ONE_MONTH = 4.0
    MAX_RETRO_HOURS_ONE_MONTH = 3.0

    @classmethod
    def validate_sprint_duration(cls, days: int) -> Dict[str, Any]:
        """Sprint must be one month or less (<= 31 days)."""
        if days <= 0:
            return {"valid": False, "message": "Độ dài Sprint phải lớn hơn 0 ngày."}
        if days > cls.MAX_SPRINT_DAYS:
            return {
                "valid": False,
                "message": f"Sprint kéo dài {days} ngày vi phạm quy định Scrum Guide 2020 (tối đa 1 tháng / 31 ngày)."
            }
        return {"valid": True, "message": f"Độ dài Sprint {days} ngày hợp lệ theo Scrum Guide."}

    @classmethod
    def validate_planning_timebox(cls, hours: float, sprint_days: int = 30) -> Dict[str, Any]:
        """Sprint Planning is maximum 8 hours for a one-month Sprint, shorter for shorter Sprints."""
        if sprint_days >= 28:
            limit = cls.MAX_PLANNING_HOURS_ONE_MONTH
        elif sprint_days >= 14:
            limit = 4.0 # Typical timebox for 2-week sprint
        else:
            limit = 2.0
            
        if hours > limit:
            return {
                "valid": False,
                "message": f"Sprint Planning {hours}h vượt quá giới hạn khuyến nghị {limit}h cho Sprint {sprint_days} ngày (Tối đa 8h cho Sprint 1 tháng)."
            }
        return {"valid": True, "message": f"Sprint Planning {hours}h tuân thủ timebox (ngưỡng {limit}h)."}

    @classmethod
    def validate_daily_scrum(cls, minutes: int) -> Dict[str, Any]:
        """Daily Scrum must be a 15-minute event for Developers."""
        if minutes > cls.MAX_DAILY_SCRUM_MINUTES:
            return {
                "valid": False,
                "message": f"Daily Scrum {minutes} phút vi phạm giới hạn 15 phút của Scrum Guide 2020."
            }
        return {"valid": True, "message": f"Daily Scrum {minutes} phút hợp lệ theo Scrum Guide."}

    @classmethod
    def validate_review_timebox(cls, hours: float, sprint_days: int = 30) -> Dict[str, Any]:
        """Sprint Review is maximum 4 hours for a one-month Sprint."""
        limit = cls.MAX_REVIEW_HOURS_ONE_MONTH if sprint_days >= 28 else 2.0
        if hours > limit:
            return {
                "valid": False,
                "message": f"Sprint Review {hours}h vượt quá giới hạn {limit}h cho Sprint {sprint_days} ngày (Tối đa 4h cho Sprint 1 tháng)."
            }
        return {"valid": True, "message": f"Sprint Review {hours}h tuân thủ timebox."}

    @classmethod
    def validate_retro_timebox(cls, hours: float, sprint_days: int = 30) -> Dict[str, Any]:
        """Sprint Retrospective is maximum 3 hours for a one-month Sprint."""
        limit = cls.MAX_RETRO_HOURS_ONE_MONTH if sprint_days >= 28 else 1.5
        if hours > limit:
            return {
                "valid": False,
                "message": f"Sprint Retrospective {hours}h vượt quá giới hạn {limit}h cho Sprint {sprint_days} ngày (Tối đa 3h cho Sprint 1 tháng)."
            }
        return {"valid": True, "message": f"Sprint Retrospective {hours}h tuân thủ timebox."}

    @classmethod
    def validate_scrum_myths(cls, text: str) -> List[Dict[str, Any]]:
        """Checks text for common misconceptions falsely attributed to the Scrum Guide."""
        issues = []
        lower = text.lower()
        if "8 giờ làm việc mỗi ngày là quy định của scrum" in lower or "scrum guide bắt buộc 8 tiếng mỗi ngày" in lower:
            issues.append({
                "rule": "RULE-SCRUM-001",
                "severity": "CRITICAL",
                "message": "Không được diễn giải 8 giờ làm việc mỗi ngày là quy định của Scrum Guide (Scrum Guide chỉ quy định timebox sự kiện)."
            })
        if "bắt buộc mọi sprint phải dài 2 tuần" in lower or "scrum bắt buộc sprint đúng 2 tuần" in lower:
            issues.append({
                "rule": "RULE-SCRUM-011",
                "severity": "CRITICAL",
                "message": "Scrum Guide không bắt buộc mọi Sprint phải dài đúng 2 tuần; độ dài từ 1 tháng trở xuống do nhóm quyết định."
            })
        return issues

    @classmethod
    def validate_definition_of_ready_classification(cls, rule_type: str) -> Dict[str, Any]:
        """Definition of Ready must NOT be classified as OFFICIAL_REQUIREMENT of Scrum Guide."""
        if rule_type == "OFFICIAL_REQUIREMENT":
            return {
                "valid": False,
                "message": "Definition of Ready bị phân loại sai thành OFFICIAL_REQUIREMENT. Scrum Guide 2020 không có DoR bắt buộc; phải là RECOMMENDATION hoặc INTERNAL_POLICY."
            }
        return {"valid": True, "message": f"Definition of Ready phân loại đúng ({rule_type})."}
