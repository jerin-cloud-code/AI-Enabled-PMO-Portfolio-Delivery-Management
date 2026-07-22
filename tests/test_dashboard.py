"""
Output validation tests for HTML Dashboard (TEST-066..070).
"""
import os
import shutil
import unittest
from src.importers.csv_importer import CSVImporter
from src.outputs.dashboard import DashboardGenerator

class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        self.out_dir = os.path.join(self.base_dir, "outputs", "test_dash_dir")
        importer = CSVImporter()
        self.initiatives = importer.load_initiatives(self.csv_path)

    def test_dashboard_generation(self):
        """TEST-066: Validate HTML dashboard generator creates index.html and copies CSS."""
        gen = DashboardGenerator()
        res = gen.generate_dashboard(self.initiatives, self.out_dir)
        self.assertTrue(os.path.exists(res))
        self.assertTrue(os.path.exists(os.path.join(self.out_dir, "styles.css")))

    def tearDown(self):
        if os.path.exists(self.out_dir):
            shutil.rmtree(self.out_dir)

if __name__ == "__main__":
    unittest.main()
