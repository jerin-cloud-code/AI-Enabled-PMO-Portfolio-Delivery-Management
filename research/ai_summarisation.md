# AI-Assisted Portfolio Summarisation & Assurance Research

> **Source ID References:** `SRC-008` (NIST AI Risk Management Framework - NIST AI 100-1), `SRC-009` (ISO/IEC 42001 AI Management System Standard), `SRC-010` (EU AI Act Trustworthy AI Principles).

## 1. AI Assistance in PMO Governance

AI language models can streamline PMO operations by:
1. Drafting executive narrative summaries from raw Jira issue descriptions and RAID records.
2. Generating risk highlights and trend commentaries.
3. Translating technical progress into business-oriented status notes.

## 2. Risk Mitigation & Factual Assurance Framework

AI outputs must be subjected to rigorous factual validation against ground-truth source data before being presented to executives.

### Factual Validation Taxonomy (6 Core Checks):
1. **VAL-01 (`status_match`):** Verify RAG/lifecycle stage cited in summary matches dataset status.
2. **VAL-02 (`count_match`):** Verify numerical metrics (e.g. "12 active projects") reconcile exactly with portfolio counts.
3. **VAL-03 (`date_consistency`):** Verify milestone dates in narrative match target end dates in underlying data.
4. **VAL-04 (`rag_consistency`):** Verify health color descriptions match calculated quantitative thresholds.
5. **VAL-05 (`named_entity_match`):** Verify initiative titles and owner names exist in the portfolio register.
6. **VAL-06 (`completeness_check`):** Verify all portfolios/sub-domains are represented without omission.

## 3. Human-in-the-Loop Review Workflow

AI content is generated in `DRAFT` state and cannot be published until explicit human review is recorded:
- States: `DRAFT` → `UNDER_REVIEW` → `APPROVED` / `CORRECTION_REQUIRED` / `REJECTED`.
- Complete audit trail capturing timestamp, human reviewer ID, feedback, and version history.

## 4. Deterministic Offline Fallback Pattern

To guarantee zero API dependency for offline/default operation:
- Template-based summarisation engine (Jinja2) populates structured text using exact source metrics.
- Output metadata flags: `generation_mode: OFFLINE_FALLBACK`, `confidence_score: HIGH`.
