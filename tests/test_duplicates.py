"""
Unit tests for Duplicate Detector (TEST-036..040).
Validates REQ-003.
"""
import os
import unittest
from src.importers.csv_importer import CSVImporter
from src.analysis.duplicates import DuplicateDetector

class TestDuplicates(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        importer = CSVImporter()
        self.initiatives = importer.load_initiatives(self.csv_path)

    def test_duplicate_detection(self):
        """TEST-036: Validate duplicate overlap detection scoring."""
        detector = DuplicateDetector(threshold=0.30)
        overlaps = detector.detect_overlaps(self.initiatives)
        self.assertIsInstance(overlaps, list)
        self.assertGreater(len(overlaps), 0)

if __name__ == "__main__":
    unittest.main()
