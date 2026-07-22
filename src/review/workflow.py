"""
Human Review Workflow Engine.
Implements state machine: DRAFT -> UNDER_REVIEW -> APPROVED / CORRECTION_REQUIRED / REJECTED.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, List

class ReviewState:
    DRAFT = "DRAFT"
    UNDER_REVIEW = "UNDER_REVIEW"
    APPROVED = "APPROVED"
    CORRECTION_REQUIRED = "CORRECTION_REQUIRED"
    REJECTED = "REJECTED"

@dataclass
class ReviewRecord:
    content_id: str
    content_text: str
    state: str
    reviewer: str
    review_timestamp: str
    feedback: str
    factual_validation_passed: bool

class HumanReviewWorkflow:
    def __init__(self):
        self.records: Dict[str, ReviewRecord] = {}

    def create_draft(self, content_id: str, content_text: str, validation_passed: bool = True) -> ReviewRecord:
        record = ReviewRecord(
            content_id=content_id,
            content_text=content_text,
            state=ReviewState.DRAFT,
            reviewer="AI Generator",
            review_timestamp=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            feedback="",
            factual_validation_passed=validation_passed
        )
        self.records[content_id] = record
        return record

    def submit_for_review(self, content_id: str) -> ReviewRecord:
        record = self.records[content_id]
        if record.state == ReviewState.DRAFT:
            record.state = ReviewState.UNDER_REVIEW
        return record

    def approve(self, content_id: str, reviewer: str, feedback: str = "Approved for publication") -> ReviewRecord:
        record = self.records[content_id]
        record.state = ReviewState.APPROVED
        record.reviewer = reviewer
        record.feedback = feedback
        record.review_timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return record

    def reject(self, content_id: str, reviewer: str, feedback: str) -> ReviewRecord:
        record = self.records[content_id]
        record.state = ReviewState.REJECTED
        record.reviewer = reviewer
        record.feedback = feedback
        record.review_timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        return record
