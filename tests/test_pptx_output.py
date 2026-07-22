"""
Output validation tests for PowerPoint Pack (TEST-061..065).
"""
import os
import unittest
from src.importers.csv_importer import CSVImporter
from src.outputs.pptx_pack import PowerPointPackGenerator

class TestPPTXOutput(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.csv_path = os.path.join(self.base_dir, "data", "synthetic", "initiatives.csv")
        self.out_path = os.path.join(self.base_dir, "outputs", "test_pack.pptx")
        importer = CSVImporter()
        self.initiatives = importer.load_initiatives(self.csv_path)

    def test_pptx_pack_generation(self):
        """TEST-061: Validate PowerPoint governance pack generator creates valid output file."""
        gen = PowerPointPackGenerator()
        res = gen.generate_pack(self.initiatives, "Test Summary Narrative", self.out_path)
        self.assertTrue(os.path.exists(res))

    def tearDown(self):
        if os.path.exists(self.out_path):
            os.remove(self.out_path)
        txt_fallback = self.out_path + ".txt"
        if os.path.exists(txt_fallback):
            os.remove(txt_fallback)

if __name__ == "__main__":
    unittest.main()
