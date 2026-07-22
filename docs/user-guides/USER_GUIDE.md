# PMO System User Guide & Execution Commands

## Quick Start
```bash
# 1. Run full end-to-end master runner script
python scripts/run_all.py

# 2. Run automated test suite
python -m unittest discover -s tests -p "test_*.py"
```

## Generated Outputs Location
All generated executive deliverables are placed in `outputs/samples/`:
- `one_page_view.html` — Print-ready executive view
- `portfolio_workbook.csv` — Excel portfolio workbook
- `governance_pack.pptx.txt` — Executive PowerPoint review pack
- `monthly_update.html` — Monthly portfolio update report
- `data_quality_report.html` — Exception report
- `dashboard/index.html` — Local static HTML dashboard
