# RISK REGISTER — ai-enabled-portfolio-pmo

| RISK-ID | Risk | Likelihood | Impact | Severity | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| RISK-001 | Scope creep — too many features for a portfolio demo | HIGH | HIGH | CRITICAL | Prefer smaller working system; defer non-essential features; cut list in critique pass | Orchestrator | OPEN |
| RISK-002 | scikit-learn dependency adds weight for simple duplicate detection | MEDIUM | LOW | LOW | Consider simpler TF-IDF with stdlib; fallback to basic string matching | Jira/Data Agent | OPEN |
| RISK-003 | python-pptx/openpyxl produce visually poor outputs | MEDIUM | MEDIUM | MEDIUM | Use templates with pre-set styling; invest in template design | Excel/PPT Agents | OPEN |
| RISK-004 | AI fallback summaries look obviously templated | MEDIUM | MEDIUM | MEDIUM | Invest in quality Jinja2 templates with conditional logic; variety | AI Reporting Agent | OPEN |
| RISK-005 | Excessive planning files create maintenance burden | MEDIUM | MEDIUM | MEDIUM | Keep planning concise; use tables over narrative; single source of truth per concept | Orchestrator | OPEN |
| RISK-006 | Recruiter perceives project as over-engineered for a PMO role | MEDIUM | HIGH | HIGH | README emphasises PMO outcomes, not engineering; interview guide focuses on business value | Documentation Agent | OPEN |
| RISK-007 | Synthetic data lacks realism; demo unconvincing | MEDIUM | HIGH | HIGH | Model data on real portfolio patterns; include edge cases; use realistic naming | Jira/Data Agent | OPEN |
| RISK-008 | Token budget exhaustion during implementation | MEDIUM | HIGH | HIGH | Economy models for implementation; strict scope; parallelise independent work | Orchestrator | OPEN |
| RISK-009 | Cross-reference identifiers become inconsistent | MEDIUM | MEDIUM | MEDIUM | Automated cross-ref check script; identifier registry as single source | Cross-Ref Agent | OPEN |
| RISK-010 | Interview candidate cannot explain technical components | LOW | HIGH | MEDIUM | Interview demo guide with plain-English explanations; talking points per module | Documentation Agent | OPEN |
| RISK-011 | Real company data accidentally included | LOW | CRITICAL | HIGH | Adversarial audit; automated name/company scan; synthetic data clearly labelled | Security Agent | OPEN |
| RISK-012 | Secrets or API keys accidentally committed | LOW | CRITICAL | HIGH | .gitignore; pre-commit hook guidance; secret scan at Gate 8 | Security Agent | OPEN |
| RISK-013 | Project claims imply real deployment | LOW | HIGH | MEDIUM | README disclaimer; PORTFOLIO_WORDING_GUIDE.md; adversarial review | Adversarial Agent | OPEN |
| RISK-014 | Dashboard looks amateurish | MEDIUM | MEDIUM | MEDIUM | Use modern CSS; clean typography; pre-generated sample with styling | Dashboard Agent | OPEN |
| RISK-015 | Implementation agents produce inconsistent code style | MEDIUM | LOW | LOW | Ruff linter config; consistent patterns in blueprint; code review by Test Agent | Test Agent | OPEN |
| RISK-016 | Interruption causes loss of state | LOW | HIGH | MEDIUM | Git commits at each gate; PROJECT_STATE.json; checklist is authoritative | Orchestrator | OPEN |
| RISK-017 | Traceability overhead slows implementation | MEDIUM | MEDIUM | MEDIUM | Automate traceability checks; don't require manual updates for each file | Cross-Ref Agent | OPEN |
