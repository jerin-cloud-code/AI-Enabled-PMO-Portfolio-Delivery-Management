# PROJECT CHARTER — ai-enabled-portfolio-pmo

## Project Title
AI-Enabled Portfolio PMO — GitHub Portfolio Repository

## Document ID
DEC-001 — Project Charter Approval

## Purpose
Demonstrate the practical capabilities expected of an AI-enabled PMO Analyst through a company-neutral, production-quality GitHub repository using only synthetic data.

## Objectives

| ID | Objective |
|---|---|
| OBJ-01 | Demonstrate AI-assisted portfolio reporting and summarisation |
| OBJ-02 | Demonstrate structured portfolio data management |
| OBJ-03 | Demonstrate governance cadence support |
| OBJ-04 | Demonstrate data-quality assurance |
| OBJ-05 | Demonstrate executive-ready output generation (Excel, PowerPoint, HTML) |
| OBJ-06 | Demonstrate RAID and dependency management |
| OBJ-07 | Demonstrate duplicate/overlap detection |
| OBJ-08 | Demonstrate human-in-the-loop AI review workflow |
| OBJ-09 | Provide interview-ready demonstration material |
| OBJ-10 | Reduce manual PMO effort through automation |

## In Scope

- Synthetic enterprise portfolio dataset (5 portfolios, 40+ initiatives)
- Jira-style CSV and JSON import pipeline
- Data validation, staleness detection, exception reporting
- Initiative intake and shaping lifecycle
- Portfolio metrics and RAG status calculation
- RAID and dependency tracking
- Decision and action tracking
- Duplicate/overlap detection (deterministic + optional AI)
- AI-assisted portfolio summary drafting (offline fallback + optional LLM)
- Human review and approval workflow for AI outputs
- AI-output factual validation against source data
- One-page executive portfolio view
- Excel portfolio workbook generation
- PowerPoint governance pack generation
- Monthly portfolio update report
- Lightweight local HTML dashboard
- Reusable PMO templates and prompt templates
- Automated testing suite
- Interview demonstration guide
- Honest CV/LinkedIn portfolio wording guide
- Full requirements traceability

## Out of Scope

| Exclusion | Rationale |
|---|---|
| Live Jira integration | No credentials required; synthetic data only |
| Microsoft 365/SharePoint integration | No tenant required; guidance documentation only |
| Real LLM API dependency | Deterministic fallback required; optional adapter |
| Paid cloud services | Must run locally without cost |
| Real company data | Company-neutral; synthetic only |
| Production deployment | Portfolio demonstration, not operational system |
| Financial portfolio management | PMO project/programme portfolio, not investment |
| Custom CI/CD pipeline | Local build and test only |

## Non-Negotiable Boundaries

1. **Company-neutral** — No real company names, logos, terminology or identifying details
2. **Synthetic data only** — All data clearly labelled as synthetic
3. **No paid services** — Default demo runs free of charge
4. **No credentials required** — No Jira, M365 or LLM API keys for core functionality
5. **Deterministic fallback** — All AI features work offline with template-based fallback
6. **No secrets stored** — Repository contains zero credentials, tokens or keys
7. **Honest positioning** — Clearly distinguished from professional employment experience
8. **Reusable** — Applicable to technology, data, AI, cyber-security and fraud-prevention portfolios

## Target Portfolios

The synthetic dataset will include initiatives from:
- Technology Delivery
- Data & Analytics
- AI & Machine Learning
- Cyber Security
- Fraud Prevention

## Success Criteria

| Criterion | Measure |
|---|---|
| All role requirements evidenced | 100% REQ-### coverage in traceability |
| Clean build from fresh clone | Install → test → generate outputs: all pass |
| No real-company leakage | Adversarial audit passes |
| Executive outputs are decision-ready | PMO review confirms quality |
| AI outputs validated against source | Factual validation tests pass |
| Candidate can explain every component | Interview guide covers all modules |
| No paid runtime dependencies | Dependency audit confirms |
| No stored secrets | Secret scan passes |

## Stakeholders

| Role | Interest |
|---|---|
| Repository Owner (Candidate) | Career portfolio demonstration |
| Hiring Manager | Evidence of PMO + AI capabilities |
| Recruiter | GitHub portfolio quality signal |
| Technical Interviewer | Code quality, testing, architecture |
| PMO Interviewer | Domain knowledge, governance, reporting |

## Constraints

- Planning by expensive model; implementation by economy model + specialist agents
- Token conservation required throughout
- Must be interruptible and resumable at any point
- All planning files committed before implementation begins
