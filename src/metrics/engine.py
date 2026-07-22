"""
Master Metrics Calculation Engine.
Calculates portfolio-level aggregate totals, RAG distribution, budget vs actuals, and health scores.
"""
from typing import List, Dict, Any
from src.models.initiative import Initiative
from src.metrics.health import calculate_portfolio_health_score
from src.metrics.demand import calculate_demand_metrics

class MetricsEngine:
    def calculate_portfolio_summary(self, initiatives: List[Initiative]) -> Dict[str, Any]:
        total_initiatives = len(initiatives)
        total_budget = sum(i.budget for i in initiatives)
        total_actual = sum(i.actual_cost for i in initiatives)
        total_forecast = sum(i.forecast_cost for i in initiatives)
        total_benefit = sum(i.expected_benefit for i in initiatives)

        red_count = sum(1 for i in initiatives if i.rag_status == "RED")
        amber_count = sum(1 for i in initiatives if i.rag_status == "AMBER")
        green_count = sum(1 for i in initiatives if i.rag_status == "GREEN")

        overall_rag = "RED" if red_count >= 3 else ("AMBER" if red_count > 0 or amber_count >= 5 else "GREEN")
        health_score = calculate_portfolio_health_score(initiatives)
        demand_metrics = calculate_demand_metrics(initiatives)

        by_category = {}
        for cat in ["Technology", "Data", "AI", "Cyber Security", "Fraud Prevention"]:
            cat_inits = [i for i in initiatives if i.portfolio_category == cat]
            by_category[cat] = {
                "count": len(cat_inits),
                "budget": sum(i.budget for i in cat_inits),
                "actual_cost": sum(i.actual_cost for i in cat_inits),
                "red_count": sum(1 for i in cat_inits if i.rag_status == "RED"),
                "amber_count": sum(1 for i in cat_inits if i.rag_status == "AMBER"),
                "green_count": sum(1 for i in cat_inits if i.rag_status == "GREEN"),
            }

        return {
            "total_initiatives": total_initiatives,
            "overall_rag": overall_rag,
            "health_score": health_score,
            "total_budget": total_budget,
            "total_actual_cost": total_actual,
            "total_forecast_cost": total_forecast,
            "total_expected_benefit": total_benefit,
            "spend_variance_pct": round(((total_actual - total_budget) / total_budget) * 100.0, 2) if total_budget > 0 else 0.0,
            "red_count": red_count,
            "amber_count": amber_count,
            "green_count": green_count,
            "by_category": by_category,
            "demand": demand_metrics,
        }
