# DECISION LOG — ai-enabled-portfolio-pmo

| DEC-ID | Date | Decision | Rationale | Alternatives Considered | Status |
|---|---|---|---|---|---|
| DEC-001 | 2026-07-22 | Python 3.10+ as implementation language | Ubiquitous; rich ecosystem for pandas, openpyxl, python-pptx; familiar to data analysts | Node.js (weaker Excel/PPTX), Java (heavyweight), R (limited PPTX) | APPROVED |
| DEC-002 | 2026-07-22 | No database; CSV/JSON file-based storage | Zero infrastructure; git-versioned; easy to demo; matches Jira export paradigm | SQLite (adds complexity), PostgreSQL (requires server) | APPROVED |
| DEC-003 | 2026-07-22 | Deterministic template fallback for AI features | Must work without API key; predictable output for testing; demonstrates approach without cost | Mock LLM responses (less realistic), skip AI (misses requirement) | APPROVED |
| DEC-004 | 2026-07-22 | Abstract AI adapter with optional LLM plug-in | Future-proof; demonstrates integration design; user configures if desired | Hard-coded OpenAI client (credential dependency), no AI at all | APPROVED |
| DEC-005 | 2026-07-22 | Static HTML dashboard, no server | Opens from filesystem; no npm/node; easy to demo; works offline | React SPA (needs build), Streamlit (needs server), Dash (needs server) | APPROVED |
| DEC-006 | 2026-07-22 | 5 synthetic portfolios: Tech, Data, AI, Cyber, Fraud | Matches target role domains; demonstrates breadth without excessive data | 3 portfolios (too narrow), 10 (excessive) | APPROVED |
| DEC-007 | 2026-07-22 | Pre-generated sample outputs committed to git | Immediate demo without running scripts; shows quality upfront | Generate on clone (slow; dependencies needed first) | APPROVED |
| DEC-008 | 2026-07-22 | Makefile as task runner | Universal on macOS/Linux; simple; no framework dependency | npm scripts (needs node), invoke (Python; less standard), just (requires install) | APPROVED |
| DEC-009 | 2026-07-22 | YAML for configuration | Human-readable; version-controllable; standard for Python projects | JSON (less readable), TOML (less flexible for nested config), .env (too flat) | APPROVED |
| DEC-010 | 2026-07-22 | 15 specialist agents with economy models | Token efficiency; separation of concerns; independent verification | Single agent (context limits), 5 agents (too broad per agent) | APPROVED |
| DEC-011 | 2026-07-22 | Three-pass planning (arch → critique → revise) | Catches gaps before implementation; reduces rework; addresses multiple stakeholder views | Single-pass (misses issues), five-pass (excessive token cost) | APPROVED |
| DEC-012 | 2026-07-22 | Prompt templates in version control | Reusable; auditable; demonstrates prompt engineering skill | Dynamic prompt generation (harder to audit), no templates (misses requirement) | APPROVED |
| DEC-013 | 2026-07-22 | Human review as explicit state machine | Clear audit trail; demonstrates governance; required by role spec | Implicit approval (no trail), email-based (no email system) | APPROVED |
| DEC-014 | 2026-07-22 | Historical snapshots for month-over-month trending | No database needed; simple file comparison; demonstrates temporal analysis | Database with timestamps (infrastructure), single-point-in-time only (misses trending) | APPROVED |
| DEC-015 | 2026-07-22 | TF-IDF for duplicate detection (offline) | No API needed; well-understood; deterministic; scikit-learn widely available | Embedding models (need API), exact matching (too restrictive), fuzzy string (weak for sentences) | APPROVED |
| DEC-016 | 2026-07-22 | Plan revision: added Makefile Windows compatibility note | Makefile less common on Windows; README must document PowerShell equivalents | Switch to invoke (adds dependency) | APPROVED |
