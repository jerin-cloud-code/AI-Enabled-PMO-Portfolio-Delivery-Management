"""
Risk and Dependency Summary Report Generator.
"""
import os
from typing import List
from src.models.raid import RAIDItem, DecisionItem

class RiskDependencyReportGenerator:
    def generate_report(self, raid_items: List[RAIDItem], decisions: List[DecisionItem], output_path: str) -> str:
        risks = [r for r in raid_items if r.item_type == "Risk"]
        issues = [r for r in raid_items if r.item_type == "Issue"]
        deps = [r for r in raid_items if r.item_type == "Dependency"]

        md_content = f"""# Portfolio Risk, Dependency & Decision Report

> **SYNTHETIC DEMONSTRATION DATA — NOT FROM A REAL ORGANISATION**

## 1. Top Risks ({len(risks)})
"""
        for r in risks:
            md_content += f"- **[{r.raid_id}] ({r.initiative_id}):** {r.summary} | Impact: {r.severity_impact} | Owner: {r.owner}\n"

        md_content += f"\n## 2. Active Issues ({len(issues)})\n"
        for i in issues:
            md_content += f"- **[{i.raid_id}] ({i.initiative_id}):** {i.summary} | Owner: {i.owner}\n"

        md_content += f"\n## 3. Cross-Portfolio Dependencies ({len(deps)})\n"
        for d in deps:
            md_content += f"- **[{d.raid_id}] ({d.initiative_id}):** {d.summary} | Target Date: {d.target_date}\n"

        md_content += f"\n## 4. Pending Decisions Required ({len(decisions)})\n"
        for dec in decisions:
            md_content += f"- **[{dec.decision_id}] ({dec.initiative_id}):** {dec.ask} | Recommended: {dec.recommendation}\n"

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        return output_path
