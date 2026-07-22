#!/usr/bin/env python3
"""
Primary Full-Run Command for AI-Enabled Portfolio PMO.
Executes data generation, validation, output creation, test suite, and GO/NO-GO assessment.
"""
import os
import sys

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    print("==========================================================")
    print("   AI-ENABLED PORTFOLIO PMO - MASTER RUNNER              ")
    print("==========================================================")

    # 1. Generate Synthetic Data
    print("\n[Step 1/4] Generating Synthetic Enterprise Portfolio Data...")
    from scripts.generate_synthetic_data import main as generate_data
    generate_data()

    # 2. Generate Master Deliverables
    print("\n[Step 2/4] Generating Master Executive PMO Deliverables...")
    from scripts.generate_all import main as generate_outputs
    generate_outputs()

    # 3. Run Automated Tests
    print("\n[Step 3/4] Running Automated Test Suite...")
    import unittest
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.join(base_dir, "tests"), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
    if not result.wasSuccessful():
        print("ERROR: Test suite failed!")
        sys.exit(1)

    print("\n[Step 4/4] Final Verification Complete — All Systems GO!")
    print("Outputs available in: outputs/samples/")
    print("==========================================================")

if __name__ == "__main__":
    main()
