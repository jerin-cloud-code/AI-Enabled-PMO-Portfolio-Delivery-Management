"""
RAID and Decision Tracker.
Provides CRUD, filtering, and dependency linkage mapping for RAID items and Decisions.
"""
import csv
from typing import List, Dict, Any
from src.models.raid import RAIDItem, DecisionItem

class RAIDTracker:
    def __init__(self):
        self.raid_items: List[RAIDItem] = []
        self.decisions: List[DecisionItem] = []

    def load_raid_log(self, file_path: str):
        self.raid_items = []
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = RAIDItem(
                    raid_id=row.get("raid_id", ""),
                    initiative_id=row.get("initiative_id", ""),
                    item_type=row.get("item_type", "Risk"),
                    summary=row.get("summary", ""),
                    severity_impact=row.get("severity_impact", "Medium"),
                    probability=row.get("probability", "Medium"),
                    status=row.get("status", "Open"),
                    owner=row.get("owner", "Unassigned"),
                    target_date=row.get("target_date", ""),
                )
                self.raid_items.append(item)

    def load_decisions(self, file_path: str):
        self.decisions = []
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = DecisionItem(
                    decision_id=row.get("decision_id", ""),
                    initiative_id=row.get("initiative_id", ""),
                    ask=row.get("ask", ""),
                    options_considered=row.get("options_considered", ""),
                    recommendation=row.get("recommendation", ""),
                    decision_owner=row.get("decision_owner", ""),
                    status=row.get("status", "PENDING_APPROVAL"),
                    decision_date=row.get("decision_date", ""),
                )
                self.decisions.append(item)

    def get_open_risks(self) -> List[RAIDItem]:
        return [i for i in self.raid_items if i.item_type == "Risk" and i.status == "Open"]

    def get_open_issues(self) -> List[RAIDItem]:
        return [i for i in self.raid_items if i.item_type == "Issue" and i.status == "Open"]

    def get_pending_decisions(self) -> List[DecisionItem]:
        return [d for d in self.decisions if d.status == "PENDING_APPROVAL"]
