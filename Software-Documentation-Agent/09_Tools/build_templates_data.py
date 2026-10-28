import os
import yaml
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENT_ROOT = os.path.join(BASE_DIR, "Software-Documentation-Agent")
CONFIG_DIR = os.path.join(AGENT_ROOT, "config")
TEMPLATES_DIR = os.path.join(AGENT_ROOT, "03_Templates")

os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. 59 DOCUMENTS DEFINITION
# -------------------------------------------------------------
documents = [
    # NHOM A: Project Management & Requirements (11 docs)
    {
        "document_id": "DOC-PM-001",
        "official_name": "Project Charter",
        "aliases": ["Tai lieu khoi tao du an", "Charter"],
        "group": "Project_Management",
        "purpose": "Uy quyen chinh thuc su ton tai cua du an va trao quyen cho Project Manager",
        "applicability": "Moi du an phan mem o giai doan khoi tao",
        "is_optional": False,
        "required_inputs": ["business_need", "project_objectives", "stakeholders"],
        "optional_inputs": ["budget_constraints", "initial_risks"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Project_Charter_Rules.md"],
        "preferred_template_id": "TPL-PM-001",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Project Objective", "Business Case", "Scope Summary", "Initial Milestones", "Key Stakeholders", "Authority & Approval"],
        "dependencies": [],
        "traceability_requirements": ["DOC-PM-002", "DOC-PM-003"],
        "validation_profile": "PM_CHARTER_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-PM-002",
        "official_name": "Project Scope Statement",
        "aliases": ["Tuyen bo pham vi du an", "Scope Statement"],
        "group": "Project_Management",
        "purpose": "Xac dinh ranh gioi chi tiet ve san pham, ket qua ban giao va cong viec cua du an",
        "applicability": "Giai doan lap ke hoach du an",
        "is_optional": False,
        "required_inputs": ["in_scope", "out_of_scope", "deliverables"],
        "optional_inputs": ["acceptance_criteria", "constraints"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Project_Scope_Rules.md"],
        "preferred_template_id": "TPL-PM-002",
        "related_standards": ["STD-PM-21500", "STD-REQ-29148"],
        "required_sections": ["Project Scope Description", "Major Deliverables", "Acceptance Criteria", "Exclusions / Out of Scope", "Constraints & Assumptions"],
        "dependencies": ["DOC-PM-001"],
        "traceability_requirements": ["DOC-REQ-001", "DOC-DEL-002"],
        "validation_profile": "PM_SCOPE_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-PM-003",
        "official_name": "Stakeholder Register",
        "aliases": ["Danh sach ben lien quan", "Stakeholder Matrix"],
        "group": "Project_Management",
        "purpose": "Nhan dien va quan ly thong tin, vai tro, ky vong cua cac ben lien quan",
        "applicability": "Khoi tao va xuyen suot vong doi du an",
        "is_optional": False,
        "required_inputs": ["stakeholder_list", "roles"],
        "optional_inputs": ["influence_level", "communication_needs"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Stakeholder_Register_Rules.md"],
        "preferred_template_id": "TPL-PM-003",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Stakeholder ID", "Name / Organization", "Role / Title", "Interest & Influence", "Expectations", "Engagement Strategy"],
        "dependencies": ["DOC-PM-001"],
        "traceability_requirements": ["DOC-REQ-001"],
        "validation_profile": "PM_STAKEHOLDER_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-REQ-001",
        "official_name": "Software Requirements Specification",
        "aliases": ["SRS", "Dac ta yeu cau phan mem"],
        "group": "Requirements",
        "purpose": "Mieu ta toan dien cac yeu cau chuc nang, phi chuc nang, giao dien va rang buoc he thong theo ISO 29148",
        "applicability": "Phan tich va dac ta yeu cau ky thuat phan mem",
        "is_optional": False,
        "required_inputs": ["functional_requirements", "non_functional_requirements", "system_interfaces"],
        "optional_inputs": ["user_characteristics", "assumptions"],
        "output_formats": ["docx", "md"],
        "rule_references": ["SRS_Rules.md"],
        "preferred_template_id": "TPL-REQ-001",
        "related_standards": ["STD-REQ-29148"],
        "required_sections": ["Purpose & Scope", "Overall Description", "System Features / Functional Requirements", "Non-Functional Requirements", "External Interface Requirements", "Verification Criteria"],
        "dependencies": ["DOC-PM-002"],
        "traceability_requirements": ["DOC-ARCH-001", "DOC-TEST-001"],
        "validation_profile": "REQ_SRS_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-REQ-002",
        "official_name": "Product Vision",
        "aliases": ["Tam nhin san pham", "Vision Document"],
        "group": "Requirements",
        "purpose": "Dinh huong muc tieu chien luoc dai han va gia tri cot loi cua san pham",
        "applicability": "Giai doan khoi tao san pham",
        "is_optional": False,
        "required_inputs": ["target_audience", "problem_statement", "value_proposition"],
        "optional_inputs": ["competitor_analysis", "success_metrics"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Product_Vision_Rules.md"],
        "preferred_template_id": "TPL-REQ-002",
        "related_standards": ["STD-REQ-29148"],
        "required_sections": ["Target Customer & Need", "Product Vision Statement", "Key Capabilities", "Business Goals & Success Metrics", "Strategic Alignment"],
        "dependencies": [],
        "traceability_requirements": ["DOC-SCRUM-002", "DOC-REQ-001"],
        "validation_profile": "REQ_VISION_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-REQ-003",
        "official_name": "Functional Requirements Specification",
        "aliases": ["FRS", "Dac ta yeu cau chuc nang"],
        "group": "Requirements",
        "purpose": "Dac ta chi tiet tung chuc nang, logic nghiep vu, dau vao va dau ra",
        "applicability": "Phan tich chuc nang chi tiet",
        "is_optional": False,
        "required_inputs": ["feature_breakdown", "business_logic", "input_output_data"],
        "optional_inputs": ["exception_flows", "data_validation_rules"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Functional_Requirements_Rules.md"],
        "preferred_template_id": "TPL-REQ-003",
        "related_standards": ["STD-REQ-29148"],
        "required_sections": ["Feature ID", "Module / Category", "Feature Name", "Detailed Description", "Business Rules", "Verification Method"],
        "dependencies": ["DOC-REQ-001"],
        "traceability_requirements": ["DOC-REQ-005", "DOC-TEST-003"],
        "validation_profile": "REQ_FUNCTIONAL_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-REQ-004",
        "official_name": "Non-Functional Requirements Specification",
        "aliases": ["NFRS", "Dac ta yeu cau phi chuc nang"],
        "group": "Requirements",
        "purpose": "Xac dinh cac chi tieu ve hieu nang, bao mat, do tin cay, kha nang mo rong",
        "applicability": "Xuyen suot kien truc va kiem thu",
        "is_optional": False,
        "required_inputs": ["performance_metrics", "security_requirements", "scalability_goals"],
        "optional_inputs": ["compliance_rules", "availability_sla"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Non_Functional_Requirements_Rules.md"],
        "preferred_template_id": "TPL-REQ-004",
        "related_standards": ["STD-REQ-29148", "STD-SEC-OWASP2021"],
        "required_sections": ["NFR ID", "Category", "Target Metric / Threshold", "Measurement Method", "Priority", "Architecture Impact"],
        "dependencies": ["DOC-REQ-001"],
        "traceability_requirements": ["DOC-ARCH-001", "DOC-TEST-001"],
        "validation_profile": "REQ_NON_FUNCTIONAL_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-REQ-005",
        "official_name": "Use Case Specification",
        "aliases": ["Dac ta ca su dung", "Use Case Document"],
        "group": "Requirements",
        "purpose": "Mo ta luong tuong tac giua tac nhan (Actor) va he thong de dat duoc muc tieu",
        "applicability": "Phan tich hanh vi he thong",
        "is_optional": False,
        "required_inputs": ["actors", "main_flow", "preconditions"],
        "optional_inputs": ["alternative_flows", "postconditions"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Use_Case_Rules.md"],
        "preferred_template_id": "TPL-REQ-005",
        "related_standards": ["STD-REQ-29148"],
        "required_sections": ["Use Case ID", "Use Case Name", "Actors", "Preconditions", "Basic Flow", "Alternative / Exception Flows", "Postconditions"],
        "dependencies": ["DOC-REQ-003"],
        "traceability_requirements": ["DOC-ARCH-002", "DOC-TEST-002"],
        "validation_profile": "REQ_USECASE_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-REQ-006",
        "official_name": "User Story Specification",
        "aliases": ["User Story Document", "Dac ta User Story"],
        "group": "Requirements",
        "purpose": "Dac ta yeu cau duoi goc do nguoi dung theo cau truc As a/I want/So that",
        "applicability": "Phat trien theo Agile / Scrum",
        "is_optional": False,
        "required_inputs": ["user_persona", "user_goal", "business_value"],
        "optional_inputs": ["story_dependencies", "estimated_complexity"],
        "output_formats": ["xlsx", "docx", "md"],
        "rule_references": ["User_Story_Rules.md"],
        "preferred_template_id": "TPL-REQ-006",
        "related_standards": ["STD-REQ-29148", "STD-SCRUM-2020"],
        "required_sections": ["Story ID", "Title", "Role (As a)", "Action (I want)", "Benefit (So that)", "Priority", "Status"],
        "dependencies": ["DOC-REQ-002"],
        "traceability_requirements": ["DOC-REQ-008", "DOC-SCRUM-003"],
        "validation_profile": "REQ_USERSTORY_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-REQ-007",
        "official_name": "Requirements Traceability Matrix",
        "aliases": ["RTM", "Ma tran truy xuat yeu cau"],
        "group": "Requirements",
        "purpose": "Theo doi lien ket 2 chieu tu yeu cau, thiet ke, ca kiem thu den ket qua ban giao",
        "applicability": "Quan ly chat luong va truy xuat nguon goc",
        "is_optional": False,
        "required_inputs": ["requirements_list", "design_links", "test_case_links"],
        "optional_inputs": ["defect_links", "release_links"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["RTM_Rules.md"],
        "preferred_template_id": "TPL-REQ-007",
        "related_standards": ["STD-REQ-29148"],
        "required_sections": ["Requirement ID", "Requirement Description", "Category", "Architecture / Design ID", "Test Case ID", "Test Execution Status", "Deliverable / Release"],
        "dependencies": ["DOC-REQ-001", "DOC-TEST-003"],
        "traceability_requirements": ["DOC-DEL-009"],
        "validation_profile": "REQ_RTM_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-REQ-008",
        "official_name": "Acceptance Criteria Specification",
        "aliases": ["Tieu chi chap nhan", "AC Spec"],
        "group": "Requirements",
        "purpose": "Dac ta cac tieu chi kiem chung cu the (Given-When-Then hoac checklist) de xac nhan User Story hoan thanh",
        "applicability": "Xac nhan yeu cau va nghiem thu story",
        "is_optional": False,
        "required_inputs": ["story_id", "conditions", "expected_behavior"],
        "optional_inputs": ["edge_cases", "boundary_values"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Acceptance_Criteria_Rules.md"],
        "preferred_template_id": "TPL-REQ-008",
        "related_standards": ["STD-REQ-29148", "STD-SCRUM-2020"],
        "required_sections": ["Story ID", "Criterion ID", "Scenario Title", "Given Condition", "When Action", "Then Expected Result", "Verification Status"],
        "dependencies": ["DOC-REQ-006"],
        "traceability_requirements": ["DOC-TEST-003"],
        "validation_profile": "REQ_AC_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },

    # NHOM B: SCRUM (17 docs)
    {
        "document_id": "DOC-SCRUM-001",
        "official_name": "Product Backlog",
        "aliases": ["Danh muc san pham", "PBL"],
        "group": "Scrum",
        "purpose": "Danh sach sap xep theo thu tu uu tien cua tat ca nhung gi can thiet cho san pham",
        "applicability": "Vong doi phat trien Scrum",
        "is_optional": False,
        "required_inputs": ["product_goal", "item_list", "ordering"],
        "optional_inputs": ["estimates", "value_points"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Scrum_Rules.md", "Product_Backlog_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-001",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Item ID", "Title", "Description / Acceptance Criteria", "Order / Priority", "Estimate", "Status", "Product Goal Alignment"],
        "dependencies": ["DOC-SCRUM-002"],
        "traceability_requirements": ["DOC-SCRUM-007"],
        "validation_profile": "SCRUM_PBL_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-002",
        "official_name": "Product Goal",
        "aliases": ["Muc tieu san pham", "Scrum Product Goal"],
        "group": "Scrum",
        "purpose": "Cam ket chinh thuc cua Product Backlog, mo ta trang thai tuong lai cua san pham",
        "applicability": "Scrum Guide 2020 bat buoc",
        "is_optional": False,
        "required_inputs": ["vision", "current_target_state"],
        "optional_inputs": ["business_metrics"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "Product_Goal_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-002",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Product Goal Statement", "Target Outcome", "Evaluation Criteria", "Progress Indicator", "Commitment Record"],
        "dependencies": ["DOC-REQ-002"],
        "traceability_requirements": ["DOC-SCRUM-001"],
        "validation_profile": "SCRUM_PRODUCT_GOAL_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-003",
        "official_name": "Product Backlog Item (PBI) / User Story",
        "aliases": ["PBI", "Scrum User Story"],
        "group": "Scrum",
        "purpose": "Dac ta tung muc trong Product Backlog gom mo ta, thu tu, uoc luong va tieu chi chap nhan",
        "applicability": "Moi item duoc quan ly trong Product Backlog",
        "is_optional": False,
        "required_inputs": ["pbi_description", "ordering_rank"],
        "optional_inputs": ["story_points", "dependencies"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "PBI_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-003",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["PBI ID", "Title", "Description", "Value to User", "Acceptance Criteria", "Order / Priority", "Estimation"],
        "dependencies": ["DOC-SCRUM-001"],
        "traceability_requirements": ["DOC-SCRUM-007"],
        "validation_profile": "SCRUM_PBI_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-004",
        "official_name": "Backlog Refinement Record",
        "aliases": ["Bien ban lam min backlog", "Grooming Record"],
        "group": "Scrum",
        "purpose": "Ghi lai hoat dong lam ro, chia nho va uoc luong cac PBI truoc Sprint Planning",
        "applicability": "Hoat dong lien tuc trong Sprint",
        "is_optional": False,
        "required_inputs": ["items_reviewed", "clarifications_made"],
        "optional_inputs": ["re_estimations", "split_items"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "Backlog_Refinement_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-004",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Refinement Date", "Items Reviewed", "Clarifications Added", "Items Split / Re-estimated", "Ready for Sprint Planning Items"],
        "dependencies": ["DOC-SCRUM-001"],
        "traceability_requirements": ["DOC-SCRUM-006"],
        "validation_profile": "SCRUM_REFINEMENT_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-005",
        "official_name": "Release Plan / Release Backlog",
        "aliases": ["Ke hoach phat hanh", "Release Schedule"],
        "group": "Scrum",
        "purpose": "Dinh hinh ke hoach ban giao cac phien ban phan mem qua cac Sprint (Thong le tuy chon)",
        "applicability": "Tuy chon theo quy mo du an",
        "is_optional": True,
        "required_inputs": ["target_release_dates", "candidate_pbis"],
        "optional_inputs": ["forecast_velocity", "release_themes"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Scrum_Rules.md", "Release_Plan_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-005",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Release ID", "Target Date", "Release Goal", "Included PBIs", "Release Risks & Assumptions"],
        "dependencies": ["DOC-SCRUM-001"],
        "traceability_requirements": ["DOC-DEL-009"],
        "validation_profile": "SCRUM_RELEASE_PLAN_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-006",
        "official_name": "Sprint Planning Record",
        "aliases": ["Bien ban lap ke hoach Sprint", "Sprint Planning Minutes"],
        "group": "Scrum",
        "purpose": "Ghi lai ket qua phien hop Sprint Planning: Tai sao, Cai gi va Lam the nao",
        "applicability": "Dau moi Sprint. Timebox: toi da 8h cho Sprint 1 thang",
        "is_optional": False,
        "required_inputs": ["sprint_goal", "selected_pbis", "plan_for_delivery"],
        "optional_inputs": ["capacity", "scrum_team_attendees"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "Sprint_Planning_Rules.md", "Timebox_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-006",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Sprint Identification & Duration", "Topic 1: Why is this Sprint valuable? (Sprint Goal)", "Topic 2: What can be Done this Sprint? (Selected PBIs)", "Topic 3: How will the chosen work get done?", "Timebox Compliance Record"],
        "dependencies": ["DOC-SCRUM-001"],
        "traceability_requirements": ["DOC-SCRUM-007", "DOC-SCRUM-008"],
        "validation_profile": "SCRUM_PLANNING_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-007",
        "official_name": "Sprint Backlog",
        "aliases": ["Ke hoach cong viec Sprint", "SBL"],
        "group": "Scrum",
        "purpose": "Ke hoach do va cho Developers gom Sprint Goal, cac PBI duoc chon va ke hoach hanh dong tao Increment",
        "applicability": "Moi Sprint trong Scrum",
        "is_optional": False,
        "required_inputs": ["sprint_goal", "selected_pbis", "actionable_plan"],
        "optional_inputs": ["tasks", "remaining_work"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Scrum_Rules.md", "Sprint_Backlog_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-007",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Sprint Goal Header", "Selected PBIs", "Actionable Tasks Breakdown", "Task Status (To Do, Doing, Done)", "Assignee (if known)", "Remaining Work"],
        "dependencies": ["DOC-SCRUM-006", "DOC-SCRUM-008"],
        "traceability_requirements": ["DOC-SCRUM-015"],
        "validation_profile": "SCRUM_BACKLOG_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-008",
        "official_name": "Sprint Goal",
        "aliases": ["Muc tieu Sprint", "Goal of Sprint"],
        "group": "Scrum",
        "purpose": "Cam ket duy nhat cho Sprint Backlog, mang lai su tap trung va linh hoat ve pham vi",
        "applicability": "Bat buoc cho tung Sprint",
        "is_optional": False,
        "required_inputs": ["sprint_value_target", "rationale"],
        "optional_inputs": ["success_criteria"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "Sprint_Goal_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-008",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Sprint Number", "Sprint Goal Statement", "Business Value & Context", "Flexibility Boundaries", "Evaluation Criteria"],
        "dependencies": ["DOC-SCRUM-006"],
        "traceability_requirements": ["DOC-SCRUM-007", "DOC-SCRUM-012"],
        "validation_profile": "SCRUM_GOAL_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-009",
        "official_name": "Task Breakdown",
        "aliases": ["Phan ra cong viec Sprint", "Sprint Tasks"],
        "group": "Scrum",
        "purpose": "Phan chia cac PBI thanh cac cong viec ky thuat nho du de thuc hien trong mot hoac vai ngay",
        "applicability": "Xuyen suot Sprint boi Developers",
        "is_optional": False,
        "required_inputs": ["pbi_id", "task_descriptions"],
        "optional_inputs": ["estimated_hours", "owner"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Scrum_Rules.md", "Task_Breakdown_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-009",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Task ID", "Parent PBI ID", "Task Description", "Task Type", "Estimate", "Status", "Assignee"],
        "dependencies": ["DOC-SCRUM-007"],
        "traceability_requirements": ["DOC-SCRUM-015"],
        "validation_profile": "SCRUM_TASK_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-010",
        "official_name": "Sprint Schedule",
        "aliases": ["Lich trinh Sprint", "Sprint Calendar"],
        "group": "Scrum",
        "purpose": "Xac dinh khung thoi gian, ngay bat dau, ket thuc va thoi gian bieu cac su kien Scrum",
        "applicability": "Moi Sprint; do dai toi da 1 thang",
        "is_optional": False,
        "required_inputs": ["start_date", "end_date", "event_timeboxes"],
        "optional_inputs": ["holidays", "working_days"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Scrum_Rules.md", "Sprint_Schedule_Rules.md", "Timebox_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-010",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Sprint ID", "Start Date", "End Date", "Duration in Weeks / Days", "Scrum Events Schedule", "Timebox Limits Check"],
        "dependencies": ["DOC-SCRUM-006"],
        "traceability_requirements": ["DOC-DEL-001"],
        "validation_profile": "SCRUM_SCHEDULE_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-011",
        "official_name": "Daily Scrum Log",
        "aliases": ["Nhat ky Daily Scrum", "Daily Standup Notes"],
        "group": "Scrum",
        "purpose": "Ghi nhan tien do va tro ngai trong su kien 15 phut Daily Scrum (Thong le tuy chon)",
        "applicability": "Tuy chon theo nhu cau nhom (Timebox Daily Scrum bat buoc 15 phut)",
        "is_optional": True,
        "required_inputs": ["date", "progress_towards_sprint_goal", "impediments"],
        "optional_inputs": ["plan_for_next_24h"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Scrum_Rules.md", "Daily_Scrum_Log_Rules.md", "Timebox_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-011",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Date", "Progress towards Sprint Goal", "Impediments / Blockers", "Adjustments to Sprint Plan", "15-min Timebox Compliance"],
        "dependencies": ["DOC-SCRUM-007"],
        "traceability_requirements": ["DOC-DEL-004"],
        "validation_profile": "SCRUM_DAILY_LOG_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-012",
        "official_name": "Sprint Review Report",
        "aliases": ["Bao cao Sprint Review", "Sprint Demo Report"],
        "group": "Scrum",
        "purpose": "Kiem tra ket qua Increment duoc tao ra va xac dinh cac dieu chinh Backlog tiep theo",
        "applicability": "Cuoi Sprint. Timebox: toi da 4h cho Sprint 1 thang",
        "is_optional": False,
        "required_inputs": ["completed_pbis", "demonstrated_increment", "stakeholder_feedback"],
        "optional_inputs": ["not_completed_items", "backlog_adjustments"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "Sprint_Review_Rules.md", "Timebox_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-012",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Sprint Identification", "Sprint Goal Assessment", "Items Done (Meeting DoD)", "Items Not Done (Returned to PBL)", "Demonstrated Capabilities", "Stakeholder Feedback & Next Steps"],
        "dependencies": ["DOC-SCRUM-008", "DOC-SCRUM-014", "DOC-SCRUM-015"],
        "traceability_requirements": ["DOC-SCRUM-001"],
        "validation_profile": "SCRUM_REVIEW_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-013",
        "official_name": "Sprint Retrospective Report",
        "aliases": ["Bao cao cai tien Sprint", "Retrospective Notes"],
        "group": "Scrum",
        "purpose": "Lap ke hoach nang cao chat luong va hieu qua ve con nguoi, quan he, quy trinh va cong cu",
        "applicability": "Ket thuc Sprint. Timebox: toi da 3h cho Sprint 1 thang",
        "is_optional": False,
        "required_inputs": ["what_went_well", "what_could_be_improved", "actionable_improvements"],
        "optional_inputs": ["previous_actions_review"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "Sprint_Retrospective_Rules.md", "Timebox_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-013",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Sprint ID", "Attendees / Roles", "Successes / Positives", "Challenges / Impediments", "Action Items for Next Sprint (with Owner)", "Definition of Done Enhancements"],
        "dependencies": ["DOC-SCRUM-012"],
        "traceability_requirements": ["DOC-SCRUM-006"],
        "validation_profile": "SCRUM_RETRO_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-014",
        "official_name": "Definition of Done",
        "aliases": ["Dinh nghia Hoan thanh", "DoD"],
        "group": "Scrum",
        "purpose": "Mo ta hinh thuc ve trang thai cua Increment khi no dap ung cac bien phap chat luong can thiet",
        "applicability": "Cam ket bat buoc cua Scrum Guide 2020 cho Increment",
        "is_optional": False,
        "required_inputs": ["quality_criteria", "testing_criteria", "documentation_criteria"],
        "optional_inputs": ["compliance_checks", "deployment_criteria"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "Definition_of_Done_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-014",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["DoD Scope", "Coding & Style Standards", "Automated Testing & Coverage Requirements", "Code Review Criteria", "Documentation Completeness", "Deployment & Verification"],
        "dependencies": [],
        "traceability_requirements": ["DOC-SCRUM-015", "DOC-TEST-007"],
        "validation_profile": "SCRUM_DOD_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-015",
        "official_name": "Increment / Sprint Deliverables Record",
        "aliases": ["Ho so ban giao Increment", "Sprint Deliverables"],
        "group": "Scrum",
        "purpose": "Ghi nhan Increment thuc te dat Definition of Done va co the su dung duoc ngay",
        "applicability": "Ket qua bat buoc cua moi Sprint",
        "is_optional": False,
        "required_inputs": ["increment_features", "dod_compliance_status"],
        "optional_inputs": ["build_artifacts", "commit_hash"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Scrum_Rules.md", "Sprint_Deliverables_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-015",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Increment Version / Tag", "Included PBIs Verified against DoD", "Deployable Build / Package Reference", "Verification Evidence", "Release Readiness Status"],
        "dependencies": ["DOC-SCRUM-007", "DOC-SCRUM-014"],
        "traceability_requirements": ["DOC-DEL-009"],
        "validation_profile": "SCRUM_INCREMENT_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-016",
        "official_name": "Sprint Metrics / Burndown Report",
        "aliases": ["Bao cao chi so Sprint", "Burndown Chart Report"],
        "group": "Scrum",
        "purpose": "Tong hop cac chi so tien do, toc do va do thi burndown dua tren du lieu thuc te (Thong le tuy chon)",
        "applicability": "Tuy chon theo thong le nhom (Khong phai bat buoc cua Scrum Guide)",
        "is_optional": True,
        "required_inputs": ["daily_remaining_points_or_tasks", "total_planned"],
        "optional_inputs": ["velocity_history", "spillover_points"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Scrum_Rules.md", "Sprint_Metrics_Rules.md", "Estimation_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-016",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Sprint Identification", "Planned Points vs Completed Points", "Daily Burndown Data Table", "Velocity Analysis", "Optional Practice Disclaimer"],
        "dependencies": ["DOC-SCRUM-007"],
        "traceability_requirements": ["DOC-DEL-008"],
        "validation_profile": "SCRUM_METRICS_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-SCRUM-017",
        "official_name": "Definition of Ready",
        "aliases": ["Dinh nghia San sang", "DoR"],
        "group": "Scrum",
        "purpose": "Quy uoc noi bo cua nhom de xac nhan PBI da du ro rang de dua vao Sprint Planning (Thong le bo tro)",
        "applicability": "Thong le tuy chon cua nhom; phai danh dau ro la INTERNAL_POLICY, khong phai Scrum Guide",
        "is_optional": True,
        "required_inputs": ["pbi_readiness_checklist"],
        "optional_inputs": ["dependencies_resolved_check", "estimation_rule"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Scrum_Rules.md", "Definition_of_Ready_Rules.md"],
        "preferred_template_id": "TPL-SCRUM-017",
        "related_standards": ["STD-SCRUM-2020"],
        "required_sections": ["Scope & Optional Status Notice", "PBI Clarity Criteria", "Acceptance Criteria Clarity", "Estimation Completeness", "Dependency Resolution Criteria"],
        "dependencies": [],
        "traceability_requirements": ["DOC-SCRUM-003"],
        "validation_profile": "SCRUM_DOR_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },

    # NHOM C: Architecture & Design (10 docs)
    {
        "document_id": "DOC-ARCH-001",
        "official_name": "Software Architecture Description",
        "aliases": ["SAD", "Mo ta kien truc phan mem"],
        "group": "Architecture_Design",
        "purpose": "Dac ta tong the kien truc phan mem qua cac goc nhin theo ISO/IEC/IEEE 42010",
        "applicability": "Thiet ke kien truc he thong",
        "is_optional": False,
        "required_inputs": ["system_context", "architectural_views", "key_decisions"],
        "optional_inputs": ["quality_attribute_scenarios", "evolution_paths"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Architecture_Rules.md"],
        "preferred_template_id": "TPL-ARCH-001",
        "related_standards": ["STD-ARCH-42010"],
        "required_sections": ["Architecture Context & Stakeholders", "Architectural Viewpoints", "Component / Module View", "Execution / Runtime View", "Deployment View", "Quality Attribute Realization"],
        "dependencies": ["DOC-REQ-001", "DOC-REQ-004"],
        "traceability_requirements": ["DOC-ARCH-007", "DOC-ARCH-008"],
        "validation_profile": "ARCH_SAD_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-002",
        "official_name": "Software Design Description",
        "aliases": ["SDD", "Dac ta thiet ke phan mem chi tiet"],
        "group": "Architecture_Design",
        "purpose": "Mo ta thiet ke chi tiet cac module, lop, giao dien va luong du lieu",
        "applicability": "Thiet ke chi tiet truoc hoac song song lap trinh",
        "is_optional": False,
        "required_inputs": ["module_interfaces", "class_designs", "interaction_flows"],
        "optional_inputs": ["design_patterns_used"],
        "output_formats": ["docx", "md"],
        "rule_references": ["System_Design_Rules.md"],
        "preferred_template_id": "TPL-ARCH-002",
        "related_standards": ["STD-ARCH-42010"],
        "required_sections": ["Design Overview", "Module Decomposition", "Interface Specifications", "Data Flow & Interaction Diagrams", "Error Handling Strategy"],
        "dependencies": ["DOC-ARCH-001"],
        "traceability_requirements": ["DOC-REQ-003", "DOC-TEST-003"],
        "validation_profile": "ARCH_SDD_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-003",
        "official_name": "Database Design Specification",
        "aliases": ["Thiet ke co so du lieu", "Database Spec"],
        "group": "Architecture_Design",
        "purpose": "Dac ta chi tiet schema, bang, khoa, quan he, index va rang buoc CSDL",
        "applicability": "He thong co luu tru du lieu",
        "is_optional": False,
        "required_inputs": ["table_definitions", "foreign_keys", "indexes"],
        "optional_inputs": ["migration_scripts", "data_retention_policy"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Database_Design_Rules.md"],
        "preferred_template_id": "TPL-ARCH-003",
        "related_standards": ["STD-ARCH-42010"],
        "required_sections": ["Database Engine & Version", "Logical Data Model", "Physical Schema Specification (Tables, Columns, Types, Constraints)", "Indexes & Optimization", "Migration Strategy"],
        "dependencies": ["DOC-ARCH-004"],
        "traceability_requirements": ["DOC-REQ-003"],
        "validation_profile": "ARCH_DB_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-004",
        "official_name": "Entity Relationship Diagram",
        "aliases": ["ERD", "So do thuc the quan he"],
        "group": "Architecture_Design",
        "purpose": "Truc quan hoa cac thuc the du lieu va quan he 1-1, 1-n, n-n giua chung",
        "applicability": "He thong co mo hinh thuc the du lieu",
        "is_optional": False,
        "required_inputs": ["entity_list", "relationships"],
        "optional_inputs": ["cardinalities", "attribute_details"],
        "output_formats": ["mmd", "md"],
        "rule_references": ["ERD_Rules.md"],
        "preferred_template_id": "TPL-ARCH-004",
        "related_standards": ["STD-ARCH-42010"],
        "required_sections": ["Entity Definitions", "Relationship Matrix", "Mermaid ER Diagram Source", "Cardinality Descriptions"],
        "dependencies": [],
        "traceability_requirements": ["DOC-ARCH-003"],
        "validation_profile": "ARCH_ERD_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-005",
        "official_name": "API Specification",
        "aliases": ["OpenAPI Spec", "Dac ta API"],
        "group": "Architecture_Design",
        "purpose": "Dac ta toan bo endpoint, HTTP method, payload, ma loi va co che xac thuc theo OpenAPI 3.1",
        "applicability": "He thong co giao dien Web / REST API",
        "is_optional": False,
        "required_inputs": ["endpoints", "schemas", "security_schemes"],
        "optional_inputs": ["example_requests", "response_headers"],
        "output_formats": ["yaml", "json", "md"],
        "rule_references": ["API_Specification_Rules.md"],
        "preferred_template_id": "TPL-ARCH-005",
        "related_standards": ["STD-API-OAS31"],
        "required_sections": ["OpenAPI Version & Info", "Base URL & Servers", "Security Schemes", "Endpoints / Paths", "Component Schemas", "Standard Error Codes"],
        "dependencies": ["DOC-ARCH-001"],
        "traceability_requirements": ["DOC-REQ-003", "DOC-TEST-003"],
        "validation_profile": "ARCH_API_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-006",
        "official_name": "UI/UX Specification",
        "aliases": ["Dac ta giao dien nguoi dung", "UI Spec"],
        "group": "Architecture_Design",
        "purpose": "Dac ta luong dieu huong man hinh, component UI, quy tac tuong tac va style guide",
        "applicability": "He thong co giao dien nguoi dung (Frontend/Mobile)",
        "is_optional": False,
        "required_inputs": ["screens_list", "navigation_flow"],
        "optional_inputs": ["color_palette", "wireframes_ref"],
        "output_formats": ["docx", "md"],
        "rule_references": ["UI_UX_Specification_Rules.md"],
        "preferred_template_id": "TPL-ARCH-006",
        "related_standards": ["STD-ARCH-42010"],
        "required_sections": ["Design Principles & Guidelines", "Screen Catalog & Sitemap", "Navigation Flows", "Component Specifications", "Responsive & Accessibility Rules"],
        "dependencies": ["DOC-REQ-005"],
        "traceability_requirements": ["DOC-REQ-003"],
        "validation_profile": "ARCH_UIUX_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-007",
        "official_name": "Component Diagram",
        "aliases": ["So do thanh phan", "Component Architecture"],
        "group": "Architecture_Design",
        "purpose": "Mo ta cac thanh phan phan mem (packages, modules, services) va giao dien lien ket giua chung",
        "applicability": "Moi he thong module / microservice",
        "is_optional": False,
        "required_inputs": ["components", "interfaces", "dependencies"],
        "optional_inputs": ["ports", "protocols"],
        "output_formats": ["mmd", "md"],
        "rule_references": ["Component_Diagram_Rules.md"],
        "preferred_template_id": "TPL-ARCH-007",
        "related_standards": ["STD-ARCH-42010"],
        "required_sections": ["Component Catalog", "Interface Definitions", "Mermaid Component Diagram Source", "Dependency Explanations"],
        "dependencies": ["DOC-ARCH-001"],
        "traceability_requirements": ["DOC-ARCH-002"],
        "validation_profile": "ARCH_COMPONENT_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-008",
        "official_name": "Deployment Architecture",
        "aliases": ["Kien truc trien khai", "Deployment Diagram"],
        "group": "Architecture_Design",
        "purpose": "Dac ta ha tang phan cung, mang, container, cum server va vi tri chay cac thanh phan",
        "applicability": "Ha tang va van hanh he thong",
        "is_optional": False,
        "required_inputs": ["nodes", "networks", "container_runtimes"],
        "optional_inputs": ["cloud_regions", "firewalls"],
        "output_formats": ["mmd", "docx", "md"],
        "rule_references": ["Deployment_Architecture_Rules.md"],
        "preferred_template_id": "TPL-ARCH-008",
        "related_standards": ["STD-ARCH-42010"],
        "required_sections": ["Deployment Topology", "Node & Resource Allocations", "Network Topology & Ports", "Mermaid Deployment Diagram Source", "Disaster Recovery Setup"],
        "dependencies": ["DOC-ARCH-001"],
        "traceability_requirements": ["DOC-DEL-011", "DOC-DEL-013"],
        "validation_profile": "ARCH_DEPLOYMENT_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-009",
        "official_name": "Technical Design Document",
        "aliases": ["TDD", "Thiet ke ky thuat"],
        "group": "Architecture_Design",
        "purpose": "Tai lieu hop nhat ve giai phap ky thuat, thuat toan, xu ly ngoai le va bao mat",
        "applicability": "Cac tinh nang ky thuat phuc tap",
        "is_optional": False,
        "required_inputs": ["feature_architecture", "algorithms", "security_model"],
        "optional_inputs": ["benchmarks", "performance_tradeoffs"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Technical_Design_Rules.md"],
        "preferred_template_id": "TPL-ARCH-009",
        "related_standards": ["STD-ARCH-42010", "STD-SEC-OWASP2021"],
        "required_sections": ["Technical Overview", "Detailed Solution Design", "Algorithms & Data Structures", "Security Controls (OWASP)", "Performance & Scalability Considerations"],
        "dependencies": ["DOC-ARCH-001", "DOC-REQ-004"],
        "traceability_requirements": ["DOC-TEST-003"],
        "validation_profile": "ARCH_TECH_DESIGN_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-ARCH-010",
        "official_name": "Architecture Decision Record",
        "aliases": ["ADR", "Ban ghi quyet dinh kien truc"],
        "group": "Architecture_Design",
        "purpose": "Ghi lai boi canh, quyet dinh, cac lua chon da can nhac va he qua cua mot quyet dinh kien truc quan trong",
        "applicability": "Moi quyet dinh kien truc quan trong trong du an",
        "is_optional": False,
        "required_inputs": ["context", "decision", "consequences"],
        "optional_inputs": ["options_considered", "status"],
        "output_formats": ["md"],
        "rule_references": ["ADR_Rules.md"],
        "preferred_template_id": "TPL-ARCH-010",
        "related_standards": ["STD-ARCH-42010"],
        "required_sections": ["ADR ID & Title", "Status (Proposed, Accepted, Deprecated, Superseded)", "Context & Problem Statement", "Considered Options", "Decision Outcome & Rationale", "Consequences (Positive & Negative)"],
        "dependencies": [],
        "traceability_requirements": ["DOC-ARCH-001", "DOC-DEL-005"],
        "validation_profile": "ARCH_ADR_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },

    # NHOM D: Testing & Quality (8 docs)
    {
        "document_id": "DOC-TEST-001",
        "official_name": "Test Plan",
        "aliases": ["Ke hoach kiem thu", "Software Test Plan"],
        "group": "Testing_Quality",
        "purpose": "Xac dinh pham vi, cach tiep can, tai nguyen, lich trinh va tieu chi dung kiem thu theo ISO 29119-3",
        "applicability": "Moi du an hoac dot release",
        "is_optional": False,
        "required_inputs": ["test_scope", "test_levels", "suspension_criteria"],
        "optional_inputs": ["test_environment_needs", "staffing"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Test_Plan_Rules.md"],
        "preferred_template_id": "TPL-TEST-001",
        "related_standards": ["STD-TEST-29119-1", "STD-TEST-29119-2", "STD-TEST-29119-3"],
        "required_sections": ["Test Strategy & Approach", "In-Scope & Out-of-Scope Testing", "Test Levels (Unit, Integration, System, Acceptance)", "Entry & Exit Criteria", "Test Environment Requirements", "Test Schedule & Roles"],
        "dependencies": ["DOC-REQ-001"],
        "traceability_requirements": ["DOC-TEST-003", "DOC-TEST-004"],
        "validation_profile": "TEST_PLAN_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-TEST-002",
        "official_name": "Test Scenario",
        "aliases": ["Kich ban kiem thu", "Test Scenarios Specification"],
        "group": "Testing_Quality",
        "purpose": "Xac dinh cac chuoi hanh vi va tinh huong can kiem tra de dam bao tinh nang hoat dong dung",
        "applicability": "Thiet ke kiem thu nghiep vu",
        "is_optional": False,
        "required_inputs": ["feature_id", "scenario_descriptions"],
        "optional_inputs": ["priority", "risk_rating"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Test_Scenario_Rules.md"],
        "preferred_template_id": "TPL-TEST-002",
        "related_standards": ["STD-TEST-29119-3", "STD-TEST-29119-4"],
        "required_sections": ["Scenario ID", "Target Requirement / Feature ID", "Scenario Title", "Scenario Description", "Techniques Used", "Priority"],
        "dependencies": ["DOC-TEST-001", "DOC-REQ-005"],
        "traceability_requirements": ["DOC-TEST-003"],
        "validation_profile": "TEST_SCENARIO_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-TEST-003",
        "official_name": "Test Case Specification",
        "aliases": ["Dac ta ca kiem thu", "Test Cases"],
        "group": "Testing_Quality",
        "purpose": "Dac ta chi tiet tung test case gom precondition, input, steps, expected result va cach xac thuc",
        "applicability": "Thiet ke test case chi tiet",
        "is_optional": False,
        "required_inputs": ["preconditions", "test_steps", "expected_results"],
        "optional_inputs": ["test_data", "cleanup_steps"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Test_Case_Rules.md"],
        "preferred_template_id": "TPL-TEST-003",
        "related_standards": ["STD-TEST-29119-3", "STD-TEST-29119-4"],
        "required_sections": ["Test Case ID", "Scenario / Requirement Ref", "Test Title", "Preconditions", "Test Steps & Input Data", "Expected Result", "Verification Method"],
        "dependencies": ["DOC-TEST-002", "DOC-REQ-003"],
        "traceability_requirements": ["DOC-TEST-004", "DOC-REQ-007"],
        "validation_profile": "TEST_CASE_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-TEST-004",
        "official_name": "Test Execution Report",
        "aliases": ["Bao cao thuc thi kiem thu", "Test Run Log"],
        "group": "Testing_Quality",
        "purpose": "Ghi nhan ket qua chay thuc te cua cac test case (Pass, Fail, Blocked, Not Executed) va bang chung",
        "applicability": "Chi duoc tao khi co du lieu thuc thi that",
        "is_optional": False,
        "required_inputs": ["execution_date", "actual_results", "statuses"],
        "optional_inputs": ["environment_details", "tester_id"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Test_Execution_Rules.md"],
        "preferred_template_id": "TPL-TEST-004",
        "related_standards": ["STD-TEST-29119-2", "STD-TEST-29119-3"],
        "required_sections": ["Execution Run ID & Date", "Environment Config", "Test Case ID", "Actual Result Observed", "Execution Status (PASS/FAIL/BLOCKED/NOT_EXECUTED)", "Execution Evidence / Log Ref", "Defect ID Ref (if failed)"],
        "dependencies": ["DOC-TEST-003"],
        "traceability_requirements": ["DOC-TEST-005", "DOC-DEL-009"],
        "validation_profile": "TEST_EXECUTION_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-TEST-005",
        "official_name": "Bug / Defect Report",
        "aliases": ["Bao cao loi", "Defect Log"],
        "group": "Testing_Quality",
        "purpose": "Mo ta chi tiet su co phan mem gom hanh vi thuc te, hanh vi mong doi, cach tai hien va muc do",
        "applicability": "Quan ly loi va su co phan mem",
        "is_optional": False,
        "required_inputs": ["actual_behavior", "expected_behavior", "steps_to_reproduce", "severity"],
        "optional_inputs": ["screenshots", "logs", "fix_version"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Bug_Report_Rules.md"],
        "preferred_template_id": "TPL-TEST-005",
        "related_standards": ["STD-TEST-29119-3"],
        "required_sections": ["Defect ID", "Summary", "Associated Test Case / Requirement", "Severity & Priority", "Environment", "Steps to Reproduce", "Expected vs Actual Behavior", "Status"],
        "dependencies": ["DOC-TEST-004"],
        "traceability_requirements": ["DOC-DEL-004"],
        "validation_profile": "TEST_BUG_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-TEST-006",
        "official_name": "User Acceptance Testing (UAT) Record",
        "aliases": ["Bien ban nghiem thu nguoi dung", "UAT Signoff"],
        "group": "Testing_Quality",
        "purpose": "Ghi nhan ket qua kiem thu nghiem thu boi nguoi dung cuoi hoac dai dien nghiep vu",
        "applicability": "Giai doan ban giao / nghiem thu san pham",
        "is_optional": False,
        "required_inputs": ["business_acceptance_criteria", "participant_records", "decision"],
        "optional_inputs": ["minor_reservations", "feedback_comments"],
        "output_formats": ["docx", "md"],
        "rule_references": ["UAT_Rules.md"],
        "preferred_template_id": "TPL-TEST-006",
        "related_standards": ["STD-TEST-29119-3"],
        "required_sections": ["UAT Scope & Environment", "Business Scenarios Verified", "Participant List & Roles", "Findings / Open Items", "Formal Signoff / Acceptance Decision"],
        "dependencies": ["DOC-TEST-004", "DOC-REQ-008"],
        "traceability_requirements": ["DOC-DEL-012"],
        "validation_profile": "TEST_UAT_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-TEST-007",
        "official_name": "Code Review Checklist",
        "aliases": ["Danh muc kiem tra ma nguon", "Code Review Guide"],
        "group": "Testing_Quality",
        "purpose": "Quy chuan tieu chi danh gia ma nguon ve chat luong, bao mat, hieu nang truoc khi merge",
        "applicability": "Quy trinh phat trien phan mem va DoD",
        "is_optional": False,
        "required_inputs": ["review_criteria_categories"],
        "optional_inputs": ["tooling_linters_config"],
        "output_formats": ["md"],
        "rule_references": ["Code_Review_Rules.md"],
        "preferred_template_id": "TPL-TEST-007",
        "related_standards": ["STD-SEC-OWASP2021"],
        "required_sections": ["Checklist Categories", "Code Style & Conventions", "Security & OWASP Defenses", "Performance & Resource Management", "Test Coverage Verification", "Reviewer Verification Rules"],
        "dependencies": ["DOC-SCRUM-014"],
        "traceability_requirements": ["DOC-SCRUM-014"],
        "validation_profile": "TEST_CODE_REVIEW_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-TEST-008",
        "official_name": "Quality Metrics Report",
        "aliases": ["Bao cao chi so chat luong", "QA Metrics"],
        "group": "Testing_Quality",
        "purpose": "Tong hop cac chi so chat luong (test pass rate, defect density, code coverage) tu nguon do thuc te",
        "applicability": "Bao cao dinh ky ve chat luong",
        "is_optional": False,
        "required_inputs": ["data_source", "measurement_time", "metric_values"],
        "optional_inputs": ["historical_trend", "coverage_report"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Quality_Metrics_Rules.md"],
        "preferred_template_id": "TPL-TEST-008",
        "related_standards": ["STD-TEST-29119-1"],
        "required_sections": ["Measurement Scope & Window", "Data Sources & Formulas", "Metrics Table (Pass Rate, Defect Density, Coverage)", "Analysis & Limitations", "Target Thresholds Evaluation"],
        "dependencies": ["DOC-TEST-004", "DOC-TEST-005"],
        "traceability_requirements": ["DOC-DEL-008"],
        "validation_profile": "TEST_METRICS_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },

    # NHOM E: Delivery & Tracking (13 docs)
    {
        "document_id": "DOC-DEL-001",
        "official_name": "Project Schedule",
        "aliases": ["Lich trinh du an", "Master Schedule"],
        "group": "Delivery",
        "purpose": "Theo doi timeline tong the, cac moc quan trong (milestones) va tien do cac giai doan",
        "applicability": "Theo doi va quan ly tien do du an",
        "is_optional": False,
        "required_inputs": ["milestones", "phase_dates"],
        "optional_inputs": ["critical_path", "resource_assignments"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Project_Schedule_Rules.md"],
        "preferred_template_id": "TPL-DEL-001",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Project Milestones", "Work Packages Timeline", "Planned Start & End Dates", "Actual Progress Percentage", "Schedule Variance Analysis"],
        "dependencies": ["DOC-PM-002", "DOC-DEL-002"],
        "traceability_requirements": ["DOC-DEL-008"],
        "validation_profile": "DEL_SCHEDULE_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-002",
        "official_name": "Work Breakdown Structure (WBS)",
        "aliases": ["Cau truc phan ra cong viec", "WBS Dictionary"],
        "group": "Delivery",
        "purpose": "Phan ra co he thong toan bo pham vi du an thanh cac goi cong viec quan ly duoc",
        "applicability": "Quan ly pham vi va ke hoach thuc hien",
        "is_optional": False,
        "required_inputs": ["deliverables_breakdown", "work_packages"],
        "optional_inputs": ["wbs_code_hierarchy", "package_owner"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["WBS_Rules.md"],
        "preferred_template_id": "TPL-DEL-002",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["WBS Code", "Level", "Work Package Name", "Description of Work", "Deliverable Output", "Completion Criteria"],
        "dependencies": ["DOC-PM-002"],
        "traceability_requirements": ["DOC-DEL-001"],
        "validation_profile": "DEL_WBS_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-003",
        "official_name": "Risk Register",
        "aliases": ["So theo doi rui ro", "Risk Log"],
        "group": "Delivery",
        "purpose": "Nhan dien, danh gia xac suat, tac dong va bien phap giam thieu cac rui ro du an",
        "applicability": "Quan ly rui ro xuyen suot du an",
        "is_optional": False,
        "required_inputs": ["risk_descriptions", "probability", "impact"],
        "optional_inputs": ["mitigation_plan", "risk_owner"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Risk_Register_Rules.md"],
        "preferred_template_id": "TPL-DEL-003",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Risk ID", "Risk Description", "Probability", "Impact", "Risk Severity Score", "Mitigation Strategy", "Contingency Plan", "Owner", "Status"],
        "dependencies": ["DOC-PM-001"],
        "traceability_requirements": ["DOC-DEL-004", "DOC-DEL-005"],
        "validation_profile": "DEL_RISK_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-004",
        "official_name": "Issue Log",
        "aliases": ["Nhat ky van de", "Issue Tracker"],
        "group": "Delivery",
        "purpose": "Theo doi cac van de, tro ngai da thuc su phat sinh can xu ly va giai quyet",
        "applicability": "Van hanh va kiem soat du an",
        "is_optional": False,
        "required_inputs": ["issue_description", "severity", "assigned_to"],
        "optional_inputs": ["resolution_summary", "closed_date"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Issue_Log_Rules.md"],
        "preferred_template_id": "TPL-DEL-004",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Issue ID", "Date Reported", "Description", "Severity", "Related Risk / PBI", "Assignee", "Action Plan", "Target Resolution Date", "Status"],
        "dependencies": ["DOC-DEL-003"],
        "traceability_requirements": ["DOC-DEL-008"],
        "validation_profile": "DEL_ISSUE_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-005",
        "official_name": "Decision Log",
        "aliases": ["So theo doi quyet dinh", "Project Decision Record"],
        "group": "Delivery",
        "purpose": "Ghi lai cac quyet dinh quan ly va nghiep vu quan trong, nguoi quyet dinh va ly do",
        "applicability": "Quan tri du an",
        "is_optional": False,
        "required_inputs": ["decision_topic", "decision_taken", "decision_maker"],
        "optional_inputs": ["rationale", "affected_parties"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Decision_Log_Rules.md"],
        "preferred_template_id": "TPL-DEL-005",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Decision ID", "Date", "Topic / Problem", "Decision Made", "Decision Maker / Authority", "Rationale & Alternatives", "Impacted Areas", "Status"],
        "dependencies": [],
        "traceability_requirements": ["DOC-ARCH-010", "DOC-DEL-008"],
        "validation_profile": "DEL_DECISION_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-006",
        "official_name": "Change Request Log",
        "aliases": ["So theo doi yeu cau thay doi", "CR Log"],
        "group": "Delivery",
        "purpose": "Ghi nhan, danh gia tac dong va phe duyet cac yeu cau thay doi pham vi, chi phi hoac tien do",
        "applicability": "Kiem soat thay doi trong du an",
        "is_optional": False,
        "required_inputs": ["change_description", "reason", "impact_analysis"],
        "optional_inputs": ["approval_status", "implementation_plan"],
        "output_formats": ["xlsx", "md"],
        "rule_references": ["Change_Request_Rules.md"],
        "preferred_template_id": "TPL-DEL-006",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["CR ID", "Date Requested", "Requested By", "Description of Change", "Impact Analysis (Scope, Schedule, Cost)", "Review & Decision Status", "Implementation Verified"],
        "dependencies": ["DOC-PM-002"],
        "traceability_requirements": ["DOC-REQ-001", "DOC-DEL-009"],
        "validation_profile": "DEL_CHANGE_REQ_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-007",
        "official_name": "Meeting Minutes",
        "aliases": ["Bien ban cuoc hop", "Meeting Notes"],
        "group": "Delivery",
        "purpose": "Ghi nhan noi dung thao luan, ket luan va hanh dong sau cac cuoc hop du an da dien ra",
        "applicability": "Chi lap khi cuoc hop da dien ra tren thuc te",
        "is_optional": False,
        "required_inputs": ["meeting_date", "attendees", "decisions_reached"],
        "optional_inputs": ["agenda", "action_items"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Meeting_Minutes_Rules.md"],
        "preferred_template_id": "TPL-DEL-007",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Meeting Info (Date, Time, Location)", "Attendees & Apologies", "Agenda Topics", "Key Discussions", "Agreed Decisions", "Action Items (Action, Owner, Due Date)"],
        "dependencies": [],
        "traceability_requirements": ["DOC-DEL-005"],
        "validation_profile": "DEL_MINUTES_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-008",
        "official_name": "Progress Report",
        "aliases": ["Bao cao tien do dinh ky", "Status Report"],
        "group": "Delivery",
        "purpose": "Tong hop tinh hinh thuc hien, tien do, chi so, rui ro va ke hoach giai doan tiep theo",
        "applicability": "Bao cao dinh ky cho lanh dao va stakeholders",
        "is_optional": False,
        "required_inputs": ["reporting_period", "accomplishments", "current_status"],
        "optional_inputs": ["planned_next_period", "open_blockers"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Progress_Report_Rules.md"],
        "preferred_template_id": "TPL-DEL-008",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Reporting Window & Author", "Executive Summary", "Key Accomplishments this Period", "Milestone & Schedule Status", "Issues & Critical Risks", "Plan for Next Period"],
        "dependencies": ["DOC-DEL-001"],
        "traceability_requirements": ["DOC-DEL-003", "DOC-DEL-004"],
        "validation_profile": "DEL_PROGRESS_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-009",
        "official_name": "Release Notes",
        "aliases": ["Thong tin phat hanh", "Version Release Notes"],
        "group": "Delivery",
        "purpose": "Cong bo cac tinh nang moi, sua loi, cai tien va huong dan nang cap cua phien ban",
        "applicability": "Moi dot phat hanh san pham",
        "is_optional": False,
        "required_inputs": ["version_number", "release_date", "features_added", "bugs_fixed"],
        "optional_inputs": ["known_issues", "breaking_changes"],
        "output_formats": ["md"],
        "rule_references": ["Release_Notes_Rules.md"],
        "preferred_template_id": "TPL-DEL-009",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Release Header (Version, Date)", "Overview / Summary", "New Features & Enhancements", "Bug Fixes & Security Patches", "Breaking Changes & Migration Steps", "Known Issues"],
        "dependencies": ["DOC-TEST-004"],
        "traceability_requirements": ["DOC-REQ-007", "DOC-SCRUM-015"],
        "validation_profile": "DEL_RELEASE_NOTES_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-010",
        "official_name": "User Manual",
        "aliases": ["Huong dan su dung", "User Guide"],
        "group": "Delivery",
        "purpose": "Huong dan nguoi dung cuoi cach su dung cac tinh nang phan mem tung buoc kem anh/vi du",
        "applicability": "Ban giao san pham cho nguoi dung",
        "is_optional": False,
        "required_inputs": ["feature_walkthroughs", "user_roles"],
        "optional_inputs": ["troubleshooting_faq", "glossary"],
        "output_formats": ["docx", "md"],
        "rule_references": ["User_Manual_Rules.md"],
        "preferred_template_id": "TPL-DEL-010",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["System Overview & Target Audience", "Getting Started & Login", "Step-by-Step Feature Walkthroughs", "Common Error Messages & FAQs", "Support Contact"],
        "dependencies": ["DOC-REQ-003", "DOC-ARCH-006"],
        "traceability_requirements": ["DOC-REQ-003"],
        "validation_profile": "DEL_USER_MANUAL_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-011",
        "official_name": "Installation Guide",
        "aliases": ["Huong dan cai dat", "Install Guide"],
        "group": "Delivery",
        "purpose": "Huong dan chi tiet cac buoc cai dat moi truong, thu vien, cau hinh va khoi chay he thong",
        "applicability": "Ban giao ky thuat va onboarding lap trinh vien",
        "is_optional": False,
        "required_inputs": ["prerequisites", "installation_commands", "configuration_steps"],
        "optional_inputs": ["verification_checks", "troubleshooting"],
        "output_formats": ["md"],
        "rule_references": ["Installation_Guide_Rules.md"],
        "preferred_template_id": "TPL-DEL-011",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Prerequisites & System Requirements", "Environment Variables & Configuration", "Step-by-Step Installation Commands", "Verification / Smoke Test Steps", "Troubleshooting Common Issues"],
        "dependencies": ["DOC-ARCH-008"],
        "traceability_requirements": ["DOC-DEL-013"],
        "validation_profile": "DEL_INSTALL_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-012",
        "official_name": "Project Handover Report",
        "aliases": ["Bien ban ban giao du an", "Handover Document"],
        "group": "Delivery",
        "purpose": "Ghi nhan ban giao toan dien san pham, ma nguon, tai lieu, tai nguyen va nghiem thu giua cac ben",
        "applicability": "Dong du an hoac chuyen giao van hanh",
        "is_optional": False,
        "required_inputs": ["deliverables_inventory", "handover_scope", "recipient_confirmation"],
        "optional_inputs": ["warranty_terms", "support_period"],
        "output_formats": ["docx", "md"],
        "rule_references": ["Project_Handover_Rules.md"],
        "preferred_template_id": "TPL-DEL-012",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Handover Identification & Parties", "Deliverables Inventory (Code, Docs, Environments, Accounts)", "Verification & Acceptance Summary", "Outstanding Items & Warranty Terms", "Formal Handover Acknowledgement"],
        "dependencies": ["DOC-PM-002", "DOC-TEST-006"],
        "traceability_requirements": ["DOC-DEL-009"],
        "validation_profile": "DEL_HANDOVER_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    },
    {
        "document_id": "DOC-DEL-013",
        "official_name": "Deployment Guide",
        "aliases": ["Huong dan trien khai production", "Deployment Runbook"],
        "group": "Delivery",
        "purpose": "Dac ta quy trinh dong goi, trien khai CI/CD, migration DB, rollback va kiem tra sau deploy",
        "applicability": "Van hanh deploy tren moi truong Staging / Production",
        "is_optional": False,
        "required_inputs": ["deployment_steps", "rollback_procedure", "post_deploy_checks"],
        "optional_inputs": ["ci_cd_pipeline_details", "monitoring_alerts"],
        "output_formats": ["md"],
        "rule_references": ["Deployment_Rules.md"],
        "preferred_template_id": "TPL-DEL-013",
        "related_standards": ["STD-PM-21500"],
        "required_sections": ["Target Deployment Environments", "Pre-deployment Checklist & Backup", "Deployment Execution Steps", "Database Migration Procedure", "Rollback Procedure", "Post-deployment Smoke Testing"],
        "dependencies": ["DOC-ARCH-008", "DOC-DEL-011"],
        "traceability_requirements": ["DOC-DEL-009"],
        "validation_profile": "DEL_DEPLOYMENT_PROFILE",
        "version": "1.0.0",
        "lifecycle_status": "ACTIVE"
    }
]

# Write document registry
doc_reg_path = os.path.join(CONFIG_DIR, "document_registry.yaml")
with open(doc_reg_path, "w", encoding="utf-8") as f:
    yaml.dump({"documents": documents}, f, allow_unicode=True, sort_keys=False)
print(f"[OK] Wrote {len(documents)} document entries to {doc_reg_path}")

# -------------------------------------------------------------
# 2. TEMPLATES DEFINITION & GENERATION
# -------------------------------------------------------------
templates = [
    # 8.1 Project Management
    {"template_id": "TPL-PM-001", "template_name": "Project Charter Template", "folder": "Project_Management", "file_name": "Project_Charter_Template.docx", "doc_ids": ["DOC-PM-001"], "format": "docx"},
    {"template_id": "TPL-PM-002", "template_name": "Project Scope Statement Template", "folder": "Project_Management", "file_name": "Project_Scope_Template.docx", "doc_ids": ["DOC-PM-002"], "format": "docx"},
    {"template_id": "TPL-PM-003", "template_name": "Stakeholder Register Template", "folder": "Project_Management", "file_name": "Stakeholder_Register_Template.xlsx", "doc_ids": ["DOC-PM-003"], "format": "xlsx"},
    {"template_id": "TPL-DEL-001", "template_name": "Project Schedule Template", "folder": "Project_Management", "file_name": "Project_Schedule_Template.xlsx", "doc_ids": ["DOC-DEL-001"], "format": "xlsx"},
    {"template_id": "TPL-DEL-002", "template_name": "Work Breakdown Structure Template", "folder": "Project_Management", "file_name": "WBS_Template.xlsx", "doc_ids": ["DOC-DEL-002"], "format": "xlsx"},
    {"template_id": "TPL-DEL-003", "template_name": "Risk Register Template", "folder": "Project_Management", "file_name": "Risk_Register_Template.xlsx", "doc_ids": ["DOC-DEL-003"], "format": "xlsx"},
    {"template_id": "TPL-DEL-004", "template_name": "Issue Log Template", "folder": "Project_Management", "file_name": "Issue_Log_Template.xlsx", "doc_ids": ["DOC-DEL-004"], "format": "xlsx"},
    {"template_id": "TPL-DEL-005", "template_name": "Decision Log Template", "folder": "Project_Management", "file_name": "Decision_Log_Template.xlsx", "doc_ids": ["DOC-DEL-005"], "format": "xlsx"},
    {"template_id": "TPL-DEL-006", "template_name": "Change Request Log Template", "folder": "Project_Management", "file_name": "Change_Request_Log_Template.xlsx", "doc_ids": ["DOC-DEL-006"], "format": "xlsx"},
    {"template_id": "TPL-DEL-007", "template_name": "Meeting Minutes Template", "folder": "Project_Management", "file_name": "Meeting_Minutes_Template.docx", "doc_ids": ["DOC-DEL-007"], "format": "docx"},
    {"template_id": "TPL-DEL-008", "template_name": "Progress Report Template", "folder": "Project_Management", "file_name": "Progress_Report_Template.docx", "doc_ids": ["DOC-DEL-008"], "format": "docx"},
    {"template_id": "TPL-DEL-012", "template_name": "Project Handover Template", "folder": "Project_Management", "file_name": "Project_Handover_Template.docx", "doc_ids": ["DOC-DEL-012"], "format": "docx"},

    # 8.2 Requirements
    {"template_id": "TPL-REQ-001", "template_name": "SRS Template", "folder": "Requirements", "file_name": "SRS_Template.docx", "doc_ids": ["DOC-REQ-001"], "format": "docx"},
    {"template_id": "TPL-REQ-002", "template_name": "Product Vision Template", "folder": "Requirements", "file_name": "Product_Vision_Template.docx", "doc_ids": ["DOC-REQ-002"], "format": "docx"},
    {"template_id": "TPL-REQ-003", "template_name": "Functional Requirements Template", "folder": "Requirements", "file_name": "Functional_Requirements_Template.xlsx", "doc_ids": ["DOC-REQ-003"], "format": "xlsx"},
    {"template_id": "TPL-REQ-004", "template_name": "Non-Functional Requirements Template", "folder": "Requirements", "file_name": "Non_Functional_Requirements_Template.xlsx", "doc_ids": ["DOC-REQ-004"], "format": "xlsx"},
    {"template_id": "TPL-REQ-005", "template_name": "Use Case Template", "folder": "Requirements", "file_name": "Use_Case_Template.docx", "doc_ids": ["DOC-REQ-005"], "format": "docx"},
    {"template_id": "TPL-REQ-006", "template_name": "User Story Template", "folder": "Requirements", "file_name": "User_Story_Acceptance_Criteria_Template.xlsx", "doc_ids": ["DOC-REQ-006"], "format": "xlsx"},
    {"template_id": "TPL-REQ-007", "template_name": "Requirements Traceability Matrix Template", "folder": "Requirements", "file_name": "Requirements_Traceability_Matrix_Template.xlsx", "doc_ids": ["DOC-REQ-007"], "format": "xlsx"},
    {"template_id": "TPL-REQ-008", "template_name": "Acceptance Criteria Template", "folder": "Requirements", "file_name": "Acceptance_Criteria_Template.xlsx", "doc_ids": ["DOC-REQ-008"], "format": "xlsx"},

    # 8.3 Scrum
    {"template_id": "TPL-SCRUM-001", "template_name": "Product Backlog Template", "folder": "Scrum", "file_name": "Product_Backlog_Template.xlsx", "doc_ids": ["DOC-SCRUM-001"], "format": "xlsx"},
    {"template_id": "TPL-SCRUM-002", "template_name": "Product Goal Template", "folder": "Scrum", "file_name": "Product_Goal_Template.docx", "doc_ids": ["DOC-SCRUM-002"], "format": "docx"},
    {"template_id": "TPL-SCRUM-003", "template_name": "PBI User Story Template", "folder": "Scrum", "file_name": "PBI_User_Story_Template.docx", "doc_ids": ["DOC-SCRUM-003"], "format": "docx"},
    {"template_id": "TPL-SCRUM-004", "template_name": "Backlog Refinement Template", "folder": "Scrum", "file_name": "Backlog_Refinement_Template.docx", "doc_ids": ["DOC-SCRUM-004"], "format": "docx"},
    {"template_id": "TPL-SCRUM-005", "template_name": "Release Plan Template", "folder": "Scrum", "file_name": "Release_Plan_Template.xlsx", "doc_ids": ["DOC-SCRUM-005"], "format": "xlsx"},
    {"template_id": "TPL-SCRUM-006", "template_name": "Sprint Planning Template", "folder": "Scrum", "file_name": "Sprint_Planning_Template.docx", "doc_ids": ["DOC-SCRUM-006"], "format": "docx"},
    {"template_id": "TPL-SCRUM-007", "template_name": "Sprint Backlog Template", "folder": "Scrum", "file_name": "Sprint_Backlog_Template.xlsx", "doc_ids": ["DOC-SCRUM-007"], "format": "xlsx"},
    {"template_id": "TPL-SCRUM-008", "template_name": "Sprint Goal Template", "folder": "Scrum", "file_name": "Sprint_Goal_Template.docx", "doc_ids": ["DOC-SCRUM-008"], "format": "docx"},
    {"template_id": "TPL-SCRUM-009", "template_name": "Task Breakdown Template", "folder": "Scrum", "file_name": "Task_Breakdown_Template.xlsx", "doc_ids": ["DOC-SCRUM-009"], "format": "xlsx"},
    {"template_id": "TPL-SCRUM-010", "template_name": "Sprint Schedule Template", "folder": "Scrum", "file_name": "Sprint_Schedule_Template.xlsx", "doc_ids": ["DOC-SCRUM-010"], "format": "xlsx"},
    {"template_id": "TPL-SCRUM-011", "template_name": "Daily Scrum Log Template", "folder": "Scrum", "file_name": "Daily_Scrum_Log_Template.xlsx", "doc_ids": ["DOC-SCRUM-011"], "format": "xlsx"},
    {"template_id": "TPL-SCRUM-012", "template_name": "Sprint Review Report Template", "folder": "Scrum", "file_name": "Sprint_Review_Report_Template.docx", "doc_ids": ["DOC-SCRUM-012"], "format": "docx"},
    {"template_id": "TPL-SCRUM-013", "template_name": "Sprint Retrospective Template", "folder": "Scrum", "file_name": "Sprint_Retrospective_Template.docx", "doc_ids": ["DOC-SCRUM-013"], "format": "docx"},
    {"template_id": "TPL-SCRUM-014", "template_name": "Definition of Done Template", "folder": "Scrum", "file_name": "Definition_of_Done_Template.docx", "doc_ids": ["DOC-SCRUM-014"], "format": "docx"},
    {"template_id": "TPL-SCRUM-015", "template_name": "Increment Deliverables Template", "folder": "Scrum", "file_name": "Sprint_Deliverables_Template.xlsx", "doc_ids": ["DOC-SCRUM-015"], "format": "xlsx"},
    {"template_id": "TPL-SCRUM-016", "template_name": "Sprint Metrics Burndown Template", "folder": "Scrum", "file_name": "Sprint_Metrics_Burndown_Template.xlsx", "doc_ids": ["DOC-SCRUM-016"], "format": "xlsx"},
    {"template_id": "TPL-SCRUM-017", "template_name": "Definition of Ready Template", "folder": "Scrum", "file_name": "Definition_of_Ready_Template.docx", "doc_ids": ["DOC-SCRUM-017"], "format": "docx"},

    # 8.4 Architecture & Design
    {"template_id": "TPL-ARCH-001", "template_name": "SAD Template", "folder": "Architecture_Design", "file_name": "SAD_Template.docx", "doc_ids": ["DOC-ARCH-001"], "format": "docx"},
    {"template_id": "TPL-ARCH-002", "template_name": "SDD Template", "folder": "Architecture_Design", "file_name": "SDD_Template.docx", "doc_ids": ["DOC-ARCH-002"], "format": "docx"},
    {"template_id": "TPL-ARCH-003", "template_name": "Database Design Template", "folder": "Architecture_Design", "file_name": "Database_Design_Template.docx", "doc_ids": ["DOC-ARCH-003"], "format": "docx"},
    {"template_id": "TPL-ARCH-004", "template_name": "ERD Template", "folder": "Architecture_Design", "file_name": "ERD_Template.mmd", "doc_ids": ["DOC-ARCH-004"], "format": "mmd"},
    {"template_id": "TPL-ARCH-005", "template_name": "API Specification Template", "folder": "Architecture_Design", "file_name": "API_Specification_Template.yaml", "doc_ids": ["DOC-ARCH-005"], "format": "yaml"},
    {"template_id": "TPL-ARCH-006", "template_name": "UI UX Specification Template", "folder": "Architecture_Design", "file_name": "UI_UX_Specification_Template.docx", "doc_ids": ["DOC-ARCH-006"], "format": "docx"},
    {"template_id": "TPL-ARCH-007", "template_name": "Component Diagram Template", "folder": "Architecture_Design", "file_name": "Component_Diagram_Template.mmd", "doc_ids": ["DOC-ARCH-007"], "format": "mmd"},
    {"template_id": "TPL-ARCH-008", "template_name": "Deployment Architecture Template", "folder": "Architecture_Design", "file_name": "Deployment_Architecture_Template.mmd", "doc_ids": ["DOC-ARCH-008"], "format": "mmd"},
    {"template_id": "TPL-ARCH-009", "template_name": "Technical Design Document Template", "folder": "Architecture_Design", "file_name": "Technical_Design_Template.docx", "doc_ids": ["DOC-ARCH-009"], "format": "docx"},
    {"template_id": "TPL-ARCH-010", "template_name": "ADR Template", "folder": "Architecture_Design", "file_name": "ADR_Template.md", "doc_ids": ["DOC-ARCH-010"], "format": "md"},

    # 8.5 Testing & Quality
    {"template_id": "TPL-TEST-001", "template_name": "Test Plan Template", "folder": "Testing", "file_name": "Test_Plan_Template.docx", "doc_ids": ["DOC-TEST-001"], "format": "docx"},
    {"template_id": "TPL-TEST-002", "template_name": "Test Scenario Template", "folder": "Testing", "file_name": "Test_Scenario_Template.xlsx", "doc_ids": ["DOC-TEST-002"], "format": "xlsx"},
    {"template_id": "TPL-TEST-003", "template_name": "Test Case Specification Template", "folder": "Testing", "file_name": "Test_Case_Template.xlsx", "doc_ids": ["DOC-TEST-003"], "format": "xlsx"},
    {"template_id": "TPL-TEST-004", "template_name": "Test Execution Report Template", "folder": "Testing", "file_name": "Test_Execution_Report_Template.xlsx", "doc_ids": ["DOC-TEST-004"], "format": "xlsx"},
    {"template_id": "TPL-TEST-005", "template_name": "Bug Report Template", "folder": "Testing", "file_name": "Bug_Report_Template.xlsx", "doc_ids": ["DOC-TEST-005"], "format": "xlsx"},
    {"template_id": "TPL-TEST-006", "template_name": "UAT Template", "folder": "Testing", "file_name": "UAT_Template.docx", "doc_ids": ["DOC-TEST-006"], "format": "docx"},
    {"template_id": "TPL-TEST-007", "template_name": "Code Review Checklist Template", "folder": "Testing", "file_name": "Code_Review_Checklist_Template.md", "doc_ids": ["DOC-TEST-007"], "format": "md"},
    {"template_id": "TPL-TEST-008", "template_name": "Quality Metrics Template", "folder": "Testing", "file_name": "Quality_Metrics_Template.xlsx", "doc_ids": ["DOC-TEST-008"], "format": "xlsx"},

    # 8.6 Delivery
    {"template_id": "TPL-DEL-009", "template_name": "Release Notes Template", "folder": "Delivery", "file_name": "Release_Notes_Template.md", "doc_ids": ["DOC-DEL-009"], "format": "md"},
    {"template_id": "TPL-DEL-010", "template_name": "User Manual Template", "folder": "Delivery", "file_name": "User_Manual_Template.docx", "doc_ids": ["DOC-DEL-010"], "format": "docx"},
    {"template_id": "TPL-DEL-011", "template_name": "Installation Guide Template", "folder": "Delivery", "file_name": "Installation_Guide_Template.md", "doc_ids": ["DOC-DEL-011"], "format": "md"},
    {"template_id": "TPL-DEL-013", "template_name": "Deployment Guide Template", "folder": "Delivery", "file_name": "Deployment_Guide_Template.md", "doc_ids": ["DOC-DEL-013"], "format": "md"},
]

template_records = []

for tpl in templates:
    rel_path = f"03_Templates/{tpl['folder']}/{tpl['file_name']}"
    full_path = os.path.join(TEMPLATES_DIR, tpl['folder'], tpl['file_name'])
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    # Create the template file physically
    fmt = tpl["format"]
    if fmt == "docx":
        doc = docx.Document()
        title_p = doc.add_paragraph()
        run = title_p.add_run(tpl["template_name"].upper())
        run.bold = True
        run.font.size = Pt(20)
        run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
        
        doc.add_paragraph(f"Document ID: {tpl['doc_ids'][0]} | Status: TEMPLATE_ORIGIN: GENERATED_TEMPLATE")
        doc.add_paragraph("Project Name: {{PROJECT_NAME}}")
        doc.add_paragraph("Version: {{VERSION}} | Date: {{DATE}} | Author: {{AUTHOR}}")
        doc.add_heading("1. Executive Summary & Purpose", level=1)
        doc.add_paragraph("{{EXECUTIVE_SUMMARY_CONTENT}}")
        
        doc.add_heading("2. Core Specification Details", level=1)
        table = doc.add_table(rows=3, cols=3)
        table.style = 'Table Grid'
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = "Item Key"
        hdr_cells[1].text = "Specification Parameter"
        hdr_cells[2].text = "Value / Status"
        for i, val in enumerate(["Scope Boundary", "Acceptance Rule"]):
            row_cells = table.rows[i+1].cells
            row_cells[0].text = f"ITEM-00{i+1}"
            row_cells[1].text = val
            row_cells[2].text = "{{VALUE}}"
            
        doc.add_heading("3. Verification and Evidence", level=1)
        doc.add_paragraph("{{VERIFICATION_EVIDENCE_CONTENT}}")
        doc.save(full_path)

    elif fmt == "xlsx":
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Registry_Data"
        header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
        header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        border = Border(left=Side(style='thin', color='D9D9D9'),
                        right=Side(style='thin', color='D9D9D9'),
                        top=Side(style='thin', color='D9D9D9'),
                        bottom=Side(style='thin', color='D9D9D9'))
        
        headers = ["ID", "Category", "Item Name", "Description", "Status", "Owner", "Evidence_Ref"]
        ws.append(headers)
        for col_num in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col_num)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center", vertical="center")
            
        sample_rows = [
            ["ID-001", "Core", "{{ITEM_1}}", "{{DESCRIPTION_1}}", "VERIFIED", "DevTeam", "src/index.ts"],
            ["ID-002", "Support", "{{ITEM_2}}", "{{DESCRIPTION_2}}", "INFERRED", "QA", "tests/main_test.py"],
        ]
        for row in sample_rows:
            ws.append(row)
            
        for row in ws.iter_rows(min_row=1, max_row=3, min_col=1, max_col=7):
            for cell in row:
                cell.border = border
                
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 4, 14)
            
        wb.save(full_path)

    elif fmt == "mmd":
        content = f"""%% Mermaid Template for {tpl['template_name']}
flowchart TD
    subgraph ClientLayer ["Client Application"]
        UI["User Interface (Web/Mobile)"]
    end

    subgraph ServiceLayer ["Application Services"]
        API["API Gateway / Controller"]
        AUTH["Auth Service (JWT/RBAC)"]
        SVC["Business Service Engine"]
    end

    subgraph DataLayer ["Data & Storage"]
        DB[("Primary Database (PostgreSQL/MySQL)")]
        CACHE[("Redis Cache")]
    end

    UI -->|HTTPS/REST| API
    API --> AUTH
    API --> SVC
    SVC --> DB
    SVC --> CACHE
"""
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    elif fmt == "yaml":
        content = f"""# {tpl['template_name']}
openapi: 3.1.0
info:
  title: "{{PROJECT_NAME}} API"
  version: "1.0.0"
  description: "Official REST API Specification for {{PROJECT_NAME}}"
servers:
  - url: "https://api.example.com/v1"
    description: "Production Server"
paths:
  /health:
    get:
      summary: "System Health Check"
      responses:
        '200':
          description: "Service is running normally"
components:
  schemas:
    HealthResponse:
      type: object
      properties:
        status:
          type: string
          example: "UP"
"""
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    elif fmt == "md":
        content = f"""# {tpl['template_name']}

- **Document ID**: {tpl['doc_ids'][0]}
- **Project**: `{{{{PROJECT_NAME}}}}`
- **Version**: `{{{{VERSION}}}}`
- **Status**: `GENERATED_TEMPLATE`
- **Date**: `{{{{DATE}}}}`

---

## 1. Context & Purpose
{{{{CONTEXT_CONTENT}}}}

## 2. Specification & Implementation Details
{{{{DETAILS_CONTENT}}}}

## 3. Verification & Evidence
{{{{EVIDENCE_CONTENT}}}}
"""
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    record = {
        "template_id": tpl["template_id"],
        "template_name": tpl["template_name"],
        "file_path": rel_path,
        "document_ids": tpl["doc_ids"],
        "format": fmt,
        "origin_type": "GENERATED_TEMPLATE",
        "source_id": "SYS-BUILTIN-TEMPLATES",
        "license_status": "Internal / MIT Open Documentation",
        "version": "1.0.0",
        "status": "GENERATED_TEMPLATE",
        "required_sections": ["Header & Identification", "Executive Summary", "Detailed Specification", "Verification Evidence"],
        "format_preservation_requirements": [
            "Preserve table structure and cell formulas",
            "Preserve heading hierarchy and styling",
            "Replace placeholders without altering layout"
        ],
        "validation_profile": f"{tpl['format'].upper()}_PRESERVATION_PROFILE"
    }
    template_records.append(record)

# Write template registry
tpl_reg_path = os.path.join(CONFIG_DIR, "template_registry.yaml")
with open(tpl_reg_path, "w", encoding="utf-8") as f:
    yaml.dump({"templates": template_records}, f, allow_unicode=True, sort_keys=False)
print(f"[OK] Wrote {len(template_records)} template entries to {tpl_reg_path}")

# Write GENERATED_TEMPLATES_NOTICE.md
notice_path = os.path.join(TEMPLATES_DIR, "GENERATED_TEMPLATES_NOTICE.md")
with open(notice_path, "w", encoding="utf-8") as f:
    f.write("""# GENERATED TEMPLATES NOTICE — THÔNG BÁO VỀ MẪU TÀI LIỆU KHỞI TẠO

Tất cả các tệp mẫu trong thư mục `03_Templates/` được hệ thống khởi tạo tự động theo cấu trúc thực dụng chuyên nghiệp và tuân thủ các tiêu chuẩn kỹ thuật (ISO 29148, ISO 42010, ISO 29119, Scrum Guide 2020, OpenAPI 3.1).

## 1. Nguồn Gốc và Phân Loại Mẫu
- **Trạng thái**: `GENERATED_TEMPLATE`
- **Tác giả khởi tạo**: Software Documentation Agent System.
- **Tính chất**: Mẫu cấu trúc chuẩn hóa, sẵn sàng đưa vào sử dụng ngay (Production-ready templates).
- **Quy tắc bảo vệ tính xác thực**: Tuyệt đối không đánh tráo nhãn các mẫu do AI/hệ thống khởi tạo này thành mẫu chính thức từ tổ chức tiêu chuẩn (không ghi `OFFICIAL_SOURCE` khi chưa có bản gốc từ tổ chức).

## 2. Ưu Tiên Áp Dụng Mẫu
Khi người dùng cung cấp mẫu riêng của tổ chức (Word .docx, Excel .xlsx, v.v.):
1. Hệ thống sẽ lập tức chuyển trạng thái sang `USER_PROVIDED`.
2. Hệ thống lưu giữ nguyên vẹn cấu trúc bảng biểu, style heading, công thức tính toán và chỉ thay thế các placeholder nội dung tương ứng.
3. Không bao giờ ghi đè lên mẫu gốc do người dùng cung cấp.
""")
print(f"[OK] Created notice at {notice_path}")
