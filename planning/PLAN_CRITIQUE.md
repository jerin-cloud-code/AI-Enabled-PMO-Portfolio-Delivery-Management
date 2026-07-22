# PLAN CRITIQUE — ai-enabled-portfolio-pmo
## Pass 2: Critical Challenge from 10 Perspectives

---

## 1. Senior PMO Leader

**Strengths:**
- Covers the core PMO cadence: intake → shaping → delivery → governance review
- RAID management and decision tracking are essential and present
- Data-quality focus is a genuine PMO pain point — good inclusion

**Concerns:**
- **Missing: stakeholder mapping and communication plan outputs.** A real PMO produces RACI-style artefacts. Consider adding a simple stakeholder view to the governance pack.
- **Missing: benefits tracking.** Portfolio PMO increasingly asked about benefits realisation. Even a placeholder field in the data model would show awareness.
- **Prioritisation model risks looking academic.** Weighted scoring is fine, but the demo should show how it supports a real investment committee decision, not just a ranked list.
- **Governance pack needs to feel decision-ready**, not just data-complete. Include a "Decisions Required" slide with clear ask/options/recommendation structure.

**Recommendations:**
- Add a `benefits_status` field to the data model (lightweight; shows awareness)
- Ensure governance pack includes a "Decisions Required" slide
- Keep prioritisation simple; show the *output* not the math

---

## 2. Portfolio Data Analyst

**Strengths:**
- Data validation engine with configurable rules is solid
- Staleness detection addresses a real problem
- JSON Schema for structural validation is appropriate

**Concerns:**
- **40 initiatives across 5 portfolios is thin.** 8 per portfolio gives limited variation. Consider 50–60 for more realistic distributions.
- **Historical snapshots (2 months) insufficient for trending.** Need at least 3–4 data points for a meaningful trend line.
- **No data lineage.** When a metric is wrong, can you trace back to which record caused it? Add a simple provenance chain.
- **Validation rule catalogue should include severity levels** (BLOCKER, WARNING, INFO) — not all exceptions are equal.

**Recommendations:**
- Increase to 50 initiatives minimum; 3 monthly snapshots
- Add severity to validation rules (already implied but not explicit)
- Add a "last validated" timestamp to each record

---

## 3. Executive Report Recipient

**Strengths:**
- One-page view is the #1 thing executives want — good that it's prominent
- RAG status is universally understood

**Concerns:**
- **One-page view must genuinely fit on one page.** If HTML renders as multi-page, it fails the test. Use print CSS media queries.
- **Monthly update needs "So what?" narrative**, not just data tables. The AI summary must add interpretive value.
- **Governance pack must be < 10 slides.** 6–8 is optimal. More than that and it won't be read.
- **Where is the escalation/exception path?** Executives want to see what needs their attention, not everything.

**Recommendations:**
- Add print-ready CSS to one-page view
- Cap governance pack at 8 slides
- Include an "Escalations" section in the monthly update
- Add a "requires attention" filter to the dashboard

---

## 4. AI Assurance Reviewer

**Strengths:**
- Factual validation against source data is the right approach
- Human review workflow with audit trail is essential
- Deterministic fallback demonstrates responsible AI design

**Concerns:**
- **Factual validation scope is vague.** What exactly is checked? Numerical claims? Status values? Named entities? Define the validation taxonomy.
- **No confidence scoring on AI outputs.** Even the fallback should indicate whether the summary is "high confidence" (all data present) vs "low confidence" (data gaps).
- **Prompt templates need version control and a changelog.** Demonstrate prompt governance.
- **Missing: AI risk documentation.** Even for a portfolio demo, include a brief "AI Approach" doc covering limitations, risks, and human oversight.

**Recommendations:**
- Define 5–8 specific factual validation checks (status match, count match, date consistency, etc.)
- Add confidence indicator to generated summaries
- docs/AI_APPROACH.md is planned (ART-065) — ensure it covers limitations and risks explicitly
- Add a `version` field to prompt templates

---

## 5. Jira Specialist

**Strengths:**
- CSV and JSON import covers the two common Jira export formats
- Field mapping approach is flexible

**Concerns:**
- **Jira exports are messy.** The importer needs to handle: multi-value fields (comma-separated labels), HTML in description fields, custom field names, missing fields, date format variations.
- **No mention of Jira statuses to lifecycle mapping.** Jira has its own status workflow; the importer needs a configurable mapping from Jira statuses to portfolio lifecycle states.
- **Sprint/version data is missing.** Real Jira exports include sprint assignments and fix versions — even if not primary, showing awareness helps.
- **Jira JSON export is not the same as Jira REST API JSON.** Clarify which format is being simulated.

**Recommendations:**
- Add a `field_mapping.yaml` configuration for Jira field → portfolio field mapping
- Add a status mapping configuration
- Document which Jira export format is simulated (CSV export from filter, not API)
- Handle HTML stripping in descriptions

---

## 6. Recruiter Reviewing the GitHub Project

**Strengths:**
- README-first approach is essential
- Interview demo guide shows preparation
- Honest CV wording guide shows integrity

**Concerns:**
- **The `.planning/` directory is overwhelming.** 17 planning files for a portfolio demo looks like process theatre. Consider whether all should be visible in the default branch.
- **Risk of "all planning, no substance."** If the outputs aren't visually impressive, the planning rigour won't compensate. Prioritise output quality.
- **Too technical for a PMO role.** The README must lead with PMO value, not Python architecture. Technical details should be secondary.
- **Sample outputs must be immediately visible.** Don't make the recruiter clone and run the project. Include screenshots or link to sample HTML.

**Recommendations:**
- Move `.planning/` to a `planning` branch or a docs subdirectory — keep main branch clean
- Add screenshots/GIFs of outputs in README
- Lead README with "What this demonstrates" (PMO language), not "How it works" (tech language)
- Include a live GitHub Pages demo if possible (static HTML dashboard)

---

## 7. Software Quality Engineer

**Strengths:**
- Test strategy is well-structured with clear coverage targets
- Test naming convention with TEST-### IDs enables traceability
- Clean-build reproduction test is essential

**Concerns:**
- **Coverage targets are aspirational without enforcement.** Add `--cov-fail-under` to pytest config.
- **No mutation testing or property-based testing mentioned.** Overkill for a portfolio demo, but at least mention awareness in TEST_STRATEGY.md.
- **Integration test scope is vague.** What specific end-to-end flow is tested? Define the exact sequence.
- **No CI/CD even for local use.** A `Makefile` with `make test` is fine, but consider a simple GitHub Actions workflow for credibility.

**Recommendations:**
- Add `--cov-fail-under=80` to pytest configuration
- Define the integration test as: import → validate → metrics → generate all outputs → verify outputs
- Consider a simple `.github/workflows/test.yml` for automated testing on push
- Keep quality engineering proportional — this is a demo, not a production system

---

## 8. Security Reviewer

**Strengths:**
- Secret scan is planned
- No-credentials-required design is correct
- Dependency audit is appropriate

**Concerns:**
- **`.gitignore` must be created early**, not as an afterthought. It should exclude `.env`, `__pycache__`, `outputs/` (except samples), `.planning/` drafts.
- **AI adapter config could accidentally include API keys.** The `ai_config.yaml` should explicitly NOT contain keys; document that keys go in environment variables only.
- **No mention of dependency pinning for security.** `requirements.txt` with pinned versions prevents supply-chain attacks.
- **Synthetic data generation must not accidentally pull real data.** The generation script should be obviously self-contained.

**Recommendations:**
- Create `.gitignore` as one of the first files
- Add explicit comment in `ai_config.yaml`: "API keys must be in environment variables, never in this file"
- Pin all dependencies in `requirements.txt`
- Ensure synthetic data generator is clearly self-contained with no external data fetching

---

## 9. Hiring Manager Concerned About Exaggerated Claims

**Strengths:**
- PORTFOLIO_WORDING_GUIDE.md explicitly addresses honest positioning
- Adversarial audit checks for exaggerated claims
- Clear separation from professional employment experience

**Concerns:**
- **"Production-quality" in the prompt could leak into README.** This is a demonstration, not a production system. Avoid the term.
- **"AI-enabled PMO" could imply enterprise AI deployment experience.** The README and guide must clearly state this is a portfolio project demonstrating approach and capability.
- **Risk of interviewer asking "Did you deploy this?"** The interview guide must prepare the candidate with an honest, confident answer.
- **"15 specialist agents" sounds impressive but could be questioned.** Be prepared to explain that these are LLM subagents used during development, not deployed software components.

**Recommendations:**
- README: "This is a portfolio project demonstrating..." not "This production system..."
- Interview guide: include a prepared answer for "Was this deployed in production?"
- Avoid technical jargon about agents in user-facing documentation
- Frame as "I built this to demonstrate how AI can support PMO functions"

---

## 10. Candidate Who Must Explain the Project in an Interview

**Strengths:**
- Interview demo guide is a dedicated artefact — excellent preparation
- Modular design means each component can be explained independently
- Honest wording guide prevents overreach

**Concerns:**
- **76 artefacts is too many to know intimately.** The candidate needs a "top 10" walkthrough, not an exhaustive tour.
- **Technical implementation details may dominate over PMO narrative.** The candidate should lead with business value, not code.
- **Duplicate detection via TF-IDF needs a simple explanation.** "It compares initiative descriptions to find similar text" — not a linear algebra lecture.
- **The planning overhead needs a story.** "I used structured planning to ensure every portfolio requirement was traceable" — one sentence, not a 17-file walkthrough.

**Recommendations:**
- Interview guide: define a 5-minute, 15-minute, and 30-minute demo path
- Lead every explanation with the PMO problem, then the solution, then (if asked) the technology
- Prepare one-liner explanations for every technical component
- The "top 5" demo stops: dashboard → governance pack → data quality report → AI summary with review → duplicate detector

---

## Summary of Identified Issues

| # | Issue | Severity | Source Perspective | Addressed In |
|---|---|---|---|---|
| C-01 | Missing benefits tracking field | LOW | PMO Leader | Data model update |
| C-02 | Governance pack needs "Decisions Required" slide | MEDIUM | PMO Leader | PPT template design |
| C-03 | 40 initiatives too thin; need 50+ | LOW | Data Analyst | Synthetic data spec |
| C-04 | Only 2 historical snapshots; need 3–4 | LOW | Data Analyst | Synthetic data spec |
| C-05 | Validation rules need severity levels | MEDIUM | Data Analyst | Validation rules design |
| C-06 | One-page view must have print CSS | MEDIUM | Executive | Dashboard agent scope |
| C-07 | Governance pack must be ≤8 slides | MEDIUM | Executive | PPT template design |
| C-08 | Missing escalation section in monthly update | MEDIUM | Executive | Dashboard agent scope |
| C-09 | AI validation checks need taxonomy | HIGH | AI Assurance | AI validation design |
| C-10 | Need confidence indicator on AI outputs | MEDIUM | AI Assurance | AI adapter design |
| C-11 | Need Jira field mapping configuration | MEDIUM | Jira Specialist | Importer design |
| C-12 | Need Jira status → lifecycle mapping | MEDIUM | Jira Specialist | Importer design |
| C-13 | .planning/ directory overwhelming for recruiters | HIGH | Recruiter | Repo structure revision |
| C-14 | README must lead with PMO value, not tech | HIGH | Recruiter | README design |
| C-15 | Need screenshots/GIFs in README | HIGH | Recruiter | Documentation agent |
| C-16 | Need GitHub Actions CI workflow | LOW | Quality Engineer | Nice-to-have |
| C-17 | .gitignore must be created early | MEDIUM | Security | First implementation task |
| C-18 | AI config must not contain API keys | MEDIUM | Security | Config design |
| C-19 | Avoid "production-quality" language | HIGH | Hiring Manager | README, all docs |
| C-20 | Prepare "Was this deployed?" answer | HIGH | Hiring Manager | Interview guide |
| C-21 | 76 artefacts too many to know intimately | MEDIUM | Candidate | Demo path design |
| C-22 | Need 5/15/30-minute demo paths | HIGH | Candidate | Interview guide |
| C-23 | Makefile less common on Windows | MEDIUM | General | Add PowerShell equivalents |
