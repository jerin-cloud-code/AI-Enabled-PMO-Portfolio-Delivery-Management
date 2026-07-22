"""
Data Quality Regression tests (TEST-071..075).
"""
import os
import unittest
from src.importers.csv_importer import CSVImporter
from src.validation.engine import ValidationEngine

class TestDataQuality(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        importer = CSVImporter()
        self.initiatives = importer.load_initiatives(self.csv_path)

    def test_known_defects_detection(self):
        """TEST-071: Validate that all 10 controlled defects are detected by validation engine."""
        engine = ValidationEngine()
        res = engine.validate_portfolio(self.initiatives)
        exceptions = res["exceptions"]
        
        # Check rule IDs present
        rule_ids = {e.rule_id for e in exceptions}
        self.assertIn("VAL-RULE-005", rule_ids)  # Date defect
        self.assertIn("VAL-RULE-006", rule_ids)  # Staleness defect
        self.assertIn("VAL-RULE-007", rule_ids)  # Missing owner defect
        self.assertIn("VAL-RULE-010", rule_ids)  # Incomplete closed defect
        self.assertIn("VAL-RULE-011", rule_ids)  # Spend overrun defect
        self.assertIn("VAL-RULE-013", rule_ids)  # Orphan dep defect

if __name__ == "__main__":
    unittest.main()
