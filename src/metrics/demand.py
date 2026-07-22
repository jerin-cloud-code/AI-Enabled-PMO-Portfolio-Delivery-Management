"""
Demand Pipeline Metrics Calculation.
Computes funnel counts across intake and shaping stages.
"""
from typing import List, Dict, Any
from src.models.initiative import Initiative

def calculate_demand_metrics(initiatives: List[Initiative]) -> Dict[str, Any]:
    intake_count = sum(1 for i in initiatives if i.lifecycle_stage == "Intake")
    shaping_count = sum(1 for i in initiatives if i.lifecycle_stage == "Shaping")
    approved_count = sum(1 for i in initiatives if i.lifecycle_stage == "Approved")
    active_count = sum(1 for i in initiatives if i.lifecycle_stage == "Active")
    closed_count = sum(1 for i in initiatives if i.lifecycle_stage == "Closed")

    shaping_by_stage = {
        "Submitted": sum(1 for i in initiatives if i.shaping_stage == "Submitted"),
        "Triage": sum(1 for i in initiatives if i.shaping_stage == "Triage"),
        "Business_Case": sum(1 for i in initiatives if i.shaping_stage == "Business_Case"),
        "Governance_Gate": sum(1 for i in initiatives if i.shaping_stage == "Governance_Gate"),
    }

    return {
        "intake_count": intake_count,
        "shaping_count": shaping_count,
        "approved_count": approved_count,
        "active_count": active_count,
        "closed_count": closed_count,
        "shaping_by_stage": shaping_by_stage,
        "total_demand_pipeline": intake_count + shaping_count + approved_count,
    }
