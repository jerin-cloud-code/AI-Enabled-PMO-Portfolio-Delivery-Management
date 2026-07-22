# REPOSITORY BLUEPRINT — ai-enabled-portfolio-pmo

## Repository Structure

```
ai-enabled-portfolio-pmo/
│
├── README.md                          # ART-001: Project overview, setup, usage
├── LICENSE                            # ART-002: MIT or Apache 2.0
├── pyproject.toml                     # ART-003: Project metadata, dependencies
├── requirements.txt                   # ART-004: Pinned dependencies
├── Makefile                           # ART-005: Build, test, generate commands
│
├── .planning/                         # Planning and control (not shipped)
│   ├── MASTER_CHECKLIST.md
│   ├── (all planning files)
│   └── ...
│
├── config/
│   ├── settings.yaml                  # ART-006: Portfolio names, thresholds, paths
│   ├── validation_rules.yaml          # ART-007: Data validation rule definitions
│   ├── rag_thresholds.yaml            # ART-008: RAG status calculation rules
│   └── ai_config.yaml                 # ART-009: AI adapter config (model, fallback)
│
├── data/
│   ├── synthetic/
│   │   ├── README.md                  # ART-010: Synthetic data disclaimer
│   │   ├── portfolios.csv             # ART-011: Portfolio definitions
│   │   ├── initiatives.csv            # ART-012: 40+ synthetic initiatives
│   │   ├── initiatives.json           # ART-013: JSON equivalent (Jira-style)
│   │   ├── raid_log.csv               # ART-014: Risks, actions, issues, deps
│   │   ├── decisions.csv              # ART-015: Decision register
│   │   ├── intake_register.csv        # ART-016: Demand pipeline
│   │   └── historical_snapshots/      # ART-017: Prior-month data for trending
│   │       ├── 2025-01.csv
│   │       └── 2025-02.csv
│   └── schemas/
│       ├── initiative_schema.json     # ART-018: JSON Schema for validation
│       └── raid_schema.json           # ART-019: RAID JSON Schema
│
├── src/
│   ├── __init__.py
│   │
│   ├── importers/
│   │   ├── __init__.py
│   │   ├── csv_importer.py            # ART-020: CSV import with field mapping
│   │   └── json_importer.py           # ART-021: JSON import (Jira export format)
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── initiative.py              # ART-022: Initiative data model
│   │   ├── portfolio.py               # ART-023: Portfolio container model
│   │   ├── raid.py                    # ART-024: RAID item models
│   │   └── lifecycle.py               # ART-025: Initiative lifecycle states
│   │
│   ├── validation/
│   │   ├── __init__.py
│   │   ├── engine.py                  # ART-026: Validation rule engine
│   │   ├── rules.py                   # ART-027: Validation rule implementations
│   │   ├── staleness.py               # ART-028: Stale-update detection
│   │   └── exceptions.py             # ART-029: Data-quality exception model
│   │
│   ├── metrics/
│   │   ├── __init__.py
│   │   ├── engine.py                  # ART-030: Metrics calculation engine
│   │   ├── rag.py                     # ART-031: RAG status calculator
│   │   ├── health.py                  # ART-032: Portfolio health scoring
│   │   └── demand.py                  # ART-033: Demand pipeline metrics
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── duplicates.py              # ART-034: Duplicate/overlap detector
│   │   └── prioritisation.py          # ART-035: Weighted scoring prioritisation
│   │
│   ├── intake/
│   │   ├── __init__.py
│   │   └── pipeline.py               # ART-036: Intake → Shaping → Approval
│   │
│   ├── raid/
│   │   ├── __init__.py
│   │   └── tracker.py                # ART-037: RAID CRUD and dependency graph
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── adapter.py                 # ART-038: AI adapter interface
│   │   ├── fallback.py                # ART-039: Deterministic template-based fallback
│   │   ├── summariser.py              # ART-040: Portfolio summary generator
│   │   └── validation.py              # ART-041: AI-output factual validator
│   │
│   ├── review/
│   │   ├── __init__.py
│   │   └── workflow.py                # ART-042: Human review Draft→Review→Approve
│   │
│   └── outputs/
│       ├── __init__.py
│       ├── one_page_view.py           # ART-043: One-page executive view generator
│       ├── excel_workbook.py          # ART-044: Excel portfolio workbook generator
│       ├── pptx_pack.py              # ART-045: PowerPoint governance pack generator
│       ├── monthly_update.py          # ART-046: Monthly update report generator
│       ├── dashboard.py               # ART-047: HTML dashboard generator
│       ├── data_quality_report.py     # ART-048: Data-quality exception report
│       ├── demand_report.py           # ART-049: Demand pipeline report
│       └── risk_dependency_report.py  # ART-050: Risk and dependency report
│
├── templates/
│   ├── governance_pack.pptx           # ART-051: PowerPoint template
│   ├── portfolio_workbook.xlsx        # ART-052: Excel template
│   ├── one_page_view.html             # ART-053: HTML template for one-page view
│   ├── monthly_update.html            # ART-054: Monthly update template
│   ├── dashboard/                     # ART-055: Dashboard template (CSS, JS)
│   │   ├── index.html
│   │   ├── styles.css
│   │   └── dashboard.js
│   └── prompts/
│       ├── portfolio_summary.txt      # ART-056: AI prompt for portfolio summary
│       ├── initiative_summary.txt     # ART-057: AI prompt for initiative summary
│       ├── risk_narrative.txt         # ART-058: AI prompt for risk narrative
│       └── monthly_highlights.txt     # ART-059: AI prompt for monthly highlights
│
├── outputs/                           # Generated outputs (gitignored except samples)
│   ├── .gitkeep
│   └── samples/                       # Pre-generated sample outputs for demo
│       ├── one_page_view.html
│       ├── portfolio_workbook.xlsx
│       ├── governance_pack.pptx
│       ├── monthly_update.html
│       ├── data_quality_report.html
│       └── dashboard/
│           └── index.html
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                    # ART-060: Shared fixtures
│   ├── test_importers.py             # TEST-001..005
│   ├── test_validation.py            # TEST-010..020
│   ├── test_metrics.py               # TEST-021..030
│   ├── test_raid.py                  # TEST-031..035
│   ├── test_duplicates.py            # TEST-036..040
│   ├── test_ai_adapter.py            # TEST-041..045
│   ├── test_ai_validation.py         # TEST-046..050
│   ├── test_pipeline.py              # TEST-051..055
│   ├── test_excel_output.py          # TEST-056..060
│   ├── test_pptx_output.py           # TEST-061..065
│   ├── test_dashboard.py             # TEST-066..070
│   ├── test_data_quality.py          # TEST-071..075
│   └── test_security.py              # TEST-076..080
│
├── docs/
│   ├── DATA_MODEL.md                  # ART-061: Entity-relationship documentation
│   ├── SYNTHETIC_DATA_SPEC.md         # ART-062: Synthetic data generation spec
│   ├── VALIDATION_RULES.md            # ART-063: Data validation rule catalogue
│   ├── IDENTIFIER_SYSTEM.md           # ART-064: Identifier taxonomy
│   ├── AI_APPROACH.md                 # ART-065: AI adapter, fallback, validation
│   ├── GOVERNANCE_GUIDE.md            # ART-066: Governance cadence & pack guide
│   ├── SHAREPOINT_GUIDANCE.md         # ART-067: SharePoint/Teams structure guidance
│   ├── INTERVIEW_DEMO_GUIDE.md        # ART-068: Interview walkthrough script
│   ├── PORTFOLIO_WORDING_GUIDE.md     # ART-069: Honest CV/LinkedIn wording
│   ├── SOURCE_REGISTER.md             # ART-070: Research source register
│   └── ARCHITECTURE.md               # ART-071: Technical architecture overview
│
├── scripts/
│   ├── generate_all.py                # ART-072: Master output generation script
│   ├── validate_data.py               # ART-073: Standalone data validation runner
│   ├── go_no_go.py                    # ART-074: Automated GO/NO-GO checker
│   └── clean_build_test.sh            # ART-075: Clean-build reproduction script
│
└── .gitignore                         # ART-076: Ignore outputs/, .env, __pycache__
```

## Module Descriptions

| Module | Purpose | Key Dependencies |
|---|---|---|
| `importers` | Parse Jira-style CSV/JSON exports into internal models | `models` |
| `models` | Data classes for initiatives, portfolios, RAID items, lifecycle states | — |
| `validation` | Rule engine for data completeness, consistency, staleness | `models`, `config` |
| `metrics` | Calculate RAG status, health scores, demand pipeline metrics | `models` |
| `analysis` | Duplicate/overlap detection (TF-IDF); weighted prioritisation | `models` |
| `intake` | Initiative intake register and shaping lifecycle management | `models` |
| `raid` | RAID item CRUD, dependency graph, decision tracking | `models` |
| `ai` | AI adapter (fallback + optional LLM), summariser, factual validator | `models`, `metrics`, `templates/prompts` |
| `review` | Human review workflow: Draft → Review → Approve/Reject | `ai` |
| `outputs` | Generate all executive-facing deliverables | All upstream modules |

## Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                         DATA SOURCES                            │
│  CSV/JSON (Jira-style) ──► Importers ──► Internal Models        │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DATA PROCESSING                           │
│  Validation Engine ──► Exception Report                         │
│  Staleness Detector ──► Stale Items                             │
│  Metrics Engine ──► RAG, Health, Demand                         │
│  RAID Tracker ──► Risk/Dep/Action/Issue/Decision views          │
│  Intake Pipeline ──► Lifecycle status updates                   │
│  Duplicate Detector ──► Overlap candidates                      │
│  Prioritisation ──► Ranked initiative list                      │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                       AI ASSISTANCE                             │
│  AI Adapter (Fallback / Optional LLM)                           │
│  ├── Portfolio Summary Drafts                                   │
│  ├── Initiative Narratives                                      │
│  └── Risk Narratives                                            │
│  Factual Validator ──► Cross-checks vs source data              │
│  Human Review ──► Draft → Review → Approve/Reject               │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                       OUTPUT GENERATION                          │
│  One-Page Executive View ──► HTML                               │
│  Excel Portfolio Workbook ──► .xlsx                              │
│  PowerPoint Governance Pack ──► .pptx                           │
│  Monthly Update ──► HTML/MD                                     │
│  Data Quality Report ──► HTML/MD                                │
│  Demand Pipeline ──► HTML/MD                                    │
│  Risk & Dependency Report ──► HTML/MD                           │
│  HTML Dashboard ──► Static site                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Technology Stack

| Component | Technology | Rationale |
|---|---|---|
| Language | Python 3.10+ | Ubiquitous; rich ecosystem for data, Excel, PPTX |
| Data handling | pandas, dataclasses | Standard portfolio data manipulation |
| Validation | jsonschema, custom rules | Schema + business rule validation |
| Excel output | openpyxl | .xlsx generation without Excel dependency |
| PowerPoint output | python-pptx | .pptx generation without PowerPoint dependency |
| HTML output | Jinja2 | Template-based HTML rendering |
| Dashboard | Vanilla HTML/CSS/JS | No framework; runs from filesystem |
| Duplicate detection | scikit-learn (TF-IDF) | Offline text similarity; no API needed |
| AI fallback | String templates (Jinja2) | Deterministic offline; no LLM required |
| AI optional | Abstract adapter | User plugs in OpenAI/Anthropic/Gemini if desired |
| Testing | pytest | Standard Python test framework |
| Linting | ruff | Fast Python linter |
| Build | Make + pip/uv | Reproducible builds |

## Design Decisions

| DES-### | Decision | Rationale |
|---|---|---|
| DES-001 | Python monorepo, no microservices | Portfolio tool, not enterprise platform; simplicity |
| DES-002 | pandas for data processing | Standard for tabular data; familiar to PMO analysts |
| DES-003 | Template-based AI fallback | Offline deterministic output; no API key required |
| DES-004 | Abstract AI adapter interface | Supports future LLM integration without code changes |
| DES-005 | Static HTML dashboard | Runs from filesystem; no server; easy to demo |
| DES-006 | YAML configuration | Human-readable; version-controllable thresholds |
| DES-007 | Pre-generated sample outputs in git | Immediate demo without running generation scripts |
| DES-008 | Makefile as task runner | Universal; no npm/node dependency; simple commands |
| DES-009 | Separate `models` layer | Clean separation; importers and outputs share models |
| DES-010 | Human review as state machine | Draft → Review → Approved/Rejected with audit trail |
| DES-011 | Historical snapshots for trending | Month-over-month comparison without database |
| DES-012 | Prompt templates in version control | Reusable; auditable; demonstrates prompt engineering |
| DES-013 | Five synthetic portfolios | Tech, Data, AI, Cyber, Fraud — matches target roles |
| DES-014 | JSON Schema for validation | Standard; can validate both CSV-parsed and JSON data |
| DES-015 | No database requirement | CSV/JSON files; zero infrastructure; git-versioned |
