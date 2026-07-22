"""
Lifecycle state definitions for enterprise portfolio management.
"""
from enum import Enum

class LifecycleStage(str, Enum):
    INTAKE = "Intake"
    SHAPING = "Shaping"
    APPROVED = "Approved"
    ACTIVE = "Active"
    CLOSED = "Closed"

class ShapingStage(str, Enum):
    SUBMITTED = "Submitted"
    TRIAGE = "Triage"
    BUSINESS_CASE = "Business_Case"
    GOVERNANCE_GATE = "Governance_Gate"
    COMPLETED = "Completed"

class RAGStatus(str, Enum):
    RED = "RED"
    AMBER = "AMBER"
    GREEN = "GREEN"

class ConfidenceLevel(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
