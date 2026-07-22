"""
Shared Pytest Fixtures for AI PMO Test Suite.
"""
import os
import sys
import pytest

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from src.importers.csv_importer import CSVImporter
from src.models.initiative import Initiative

@pytest.fixture
def sample_initiatives():
    data_path = os.path.join(base_dir, "data", "synthetic", "initiatives.csv")
    importer = CSVImporter()
    return importer.load_initiatives(data_path)
