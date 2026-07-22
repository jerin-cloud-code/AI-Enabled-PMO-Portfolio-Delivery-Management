# Anticipated Interview Questions & Defensible Answers

## Question 1: "Was this project deployed in a real enterprise environment?"
**Defensible Answer:**
"No, this is a personal portfolio demonstration project that I built to model enterprise PMO workflows. All data is 100% synthetic. I designed it to showcase how I approach structured portfolio data management, data quality validation, AI assistance with factual controls, and executive reporting."

## Question 2: "How do you ensure AI-generated portfolio summaries don't contain hallucinations?"
**Defensible Answer:**
"I built a 6-part factual validation engine aligned with the NIST AI Risk Management Framework. Every AI narrative draft is cross-checked against underlying ground-truth metrics for status match, initiative counts, date consistency, and RAG alignment before being submitted to a human review workflow."

## Question 3: "How does your duplicate detection engine identify overlapping proposals?"
**Defensible Answer:**
"It processes proposal titles and descriptions using term frequency-inverse document frequency (TF-IDF) vectorization and cosine similarity scoring. It flags initiative pairs exceeding similarity thresholds for PMO shaping review, combined with category and objective matching."

## Question 4: "How do you handle incomplete or poor-quality Jira data?"
**Defensible Answer:**
"The system includes an automated validation engine with 15 business rules categorized by BLOCKER, WARNING, and INFO severity. It identifies missing required fields, stale records (>30 days), budget overruns (>15%), and orphan dependencies, generating an exception report for PMO follow-up."
