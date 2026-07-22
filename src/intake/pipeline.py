"""
Intake & Shaping Pipeline Manager.
Tracks proposals through front-door intake, triage, business case shaping, and governance gate approval.
"""
from typing import List, Dict, Any
from src.models.initiative import Initiative

class IntakePipeline:
    def __init__(self, initiatives: List[Initiative]):
        self.initiatives = initiatives

    def get_shaping_funnel(self) -> Dict[str, Any]:
        intake_items = [i for i in self.initiatives if i.lifecycle_stage == "Intake"]
        shaping_items = [i for i in self.initiatives if i.lifecycle_stage == "Shaping"]
        approved_items = [i for i in self.initiatives if i.lifecycle_stage == "Approved"]

        return {
            "intake_count": len(intake_items),
            "shaping_count": len(shaping_items),
            "approved_count": len(approved_items),
            "intake_proposals": [
                {
                    "initiative_id": i.initiative_id,
                    "title": i.title,
                    "portfolio_category": i.portfolio_category,
                    "sponsor": i.sponsor,
                    "shaping_stage": i.shaping_stage,
                }
                for i in intake_items + shaping_items
            ]
        }
