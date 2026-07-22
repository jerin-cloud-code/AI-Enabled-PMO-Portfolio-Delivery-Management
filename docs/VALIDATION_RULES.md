# Data Validation Rule Catalogue — ai-enabled-portfolio-pmo

> **Validation Engine Rule Definitions & Severity Taxonomy**

## Rule Severity Classification

- **BLOCKER:** Fatal data error; record cannot be ingested or processed.
- **WARNING:** Serious data-quality exception requiring PMO follow-up; record is ingested with warning flag.
- **INFO:** Advisory gap; low priority remediation.

## Catalogue of Validation Rules

| Rule ID | Rule Name | Target Field | Severity | Condition & Logic |
|---|---|---|---|---|
| `VAL-RULE-001` | Missing Required Fields | `initiative_id`, `title`, `portfolio_category` | BLOCKER | Field is null, empty string, or whitespace |
| `VAL-RULE-002` | Duplicate Initiative ID | `initiative_id` | BLOCKER | ID appears > 1 time in initiative register |
| `VAL-RULE-003` | Invalid Lifecycle State | `lifecycle_stage` | BLOCKER | Value not in `[Intake, Shaping, Approved, Active, Closed]` |
| `VAL-RULE-004` | Invalid RAG Status | `rag_status` | BLOCKER | Value not in `[RED, AMBER, GREEN]` |
| `VAL-RULE-005` | Start Date After End Date | `start_date`, `target_end_date` | BLOCKER | `start_date > target_end_date` |
| `VAL-RULE-006` | Stale Record Update | `last_update_date` | WARNING | `current_date - last_update_date > 30 days` |
| `VAL-RULE-007` | Missing Business Owner | `business_owner` | WARNING | Field is null or empty string |
| `VAL-RULE-008` | Missing Sponsor | `sponsor` | WARNING | Field is null or empty string |
| `VAL-RULE-009` | Progress Percentage Out of Range | `progress_pct` | BLOCKER | `progress_pct < 0.0` OR `progress_pct > 100.0` |
| `VAL-RULE-010` | Incomplete Closed Initiative | `progress_pct`, `lifecycle_stage` | WARNING | `lifecycle_stage == 'Closed'` AND `progress_pct < 100.0` |
| `VAL-RULE-011` | Budget Spend Overrun | `actual_cost`, `budget` | WARNING | `actual_cost > budget * 1.15` (15% overrun threshold) |
| `VAL-RULE-012` | Missing Benefit Definition | `expected_benefit`, `benefits_status` | INFO | `expected_benefit == 0` AND `benefits_status == 'NOT_DEFINED'` |
| `VAL-RULE-013` | Orphan Dependency Reference | `dependency_ids` | WARNING | Referenced dependency ID does not exist in dataset |
| `VAL-RULE-014` | Overdue Target Milestone | `next_milestone_date`, `rag_status` | WARNING | `next_milestone_date < current_date` AND `rag_status == 'GREEN'` |
| `VAL-RULE-015` | Status / RAG Inconsistency | `rag_status`, `actual_cost`, `budget` | WARNING | `actual_cost > budget * 1.25` AND `rag_status != 'RED'` |
