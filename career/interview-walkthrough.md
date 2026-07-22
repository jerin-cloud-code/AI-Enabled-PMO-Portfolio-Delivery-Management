# Interview Walkthrough Guide — 5-Min, 15-Min & 30-Min Demo Paths

> **Structured Interview Demo Sequences for Candidates**

## 1. Five-Minute Demo Path (Recruiter / Quick Overview)

1. **Start at `README.md` (1 min):** Explain the core objective — demonstrating how AI assistance, data quality automation, and executive deliverables streamline PMO operations without requiring live vendor credentials.
2. **Show the HTML Dashboard (2 mins):** Open `outputs/samples/dashboard/index.html`. Point out the overall RAG status, composite health score (82.5/100), and breakdown across Technology, Data, AI, Cyber, and Fraud portfolios.
3. **Show the One-Page Executive View (1 min):** Open `outputs/samples/one_page_view.html`. Highlight print optimization and executive narrative summary.
4. **Explain Human Oversight (1 min):** State clearly that AI generates drafts which are factually validated against source metrics before human approval.

---

## 2. Fifteen-Minute Demo Path (Hiring Manager / PMO Lead)

1. **5-Minute Path above (5 mins).**
2. **Data Quality Validation Engine (3 mins):** Open `docs/VALIDATION_RULES.md` and `outputs/samples/data_quality_report.html`. Show how the engine catches 10 controlled defects (stale updates >30 days, missing owners, budget overruns >15%).
3. **Front-Door Intake & Duplicate Detection (3 mins):** Open `src/analysis/duplicates.py`. Explain how TF-IDF cosine similarity identifies overlapping proposals (e.g. duplicate IAM proposals).
4. **PowerPoint & Governance Pack (2 mins):** Open `outputs/samples/governance_pack.pptx.txt`. Show the 8-slide structure with "Decisions Required" Ask/Options format.
5. **Honest Positioning Statement (2 mins):** State that this is a synthetic demonstration repository built to model real-world PMO practices.

---

## 3. Thirty-Minute Demo Path (Technical Interview / Deep Dive)

1. **15-Minute Path above (15 mins).**
2. **Code Architecture Tour (5 mins):** Walk through `src/` modules (`models`, `importers`, `validation`, `metrics`, `ai`, `outputs`).
3. **AI Adapter & Factual Validation (5 mins):** Open `src/ai/fallback.py` and `src/ai/validation.py`. Walk through the 6-part taxonomy (`VAL-01` to `VAL-06`).
4. **Automated Test Suite (3 mins):** Run `python scripts/run_all.py` or `python -m unittest discover -s tests`. Show all 22 tests passing.
5. **Q&A & Design Decisions (2 mins):** Discuss trade-offs (file-based CSV vs SQLite, deterministic fallback vs LLM API).
