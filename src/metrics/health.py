"""
Portfolio Health Scoring Engine.
Computes composite health score (0-100) across RAG mix, spend variance, and data quality status.
"""
from typing import List
from src.models.initiative import Initiative

def calculate_portfolio_health_score(initiatives: List[Initiative]) -> float:
    if not initiatives:
        return 100.0

    total = len(initiatives)
    red_count = sum(1 for i in initiatives if i.rag_status == "RED")
    amber_count = sum(1 for i in initiatives if i.rag_status == "AMBER")
    exception_count = sum(1 for i in initiatives if i.data_quality_status == "EXCEPTIONS_FOUND")

    # Penalty deductions
    red_penalty = (red_count / total) * 40.0
    amber_penalty = (amber_count / total) * 15.0
    dq_penalty = (exception_count / total) * 15.0

    score = 100.0 - red_penalty - amber_penalty - dq_penalty
    return round(max(0.0, score), 1)
