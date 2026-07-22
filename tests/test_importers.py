"""
Unit tests for CSV and JSON Importers (TEST-001..005).
Validates REQ-007, REQ-023.
"""
import os
import unittest
from src.importers.csv_importer import CSVImporter, strip_html
from src.importers.json_importer import JSONImporter

class TestImporters(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        self.json_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.json")

    def test_csv_import_valid_data(self):
        """TEST-001: Validate CSV importer parses 50 synthetic initiatives."""
        importer = CSVImporter()
        initiatives = importer.load_initiatives(self.csv_path)
        self.assertEqual(len(initiatives), 50)
        self.assertEqual(initiatives[0].initiative_id, "INIT-001")

    def test_json_import_valid_data(self):
        """TEST-002: Validate JSON importer parses 50 synthetic initiatives."""
        importer = JSONImporter()
        initiatives = importer.load_initiatives(self.json_path)
        self.assertEqual(len(initiatives), 50)
        self.assertEqual(initiatives[0].initiative_id, "INIT-001")

    def test_html_stripping(self):
        """TEST-003: Validate HTML stripping utility."""
        raw_html = "<p>Deliver <b>cloud microservices</b></p>"
        clean = strip_html(raw_html)
        self.assertEqual(clean, "Deliver cloud microservices")

if __name__ == "__main__":
    unittest.main()
