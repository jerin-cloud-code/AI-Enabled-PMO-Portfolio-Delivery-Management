# TEST STRATEGY — ai-enabled-portfolio-pmo

## Test Principles

1. Every module has unit tests before integration testing
2. No agent verifies its own implementation
3. Deterministic fallback tested first; optional AI tested separately
4. All outputs validated structurally and against source data
5. Clean-build reproduction is the final gate

## Test Categories

| Category | Scope | Tool | Gate |
|---|---|---|---|
| Unit | Individual functions/classes | pytest | Gate 5 |
| Integration | End-to-end pipeline | pytest | Gate 5 |
| Output validation | Excel, PPTX, HTML structure | pytest + openpyxl/python-pptx/beautifulsoup | Gate 5 |
| Data quality | Validation rules against known data | pytest | Gate 5 |
| AI validation | Factual accuracy of generated summaries | pytest | Gate 5 |
| Cross-reference | Identifier consistency | Custom script | Gate 6 |
| Traceability | REQ → evidence chain completeness | Custom script | Gate 6 |
| Adversarial | Claims, leakage, interview readiness | Manual + script | Gate 7 |
| Security | Secrets, dependencies | trufflehog/grep + pip audit | Gate 8 |
| Clean build | Fresh environment reproduction | Shell script | Gate 8 |

## Test File Mapping

| Test File | Tests | Module Under Test | Gate |
|---|---|---|---|
| test_importers.py | TEST-001..005 | src/importers/ | 5 |
| test_validation.py | TEST-010..020 | src/validation/ | 5 |
| test_metrics.py | TEST-021..030 | src/metrics/ | 5 |
| test_raid.py | TEST-031..035 | src/raid/ | 5 |
| test_duplicates.py | TEST-036..040 | src/analysis/ | 5 |
| test_ai_adapter.py | TEST-041..045 | src/ai/ | 5 |
| test_ai_validation.py | TEST-046..050 | src/ai/validation.py + src/review/ | 5 |
| test_pipeline.py | TEST-051..055 | End-to-end pipeline | 5 |
| test_excel_output.py | TEST-056..060 | src/outputs/excel_workbook.py | 5 |
| test_pptx_output.py | TEST-061..065 | src/outputs/pptx_pack.py | 5 |
| test_dashboard.py | TEST-066..070 | src/outputs/dashboard.py | 5 |
| test_data_quality.py | TEST-071..075 | Validation + known-bad records | 5 |
| test_security.py | TEST-076..080 | Secret scan + dependency audit | 8 |

## Coverage Targets

| Module | Target |
|---|---|
| importers | ≥90% line coverage |
| models | ≥95% line coverage |
| validation | ≥90% line coverage |
| metrics | ≥90% line coverage |
| analysis | ≥85% line coverage |
| ai (fallback) | ≥90% line coverage |
| raid | ≥90% line coverage |
| intake | ≥85% line coverage |
| outputs | ≥80% line coverage (structural validation) |

## Test Data Strategy

- **Good data**: Standard synthetic dataset that passes all validation
- **Bad data**: Deliberately flawed records for validation testing
  - Missing required fields
  - Inconsistent dates
  - Stale records (last updated > threshold)
  - Duplicate initiatives (planted)
  - Invalid RAG values
- **AI test data**: Summaries with planted factual errors for validation testing

## Test Execution

```bash
# Unit + integration tests
make test

# With coverage
make test-coverage

# Security scan
make security-scan

# Clean build test
make clean-build-test

# Full verification
make verify-all
```

## Test Naming Convention

```
TEST-001: test_csv_import_valid_data
TEST-002: test_csv_import_missing_fields
...
```

Each test docstring references its TEST-### ID and the REQ-### it validates.
