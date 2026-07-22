"""
Initiative data model representation.
"""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Initiative:
    initiative_id: str
    title: str
    description: str
    portfolio_category: str
    initiative_type: str = "Project"
    strategic_objective: str = ""
    business_owner: str = ""
    delivery_owner: str = ""
    sponsor: str = ""
    lifecycle_stage: str = "Active"
    shaping_stage: str = "Completed"
    priority: str = "Medium"
    rag_status: str = "GREEN"
    confidence_level: str = "HIGH"
    start_date: str = ""
    target_end_date: str = ""
    last_update_date: str = ""
    progress_pct: float = 0.0
    budget: float = 0.0
    actual_cost: float = 0.0
    forecast_cost: float = 0.0
    expected_benefit: float = 0.0
    benefits_status: str = "NOT_DEFINED"
    benefits_description: str = ""
    risk_exposure: str = "LOW"
    dependency_ids: str = ""
    decision_required: bool = False
    next_milestone: str = ""
    next_milestone_date: str = ""
    data_quality_status: str = "VALIDATED"
    executive_summary: str = ""
    source_system_reference: str = ""

    def is_stale(self, reference_date_str: str = "2025-03-22", threshold_days: int = 30) -> bool:
        if not self.last_update_date:
            return True
        try:
            from datetime import datetime
            ref_dt = datetime.strptime(reference_date_str, "%Y-%m-%d")
            upd_dt = datetime.strptime(self.last_update_date, "%Y-%m-%d")
            return (ref_dt - upd_dt).days > threshold_days
        except ValueError:
            return True
