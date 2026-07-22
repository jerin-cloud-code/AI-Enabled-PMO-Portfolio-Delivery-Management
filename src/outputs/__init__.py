"""
Outputs package initialization.
"""
from src.outputs.one_page_view import OnePageViewGenerator
from src.outputs.excel_workbook import ExcelWorkbookGenerator
from src.outputs.pptx_pack import PowerPointPackGenerator
from src.outputs.monthly_update import MonthlyUpdateGenerator
from src.outputs.data_quality_report import DataQualityReportGenerator
from src.outputs.demand_report import DemandReportGenerator
from src.outputs.risk_dependency_report import RiskDependencyReportGenerator
from src.outputs.dashboard import DashboardGenerator

__all__ = [
    "OnePageViewGenerator",
    "ExcelWorkbookGenerator",
    "PowerPointPackGenerator",
    "MonthlyUpdateGenerator",
    "DataQualityReportGenerator",
    "DemandReportGenerator",
    "RiskDependencyReportGenerator",
    "DashboardGenerator",
]
