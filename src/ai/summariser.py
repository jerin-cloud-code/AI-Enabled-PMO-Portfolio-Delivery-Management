"""
Portfolio AI Summary Generator.
Uses AI Adapter (Fallback or LLM) to generate executive portfolio and initiative narratives.
"""
from typing import Dict, Any, List
from src.ai.fallback import OfflineFallbackAIAdapter
from src.models.initiative import Initiative

class PortfolioSummariser:
    def __init__(self, ai_adapter=None):
        self.ai_adapter = ai_adapter or OfflineFallbackAIAdapter()

    def generate_portfolio_summary(self, metrics_summary: Dict[str, Any]) -> Dict[str, Any]:
        return self.ai_adapter.generate_summary("portfolio_summary", metrics_summary)

    def generate_initiative_summary(self, initiative: Initiative) -> Dict[str, Any]:
        context = {
            "initiative_id": initiative.initiative_id,
            "title": initiative.title,
            "portfolio_category": initiative.portfolio_category,
            "lifecycle_stage": initiative.lifecycle_stage,
            "rag_status": initiative.rag_status,
            "progress_pct": initiative.progress_pct,
            "budget": initiative.budget,
            "actual_cost": initiative.actual_cost,
        }
        return self.ai_adapter.generate_summary("initiative_summary", context)
