"""
CSV Importer for Jira-style exports and tabular portfolio registers.
Handles field mapping, HTML stripping, and type coercions.
"""
import csv
import re
from typing import List, Dict, Any
from src.models.initiative import Initiative

def strip_html(text: str) -> str:
    if not text:
        return ""
    return re.sub(r'<[^>]*>', '', text).strip()

class CSVImporter:
    def __init__(self, field_mapping: Dict[str, str] = None):
        self.field_mapping = field_mapping or {}

    def load_initiatives(self, file_path: str) -> List[Initiative]:
        initiatives = []
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                mapped = {}
                for key, val in row.items():
                    target_key = self.field_mapping.get(key, key)
                    mapped[target_key] = val

                init = Initiative(
                    initiative_id=mapped.get("initiative_id", ""),
                    title=strip_html(mapped.get("title", "")),
                    description=strip_html(mapped.get("description", "")),
                    portfolio_category=mapped.get("portfolio_category", ""),
                    initiative_type=mapped.get("initiative_type", "Project"),
                    strategic_objective=mapped.get("strategic_objective", ""),
                    business_owner=mapped.get("business_owner", ""),
                    delivery_owner=mapped.get("delivery_owner", ""),
                    sponsor=mapped.get("sponsor", ""),
                    lifecycle_stage=mapped.get("lifecycle_stage", "Active"),
                    shaping_stage=mapped.get("shaping_stage", "Completed"),
                    priority=mapped.get("priority", "Medium"),
                    rag_status=mapped.get("rag_status", "GREEN"),
                    confidence_level=mapped.get("confidence_level", "HIGH"),
                    start_date=mapped.get("start_date", ""),
                    target_end_date=mapped.get("target_end_date", ""),
                    last_update_date=mapped.get("last_update_date", ""),
                    progress_pct=float(mapped.get("progress_pct", 0.0) or 0.0),
                    budget=float(mapped.get("budget", 0.0) or 0.0),
                    actual_cost=float(mapped.get("actual_cost", 0.0) or 0.0),
                    forecast_cost=float(mapped.get("forecast_cost", 0.0) or 0.0),
                    expected_benefit=float(mapped.get("expected_benefit", 0.0) or 0.0),
                    benefits_status=mapped.get("benefits_status", "NOT_DEFINED"),
                    benefits_description=mapped.get("benefits_description", ""),
                    risk_exposure=mapped.get("risk_exposure", "LOW"),
                    dependency_ids=mapped.get("dependency_ids", ""),
                    decision_required=str(mapped.get("decision_required", "")).lower() in ["true", "1", "yes"],
                    next_milestone=mapped.get("next_milestone", ""),
                    next_milestone_date=mapped.get("next_milestone_date", ""),
                    data_quality_status=mapped.get("data_quality_status", "VALIDATED"),
                    executive_summary=strip_html(mapped.get("executive_summary", "")),
                    source_system_reference=mapped.get("source_system_reference", ""),
                )
                initiatives.append(init)
        return initiatives
