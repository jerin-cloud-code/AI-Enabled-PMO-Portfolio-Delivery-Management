"""
RAID and Decision data models.
"""
from dataclasses import dataclass

@dataclass
class RAIDItem:
    raid_id: str
    initiative_id: str
    item_type: str  # Risk, Action, Issue, Dependency
    summary: str
    severity_impact: str
    probability: str
    status: str
    owner: str
    target_date: str

@dataclass
class DecisionItem:
    decision_id: str
    initiative_id: str
    ask: str
    options_considered: str
    recommendation: str
    decision_owner: str
    status: str
    decision_date: str
