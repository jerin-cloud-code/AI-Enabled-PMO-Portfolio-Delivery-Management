"""
Unit tests for AI Factual Validation (TEST-046..050).
Validates REQ-005, REQ-006.
"""
import unittest
from src.ai.validation import AIFactualValidator

class TestAIValidation(unittest.TestCase):
    def test_factual_validation_pass(self):
        """TEST-046: Validate factual validation passes for accurate summary."""
        validator = AIFactualValidator()
        summary = {
            "text": "Executive Portfolio Summary (2025): Total 50 initiatives with AMBER health status. RED count: 5.",
            "source_data_snapshot": {"total_initiatives": 50, "overall_rag": "AMBER", "red_count": 5}
        }
        res = validator.validate_summary(summary, summary["source_data_snapshot"])
        self.assertTrue(res["is_factually_valid"])

    def test_factual_validation_fail_on_discrepancy(self):
        """TEST-047: Validate factual validation catches planted count discrepancy."""
        validator = AIFactualValidator()
        summary = {
            "text": "Executive Portfolio Summary (2025): Total 999 initiatives with AMBER status.",
            "source_data_snapshot": {"total_initiatives": 50, "overall_rag": "AMBER", "red_count": 5}
        }
        res = validator.validate_summary(summary, summary["source_data_snapshot"])
        self.assertFalse(res["is_factually_valid"])

if __name__ == "__main__":
    unittest.main()
