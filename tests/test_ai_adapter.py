"""
Unit tests for AI Adapter and Deterministic Fallback (TEST-041..045).
Validates REQ-001, REQ-004, REQ-037.
"""
import unittest
from src.ai.fallback import OfflineFallbackAIAdapter
from src.ai.summariser import PortfolioSummariser

class TestAIAdapter(unittest.TestCase):
    def test_offline_fallback_adapter(self):
        """TEST-041: Validate offline deterministic fallback adapter produces expected structure."""
        adapter = OfflineFallbackAIAdapter()
        res = adapter.generate_summary("portfolio_summary", {"total_initiatives": 50, "overall_rag": "AMBER"})
        self.assertEqual(res["generation_mode"], "OFFLINE_FALLBACK")
        self.assertEqual(res["confidence"], "HIGH")
        self.assertIn("Executive Portfolio Summary", res["text"])

    def test_portfolio_summariser(self):
        """TEST-042: Validate PortfolioSummariser execution with fallback."""
        summariser = PortfolioSummariser()
        res = summariser.generate_portfolio_summary({"total_initiatives": 50, "overall_rag": "GREEN"})
        self.assertIn("Executive Portfolio Summary", res["text"])

if __name__ == "__main__":
    unittest.main()
