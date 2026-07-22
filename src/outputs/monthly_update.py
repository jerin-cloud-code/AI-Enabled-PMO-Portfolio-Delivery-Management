"""
Monthly Portfolio Update Report Generator.
"""
import os
from typing import List, Dict, Any
from src.models.initiative import Initiative
from src.metrics.engine import MetricsEngine

class MonthlyUpdateGenerator:
    def generate_report(self, current_initiatives: List[Initiative], summary_text: str, output_path: str) -> str:
        engine = MetricsEngine()
        m = engine.calculate_portfolio_summary(current_initiatives)

        red_inits = [i for i in current_initiatives if i.rag_status == "RED"]

        md_content = f"""# Monthly Portfolio Update Report — March 2025

> **SYNTHETIC DEMONSTRATION DATA — NOT FROM A REAL ORGANISATION**

## 1. Executive Summary
{summary_text}

## 2. Portfolio Performance & Metrics Overview
- **Total Initiatives:** {m['total_initiatives']}
- **Overall Portfolio RAG:** {m['overall_rag']}
- **Portfolio Health Score:** {m['health_score']}/100
- **Total Approved Budget:** £{m['total_budget']:,.2f}
- **Actual Spend to Date:** £{m['total_actual_cost']:,.2f} (Variance: {m['spend_variance_pct']}%)
- **RAG Status Mix:** {m['green_count']} GREEN | {m['amber_count']} AMBER | {m['red_count']} RED

## 3. Escalations & Exceptions (Critical Review Path)
"""
        for r in red_inits:
            md_content += f"- **[{r.initiative_id}] {r.title}:** Budget £{r.budget:,.2f} vs Actual £{r.actual_cost:,.2f}. Owner: {r.delivery_owner}. Action: Variance review.\n"

        md_content += """
## 4. Key Delivery Highlights
- Technology Delivery: API Gateway modernization phase 1 completed.
- Data & Analytics: Enterprise Data Mesh architecture approved.
- AI & ML: NLP Bot initial training pipeline validated.

## 5. Next Period Governance Agenda
- Investment Committee gating review: March 25, 2025.
- Data Quality Exception remediation follow-up.
"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        return output_path
