# Identifier Taxonomy & Cross-Reference System — ai-enabled-portfolio-pmo

> **System-Wide Identifier Format & Cross-Reference Taxonomy**

## Identifier Taxonomy (10 Core Identifier Types)

| ID Type | Prefix Format | Pattern Example | Scope / Purpose |
|---|---|---|---|
| Requirement | `REQ-###` | `REQ-001` | Role & system requirements |
| Source | `SRC-###` | `SRC-001` | Research & external standards |
| Design Decision | `DES-###` | `DES-001` | Architectural design decisions |
| Data Attribute | `DATA-###` | `DATA-001` | Field-level data model items |
| Generated Artefact | `ART-###` | `ART-001` | Output deliverables & templates |
| Test Case | `TEST-###` | `TEST-001` | Automated test suite IDs |
| Risk Item | `RISK-###` | `RISK-001` | Project risk register items |
| Defect Record | `DEF-###` | `DEF-001` | Bug & issue tracker records |
| Governance Decision | `DEC-###` | `DEC-001` | Project decisions log |
| Execution Task | `TASK-###` | `TASK-001` | Work breakdown & checklist tasks |

## Identifier Mapping Rules

1. Every `REQ-###` must map to at least one `SRC-###`, one `DES-###`, one code file, one `ART-###`, and one `TEST-###`.
2. All commit messages must reference the `TASK-###` or `GATE-#` being implemented.
3. Every test function docstring must explicitly reference its corresponding `TEST-###` and `REQ-###`.
