# Python Reporting Libraries (openpyxl & python-pptx) Research

> **Source ID References:** `SRC-013` (openpyxl Official Documentation), `SRC-014` (python-pptx Official Documentation).

## 1. Excel Workbook Generation (`openpyxl`)

### Best Practices:
- Use explicit cell data types (`number_format`, `Font`, `PatternFill`, `Alignment`, `Border`).
- Auto-fit column widths based on max text length.
- Freeze header panes (`ws.freeze_panes = 'A2'`).
- Apply conditional formatting for RAG indicators (RED: `#FFC7CE`, AMBER: `#FFEB9C`, GREEN: `#C6EFCE`).
- Build multi-tab structure with clear tab hierarchy.

## 2. PowerPoint Slide Deck Generation (`python-pptx`)

### Best Practices:
- Load an existing `.pptx` template file (`templates/governance_pack.pptx`) containing branding layout and slide masters.
- Target specific shapes via named shape lookup or placeholder IDs.
- Ensure all text fits within text frames without clipping (`word_wrap = True`).
- Dynamic table generation for RAID and Decisions Required slides.
- Embedded watermark text on every slide: `"SYNTHETIC DEMONSTRATION DATA — NOT FROM A REAL ORGANISATION"`.
