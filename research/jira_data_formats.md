# Jira Data Export Formats & Schema Research

> **Source ID References:** `SRC-004` (Atlassian Jira Software CSV Export Documentation), `SRC-005` (Atlassian Jira REST API v3 Issue Export Schema).

## 1. Jira Export Formats Overview

Jira natively supports export via:
1. **CSV Filter Exports:** Flat tabular structure where issues are rows and custom fields are columns.
2. **JSON Export / REST API:** Structured JSON representations containing nested issue fields, fixVersions, labels, components, links, and worklogs.

## 2. Standard vs Custom Fields Schema Mapping

| Jira Export Field | PMO Schema Field | Data Type | Validation Rules |
|---|---|---|---|
| Issue key / ID | `initiative_id` | String | Format: `INIT-###` or `PRJ-###` |
| Summary | `title` | String | Non-empty, length 5-150 |
| Description | `description` | Text | Non-empty, HTML stripped |
| Issue Type | `initiative_type` | Enum | Project, Programme, Epic, Enabler |
| Project / Portfolio | `portfolio_category` | Enum | Tech, Data, AI, Cyber, Fraud |
| Status | `lifecycle_stage` | Enum | Intake, Shaping, Approved, Active, Closed |
| Priority | `priority` | Enum | Critical, High, Medium, Low |
| Custom Field (RAG) | `rag_status` | Enum | RED, AMBER, GREEN |
| Custom Field (Confidence) | `confidence_level` | Enum | HIGH, MEDIUM, LOW |
| Created / Updated Date | `last_update_date` | Date (ISO 8601) | YYYY-MM-DD |
| Assignee / Owner | `delivery_owner` | String | Non-empty text |
| Custom Field (Sponsor) | `sponsor` | String | Non-empty text |
| Custom Field (Budget) | `budget` | Float | Numeric ≥ 0 |
| Issue Links (Outward) | `dependency_ids` | List[String] | Comma-separated initiative IDs |

## 3. Handling Data Import Anomalies

- **Missing required fields:** Flagged with `WARNING` or `BLOCKER` in validation engine.
- **HTML tags in text:** Stripped automatically during ingestion.
- **Date format variations:** Normalised to standard `YYYY-MM-DD` ISO format.
- **Multi-value fields:** Parsed from comma-separated string format.
