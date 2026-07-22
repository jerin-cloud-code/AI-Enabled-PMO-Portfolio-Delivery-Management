"""
Staleness Detection Engine.
Identifies initiatives that have not received an update within threshold days.
"""
from datetime import datetime
from typing import List
from src.models.initiative import Initiative
from src.validation.exceptions import DataQualityException

class StalenessDetector:
    def __init__(self, threshold_days: int = 30):
        self.threshold_days = threshold_days

    def detect_stale_initiatives(self, initiatives: List[Initiative], reference_date_str: str = "2025-03-22") -> List[DataQualityException]:
        exceptions = []
        ref_dt = datetime.strptime(reference_date_str, "%Y-%m-%d")

        for init in initiatives:
            if not init.last_update_date:
                exceptions.append(DataQualityException(
                    rule_id="VAL-RULE-006",
                    rule_name="Stale Record Update",
                    severity="WARNING",
                    initiative_id=init.initiative_id,
                    field_name="last_update_date",
                    error_message="Missing update date",
                    owner=init.delivery_owner or "Unassigned",
                    age_days=999
                ))
                continue

            try:
                upd_dt = datetime.strptime(init.last_update_date, "%Y-%m-%d")
                age = (ref_dt - upd_dt).days
                if age > self.threshold_days:
                    exceptions.append(DataQualityException(
                        rule_id="VAL-RULE-006",
                        rule_name="Stale Record Update",
                        severity="WARNING",
                        initiative_id=init.initiative_id,
                        field_name="last_update_date",
                        error_message=f"Record not updated for {age} days (threshold: {self.threshold_days} days)",
                        owner=init.delivery_owner or "Unassigned",
                        age_days=age
                    ))
            except ValueError:
                exceptions.append(DataQualityException(
                    rule_id="VAL-RULE-006",
                    rule_name="Stale Record Update",
                    severity="BLOCKER",
                    initiative_id=init.initiative_id,
                    field_name="last_update_date",
                    error_message=f"Invalid date format: {init.last_update_date}",
                    owner=init.delivery_owner or "Unassigned",
                    age_days=0
                ))
        return exceptions
