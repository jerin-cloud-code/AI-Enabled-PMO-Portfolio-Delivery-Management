"""
Portfolio Prioritisation Scoring Model.
Computes multi-factor weighted priority score (0-100) for strategic ranking.
"""
from typing import List, Dict, Any
from src.models.initiative import Initiative

class PrioritisationEngine:
    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights or {
            "strategic_alignment": 0.30,
            "risk_urgency": 0.25,
            "financial_return": 0.25,
            "delivery_confidence": 0.20,
        }

    def score_initiative(self, init: Initiative) -> float:
        # Strategic Alignment Score (0-100)
        strat_score = 80.0 if init.priority == "High" else (60.0 if init.priority == "Medium" else 40.0)

        # Risk Urgency Score (0-100)
        risk_score = 90.0 if init.risk_exposure == "HIGH" else (65.0 if init.risk_exposure == "MEDIUM" else 40.0)

        # Financial Return Score (ROI ratio)
        roi_ratio = (init.expected_benefit / init.budget) if init.budget > 0 else 1.0
        fin_score = min(100.0, roi_ratio * 40.0)

        # Delivery Confidence Score
        conf_score = 90.0 if init.confidence_level == "HIGH" else (60.0 if init.confidence_level == "MEDIUM" else 30.0)

        composite = (
            strat_score * self.weights["strategic_alignment"] +
            risk_score * self.weights["risk_urgency"] +
            fin_score * self.weights["financial_return"] +
            conf_score * self.weights["delivery_confidence"]
        )
        return round(composite, 1)

    def rank_initiatives(self, initiatives: List[Initiative]) -> List[Dict[str, Any]]:
        ranked = []
        for init in initiatives:
            score = self.score_initiative(init)
            ranked.append({
                "initiative_id": init.initiative_id,
                "title": init.title,
                "portfolio_category": init.portfolio_category,
                "priority": init.priority,
                "rag_status": init.rag_status,
                "budget": init.budget,
                "expected_benefit": init.expected_benefit,
                "prioritisation_score": score,
            })
        return sorted(ranked, key=lambda x: x["prioritisation_score"], reverse=True)
