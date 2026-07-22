#!/usr/bin/env python3
"""
Synthetic Data Generator for Enterprise Portfolio PMO Demonstration.
Generates 50 initiatives across 5 portfolios with realistic distributions and 10 controlled defects.
"""
import os
import json
import csv
from datetime import datetime, timedelta

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data", "synthetic")
    os.makedirs(data_dir, exist_ok=True)
    snapshots_dir = os.path.join(data_dir, "historical_snapshots")
    os.makedirs(snapshots_dir, exist_ok=True)

    # 1. Portfolios Definition
    portfolios = [
        {"portfolio_id": "PORT-TECH", "name": "Technology Delivery", "category": "Technology", "executive_sponsor": "Chief Information Officer", "lead_pmo_analyst": "Alex Mercer"},
        {"portfolio_id": "PORT-DATA", "name": "Data & Analytics", "category": "Data", "executive_sponsor": "Chief Data Officer", "lead_pmo_analyst": "Jordan Vance"},
        {"portfolio_id": "PORT-AI", "name": "AI & Machine Learning", "category": "AI", "executive_sponsor": "Head of AI Innovation", "lead_pmo_analyst": "Taylor Reed"},
        {"portfolio_id": "PORT-CYBER", "name": "Cyber Security", "category": "Cyber Security", "executive_sponsor": "Chief Information Security Officer", "lead_pmo_analyst": "Morgan Ellis"},
        {"portfolio_id": "PORT-FRAUD", "name": "Fraud Prevention", "category": "Fraud Prevention", "executive_sponsor": "Head of Financial Crime Risk", "lead_pmo_analyst": "Sam Chen"},
    ]

    with open(os.path.join(data_dir, "portfolios.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(portfolios[0].keys()))
        writer.writeheader()
        writer.writerows(portfolios)

    # 2. 50 Synthetic Initiatives Generator
    categories = ["Technology", "Data", "AI", "Cyber Security", "Fraud Prevention"]
    initiatives = []

    for i in range(1, 51):
        init_id = f"INIT-{i:03d}"
        cat = categories[(i - 1) % 5]
        
        # Determine stage and status distributions
        if i in [1, 6, 11, 16, 21]:
            # RED Status initiatives
            stage = "Active"
            rag = "RED"
            confidence = "LOW"
            risk_exp = "HIGH"
            progress = 35.0 + (i % 15)
            budget = 1200000.0 + i * 50000
            actual = budget * 1.28  # Budget overrun
            forecast = budget * 1.35
            decision_req = True
        elif i in [2, 7, 12, 17, 22, 26, 31, 36]:
            # AMBER Status initiatives
            stage = "Active"
            rag = "AMBER"
            confidence = "MEDIUM"
            risk_exp = "MEDIUM"
            progress = 50.0 + (i % 20)
            budget = 800000.0 + i * 40000
            actual = budget * 1.10
            forecast = budget * 1.12
            decision_req = False
        elif i in [46, 47, 48, 49, 50]:
            # Closed / Completed initiatives
            stage = "Closed"
            rag = "GREEN"
            confidence = "HIGH"
            risk_exp = "LOW"
            progress = 100.0
            budget = 500000.0 + i * 20000
            actual = budget * 0.98
            forecast = actual
            decision_req = False
        elif i in [41, 42, 43, 44, 45]:
            # Shaping Stage
            stage = "Shaping"
            rag = "GREEN"
            confidence = "HIGH"
            risk_exp = "MEDIUM"
            progress = 15.0
            budget = 600000.0 + i * 30000
            actual = 45000.0
            forecast = budget
            decision_req = True
        elif i in [37, 38, 39, 40]:
            # Approved Stage
            stage = "Approved"
            rag = "GREEN"
            confidence = "HIGH"
            risk_exp = "LOW"
            progress = 5.0
            budget = 750000.0 + i * 25000
            actual = 15000.0
            forecast = budget
            decision_req = False
        else:
            # Standard Active GREEN initiatives
            stage = "Active"
            rag = "GREEN"
            confidence = "HIGH"
            risk_exp = "LOW"
            progress = 40.0 + (i % 45)
            budget = 900000.0 + i * 35000
            actual = budget * (progress / 100.0) * 0.95
            forecast = budget
            decision_req = False

        start_dt = "2025-01-15"
        end_dt = "2025-11-30"
        last_update = "2025-03-20"
        biz_owner = f"Director of {cat} Operations"
        del_owner = f"Lead Delivery Mgr ({cat})"
        sponsor = f"Exec Sponsor ({cat})"
        benefit = budget * 1.8
        benefit_status = "ON_TRACK" if stage == "Active" else "NOT_DEFINED"
        dep_ids = f"INIT-{(i-1):03d}" if i > 1 else ""

        # Controlled Defects Injection as specified in SYNTHETIC_DATA_SPEC.md
        if i == 12: # DEFECT-01: Missing Business Owner
            biz_owner = ""
        elif i == 19: # DEFECT-02: Start date after end date
            start_dt = "2025-12-01"
            end_dt = "2025-06-30"
        elif i == 24: # DEFECT-03: Stale update (>45 days old)
            last_update = "2025-01-10"
        elif i == 48: # DEFECT-04: Closed initiative with incomplete progress
            progress = 75.0
        elif i == 7: # DEFECT-05: Spend overrun without approved variance
            actual = budget * 1.45
        elif i == 33: # DEFECT-06: Orphan dependency reference
            dep_ids = "INIT-999"
        elif i == 15: # DEFECT-08: Overdue milestone with GREEN RAG
            rag = "GREEN"
        elif i == 42: # DEFECT-09: Missing benefit estimate on shaping business case
            benefit = 0.0
            benefit_status = "NOT_DEFINED"
        elif i == 3: # DEFECT-10: Inconsistent RAG status vs metrics
            actual = budget * 1.30
            rag = "GREEN"

        title_topics = {
            "Technology": ["API Gateway Modernisation", "Cloud Microservices Migration", "Enterprise Service Bus Upgrade", "Core Switch Infrastructure", "Developer Portal Automation"],
            "Data": ["Data Mesh Architecture", "Enterprise Metadata Catalog", "Automated Data Quality Pipeline", "Customer 360 Data Lake", "Real-Time Event Streaming"],
            "AI": ["Customer Service NLP Bot", "Predictive Risk Analytics Engine", "Automated Document Processing", "Fraud Detection ML Pipeline", "Generative AI Code Assistant"],
            "Cyber Security": ["Zero Trust IAM Implementation", "SOC Automation & SOAR", "Cloud Workload Security", "Vulnerability Management System", "Endpoint Detection Upgrade"],
            "Fraud Prevention": ["Real-Time Payment Monitoring", "Identity Verification Engine", "Anti-Money Laundering Suite", "Account Takeover Prevention", "Card Fraud Scoring Model"]
        }
        topic = title_topics[cat][(i - 1) % 5]
        title = f"{cat} - {topic} Phase {(i % 3) + 1}"

        item = {
            "initiative_id": init_id,
            "title": title,
            "description": f"Deliver strategic capabilities for {topic.lower()} to enhance operational resilience and control.",
            "portfolio_category": cat,
            "initiative_type": "Project" if i % 2 == 0 else "Programme",
            "strategic_objective": f"Scale {cat} Enterprise Capabilities",
            "business_owner": biz_owner,
            "delivery_owner": del_owner,
            "sponsor": sponsor,
            "lifecycle_stage": stage,
            "shaping_stage": "Governance_Gate" if stage == "Shaping" else "Completed",
            "priority": "High" if rag in ["RED", "AMBER"] else "Medium",
            "rag_status": rag,
            "confidence_level": confidence,
            "start_date": start_dt,
            "target_end_date": end_dt,
            "last_update_date": last_update,
            "progress_pct": round(progress, 1),
            "budget": round(budget, 2),
            "actual_cost": round(actual, 2),
            "forecast_cost": round(forecast, 2),
            "expected_benefit": round(benefit, 2),
            "benefits_status": benefit_status,
            "benefits_description": f"Expected efficiency gains and risk reduction from {topic}.",
            "risk_exposure": risk_exp,
            "dependency_ids": dep_ids,
            "decision_required": decision_req,
            "next_milestone": "Stage Gate Approval" if stage == "Shaping" else "Production Deployment",
            "next_milestone_date": "2025-02-15" if i == 15 else "2025-06-30",
            "data_quality_status": "VALIDATED" if not (i in [3, 7, 12, 15, 19, 24, 33, 42, 48]) else "EXCEPTIONS_FOUND",
            "executive_summary": f"Initiative {init_id} ({title}) is currently {stage} with {rag} status. Key focus is on schedule and delivery milestone execution.",
            "source_system_reference": f"JIRA-EXPORT-20250322-{init_id}"
        }
        initiatives.append(item)

    # Write initiatives.csv
    csv_path = os.path.join(data_dir, "initiatives.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(initiatives[0].keys()))
        writer.writeheader()
        writer.writerows(initiatives)

    # Write initiatives.json
    json_path = os.path.join(data_dir, "initiatives.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(initiatives, f, indent=2)

    # Write Historical Snapshots (Jan, Feb, Mar 2025)
    for month, file_name in [("2025-01-31", "2025-01.csv"), ("2025-02-28", "2025-02.csv"), ("2025-03-22", "2025-03.csv")]:
        snapshot_items = []
        for item in initiatives:
            snap = item.copy()
            snap["last_update_date"] = month
            if file_name == "2025-01.csv":
                snap["progress_pct"] = max(0.0, snap["progress_pct"] - 20.0)
                snap["actual_cost"] = round(snap["actual_cost"] * 0.6, 2)
            elif file_name == "2025-02.csv":
                snap["progress_pct"] = max(0.0, snap["progress_pct"] - 10.0)
                snap["actual_cost"] = round(snap["actual_cost"] * 0.8, 2)
            snapshot_items.append(snap)
        
        with open(os.path.join(snapshots_dir, file_name), "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(snapshot_items[0].keys()))
            writer.writeheader()
            writer.writerows(snapshot_items)

    # 3. RAID Log Generator
    raid_items = [
        {"raid_id": "RISK-001", "initiative_id": "INIT-001", "item_type": "Risk", "summary": "Key technical resource contention across Technology and Cyber portfolios", "severity_impact": "High", "probability": "High", "status": "Open", "owner": "Delivery Lead Tech", "target_date": "2025-04-15"},
        {"raid_id": "RISK-002", "initiative_id": "INIT-006", "item_type": "Risk", "summary": "Vendor delivery delays on core cloud microservices components", "severity_impact": "High", "probability": "Medium", "status": "Open", "owner": "Vendor Mgr", "target_date": "2025-05-01"},
        {"raid_id": "ISSUE-001", "initiative_id": "INIT-011", "item_type": "Issue", "summary": "Data governance approval block on customer data mesh schema", "severity_impact": "Critical", "probability": "High", "status": "Open", "owner": "Lead Data Architect", "target_date": "2025-04-01"},
        {"raid_id": "ACTION-001", "initiative_id": "INIT-001", "item_type": "Action", "summary": "Conduct architectural review board session for API gateway design", "severity_impact": "Medium", "probability": "Low", "status": "In Progress", "owner": "Solution Architect", "target_date": "2025-03-30"},
        {"raid_id": "DEP-001", "initiative_id": "INIT-016", "item_type": "Dependency", "summary": "Requires IAM Zero Trust baseline from INIT-005 before SOC deployment", "severity_impact": "High", "probability": "High", "status": "Open", "owner": "Cyber PM", "target_date": "2025-05-15"},
    ]
    with open(os.path.join(data_dir, "raid_log.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(raid_items[0].keys()))
        writer.writeheader()
        writer.writerows(raid_items)

    # 4. Decisions Register Generator
    decisions = [
        {"decision_id": "DEC-101", "initiative_id": "INIT-001", "ask": "Approve additional £250k budget variance for cloud API platform acceleration", "options_considered": "Option A: Extend timeline by 3 months; Option B: Inject £250k contractor capacity (Recommended)", "recommendation": "Option B", "decision_owner": "Portfolio Investment Committee", "status": "PENDING_APPROVAL", "decision_date": "2025-03-25"},
        {"decision_id": "DEC-102", "initiative_id": "INIT-011", "ask": "Formally endorse revised Data Mesh Domain Architecture", "options_considered": "Option A: Centralised Data Lake; Option B: Federated Data Mesh (Recommended)", "recommendation": "Option B", "decision_owner": "Chief Data Officer", "status": "APPROVED", "decision_date": "2025-02-14"},
    ]
    with open(os.path.join(data_dir, "decisions.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(decisions[0].keys()))
        writer.writeheader()
        writer.writerows(decisions)

    # 5. Intake Register Generator (Front-Door Demand)
    intake = [
        {"intake_id": "INTAKE-001", "proposal_title": "Enterprise Customer IAM Platform", "category": "Cyber Security", "sponsor": "CISO", "estimated_cost": 850000.0, "shaping_status": "Submitted", "submission_date": "2025-03-01", "notes": "Potential duplicate of active INIT-031"},
        {"intake_id": "INTAKE-002", "proposal_title": "Real-Time Transaction Fraud Model v2", "category": "Fraud Prevention", "sponsor": "Head of Fraud", "estimated_cost": 500000.0, "shaping_status": "Triage", "submission_date": "2025-03-10", "notes": "High priority fraud control initiative"},
    ]
    with open(os.path.join(data_dir, "intake_register.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(intake[0].keys()))
        writer.writeheader()
        writer.writerows(intake)

    print("Synthetic dataset successfully generated!")

if __name__ == "__main__":
    main()
