"""
Unit tests for Metrics Engine (TEST-021..030).
Validates REQ-020.
"""
import os
import unittest
from src.importers.csv_importer import CSVImporter
from src.metrics.engine import MetricsEngine
from src.metrics.rag import calculate_rag_status
from src.metrics.health import calculate_portfolio_health_score

class TestMetrics(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        importer = CSVImporter()
        self.initiatives = importer.load_initiatives(self.csv_path)

    def test_metrics_calculation(self):
        """TEST-021: Validate portfolio summary metrics calculation."""
        engine = MetricsEngine()
        m = engine.calculate_portfolio_summary(self.initiatives)
        self.assertEqual(m["total_initiatives"], 50)
        self.assertGreater(m["total_budget"], 0)
        self.assertGreater(m["red_count"], 0)

    def test_rag_calculation_thresholds(self):
        """TEST-022: Validate deterministic RAG threshold rules."""
        self.assertEqual(calculate_rag_status(100.0, 102.0, 100.0), "GREEN")
        self.assertEqual(calculate_rag_status(100.0, 110.0, 100.0), "AMBER")
        self.assertEqual(calculate_rag_status(100.0, 125.0, 100.0), "RED")

    def test_health_score(self):
        """TEST-023: Validate composite health score calculation."""
        score = calculate_portfolio_health_score(self.initiatives)
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 100.0)

if __name__ == "__main__":
    unittest.main()
