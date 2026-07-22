"""
Output validation tests for Excel Workbook (TEST-056..060).
"""
import os
import unittest
from src.importers.csv_importer import CSVImporter
from src.outputs.excel_workbook import ExcelWorkbookGenerator

class TestExcelOutput(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        self.out_path = os.path.join(self.base_dir, "outputs", "test_workbook.xlsx")
        importer = CSVImporter()
        self.initiatives = importer.load_initiatives(self.csv_path)

    def test_excel_workbook_generation(self):
        """TEST-056: Validate Excel workbook generator creates valid output file."""
        gen = ExcelWorkbookGenerator()
        res = gen.generate_workbook(self.initiatives, [], self.out_path)
        self.assertTrue(os.path.exists(res))

    def tearDown(self):
        if os.path.exists(self.out_path):
            os.remove(self.out_path)
        csv_fallback = self.out_path.replace(".xlsx", ".csv")
        if os.path.exists(csv_fallback):
            os.remove(csv_fallback)

if __name__ == "__main__":
    unittest.main()
