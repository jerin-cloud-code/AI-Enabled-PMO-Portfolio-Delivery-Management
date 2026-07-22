# REVISED MASTER PLAN — ai-enabled-portfolio-pmo
## Pass 3: Architecture Revised After Critical Challenge

---

## 1. Critique Resolution Summary

| Critique | Resolution | Impact |
|---|---|---|
| C-01: Missing benefits tracking | Add `benefits_status` and `benefits_description` fields to initiative model | Data model change |
| C-02: Need "Decisions Required" slide | Add to governance pack template; include ask/options/recommendation structure | PPT template |
| C-03: 40 initiatives too thin | Increase to 50 initiatives across 5 portfolios (10 each) | Synthetic data spec |
| C-04: Only 2 historical snapshots | Increase to 3 monthly snapshots (Jan, Feb, Mar 2025) | Synthetic data spec |
| C-05: Validation rules need severity | Add BLOCKER / WARNING / INFO severity to each validation rule | Validation rules design |
| C-06: One-page view print CSS | Add `@media print` styles to one-page view template | Dashboard agent |
| C-07: Governance pack ≤8 slides | Cap at 8 slides: Title, Portfolio Summary, RAG Overview, Decisions Required, Key Risks, Dependencies, Demand Pipeline, Next Steps | PPT template |
| C-08: Missing escalation section | Add "Escalations & Exceptions" section to monthly update | Dashboard agent |
| C-09: AI validation needs taxonomy | Define 6 validation checks: status_match, count_match, date_consistency, rag_consistency, named_entity_match, completeness_check | AI validation design |
| C-10: Confidence indicator on AI outputs | Add confidence field (HIGH/MEDIUM/LOW) based on data completeness of source records | AI adapter |
| C-11: Jira field mapping config | Add `config/field_mapping.yaml` for Jira → portfolio field mapping | Importer |
| C-12: Jira status → lifecycle mapping | Add `config/status_mapping.yaml` for Jira status → lifecycle state mapping | Importer |
| C-13: .planning/ overwhelming | Move `.planning/` to a `planning` branch after Gate 0; main branch stays clean. Keep `.planning/` in main during development, branch at final polish. | Repo structure |
| C-14: README must lead with PMO value | README structure: What This Demonstrates → Sample Outputs → Quick Start → Architecture → Limitations | README |
| C-15: Screenshots in README | Dashboard agent generates screenshots; Documentation agent embeds in README | Documentation |
| C-16: GitHub Actions CI | Add `.github/workflows/test.yml` — simple pytest run on push. Low effort, high credibility. | Test Agent |
| C-17: .gitignore early | Create `.gitignore` as TASK-001 deliverable alongside git init | Orchestrator |
| C-18: AI config no keys | Add comment header to `ai_config.yaml` prohibiting inline keys; document env var approach | Config |
| C-19: Avoid "production-quality" | Banned phrase. Use "portfolio-quality" or "demonstration-grade". All docs audited. | All docs |
| C-20: "Was this deployed?" answer | Interview guide includes: "This is a portfolio project I built to demonstrate how AI can support PMO functions. It was not deployed in a production environment." | Interview guide |
| C-21: 76 artefacts too many | Artefact count is fine for thoroughness; interview guide provides a "top 5" and "top 10" walkthrough path | Interview guide |
| C-22: 5/15/30-minute demo paths | Interview guide defines three demo paths with talking points for each | Interview guide |
| C-23: Makefile on Windows | Add PowerShell equivalents in README; consider a `run.py` wrapper as alternative | README + scripts |

---

## 2. Revised Repository Structure

Changes from original blueprint:

```diff
  config/
+   field_mapping.yaml          # Jira field → portfolio field mapping
+   status_mapping.yaml         # Jira status → lifecycle state mapping
    settings.yaml
    validation_rules.yaml       # Now with BLOCKER/WARNING/INFO severity
    rag_thresholds.yaml
    ai_config.yaml              # Header: "No API keys in this file"

  data/synthetic/
    initiatives.csv             # Now 50 initiatives (was 40)
    historical_snapshots/
      2025-01.csv
      2025-02.csv
+     2025-03.csv               # Third snapshot for trending

+ .github/
+   workflows/
+     test.yml                  # Simple pytest CI

+ .gitignore                    # Created at project init (was ART-076, now first file)

+ scripts/
+   run.py                      # Cross-platform alternative to Make
```

---

## 3. Revised Data Model Additions

| Field | Entity | Type | Rationale |
|---|---|---|---|
| `benefits_status` | Initiative | Enum: NOT_DEFINED, ON_TRACK, AT_RISK, DELAYED, REALISED | C-01: PMO leader expectation |
| `benefits_description` | Initiative | Text | C-01: Describes expected/realised benefits |
| `last_validated` | Initiative | Date | C-04: Data lineage support |
| `confidence` | AI Summary | Enum: HIGH, MEDIUM, LOW | C-10: Based on source data completeness |

---

## 4. Revised Governance Pack Structure (8 slides)

| Slide | Content |
|---|---|
| 1. Title | Portfolio name, date, "SYNTHETIC DATA — DEMONSTRATION" watermark |
| 2. Portfolio Summary | Initiative count by status, overall RAG, AI-generated narrative |
| 3. RAG Overview | Heatmap or table of all initiatives with RAG status |
| 4. Decisions Required | Ask / Options / Recommendation format per decision |
| 5. Key Risks & Issues | Top 5 risks; top 5 issues; mitigation status |
| 6. Dependencies | Cross-portfolio dependencies; blocked items |
| 7. Demand Pipeline | Intake funnel: received → shaping → approved |
| 8. Next Steps & Actions | Open actions with owners and due dates |

---

## 5. Revised AI Factual Validation Taxonomy

| Check ID | Check | What It Validates |
|---|---|---|
| VAL-01 | status_match | AI summary status matches source record status |
| VAL-02 | count_match | Numerical claims (e.g., "12 initiatives") match source counts |
| VAL-03 | date_consistency | Dates mentioned are consistent with source data |
| VAL-04 | rag_consistency | RAG colours mentioned match calculated RAG |
| VAL-05 | named_entity_match | Initiative/portfolio names in summary exist in source data |
| VAL-06 | completeness_check | Summary covers all portfolios/sections expected |

---

## 6. Revised Validation Rule Severity

| Severity | Meaning | Example |
|---|---|---|
| BLOCKER | Cannot proceed; data is unusable | Missing initiative ID; invalid lifecycle state |
| WARNING | Data quality issue; can proceed with caveat | Missing owner; RAG not set; no description |
| INFO | Advisory; nice to fix | Description under 20 characters; no benefits defined |

---

## 7. Revised Task Additions

| Task ID | Description | Phase | Agent |
|---|---|---|---|
| TASK-022 | Create .gitignore | 0 | Orchestrator |
| TASK-023 | Create config/field_mapping.yaml | 2 | Jira/Data Agent |
| TASK-024 | Create config/status_mapping.yaml | 2 | Jira/Data Agent |
| TASK-025 | Create .github/workflows/test.yml | 5 | Test Agent |
| TASK-026 | Create scripts/run.py (cross-platform runner) | 3 | Jira/Data Agent |
| TASK-027 | Generate README screenshots | 9 | Dashboard Agent |

---

## 8. Revised Interview Demo Paths

### 5-Minute Path (Recruiter/Quick Overview)
1. Open README → show purpose and sample outputs
2. Open HTML dashboard → show portfolio overview
3. Open governance pack (PPTX) → show executive quality
4. Point to AI summary → explain human review

### 15-Minute Path (Hiring Manager)
1. 5-minute path above
2. Show data quality report → explain validation engine
3. Show duplicate detector output → explain approach
4. Show Jira import → field mapping
5. Show RAID tracker → decision tracking
6. Explain honest positioning

### 30-Minute Path (Technical Interview)
1. 15-minute path above
2. Walk through code architecture
3. Show test suite and coverage
4. Explain AI adapter pattern (fallback + optional LLM)
5. Show factual validation tests
6. Walk through one end-to-end pipeline run
7. Discuss design decisions and trade-offs

---

## 9. Revised Scope — Features Removed or Deferred

| Feature | Decision | Rationale |
|---|---|---|
| Complex prioritisation model | SIMPLIFY | Show a weighted-scoring table, not an algorithm. Output matters, not math. |
| GitHub Pages deployment | DEFER | Nice-to-have; adds complexity. Static files in `outputs/samples/` suffice initially. |
| Multiple AI provider adapters | SIMPLIFY | One abstract interface + one optional implementation (e.g., OpenAI-compatible). Not per-provider. |
| SharePoint integration | DOCUMENT ONLY | `docs/SHAREPOINT_GUIDANCE.md` with folder structure guidance. No code. Already planned. |

---

## 10. Revised Execution Phases

### Phase 1: Research (1 agent, ~6 tasks)
Research Agent produces concise summaries. No blocked dependencies.

### Phase 2: Data Model & Requirements (3 agents in parallel, ~10 tasks)
PMO Req Agent + Jira/Data Agent + Data Quality Agent. All depend on Phase 1 outputs.

### Phase 3: Core Implementation (5 agents, ~15 tasks)
Jira/Data Agent (synthetic data + importers), Data Quality Agent (validation), AI Reporting + AI Assurance (AI features), PMO Req Agent (RAID + intake). Partial parallelism.

### Phase 4: Output Generation (3 agents in parallel, ~9 tasks)
Excel + PowerPoint + Dashboard agents. All depend on Phase 3 core modules.

### Phase 5: Testing (1 agent, ~12 tasks)
Test Agent writes and runs all tests. Depends on Phases 3–4.

### Phase 6: Verification (2 agents in parallel, ~4 tasks)
Cross-Ref Agent + Documentation Agent. Depend on Phase 5.

### Phase 7: Audit (2 agents in parallel, ~5 tasks)
Security Agent + Adversarial Agent. Depend on Phase 6.

### Phase 8–9: Final Polish (1 agent, ~4 tasks)
Documentation Agent finalises README, interview guide, screenshots.

### Phase 10: GO/NO-GO (1 agent, 1 task)
Automated assessment.

**Total revised task count: ~72 tasks**
**Maximum concurrent agents: 3**

---

## 11. Principle: Smaller Working System Over Large Incomplete System

The revised plan prioritises:
1. **50 synthetic initiatives that look realistic** over 100 that look generated
2. **8 polished governance slides** over 20 mediocre ones
3. **One working AI fallback** over three half-finished LLM integrations
4. **A clean HTML dashboard** over a complex React SPA
5. **Passing tests** over high coverage percentages
6. **An honest README** over an impressive but misleading one

Every feature that ships must be complete, tested, and explainable. Features that cannot meet this bar are deferred, not shipped incomplete.

---

## 12. Git Workflow

1. `main` branch: clean, demo-ready code and outputs
2. `planning` branch: `.planning/` files moved here after Gate 0
3. Feature branches: one per agent work package during implementation
4. Commits: prefixed with `[TASK-###]` for traceability
5. Gate commits: tagged `gate-N` at each gate pass

---

## 13. Interruption Recovery

1. `PROJECT_STATE.json` records current phase, active gate, last completed task
2. `MASTER_CHECKLIST.md` is the authoritative state — always up to date
3. Git commits at every gate ensure state is persisted
4. Any agent can resume by reading `PROJECT_STATE.json` and `MASTER_CHECKLIST.md`
5. No task depends on in-memory state; all context is in files
