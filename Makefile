# Makefile for AI-Enabled Portfolio PMO

.PHONY: help generate data test verify clean

help:
	@echo "Available commands:"
	@echo "  make data      - Generate synthetic dataset"
	@echo "  make generate  - Run full master output generation pipeline"
	@echo "  make test      - Run automated unittest suite"
	@echo "  make verify    - Run end-to-end verification"
	@echo "  make run-all   - Run complete pipeline from scratch"

data:
	python scripts/generate_synthetic_data.py

generate:
	python scripts/generate_all.py

test:
	python -m unittest discover -s tests -p "test_*.py"

run-all:
	python scripts/run_all.py

verify: test generate
