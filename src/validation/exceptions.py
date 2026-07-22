"""
Data Quality Exception Data Model.
"""
from dataclasses import dataclass

@dataclass
class DataQualityException:
    rule_id: str
    rule_name: str
    severity: str  # BLOCKER, WARNING, INFO
    initiative_id: str
    field_name: str
    error_message: str
    owner: str = ""
    age_days: int = 0
