"""
Security and Secret Scan tests (TEST-076..080).
"""
import os
import re
import unittest

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_no_hardcoded_secrets(self):
        """TEST-076: Scan repository for potential hardcoded API keys or secrets."""
        secret_patterns = [
            r'sk-[a-zA-Z0-9]{32,}',  # OpenAI key pattern
            r'AKIA[0-9A-Z]{16}',      # AWS Key pattern
            r'AIzaSy[a-zA-Z0-9_-]{33}' # Google API key pattern
        ]
        
        found_secrets = []
        for root, _, files in os.walk(self.base_dir):
            if '.git' in root or '.planning' in root:
                continue
            for file in files:
                if file.endswith(('.py', '.yaml', '.yml', '.json', '.md', '.csv')):
                    fpath = os.path.join(root, file)
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        for pat in secret_patterns:
                            if re.search(pat, content):
                                found_secrets.append((fpath, pat))
        
        self.assertEqual(len(found_secrets), 0, f"Potential secrets found: {found_secrets}")

if __name__ == "__main__":
    unittest.main()
