"""
Integration Test for End-to-End PMO Pipeline (TEST-051..055).
"""
import os
import unittest
from src.importers.csv_importer import CSVImporter
from src.validation.engine import ValidationEngine
from src.metrics.engine import MetricsEngine
from src.outputs.one_page_view import OnePageViewGenerator

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        self.output_path = os.path.join(self.base_dir, "outputs", "test_one_page.html")

    def test_end_to_end_pipeline(self):
        """TEST-051: Validate full import -> validate -> metrics -> output generation pipeline."""
        importer = CSVImporter()
        initiatives = importer.load_initiatives(self.csv_path)
        self.assertEqual(len(initiatives), 50)

        val_engine = ValidationEngine()
        val_res = val_engine.validate_portfolio(initiatives)
        self.assertGreater(val_res["total_exceptions"], 0)

        metrics_engine = MetricsEngine()
        m = metrics_engine.calculate_portfolio_summary(initiatives)
        self.assertEqual(m["total_initiatives"], 50)

        gen = OnePageViewGenerator()
        out = gen.generate_html(initiatives, "Test Summary Narrative", self.output_path)
        self.assertTrue(os.path.exists(out))

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

if __name__ == "__main__":
    unittest.main()
