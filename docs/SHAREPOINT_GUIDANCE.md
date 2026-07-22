# SharePoint & Microsoft Teams Document Repository Guidance

> **Repository Guidance without Requiring a Live Microsoft Tenant**

## Recommended SharePoint Document Library Structure

```
PMO Enterprise Workspace/
│
├── 01_Front_Door_Intake/
│   ├── Submitted_Proposals/
│   └── Shaping_Business_Cases/
│
├── 02_Active_Portfolio_Register/
│   ├── Monthly_Snapshots/
│   └── Change_Requests/
│
├── 03_Governance_Packs/
│   ├── Investment_Committee_Packs/
│   └── Monthly_Executive_Updates/
│
├── 04_Data_Quality_Exceptions/
│   └── Exception_Tracking_Logs/
│
└── 05_Templates_and_Prompts/
    ├── Governance_Templates/
    └── AI_Prompt_Library/
```

## Naming Conventions & Permissions
- **Naming Standard:** `YYYY-MM-DD_[Domain]_[DeliverableName]_v[Major].[Minor]`
- **Read/Write Access:** PMO Analysts (Full Control), Portfolio Leads (Edit), Executive Recipients (Read-Only).
