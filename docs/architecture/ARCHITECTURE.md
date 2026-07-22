# Enterprise Portfolio System Architecture

## System Architecture Diagram

```mermaid
graph TD
    A[Jira CSV / JSON Data] -->|Import| B[Importers Layer]
    B --> C[Internal Initiative Models]
    C --> D[Validation Engine]
    C --> E[Metrics Engine]
    C --> F[Duplicate Detector]
    D -->|Exceptions| G[Exception Reporting]
    E -->|Summary Data| H[AI Summariser & Adapter]
    H -->|Draft Narrative| I[Factual Validator]
    I -->|Passed Draft| J[Human Review Workflow]
    J -->|Approved| K[Output Deliverables]
    K --> L[One-Page View HTML]
    K --> M[Excel Workbook]
    K --> N[PowerPoint Pack]
    K --> O[HTML Dashboard]
```

## Architectural Design Decisions
- **Monorepo Structure:** Clean Python monorepo for simple maintainability.
- **File-Based Storage:** Zero database infrastructure; git-versioned synthetic CSV/JSON data.
- **Deterministic Offline Fallback:** Fully functional offline mode requiring no API key.
- **Modular Pipelines:** Decoupled data models, validation engine, metrics calculation, and output generators.
