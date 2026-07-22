"""
Demand Pipeline Report Generator.
"""
import os
from typing import Dict, Any

class DemandReportGenerator:
    def generate_report(self, demand_metrics: Dict[str, Any], output_path: str) -> str:
        md_content = f"""# Portfolio Demand Pipeline & Shaping Report

> **SYNTHETIC DEMONSTRATION DATA — NOT FROM A REAL ORGANISATION**

## 1. Funnel Overview
- **Front-Door Intake Proposals:** {demand_metrics['intake_count']}
- **Active Shaping Business Cases:** {demand_metrics['shaping_count']}
- **Approved Mobilising Initiatives:** {demand_metrics['approved_count']}
- **Total Pipeline Volume:** {demand_metrics['total_demand_pipeline']}

## 2. Shaping Stage Breakdown
"""
        for stage, cnt in demand_metrics['shaping_by_stage'].items():
            md_content += f"- **{stage}:** {cnt} proposal(s)\n"

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        return output_path
