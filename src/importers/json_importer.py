"""
JSON Importer for Jira REST API exports and structured JSON files.
"""
import json
from typing import List
from src.models.initiative import Initiative
from src.importers.csv_importer import strip_html

class JSONImporter:
    def load_initiatives(self, file_path: str) -> List[Initiative]:
        initiatives = []
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                init = Initiative(
                    initiative_id=item.get("initiative_id", ""),
                    title=strip_html(item.get("title", "")),
                    description=strip_html(item.get("description", "")),
                    portfolio_category=item.get("portfolio_category", ""),
                    initiative_type=item.get("initiative_type", "Project"),
                    strategic_objective=item.get("strategic_objective", ""),
                    business_owner=item.get("business_owner", ""),
                    delivery_owner=item.get("delivery_owner", ""),
                    sponsor=item.get("sponsor", ""),
                    lifecycle_stage=item.get("lifecycle_stage", "Active"),
                    shaping_stage=item.get("shaping_stage", "Completed"),
                    priority=item.get("priority", "Medium"),
                    rag_status=item.get("rag_status", "GREEN"),
                    confidence_level=item.get("confidence_level", "HIGH"),
                    start_date=item.get("start_date", ""),
                    target_end_date=item.get("target_end_date", ""),
                    last_update_date=item.get("last_update_date", ""),
                    progress_pct=float(item.get("progress_pct", 0.0)),
                    budget=float(item.get("budget", 0.0)),
                    actual_cost=float(item.get("actual_cost", 0.0)),
                    forecast_cost=float(item.get("forecast_cost", 0.0)),
                    expected_benefit=float(item.get("expected_benefit", 0.0)),
                    benefits_status=item.get("benefits_status", "NOT_DEFINED"),
                    benefits_description=item.get("benefits_description", ""),
                    risk_exposure=item.get("risk_exposure", "LOW"),
                    dependency_ids=item.get("dependency_ids", ""),
                    decision_required=bool(item.get("decision_required", False)),
                    next_milestone=item.get("next_milestone", ""),
                    next_milestone_date=item.get("next_milestone_date", ""),
                    data_quality_status=item.get("data_quality_status", "VALIDATED"),
                    executive_summary=strip_html(item.get("executive_summary", "")),
                    source_system_reference=item.get("source_system_reference", ""),
                )
                initiatives.append(init)
        return initiatives
