# TOKEN & MODEL HANDOFF — ai-enabled-portfolio-pmo

## Model Allocation

| Activity | Model Tier | Rationale |
|---|---|---|
| Requirements interpretation | Expensive (Opus-class) | Ambiguity resolution; design judgment |
| Solution architecture | Expensive | Structural decisions; dependency planning |
| Work breakdown | Expensive | Task granularity; acceptance criteria design |
| Plan criticism | Expensive | Multi-perspective critical analysis |
| Plan revision | Expensive | Synthesising critique into revised architecture |
| Risk analysis | Expensive | Severity assessment; mitigation design |
| Research execution | Economy (Flash) | Factual lookup; summarisation |
| Code implementation | Economy (Flash/Sonnet) | Straightforward coding from specifications |
| Test writing | Economy (Flash) | Mechanical test generation from specs |
| Data generation | Economy (Flash) | Synthetic data from templates |
| Output generation (Excel/PPTX/HTML) | Economy (Flash) | Library-based generation from specs |
| Documentation writing | Economy (Sonnet) | Narrative quality needed; not architecture |
| Cross-reference checking | Economy (Flash) | Mechanical verification |
| Security scanning | Economy (Flash) | Pattern matching; no judgment needed |
| Adversarial audit | Economy (Sonnet) | Needs some critical analysis capability |
| GO/NO-GO assessment | Economy (Flash) | Checklist evaluation |

## Handoff Protocol

### From Expensive → Economy Model

1. **Complete all planning files** before handoff
2. **Commit planning pack** to git
3. **Set APPROVAL_REQUIRED.md** to AWAITING USER APPROVAL
4. **Wait for user approval** before spawning economy agents
5. **Each economy agent receives**:
   - Its specific AGENT_WORK_PACKAGES.md section
   - REPOSITORY_BLUEPRINT.md (for structure context)
   - Relevant sections of REQUIREMENTS_REGISTER.csv
   - Relevant acceptance criteria from ACCEPTANCE_CRITERIA.md
   - DECISION_LOG.md (for design context)
   - Its task list from MASTER_CHECKLIST.md

### Economy Agent Instructions Template

```
You are the [Agent Name] for the ai-enabled-portfolio-pmo project.

YOUR WORK PACKAGE: [Paste WP section]
YOUR TASKS: [Paste task rows]
YOUR ACCEPTANCE CRITERIA: [Paste gate criteria]

RULES:
1. Implement exactly what is specified — do not redesign
2. Follow the repository blueprint for file locations
3. Use the design decisions in DECISION_LOG.md
4. Mark tasks as IN_PROGRESS when starting, IMPLEMENTED when done
5. Do not verify your own work — a separate agent will verify
6. Commit with [TASK-###] prefix messages
7. If blocked, document the blocker and stop
```

## Token Conservation Guidelines

| Guideline | Savings |
|---|---|
| Use tables over prose in planning docs | ~40% reduction |
| Reference existing docs by ID, don't repeat | ~30% reduction |
| Economy model for all implementation | ~70% cost reduction |
| Parallel agents share no context | Reduced per-agent window |
| Strict scope per agent — no exploration | Fewer tokens per task |
| Pre-defined file locations — no discovery needed | Fewer tool calls |

## Estimated Token Budget

| Phase | Estimated Tokens (Economy) | Agent Count |
|---|---|---|
| Research | 30K | 1 |
| Requirements + Data Model | 50K | 3 |
| Core Implementation | 120K | 5 |
| Output Generation | 60K | 3 |
| Testing | 40K | 1 |
| Verification | 30K | 2 |
| Audit | 20K | 2 |
| Final Polish | 30K | 1 |
| GO/NO-GO | 5K | 1 |
| **Total** | **~385K** | **15** |
