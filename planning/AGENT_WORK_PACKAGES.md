# AGENT WORK PACKAGES — ai-enabled-portfolio-pmo

## Execution Model

- Planning: Expensive model (Opus-class)
- Implementation: Economy model (Flash/Sonnet-class) + specialist subagents
- Verification: Cross-agent — no agent verifies its own output
- Parallelism: Agents without dependencies run concurrently

## Dependency Graph

```
                     ┌──────────────────┐
                     │  Research Agent   │  Phase 1 (parallel)
                     └────────┬─────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
     ┌────────────────┐ ┌──────────────┐ ┌──────────────┐
     │ PMO Req Agent  │ │ Jira/Data Ag │ │ Data Qual Ag │  Phase 2 (parallel)
     └───────┬────────┘ └──────┬───────┘ └──────┬───────┘
             │                 │                │
             └────────┬────────┴────────┬───────┘
                      ▼                 ▼
            ┌──────────────┐   ┌──────────────────┐
            │ AI Report Ag │   │ AI Assurance Ag   │  Phase 3 (parallel pair)
            └──────┬───────┘   └────────┬──────────┘
                   │                    │
     ┌─────────┬───┴────┬──────────────┘
     ▼         ▼        ▼
┌─────────┐ ┌───────┐ ┌──────────┐
│Excel Ag │ │PPT Ag │ │Dashbd Ag │  Phase 4 (parallel trio)
└────┬────┘ └───┬───┘ └────┬─────┘
     │          │          │
     └──────────┼──────────┘
                ▼
        ┌──────────────┐
        │  Test Agent   │  Phase 5
        └──────┬───────┘
               ▼
     ┌──────────────────┐
     │ Cross-Ref Agent  │  Phase 6
     └────────┬─────────┘
              ▼
     ┌──────────────────┐
     │Documentation Ag  │  Phase 6 (parallel with cross-ref)
     └────────┬─────────┘
              ▼
     ┌──────────────────┐
     │ Security Agent   │  Phase 7
     └────────┬─────────┘
              ▼
     ┌──────────────────┐
     │ Adversarial Ag   │  Phase 7
     └────────┬─────────┘
              ▼
     ┌──────────────────┐
     │ GO/NO-GO Agent   │  Phase 10
     └──────────────────┘
```

---

## WP-01: Research Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | RESEARCH_BACKLOG.md |
| **Outputs** | research/*.md, docs/SOURCE_REGISTER.md |
| **Tasks** | TASK-100 to TASK-106 |
| **Dependencies** | Gate 0 (planning approved) |
| **Parallel with** | None (first execution phase) |
| **Verification by** | Cross-Ref Agent |

**Scope**: Research PMO frameworks, Jira formats, reporting standards, AI summarisation patterns, duplicate detection, python-pptx/openpyxl, SharePoint guidance. Produce concise summaries with SRC-### citations.

---

## WP-02: PMO Requirements Agent

| Field | Value |
|---|---|
| **Model** | Economy (Sonnet) |
| **Inputs** | Research outputs, REQUIREMENTS_REGISTER.csv |
| **Outputs** | Updated REQUIREMENTS_REGISTER.csv, docs/GOVERNANCE_GUIDE.md, docs/IDENTIFIER_SYSTEM.md |
| **Tasks** | TASK-200, TASK-204, TASK-205, TASK-206 |
| **Dependencies** | Gate 1 |
| **Parallel with** | Jira/Data Agent, Data Quality Agent |
| **Verification by** | Cross-Ref Agent, Data Quality Agent |

**Scope**: Finalise requirements, define governance cadence, design RAID model, define identifier taxonomy, design initiative lifecycle. PMO domain expertise.

---

## WP-03: Jira & Portfolio Data Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | Research outputs, data model, synthetic data spec |
| **Outputs** | data/synthetic/*, src/importers/*, src/models/*, src/analysis/duplicates.py, src/analysis/prioritisation.py |
| **Tasks** | TASK-202, TASK-300, TASK-301, TASK-303, TASK-306, TASK-308 |
| **Dependencies** | Gate 1 |
| **Parallel with** | PMO Req Agent, Data Quality Agent |
| **Verification by** | Test Agent, Data Quality Agent |

**Scope**: Generate synthetic dataset, build CSV/JSON importers, implement metrics engine, build duplicate detector, implement prioritisation model.

---

## WP-04: Data Quality Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | Data model, validation rules |
| **Outputs** | src/validation/*, config/validation_rules.yaml, docs/VALIDATION_RULES.md |
| **Tasks** | TASK-201, TASK-203, TASK-302, TASK-305 |
| **Dependencies** | Gate 1 |
| **Parallel with** | PMO Req Agent, Jira/Data Agent |
| **Verification by** | Test Agent |

**Scope**: Design data model, catalogue validation rules, implement validation engine, implement staleness detection.

---

## WP-05: AI Reporting Agent

| Field | Value |
|---|---|
| **Model** | Economy (Sonnet) |
| **Inputs** | Data model, prompt templates, metrics |
| **Outputs** | src/ai/adapter.py, src/ai/fallback.py, src/ai/summariser.py, src/review/workflow.py, templates/prompts/*.txt |
| **Tasks** | TASK-309, TASK-310, TASK-311 |
| **Dependencies** | Gate 2 |
| **Parallel with** | AI Assurance Agent |
| **Verification by** | AI Assurance Agent |

**Scope**: Implement AI adapter interface, deterministic fallback, summary generator, human review workflow, prompt templates.

---

## WP-06: AI Assurance Agent

| Field | Value |
|---|---|
| **Model** | Economy (Sonnet) |
| **Inputs** | AI outputs, source data |
| **Outputs** | src/ai/validation.py |
| **Tasks** | TASK-312 |
| **Dependencies** | Gate 2 (can start after AI adapter interface defined) |
| **Parallel with** | AI Reporting Agent |
| **Verification by** | Test Agent |

**Scope**: Implement factual validation of AI-generated summaries against source data. Cross-check claims, figures, status values.

---

## WP-07: Excel Reporting Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | Data model, metrics, templates |
| **Outputs** | src/outputs/excel_workbook.py, templates/portfolio_workbook.xlsx, outputs/samples/portfolio_workbook.xlsx |
| **Tasks** | TASK-401 |
| **Dependencies** | Gate 3 |
| **Parallel with** | PowerPoint Agent, Dashboard Agent |
| **Verification by** | Test Agent, PMO Req Agent |

**Scope**: Generate multi-tab Excel workbook: summary, initiatives, RAID, metrics.

---

## WP-08: PowerPoint Reporting Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | Data model, metrics, AI summaries, templates |
| **Outputs** | src/outputs/pptx_pack.py, templates/governance_pack.pptx, outputs/samples/governance_pack.pptx |
| **Tasks** | TASK-402 |
| **Dependencies** | Gate 3 |
| **Parallel with** | Excel Agent, Dashboard Agent |
| **Verification by** | Test Agent, PMO Req Agent |

**Scope**: Generate governance pack: title, agenda, portfolio summary, RAID highlights, decisions, next steps.

---

## WP-09: Dashboard Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | Metrics, data model, templates |
| **Outputs** | src/outputs/dashboard.py, src/outputs/one_page_view.py, templates/dashboard/*, outputs/samples/dashboard/ |
| **Tasks** | TASK-400, TASK-403, TASK-404, TASK-405, TASK-406, TASK-407 |
| **Dependencies** | Gate 3 |
| **Parallel with** | Excel Agent, PowerPoint Agent |
| **Verification by** | Test Agent |

**Scope**: Generate one-page view, monthly update, data quality report, demand pipeline, risk/dependency report, HTML dashboard. All static HTML.

---

## WP-10: Documentation Agent

| Field | Value |
|---|---|
| **Model** | Economy (Sonnet) |
| **Inputs** | All outputs, architecture, test results |
| **Outputs** | README.md, docs/INTERVIEW_DEMO_GUIDE.md, docs/PORTFOLIO_WORDING_GUIDE.md, docs/ARCHITECTURE.md, docs/AI_APPROACH.md, docs/SHAREPOINT_GUIDANCE.md |
| **Tasks** | TASK-408, TASK-602, TASK-900, TASK-901, TASK-902, TASK-903 |
| **Dependencies** | Gate 5 (for final docs); can start templates at Gate 3 |
| **Parallel with** | Cross-Ref Agent (at Gate 6) |
| **Verification by** | Adversarial Agent |

**Scope**: All documentation, README, interview guide, CV wording guide, PMO templates.

---

## WP-11: Test Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | All src/ modules, test strategy |
| **Outputs** | tests/*.py, test results, coverage reports |
| **Tasks** | TASK-500 to TASK-511, TASK-800 |
| **Dependencies** | Gate 3 (unit), Gate 4 (integration/output) |
| **Parallel with** | — (tests run after implementation) |
| **Verification by** | Cross-Ref Agent, respective module agents |

**Scope**: Write and execute all unit, integration and output validation tests. Run clean-build test.

---

## WP-12: Cross-Reference Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | All planning files, source code, outputs |
| **Outputs** | TRACEABILITY_AUDIT.md, CROSS_REF_REPORT.md, RECONCILIATION_REPORT.md |
| **Tasks** | TASK-020, TASK-207, TASK-600, TASK-601, TASK-603 |
| **Dependencies** | Gate 5 |
| **Parallel with** | Documentation Agent |
| **Verification by** | Adversarial Agent, Test Agent |

**Scope**: Verify requirements traceability, identifier consistency, output-to-source reconciliation.

---

## WP-13: Security Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | Repository contents |
| **Outputs** | SECRET_SCAN.md, DEPENDENCY_AUDIT.md |
| **Tasks** | TASK-801, TASK-802 |
| **Dependencies** | Gate 7 |
| **Parallel with** | Adversarial Agent |
| **Verification by** | Adversarial Agent |

**Scope**: Scan for secrets/credentials, audit dependencies for paid/proprietary items.

---

## WP-14: Adversarial Audit Agent

| Field | Value |
|---|---|
| **Model** | Economy (Sonnet) |
| **Inputs** | Entire repository |
| **Outputs** | ADVERSARIAL_AUDIT.md |
| **Tasks** | TASK-700, TASK-701, TASK-702 |
| **Dependencies** | Gate 6 |
| **Parallel with** | Security Agent |
| **Verification by** | Orchestrator |

**Scope**: Challenge claims accuracy, check for real-company leakage, verify interview readiness. Hostile reviewer perspective.

---

## WP-15: Final GO/NO-GO Agent

| Field | Value |
|---|---|
| **Model** | Economy (Flash) |
| **Inputs** | All gate results, defect register |
| **Outputs** | GO_NO_GO.md |
| **Tasks** | TASK-999 |
| **Dependencies** | Gate 9 |
| **Parallel with** | None (final) |
| **Verification by** | Orchestrator |

**Scope**: Automated assessment of all gate statuses, critical defect count, final recommendation.

---

## Parallelism Summary

| Phase | Agents Running in Parallel | Max Concurrent |
|---|---|---|
| 1 | Research Agent | 1 |
| 2 | PMO Req + Jira/Data + Data Quality | 3 |
| 3 | AI Reporting + AI Assurance | 2 |
| 4 | Excel + PowerPoint + Dashboard | 3 |
| 5 | Test Agent | 1 |
| 6 | Cross-Ref + Documentation | 2 |
| 7 | Security + Adversarial | 2 |
| 8-9 | Documentation (final) | 1 |
| 10 | GO/NO-GO | 1 |

**Estimated parallel work packages**: 15 agents, maximum 3 concurrent.
