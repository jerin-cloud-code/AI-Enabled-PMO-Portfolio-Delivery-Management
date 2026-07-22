# Portfolio Evidence Map for PMO Role Competencies

| Competency Area | Evidence File / Code | Key Demonstrable Outcome |
|---|---|---|
| AI-Enabled PMO Support | `src/ai/summariser.py`, `src/ai/validation.py` | Automated drafting of portfolio narratives with NIST-aligned factual validation |
| Data Quality Assurance | `src/validation/engine.py`, `docs/VALIDATION_RULES.md` | Automated rule engine catching 10 controlled defects (staleness, missing owners, overruns) |
| Executive Reporting | `src/outputs/one_page_view.py`, `templates/one_page_view.html` | Print-ready one-page executive view with RAG metrics and domain breakdowns |
| Governance Pack Prep | `src/outputs/pptx_pack.py` | 8-slide PowerPoint governance pack with "Decisions Required" Ask/Options structure |
| Intake & Duplicate Review | `src/analysis/duplicates.py`, `src/intake/pipeline.py` | TF-IDF text similarity algorithm identifying overlapping initiative proposals |
| Portfolio Metrics | `src/metrics/engine.py` | Composite health score, budget variance, and RAG status calculation engine |
