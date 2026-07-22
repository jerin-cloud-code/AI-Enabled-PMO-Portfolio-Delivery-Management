"""
Unit tests for RAID Tracker (TEST-031..035).
Validates REQ-014, REQ-021.
"""
import os
import unittest
from src.raid.tracker import RAIDTracker

class TestRAID(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.raid_path = os.path.join(self.base_dir, "data", "synthetic", "raid_log.csv")
        self.decisions_path = os.path.join(self.base_dir, "data", "synthetic", "decisions.csv")

    def test_raid_loading(self):
        """TEST-031: Validate RAID log loading."""
        tracker = RAIDTracker()
        tracker.load_raid_log(self.raid_path)
        self.assertGreater(len(tracker.raid_items), 0)
        open_risks = tracker.get_open_risks()
        self.assertGreater(len(open_risks), 0)

    def test_decisions_loading(self):
        """TEST-032: Validate Decisions loading."""
        tracker = RAIDTracker()
        tracker.load_decisions(self.decisions_path)
        self.assertGreater(len(tracker.decisions), 0)

if __name__ == "__main__":
    unittest.main()
