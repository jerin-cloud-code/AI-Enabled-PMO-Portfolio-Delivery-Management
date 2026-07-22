#!/usr/bin/env python3
"""
Master Output Generator Script.
Loads synthetic dataset, runs validation, computes metrics, executes AI summarisation,
and generates all executive portfolio deliverables into outputs/samples/.
"""
import os
import sys

# Ensure src is on path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from src.importers.csv_importer import CSVImporter
from src.validation.engine import ValidationEngine
from src.metrics.engine import MetricsEngine
from src.raid.tracker import RAIDTracker
from src.ai.summariser import PortfolioSummariser
from src.outputs.one_page_view import OnePageViewGenerator
from src.outputs.excel_workbook import ExcelWorkbookGenerator
from src.outputs.pptx_pack import PowerPointPackGenerator
from src.outputs.monthly_update import MonthlyUpdateGenerator
from src.outputs.data_quality_report import DataQualityReportGenerator
from src.outputs.demand_report import DemandReportGenerator
from src.outputs.risk_dependency_report import RiskDependencyReportGenerator
from src.outputs.dashboard import DashboardGenerator

def main():
    print("Executing Master Output Generation Pipeline...")
    data_path = os.path.join(base_dir, "data", "synthetic", "initiatives.csv")
    raid_path = os.path.join(base_dir, "data", "synthetic", "raid_log.csv")
    decisions_path = os.path.join(base_dir, "data", "synthetic", "decisions.csv")
    samples_dir = os.path.join(base_dir, "outputs", "samples")
    os.makedirs(samples_dir, exist_ok=True)

    # 1. Load Data
    importer = CSVImporter()
    initiatives = importer.load_initiatives(data_path)

    raid_tracker = RAIDTracker()
    raid_tracker.load_raid_log(raid_path)
    raid_tracker.load_decisions(decisions_path)

    # 2. Validate Data
    val_engine = ValidationEngine()
    val_summary = val_engine.validate_portfolio(initiatives)

    # 3. Metrics & AI Summary
    metrics_engine = MetricsEngine()
    metrics_summary = metrics_engine.calculate_portfolio_summary(initiatives)

    summariser = PortfolioSummariser()
    ai_summary_out = summariser.generate_portfolio_summary(metrics_summary)
    summary_text = ai_summary_out["text"]

    # 4. Generate Deliverables
    print("Generating One-Page Executive View...")
    OnePageViewGenerator().generate_html(initiatives, summary_text, os.path.join(samples_dir, "one_page_view.html"))

    print("Generating Excel Portfolio Workbook...")
    ExcelWorkbookGenerator().generate_workbook(initiatives, val_summary["exceptions"], os.path.join(samples_dir, "portfolio_workbook.xlsx"))

    print("Generating PowerPoint Governance Pack...")
    PowerPointPackGenerator().generate_pack(initiatives, summary_text, os.path.join(samples_dir, "governance_pack.pptx"))

    print("Generating Monthly Portfolio Update...")
    MonthlyUpdateGenerator().generate_report(initiatives, summary_text, os.path.join(samples_dir, "monthly_update.html"))

    print("Generating Data Quality Exception Report...")
    DataQualityReportGenerator().generate_report(val_summary["exceptions"], os.path.join(samples_dir, "data_quality_report.html"))

    print("Generating Demand Pipeline Report...")
    DemandReportGenerator().generate_report(metrics_summary["demand"], os.path.join(samples_dir, "demand_pipeline.html"))

    print("Generating Risk and Dependency Report...")
    RiskDependencyReportGenerator().generate_report(raid_tracker.raid_items, raid_tracker.decisions, os.path.join(samples_dir, "risk_dependency_report.html"))

    print("Generating Local HTML Dashboard...")
    DashboardGenerator().generate_dashboard(initiatives, os.path.join(samples_dir, "dashboard"))

    print("Master Output Generation Pipeline completed successfully!")

if __name__ == "__main__":
    main()
