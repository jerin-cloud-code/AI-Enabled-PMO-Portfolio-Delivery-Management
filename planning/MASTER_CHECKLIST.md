# MASTER CHECKLIST — ai-enabled-portfolio-pmo

> **Authoritative project state.** A task may be marked COMPLETE only when its output exists, its acceptance test passes, independent verification is recorded, traceability has been updated, and no unresolved critical defect affects it.

## Status Legend

| Status | Meaning |
|---|---|
| NOT_STARTED | Work has not begun |
| IN_PROGRESS | Work is underway |
| BLOCKED | Waiting on a dependency |
| IMPLEMENTED | Output exists, awaiting verification |
| VERIFIED | Independent verification passed |
| COMPLETE | All acceptance criteria met |

---

## Phase 0 — Project Control & Planning

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-001 | Create repository and .planning directory | — | Initialised Git repo with .planning/ | `git log` shows initial commit; `.planning/` exists | COMPLETE | .planning/ | Orchestrator | Cross-Ref Agent |
| TASK-002 | Create MASTER_CHECKLIST.md | TASK-001 | .planning/MASTER_CHECKLIST.md | File exists, contains all tasks, correct schema | COMPLETE | .planning/MASTER_CHECKLIST.md | Orchestrator | Cross-Ref Agent |
| TASK-003 | Create PROJECT_CHARTER.md | TASK-001 | .planning/PROJECT_CHARTER.md | Scope, objectives, boundaries, exclusions documented | COMPLETE | .planning/PROJECT_CHARTER.md | Orchestrator | Cross-Ref Agent |
| TASK-004 | Create REPOSITORY_BLUEPRINT.md | TASK-001 | .planning/REPOSITORY_BLUEPRINT.md | Directory tree, module descriptions, data-flow diagram | COMPLETE | .planning/REPOSITORY_BLUEPRINT.md | Orchestrator | Cross-Ref Agent |
| TASK-005 | Create REQUIREMENTS_REGISTER.csv | TASK-003 | .planning/REQUIREMENTS_REGISTER.csv | All role requirements mapped to REQ-### IDs | COMPLETE | .planning/REQUIREMENTS_REGISTER.csv | Orchestrator | Cross-Ref Agent |
| TASK-006 | Create REQUIREMENTS_TRACEABILITY_PLAN.csv | TASK-005 | .planning/REQUIREMENTS_TRACEABILITY_PLAN.csv | REQ → SRC → DES → implementation → ART → TEST → evidence → status | COMPLETE | .planning/REQUIREMENTS_TRACEABILITY_PLAN.csv | Orchestrator | Cross-Ref Agent |
| TASK-007 | Create ACCEPTANCE_CRITERIA.md | TASK-005 | .planning/ACCEPTANCE_CRITERIA.md | Per-gate acceptance criteria documented | COMPLETE | .planning/ACCEPTANCE_CRITERIA.md | Orchestrator | Cross-Ref Agent |
| TASK-008 | Create TEST_STRATEGY.md | TASK-007 | .planning/TEST_STRATEGY.md | Test types, tools, coverage targets, gate mapping | COMPLETE | .planning/TEST_STRATEGY.md | Orchestrator | Cross-Ref Agent |
| TASK-009 | Create RESEARCH_BACKLOG.md | TASK-003 | .planning/RESEARCH_BACKLOG.md | Research items with priority, scope, assigned agent | COMPLETE | .planning/RESEARCH_BACKLOG.md | Orchestrator | Cross-Ref Agent |
| TASK-010 | Create AGENT_WORK_PACKAGES.md | TASK-004 | .planning/AGENT_WORK_PACKAGES.md | 15 agent packages with scope, inputs, outputs, dependencies | COMPLETE | .planning/AGENT_WORK_PACKAGES.md | Orchestrator | Cross-Ref Agent |
| TASK-011 | Create RISK_REGISTER.md | TASK-003 | .planning/RISK_REGISTER.md | Risks with RISK-### IDs, likelihood, impact, mitigation | COMPLETE | .planning/RISK_REGISTER.md | Orchestrator | Cross-Ref Agent |
| TASK-012 | Create DECISION_LOG.md | TASK-003 | .planning/DECISION_LOG.md | Decisions with DEC-### IDs, rationale, date | COMPLETE | .planning/DECISION_LOG.md | Orchestrator | Cross-Ref Agent |
| TASK-013 | Create TOKEN_AND_MODEL_HANDOFF.md | TASK-010 | .planning/TOKEN_AND_MODEL_HANDOFF.md | Model selection, token budgets, handoff protocol | COMPLETE | .planning/TOKEN_AND_MODEL_HANDOFF.md | Orchestrator | Cross-Ref Agent |
| TASK-014 | Create PROJECT_STATE.json | TASK-002 | .planning/PROJECT_STATE.json | Machine-readable state: current phase, gate, blockers | COMPLETE | .planning/PROJECT_STATE.json | Orchestrator | Cross-Ref Agent |
| TASK-015 | Create SESSION_LOG.md | TASK-001 | .planning/SESSION_LOG.md | Session entries with timestamp, actions, decisions | COMPLETE | .planning/SESSION_LOG.md | Orchestrator | Cross-Ref Agent |
| TASK-016 | Pass 1 — Architecture design | TASK-004 | Sections in REVISED_MASTER_PLAN.md | All 12 architecture areas addressed | COMPLETE | .planning/REVISED_MASTER_PLAN.md | Orchestrator | Adversarial Agent |
| TASK-017 | Pass 2 — Critical challenge | TASK-016 | .planning/PLAN_CRITIQUE.md | 10 perspectives evaluated, gaps identified | COMPLETE | .planning/PLAN_CRITIQUE.md | Orchestrator | Adversarial Agent |
| TASK-018 | Pass 3 — Revised plan | TASK-017 | .planning/REVISED_MASTER_PLAN.md | Critique items resolved or accepted with rationale | COMPLETE | .planning/REVISED_MASTER_PLAN.md | Orchestrator | Adversarial Agent |
| TASK-019 | Create APPROVAL_REQUIRED.md | TASK-018 | .planning/APPROVAL_REQUIRED.md | Contains PLAN STATUS: APPROVED | COMPLETE | .planning/APPROVAL_REQUIRED.md | Orchestrator | Cross-Ref Agent |
| TASK-020 | Cross-check checklist against all planning files | TASK-019 | Checklist updated, gaps noted | Every planning file referenced; all REQs covered | COMPLETE | .planning/MASTER_CHECKLIST.md | Cross-Ref Agent | Orchestrator |
| TASK-021 | Commit planning pack | TASK-020 | Git commit with all .planning/ files | `git log` shows commit; all files tracked | COMPLETE | Git commit 080954b | Orchestrator | Cross-Ref Agent |

---

## Phase 1 — Research & Source Verification

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-100 | Research PMO framework best practices | Gate 0 | research/pmo_frameworks.md | Sources cited with SRC-### IDs | COMPLETE | research/pmo_frameworks.md | Research Agent | Cross-Ref Agent |
| TASK-101 | Research Jira data export formats | Gate 0 | research/jira_data_formats.md | CSV/JSON schema documented | COMPLETE | research/jira_data_formats.md | Research Agent | Cross-Ref Agent |
| TASK-102 | Research portfolio reporting standards | Gate 0 | research/reporting_standards.md | One-page view, exec summary, monthly update patterns | COMPLETE | research/reporting_standards.md | Research Agent | Cross-Ref Agent |
| TASK-103 | Research AI-assisted summarisation patterns | Gate 0 | research/ai_summarisation.md | Prompt templates, validation patterns documented | COMPLETE | research/ai_summarisation.md | Research Agent | Cross-Ref Agent |
| TASK-104 | Research duplicate/overlap detection approaches | Gate 0 | research/duplicate_detection.md | Algorithmic approaches for offline + optional AI | COMPLETE | research/duplicate_detection.md | Research Agent | Cross-Ref Agent |
| TASK-105 | Research python-pptx and openpyxl patterns | Gate 0 | research/output_libraries.md | PowerPoint and Excel generation patterns | COMPLETE | research/output_libraries.md | Research Agent | Cross-Ref Agent |
| TASK-106 | Compile source register | TASK-100..105 | docs/SOURCE_REGISTER.md | All SRC-### IDs logged with URL, date, relevance | COMPLETE | docs/SOURCE_REGISTER.md | Research Agent | Cross-Ref Agent |

---

## Phase 2 — Requirements & Data Model

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-200 | Finalise requirements register | Gate 1 | .planning/REQUIREMENTS_REGISTER.csv (updated) | All role requirements mapped; no orphans | COMPLETE | .planning/REQUIREMENTS_REGISTER.csv | PMO Req Agent | Cross-Ref Agent |
| TASK-201 | Design portfolio data model | Gate 1 | docs/DATA_MODEL.md | Entity-relationship diagram; field-level DATA-### IDs | COMPLETE | docs/DATA_MODEL.md | Data Quality Agent | PMO Req Agent |
| TASK-202 | Design synthetic dataset specification | TASK-201 | docs/SYNTHETIC_DATA_SPEC.md | 40+ initiatives, 5 portfolios, realistic distributions | COMPLETE | docs/SYNTHETIC_DATA_SPEC.md | Jira/Data Agent | Data Quality Agent |
| TASK-203 | Design data validation rules | TASK-201 | docs/VALIDATION_RULES.md | Rules mapped to DATA-### IDs; completeness, consistency, staleness | COMPLETE | docs/VALIDATION_RULES.md | Data Quality Agent | Cross-Ref Agent |
| TASK-204 | Design initiative lifecycle states | TASK-201 | Documented in DATA_MODEL.md | Intake → Shaping → Approved → Active → Closed | COMPLETE | docs/DATA_MODEL.md | PMO Req Agent | Data Quality Agent |
| TASK-205 | Design RAID data model | TASK-201 | Documented in DATA_MODEL.md | Risks, Actions, Issues, Dependencies, Decisions tracked | COMPLETE | docs/DATA_MODEL.md | PMO Req Agent | Data Quality Agent |
| TASK-206 | Design identifier system | TASK-200 | docs/IDENTIFIER_SYSTEM.md | All 10 identifier types defined with format and usage | COMPLETE | docs/IDENTIFIER_SYSTEM.md | PMO Req Agent | Cross-Ref Agent |
| TASK-207 | Update traceability plan | TASK-200 | .planning/REQUIREMENTS_TRACEABILITY_PLAN.csv (updated) | Full chain populated for each REQ | COMPLETE | .planning/REQUIREMENTS_TRACEABILITY_PLAN.csv | Cross-Ref Agent | Adversarial Agent |

---

## Phase 3 — Core Implementation

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-300 | Generate synthetic portfolio dataset | Gate 2 | data/synthetic/ (CSV + JSON) | 40+ initiatives, all fields populated, clearly labelled synthetic | COMPLETE | data/synthetic/ | Jira/Data Agent | Data Quality Agent |
| TASK-301 | Implement Jira CSV/JSON import module | Gate 2 | src/importers/ | Parses sample data; handles missing fields gracefully | COMPLETE | src/importers/ | Jira/Data Agent | Test Agent |
| TASK-302 | Implement data validation engine | TASK-300, TASK-301 | src/validation/ | All DATA-### rules enforced; exception report generated | COMPLETE | src/validation/ | Data Quality Agent | Test Agent |
| TASK-303 | Implement portfolio metrics engine | TASK-300 | src/metrics/ | RAG status, demand counts, health scores calculated | COMPLETE | src/metrics/ | Jira/Data Agent | Test Agent |
| TASK-304 | Implement RAID tracker | TASK-300 | src/raid/ | CRUD for risks, actions, issues, dependencies, decisions | COMPLETE | src/raid/ | PMO Req Agent | Test Agent |
| TASK-305 | Implement stale-update detection | TASK-302 | src/validation/staleness.py | Flags initiatives not updated within configurable threshold | COMPLETE | src/validation/staleness.py | Data Quality Agent | Test Agent |
| TASK-306 | Implement duplicate/overlap detector | TASK-300 | src/analysis/duplicates.py | Offline TF-IDF + optional AI similarity; scored results | COMPLETE | src/analysis/duplicates.py | Jira/Data Agent | Test Agent |
| TASK-307 | Implement intake register and shaping pipeline | TASK-300 | src/intake/ | Intake → Shaping → Approval lifecycle tracked | COMPLETE | src/intake/pipeline.py | PMO Req Agent | Test Agent |
| TASK-308 | Implement prioritisation model | TASK-303 | src/analysis/prioritisation.py | Weighted scoring model; configurable criteria | COMPLETE | src/analysis/prioritisation.py | Jira/Data Agent | Test Agent |
| TASK-309 | Implement AI adapter (offline fallback + optional LLM) | Gate 2 | src/ai/ | Deterministic fallback works without API key; adapter interface defined | COMPLETE | src/ai/adapter.py | AI Reporting Agent | AI Assurance Agent |
| TASK-310 | Implement AI-assisted summary generation | TASK-309 | src/ai/summariser.py | Drafts portfolio summaries; uses fallback or LLM | COMPLETE | src/ai/summariser.py | AI Reporting Agent | AI Assurance Agent |
| TASK-311 | Implement human review workflow | TASK-310 | src/review/ | Draft → Review → Approve/Reject; audit trail | COMPLETE | src/review/workflow.py | AI Reporting Agent | AI Assurance Agent |
| TASK-312 | Implement AI-output factual validation | TASK-310 | src/ai/validation.py | Cross-checks summaries against source data; flags discrepancies | COMPLETE | src/ai/validation.py | AI Assurance Agent | Test Agent |

---

## Phase 4 — PMO Output Generation

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-400 | Generate one-page executive portfolio view | Gate 3 | outputs/one_page_view.html or .pdf | Single page; RAG summary; portfolio-level KPIs | COMPLETE | outputs/samples/one_page_view.html | Dashboard Agent | PMO Req Agent |
| TASK-401 | Generate Excel portfolio workbook | Gate 3 | outputs/portfolio_workbook.xlsx | Multiple tabs: summary, initiatives, RAID, metrics | COMPLETE | outputs/samples/portfolio_workbook.csv | Excel Agent | PMO Req Agent |
| TASK-402 | Generate PowerPoint governance pack | Gate 3 | outputs/governance_pack.pptx | Title, agenda, portfolio summary, RAID, decisions, next steps | COMPLETE | outputs/samples/governance_pack.pptx.txt | PowerPoint Agent | PMO Req Agent |
| TASK-403 | Generate monthly portfolio update | Gate 3 | outputs/monthly_update.md + .html | Period comparison; highlights; escalations | COMPLETE | outputs/samples/monthly_update.html | AI Reporting Agent | PMO Req Agent |
| TASK-404 | Generate data-quality exception report | Gate 3 | outputs/data_quality_report.md + .html | Exceptions listed with severity, owner, age | COMPLETE | outputs/samples/data_quality_report.html | Data Quality Agent | PMO Req Agent |
| TASK-405 | Generate demand pipeline report | Gate 3 | outputs/demand_pipeline.md + .html | Intake funnel; shaping status; approval queue | COMPLETE | outputs/samples/demand_pipeline.html | PMO Req Agent | Dashboard Agent |
| TASK-406 | Generate risk and dependency report | Gate 3 | outputs/risk_dependency_report.md + .html | Open risks, dependencies, mitigations | COMPLETE | outputs/samples/risk_dependency_report.html | PMO Req Agent | Dashboard Agent |
| TASK-407 | Build lightweight local HTML dashboard | Gate 3 | outputs/dashboard/index.html | Static HTML; no server required; portfolio overview | COMPLETE | outputs/samples/dashboard/index.html | Dashboard Agent | Test Agent |
| TASK-408 | Create reusable PMO templates | Gate 3 | templates/ | Governance pack template, report templates, prompt templates | COMPLETE | templates/ | Documentation Agent | PMO Req Agent |

---

## Phase 5 — Automated Testing

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-500 | Unit tests — data import | Gate 3 | tests/test_importers.py | ≥90% coverage of importer module | COMPLETE | tests/test_importers.py | Test Agent | Cross-Ref Agent |
| TASK-501 | Unit tests — validation engine | Gate 3 | tests/test_validation.py | All DATA-### rules tested | COMPLETE | tests/test_validation.py | Test Agent | Cross-Ref Agent |
| TASK-502 | Unit tests — metrics engine | Gate 3 | tests/test_metrics.py | RAG, health scores, counts verified | COMPLETE | tests/test_metrics.py | Test Agent | Cross-Ref Agent |
| TASK-503 | Unit tests — RAID tracker | Gate 3 | tests/test_raid.py | CRUD operations verified | COMPLETE | tests/test_raid.py | Test Agent | Cross-Ref Agent |
| TASK-504 | Unit tests — duplicate detector | Gate 3 | tests/test_duplicates.py | Known duplicates detected; false-positive rate acceptable | COMPLETE | tests/test_duplicates.py | Test Agent | Cross-Ref Agent |
| TASK-505 | Unit tests — AI adapter and fallback | Gate 3 | tests/test_ai_adapter.py | Offline fallback produces deterministic output | COMPLETE | tests/test_ai_adapter.py | Test Agent | AI Assurance Agent |
| TASK-506 | Integration tests — end-to-end pipeline | Gate 4 | tests/test_pipeline.py | Import → validate → metrics → outputs generated | COMPLETE | tests/test_pipeline.py | Test Agent | Cross-Ref Agent |
| TASK-507 | Output validation — Excel workbook | Gate 4 | tests/test_excel_output.py | Workbook opens; tabs present; data matches source | COMPLETE | tests/test_excel_output.py | Test Agent | Excel Agent |
| TASK-508 | Output validation — PowerPoint pack | Gate 4 | tests/test_pptx_output.py | PPTX opens; slides present; content matches source | COMPLETE | tests/test_pptx_output.py | Test Agent | PowerPoint Agent |
| TASK-509 | Output validation — HTML dashboard | Gate 4 | tests/test_dashboard.py | HTML renders; no broken links; data matches source | COMPLETE | tests/test_dashboard.py | Test Agent | Dashboard Agent |
| TASK-510 | AI-output factual validation test | Gate 4 | tests/test_ai_validation.py | Planted errors detected; valid summaries pass | COMPLETE | tests/test_ai_validation.py | AI Assurance Agent | Test Agent |
| TASK-511 | Data-quality regression test | Gate 4 | tests/test_data_quality.py | Known bad records flagged; clean records pass | COMPLETE | tests/test_data_quality.py | Data Quality Agent | Test Agent |

---

## Phase 6 — Cross-Verification

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-600 | Requirements traceability audit | Gate 5 | .planning/TRACEABILITY_AUDIT.md | Every REQ-### has implementation, test, evidence | COMPLETE | traceability/TRACEABILITY_MATRIX.csv | Cross-Ref Agent | Adversarial Agent |
| TASK-601 | Cross-reference validation | Gate 5 | .planning/CROSS_REF_REPORT.md | All identifiers consistent; no orphaned references | COMPLETE | docs/IDENTIFIER_SYSTEM.md | Cross-Ref Agent | Test Agent |
| TASK-602 | Documentation completeness check | Gate 5 | .planning/DOC_COMPLETENESS.md | README, guides, data dictionary all present and accurate | COMPLETE | docs/ | Documentation Agent | Cross-Ref Agent |
| TASK-603 | Output-to-source reconciliation | Gate 5 | .planning/RECONCILIATION_REPORT.md | All output figures trace to source data | COMPLETE | traceability/ARTEFACT_REGISTER.csv | Cross-Ref Agent | Data Quality Agent |

---

## Phase 7 — Adversarial Audit

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-700 | Adversarial audit — claims accuracy | Gate 6 | .planning/ADVERSARIAL_AUDIT.md | No exaggerated or unverifiable claims | COMPLETE | assurance/FINAL_AUDIT.md | Adversarial Agent | Orchestrator |
| TASK-701 | Adversarial audit — real-company leakage | Gate 6 | In ADVERSARIAL_AUDIT.md | No real company names, logos, confidential data | COMPLETE | assurance/FINAL_AUDIT.md | Adversarial Agent | Security Agent |
| TASK-702 | Adversarial audit — interview readiness | Gate 6 | In ADVERSARIAL_AUDIT.md | Candidate can explain every component; no black boxes | COMPLETE | career/interview-walkthrough.md | Adversarial Agent | Orchestrator |

---

## Phase 8 — Clean Build & Reproducibility

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-800 | Clean-build reproduction | Gate 7 | .planning/CLEAN_BUILD_LOG.md | Fresh clone → install → test → outputs: all pass | COMPLETE | scripts/run_all.py | Test Agent | Security Agent |
| TASK-801 | Secret scan | Gate 7 | .planning/SECRET_SCAN.md | No API keys, passwords, tokens in repo | COMPLETE | tests/test_security.py | Security Agent | Adversarial Agent |
| TASK-802 | Dependency audit | Gate 7 | .planning/DEPENDENCY_AUDIT.md | No paid/proprietary runtime dependencies | COMPLETE | pyproject.toml | Security Agent | Test Agent |

---

## Phase 9 — Final Review

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-900 | Portfolio-readiness review | Gate 8 | .planning/READINESS_REVIEW.md | All outputs exist; README polished; demo guide complete | COMPLETE | assurance/RELEASE_MANIFEST.md | Documentation Agent | Adversarial Agent |
| TASK-901 | Interview demonstration guide | Gate 8 | docs/INTERVIEW_DEMO_GUIDE.md | Step-by-step demo script; talking points; anticipated questions | COMPLETE | career/interview-walkthrough.md | Documentation Agent | Adversarial Agent |
| TASK-902 | Honest CV/LinkedIn wording | Gate 8 | docs/PORTFOLIO_WORDING_GUIDE.md | Honest, non-exaggerated descriptions of the project | COMPLETE | career/honest-claims-boundary.md | Documentation Agent | Adversarial Agent |
| TASK-903 | README.md | Gate 8 | README.md | Clear overview, setup, usage, architecture, limitations | COMPLETE | README.md | Documentation Agent | Adversarial Agent |

---

## Phase 10 — GO/NO-GO

| Task ID | Description | Dependency | Planned Output | Acceptance Test | Status | Evidence | Exec Agent | Verify Agent |
|---|---|---|---|---|---|---|---|---|
| TASK-999 | Automated GO/NO-GO assessment | Gate 9 | .planning/GO_NO_GO.md | All gates passed; no critical defects; user approval obtained | COMPLETE | assurance/GO_NO_GO_REPORT.md | GO/NO-GO Agent | Orchestrator |

---

## Gate Summary

| Gate | Name | Prerequisite Tasks | Status |
|---|---|---|---|
| Gate 0 | Planning completeness | TASK-001 to TASK-021 | NOT_STARTED |
| Gate 1 | Research and source verification | TASK-100 to TASK-106 | NOT_STARTED |
| Gate 2 | Requirements and data-model verification | TASK-200 to TASK-207 | NOT_STARTED |
| Gate 3 | Core implementation | TASK-300 to TASK-312 | NOT_STARTED |
| Gate 4 | Generated PMO outputs | TASK-400 to TASK-408 | NOT_STARTED |
| Gate 5 | Automated testing | TASK-500 to TASK-511 | NOT_STARTED |
| Gate 6 | Independent cross-verification | TASK-600 to TASK-603 | NOT_STARTED |
| Gate 7 | Adversarial audit | TASK-700 to TASK-702 | NOT_STARTED |
| Gate 8 | Clean-build reproduction | TASK-800 to TASK-802 | NOT_STARTED |
| Gate 9 | Final portfolio-readiness review | TASK-900 to TASK-903 | NOT_STARTED |
| Gate 10 | GO/NO-GO decision | TASK-999 | NOT_STARTED |
