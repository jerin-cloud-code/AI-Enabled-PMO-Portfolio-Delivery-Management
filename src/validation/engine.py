"""
Data Validation Engine.
Combines rule evaluation and staleness detection to generate complete exception reports.
"""
from typing import List, Dict, Any
from src.models.initiative import Initiative
from src.validation.exceptions import DataQualityException
from src.validation.rules import evaluate_initiative_rules
from src.validation.staleness import StalenessDetector

class ValidationEngine:
    def __init__(self, staleness_threshold_days: int = 30):
        self.staleness_detector = StalenessDetector(threshold_days=staleness_threshold_days)

    def validate_portfolio(self, initiatives: List[Initiative], reference_date_str: str = "2025-03-22") -> Dict[str, Any]:
        rule_exceptions = evaluate_initiative_rules(initiatives)
        stale_exceptions = self.staleness_detector.detect_stale_initiatives(initiatives, reference_date_str)
        all_exceptions = rule_exceptions + stale_exceptions

        blockers = [e for e in all_exceptions if e.severity == "BLOCKER"]
        warnings = [e for e in all_exceptions if e.severity == "WARNING"]
        infos = [e for e in all_exceptions if e.severity == "INFO"]

        # Update initiative data quality status flags
        exception_init_ids = {e.initiative_id for e in all_exceptions if e.severity in ["BLOCKER", "WARNING"]}
        for init in initiatives:
            if init.initiative_id in exception_init_ids:
                init.data_quality_status = "EXCEPTIONS_FOUND"
            else:
                init.data_quality_status = "VALIDATED"

        return {
            "total_initiatives": len(initiatives),
            "total_exceptions": len(all_exceptions),
            "blocker_count": len(blockers),
            "warning_count": len(warnings),
            "info_count": len(infos),
            "exceptions": all_exceptions,
            "blockers": blockers,
            "warnings": warnings,
            "infos": infos,
        }
