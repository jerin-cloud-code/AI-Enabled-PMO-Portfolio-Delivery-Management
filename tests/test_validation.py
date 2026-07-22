"""
Unit tests for Validation Engine (TEST-010..020).
Validates REQ-008, REQ-009, REQ-026.
"""
import os
import unittest
from src.importers.csv_importer import CSVImporter
from src.validation.engine import ValidationEngine
from src.models.initiative import Initiative

class TestValidation(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        importer = CSVImporter()
        self.initiatives = importer.load_initiatives(self.csv_path)

    def test_validation_engine_execution(self):
        """TEST-010: Validate data validation engine flags controlled defects."""
        engine = ValidationEngine()
        res = engine.validate_portfolio(self.initiatives)
        self.assertEqual(res["total_initiatives"], 50)
        self.assertGreater(res["total_exceptions"], 0)

    def test_stale_record_detection(self):
        """TEST-011: Validate stale update detection flags INIT-024."""
        engine = ValidationEngine(staleness_threshold_days=30)
        res = engine.validate_portfolio(self.initiatives, reference_date_str="2025-03-22")
        stale_exceptions = [e for e in res["exceptions"] if e.rule_id == "VAL-RULE-006"]
        self.assertTrue(any(e.initiative_id == "INIT-024" for e in stale_exceptions))

    def test_start_after_end_date(self):
        """TEST-012: Validate start date after end date detection (INIT-019)."""
        engine = ValidationEngine()
        res = engine.validate_portfolio(self.initiatives)
        date_exceptions = [e for e in res["exceptions"] if e.rule_id == "VAL-RULE-005"]
        self.assertTrue(any(e.initiative_id == "INIT-019" for e in date_exceptions))

if __name__ == "__main__":
    unittest.main()
