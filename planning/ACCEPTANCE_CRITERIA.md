# ACCEPTANCE CRITERIA — ai-enabled-portfolio-pmo

## Gate 0 — Planning Completeness

| ID | Criterion | Measure |
|---|---|---|
| AC-G0-01 | All 17 planning files exist in `.planning/` | File count = 17 |
| AC-G0-02 | MASTER_CHECKLIST.md contains all tasks | ≥70 task rows across all phases |
| AC-G0-03 | REQUIREMENTS_REGISTER.csv covers all role requirements | ≥41 REQ-### entries |
| AC-G0-04 | REQUIREMENTS_TRACEABILITY_PLAN.csv has full chain per REQ | No empty cells in chain |
| AC-G0-05 | REPOSITORY_BLUEPRINT.md has directory tree + module descriptions | Tree + table present |
| AC-G0-06 | AGENT_WORK_PACKAGES.md defines all 15 agents | 15 agent sections |
| AC-G0-07 | PLAN_CRITIQUE.md evaluates from 10 perspectives | 10 sections present |
| AC-G0-08 | REVISED_MASTER_PLAN.md addresses critique items | Each critique item resolved |
| AC-G0-09 | Git commit contains all planning files | `git log` + `git ls-files` confirm |
| AC-G0-10 | APPROVAL_REQUIRED.md shows AWAITING USER APPROVAL | File content matches |

## Gate 1 — Research & Source Verification

| ID | Criterion | Measure |
|---|---|---|
| AC-G1-01 | PMO framework research completed | research/pmo_frameworks.md exists with SRC-### |
| AC-G1-02 | Jira data format research completed | research/jira_data_formats.md exists |
| AC-G1-03 | All research items cite sources with SRC-### | Source register has ≥10 entries |
| AC-G1-04 | Source register compiled | docs/SOURCE_REGISTER.md exists |
| AC-G1-05 | Research backlog fully addressed | No OPEN items in RESEARCH_BACKLOG.md |

## Gate 2 — Requirements & Data Model

| ID | Criterion | Measure |
|---|---|---|
| AC-G2-01 | Data model documented | docs/DATA_MODEL.md with ER diagram |
| AC-G2-02 | All entities have DATA-### field IDs | ≥30 DATA-### entries |
| AC-G2-03 | Synthetic data spec complete | docs/SYNTHETIC_DATA_SPEC.md with distributions |
| AC-G2-04 | Validation rules catalogued | docs/VALIDATION_RULES.md with rule-to-DATA mapping |
| AC-G2-05 | Initiative lifecycle states defined | 5 states documented |
| AC-G2-06 | RAID model covers all 5 RAID types | Risks, Actions, Issues, Dependencies, Decisions |
| AC-G2-07 | Identifier system fully defined | docs/IDENTIFIER_SYSTEM.md with 10 types |
| AC-G2-08 | Traceability plan updated | All REQ chains populated |

## Gate 3 — Core Implementation

| ID | Criterion | Measure |
|---|---|---|
| AC-G3-01 | Synthetic dataset generated | data/synthetic/ has ≥40 initiatives across 5 portfolios |
| AC-G3-02 | CSV/JSON importers work | Parse sample data without errors |
| AC-G3-03 | Validation engine enforces all rules | Exception report generated for known-bad data |
| AC-G3-04 | Metrics engine calculates RAG + health | Output matches manual calculation |
| AC-G3-05 | RAID tracker CRUD works | Create, read, update, delete verified |
| AC-G3-06 | Stale-update detection flags old records | Configurable threshold; test data triggers alerts |
| AC-G3-07 | Duplicate detector finds planted duplicates | Known duplicates scored above threshold |
| AC-G3-08 | Intake pipeline tracks lifecycle | Initiative progresses through all states |
| AC-G3-09 | AI fallback produces output without API key | Deterministic summary generated |
| AC-G3-10 | AI adapter interface defined | Abstract class with generate() method |
| AC-G3-11 | AI summary generator works with fallback | Summary text produced, formatted correctly |
| AC-G3-12 | Human review workflow state machine works | Draft → Review → Approve/Reject transitions |
| AC-G3-13 | AI factual validator catches planted errors | Error detection rate > 80% |

## Gate 4 — Generated PMO Outputs

| ID | Criterion | Measure |
|---|---|---|
| AC-G4-01 | One-page view renders correctly | HTML opens in browser; all sections populated |
| AC-G4-02 | Excel workbook has required tabs | Summary, Initiatives, RAID, Metrics tabs present |
| AC-G4-03 | PowerPoint pack has required slides | Title, Agenda, Summary, RAID, Decisions, Next Steps |
| AC-G4-04 | Monthly update shows period comparison | Current vs previous month data |
| AC-G4-05 | Data-quality report lists exceptions | Severity, owner, age columns present |
| AC-G4-06 | Demand pipeline shows funnel | Intake → Shaping → Approved counts |
| AC-G4-07 | Risk/dependency report complete | Open items listed with mitigations |
| AC-G4-08 | Dashboard renders locally | index.html opens from filesystem |
| AC-G4-09 | Templates are reusable | Template files separate from generated outputs |

## Gate 5 — Automated Testing

| ID | Criterion | Measure |
|---|---|---|
| AC-G5-01 | All test files exist | tests/ directory has ≥13 test files |
| AC-G5-02 | Unit tests pass | `pytest tests/` returns 0 exit code |
| AC-G5-03 | Integration test passes | test_pipeline.py end-to-end succeeds |
| AC-G5-04 | AI fallback test passes | Deterministic output verified |
| AC-G5-05 | Output validation tests pass | Excel, PPTX, HTML outputs validated |
| AC-G5-06 | Data-quality regression passes | Known-bad records flagged |

## Gate 6 — Independent Cross-Verification

| ID | Criterion | Measure |
|---|---|---|
| AC-G6-01 | Every REQ-### has implementation evidence | Traceability audit: 0 gaps |
| AC-G6-02 | All identifier cross-references consistent | No orphaned IDs |
| AC-G6-03 | All documentation files present | README + docs/ complete |
| AC-G6-04 | Output figures reconcile to source data | Spot-check: 100% match |

## Gate 7 — Adversarial Audit

| ID | Criterion | Measure |
|---|---|---|
| AC-G7-01 | No exaggerated claims | All README/docs claims verifiable |
| AC-G7-02 | No real-company leakage | Zero real names, logos, confidential data |
| AC-G7-03 | Interview-ready | Every module explainable by candidate |

## Gate 8 — Clean Build & Reproducibility

| ID | Criterion | Measure |
|---|---|---|
| AC-G8-01 | Fresh clone builds successfully | pip install + generate: 0 errors |
| AC-G8-02 | All tests pass in clean environment | pytest: 0 failures |
| AC-G8-03 | No secrets in repository | Secret scan: 0 findings |
| AC-G8-04 | No paid dependencies | Dependency audit: all OSS/free |

## Gate 9 — Final Review

| ID | Criterion | Measure |
|---|---|---|
| AC-G9-01 | README polished and complete | Overview, setup, usage, architecture, limitations |
| AC-G9-02 | Interview demo guide complete | Step-by-step script with talking points |
| AC-G9-03 | CV/LinkedIn wording guide complete | Honest descriptions, no exaggeration |
| AC-G9-04 | All sample outputs in outputs/samples/ | Pre-generated files present |

## Gate 10 — GO/NO-GO

| ID | Criterion | Measure |
|---|---|---|
| AC-G10-01 | All prior gates passed | Gate 0–9: COMPLETE |
| AC-G10-02 | No critical defects open | DEF-### count with severity CRITICAL: 0 |
| AC-G10-03 | User approval obtained | APPROVAL_REQUIRED.md: APPROVED |
