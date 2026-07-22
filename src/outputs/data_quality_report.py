"""
Data Quality Exception Report Generator.
"""
import os
from typing import List
from src.validation.exceptions import DataQualityException

class DataQualityReportGenerator:
    def generate_report(self, exceptions: List[DataQualityException], output_path: str) -> str:
        blockers = [e for e in exceptions if e.severity == "BLOCKER"]
        warnings = [e for e in exceptions if e.severity == "WARNING"]
        infos = [e for e in exceptions if e.severity == "INFO"]

        md_content = f"""# Data Quality Exception Report

> **SYNTHETIC DEMONSTRATION DATA — NOT FROM A REAL ORGANISATION**

## Summary Exception Statistics
- **Total Exceptions Found:** {len(exceptions)}
- **BLOCKER Exceptions:** {len(blockers)}
- **WARNING Exceptions:** {len(warnings)}
- **INFO Advisory Items:** {len(infos)}

## Detailed Exception Log

| Rule ID | Rule Name | Severity | Initiative ID | Field | Error Message | Owner |
|---|---|---|---|---|---|---|
"""
        for exc in exceptions:
            md_content += f"| {exc.rule_id} | {exc.rule_name} | {exc.severity} | {exc.initiative_id} | {exc.field_name} | {exc.error_message} | {exc.owner} |\n"

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        return output_path
