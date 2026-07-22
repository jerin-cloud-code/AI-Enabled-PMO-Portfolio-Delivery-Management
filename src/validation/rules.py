"""
Validation Engine Rules Implementation.
Enforces validation rules defined in VAL-RULE-001 through VAL-RULE-015.
"""
from typing import List
from datetime import datetime
from src.models.initiative import Initiative
from src.validation.exceptions import DataQualityException

def evaluate_initiative_rules(initiatives: List[Initiative], known_ids: set = None) -> List[DataQualityException]:
    exceptions = []
    if known_ids is None:
        known_ids = {i.initiative_id for i in initiatives if i.initiative_id}

    seen_ids = set()
    for init in initiatives:
        # VAL-RULE-001: Missing Required Fields
        if not init.initiative_id or not init.title or not init.portfolio_category:
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-001",
                rule_name="Missing Required Fields",
                severity="BLOCKER",
                initiative_id=init.initiative_id or "UNKNOWN",
                field_name="initiative_id/title/portfolio_category",
                error_message="Required core field is missing or empty",
                owner=init.delivery_owner or "Unassigned"
            ))

        # VAL-RULE-002: Duplicate Initiative ID
        if init.initiative_id:
            if init.initiative_id in seen_ids:
                exceptions.append(DataQualityException(
                    rule_id="VAL-RULE-002",
                    rule_name="Duplicate Initiative ID",
                    severity="BLOCKER",
                    initiative_id=init.initiative_id,
                    field_name="initiative_id",
                    error_message=f"Duplicate initiative ID found: {init.initiative_id}",
                    owner=init.delivery_owner or "Unassigned"
                ))
            seen_ids.add(init.initiative_id)

        # VAL-RULE-003: Invalid Lifecycle State
        if init.lifecycle_stage not in ["Intake", "Shaping", "Approved", "Active", "Closed"]:
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-003",
                rule_name="Invalid Lifecycle State",
                severity="BLOCKER",
                initiative_id=init.initiative_id,
                field_name="lifecycle_stage",
                error_message=f"Invalid stage value: {init.lifecycle_stage}",
                owner=init.delivery_owner or "Unassigned"
            ))

        # VAL-RULE-004: Invalid RAG Status
        if init.rag_status not in ["RED", "AMBER", "GREEN"]:
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-004",
                rule_name="Invalid RAG Status",
                severity="BLOCKER",
                initiative_id=init.initiative_id,
                field_name="rag_status",
                error_message=f"Invalid RAG status: {init.rag_status}",
                owner=init.delivery_owner or "Unassigned"
            ))

        # VAL-RULE-005: Start Date After End Date
        if init.start_date and init.target_end_date:
            try:
                s_dt = datetime.strptime(init.start_date, "%Y-%m-%d")
                e_dt = datetime.strptime(init.target_end_date, "%Y-%m-%d")
                if s_dt > e_dt:
                    exceptions.append(DataQualityException(
                        rule_id="VAL-RULE-005",
                        rule_name="Start Date After End Date",
                        severity="BLOCKER",
                        initiative_id=init.initiative_id,
                        field_name="start_date/target_end_date",
                        error_message=f"Start date ({init.start_date}) is after target end date ({init.target_end_date})",
                        owner=init.delivery_owner or "Unassigned"
                    ))
            except ValueError:
                pass

        # VAL-RULE-007: Missing Business Owner
        if not init.business_owner:
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-007",
                rule_name="Missing Business Owner",
                severity="WARNING",
                initiative_id=init.initiative_id,
                field_name="business_owner",
                error_message="Business owner is not specified",
                owner="Unassigned"
            ))

        # VAL-RULE-008: Missing Sponsor
        if not init.sponsor:
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-008",
                rule_name="Missing Sponsor",
                severity="WARNING",
                initiative_id=init.initiative_id,
                field_name="sponsor",
                error_message="Executive sponsor is not specified",
                owner=init.delivery_owner or "Unassigned"
            ))

        # VAL-RULE-009: Progress Pct Out of Range
        if init.progress_pct < 0.0 or init.progress_pct > 100.0:
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-009",
                rule_name="Progress Percentage Out of Range",
                severity="BLOCKER",
                initiative_id=init.initiative_id,
                field_name="progress_pct",
                error_message=f"Progress percentage out of bounds [0-100]: {init.progress_pct}",
                owner=init.delivery_owner or "Unassigned"
            ))

        # VAL-RULE-010: Incomplete Closed Initiative
        if init.lifecycle_stage == "Closed" and init.progress_pct < 100.0:
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-010",
                rule_name="Incomplete Closed Initiative",
                severity="WARNING",
                initiative_id=init.initiative_id,
                field_name="progress_pct",
                error_message=f"Closed initiative has progress_pct = {init.progress_pct}% (< 100%)",
                owner=init.delivery_owner or "Unassigned"
            ))

        # VAL-RULE-011: Budget Spend Overrun (>15%)
        if init.budget > 0 and init.actual_cost > init.budget * 1.15:
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-011",
                rule_name="Budget Spend Overrun",
                severity="WARNING",
                initiative_id=init.initiative_id,
                field_name="actual_cost",
                error_message=f"Actual cost (£{init.actual_cost:,.2f}) exceeds budget (£{init.budget:,.2f}) by > 15%",
                owner=init.delivery_owner or "Unassigned"
            ))

        # VAL-RULE-012: Missing Benefit Definition
        if init.expected_benefit == 0.0 and init.benefits_status == "NOT_DEFINED":
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-012",
                rule_name="Missing Benefit Definition",
                severity="INFO",
                initiative_id=init.initiative_id,
                field_name="expected_benefit",
                error_message="Expected benefits are not defined",
                owner=init.delivery_owner or "Unassigned"
            ))

        # VAL-RULE-013: Orphan Dependency Reference
        if init.dependency_ids:
            deps = [d.strip() for d in init.dependency_ids.split(",") if d.strip()]
            for dep in deps:
                if dep not in known_ids:
                    exceptions.append(DataQualityException(
                        rule_id="VAL-RULE-013",
                        rule_name="Orphan Dependency Reference",
                        severity="WARNING",
                        initiative_id=init.initiative_id,
                        field_name="dependency_ids",
                        error_message=f"Referenced dependency '{dep}' does not exist",
                        owner=init.delivery_owner or "Unassigned"
                    ))

        # VAL-RULE-015: Status / RAG Inconsistency
        if init.budget > 0 and init.actual_cost > init.budget * 1.25 and init.rag_status != "RED":
            exceptions.append(DataQualityException(
                rule_id="VAL-RULE-015",
                rule_name="Status / RAG Inconsistency",
                severity="WARNING",
                initiative_id=init.initiative_id,
                field_name="rag_status",
                error_message=f"Spend variance is > 25% but RAG status is '{init.rag_status}' (expected RED)",
                owner=init.delivery_owner or "Unassigned"
            ))

    return exceptions
