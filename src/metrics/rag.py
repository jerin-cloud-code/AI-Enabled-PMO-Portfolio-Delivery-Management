"""
RAG Status Calculation Engine.
Calculates deterministic RAG status based on spend variance and milestone delay thresholds.
"""

def calculate_rag_status(budget: float, actual_cost: float, forecast_cost: float, schedule_delay_days: int = 0) -> str:
    if budget <= 0:
        return "GREEN"
    
    spend_variance_pct = ((actual_cost - budget) / budget) * 100.0 if budget > 0 else 0.0

    if spend_variance_pct > 15.0 or schedule_delay_days > 30:
        return "RED"
    elif spend_variance_pct > 5.0 or schedule_delay_days > 7:
        return "AMBER"
    else:
        return "GREEN"
