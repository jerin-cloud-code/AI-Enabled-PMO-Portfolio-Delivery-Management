"""
Portfolio container model.
"""
from dataclasses import dataclass, field
from typing import List
from src.models.initiative import Initiative

@dataclass
class Portfolio:
    portfolio_id: str
    name: str
    category: str
    executive_sponsor: str
    lead_pmo_analyst: str
    initiatives: List[Initiative] = field(default_factory=list)

    @property
    def total_budget(self) -> float:
        return sum(i.budget for i in self.initiatives)

    @property
    def total_actual_cost(self) -> float:
        return sum(i.actual_cost for i in self.initiatives)

    @property
    def red_count(self) -> int:
        return sum(1 for i in self.initiatives if i.rag_status == "RED")

    @property
    def amber_count(self) -> int:
        return sum(1 for i in self.initiatives if i.rag_status == "AMBER")

    @property
    def green_count(self) -> int:
        return sum(1 for i in self.initiatives if i.rag_status == "GREEN")
