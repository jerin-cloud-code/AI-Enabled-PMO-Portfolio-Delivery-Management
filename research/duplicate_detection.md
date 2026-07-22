# Duplicate & Overlap Detection Approaches Research

> **Source ID References:** `SRC-011` (Manning et al., Introduction to Information Retrieval - TF-IDF & Cosine Similarity), `SRC-012` (Scikit-Learn Text Feature Extraction Documentation).

## 1. Information Retrieval & Text Similarity in PMO Demand Intake

In large enterprise portfolios, multiple business units frequently submit overlapping initiative proposals (e.g. two separate teams proposing customer portal updates or AI chatbots).

## 2. Technical Approach: TF-IDF + Cosine Similarity

### Offline Deterministic Method:
1. **Preprocessing:** Lowercasing, punctuation removal, stop-word filtering (English standard stop-words + PMO domain stop-words like "project", "initiative", "phase").
2. **Vectorisation:** TF-IDF (Term Frequency - Inverse Document Frequency) vectorizer converts initiative Title + Description into a sparse vector space.
3. **Similarity Calculation:** Cosine similarity measures the angle between pairs of initiative vectors (scale 0.0 to 1.0).
4. **Multi-Factor Scoring:**
   - Text similarity score (TF-IDF cosine similarity)
   - Category match flag (Same portfolio category = +0.1 score boost)
   - Objective overlap flag (Shared strategic objective = +0.1 score boost)

## 3. Human Decision Thresholds

- **Score ≥ 0.75:** `HIGH_OVERLAP` — Flagged for mandatory PMO shaping review.
- **Score 0.50–0.74:** `POTENTIAL_OVERLAP` — Advisory flag in intake pipeline.
- **Score < 0.50:** `DISTINCT` — No overlap detected.

All overlap results are stored with human review status (`UNREVIEWED`, `CONFIRMED_DUPLICATE`, `MERGED`, `DISMISSED`).
