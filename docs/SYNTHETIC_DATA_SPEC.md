# Synthetic Portfolio Dataset Specification — ai-enabled-portfolio-pmo

> **Synthetic Dataset Design Rules & Controlled Anomaly Distribution**

## 1. Portfolio Portfolio Distribution Target (50 Initiatives Total)

| Portfolio Category | Initiative Count | Target Budget (£M) | Strategic Focus |
|---|---|---|---|
| Technology Delivery | 10 | £12.5M | Infrastructure, API platform, Cloud migration |
| Data & Analytics | 10 | £8.0M | Enterprise data mesh, Governance, Analytics |
| AI & Machine Learning | 10 | £9.5M | Predictive models, Automation, NLP |
| Cyber Security | 10 | £11.0M | Zero Trust, IAM, Vulnerability management |
| Fraud Prevention | 10 | £7.0M | Transaction monitoring, Anti-money laundering |

## 2. Status & Lifecycle Distribution

- **Active Delivery:** 28 initiatives (RED: 5, AMBER: 8, GREEN: 15)
- **Shaping / Demand:** 12 initiatives (Submitted: 4, Business Case: 5, Governance Gate: 3)
- **Approved (Mobilising):** 5 initiatives
- **Closed / Completed:** 5 initiatives

## 3. Controlled Anomaly & Data Quality Exceptions

To realistically test the data validation engine, the synthetic dataset intentionally incorporates 10 controlled defects:
1. `DEFECT-01`: Missing Business Owner (`INIT-012`).
2. `DEFECT-02`: Inconsistent dates (`start_date > target_end_date` on `INIT-019`).
3. `DEFECT-03`: Stale update (`last_update_date` > 45 days old on `INIT-024`).
4. `DEFECT-04`: Closed initiative with `progress_pct = 75.0` (`INIT-048`).
5. `DEFECT-05`: Actual spend exceeding budget without approved variance (`INIT-007`).
6. `DEFECT-06`: Orphan dependency reference (`INIT-033` points to non-existent `INIT-999`).
7. `DEFECT-07`: Duplicate proposed initiative title ("Enterprise Customer IAM Platform" in Intake vs Active `INIT-031`).
8. `DEFECT-08`: Overdue milestone with `GREEN` status (`INIT-015`).
9. `DEFECT-09`: Missing benefit estimate on shaping business case (`INIT-042`).
10. `DEFECT-10`: Inconsistent RAG status vs metrics (`INIT-003` has spend variance >25% but marked `GREEN`).

## 4. Monthly Snapshot History (3 Snapshots)

- `2025-01.csv` (January Baseline)
- `2025-02.csv` (February Progress)
- `2025-03.csv` (March Current Period)
