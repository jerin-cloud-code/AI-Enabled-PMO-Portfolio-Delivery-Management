"""
Duplicate and Overlap Detector.
Uses TF-IDF + Cosine Similarity and multi-factor scoring (offline fallback included).
"""
import re
import math
from typing import List, Dict, Any
from src.models.initiative import Initiative

def tokenize(text: str) -> List[str]:
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    stop_words = {"the", "and", "for", "with", "this", "that", "from", "project", "initiative", "phase", "delivery", "system"}
    return [w for w in words if w not in stop_words]

def compute_jaccard_similarity(text1: str, text2: str) -> float:
    set1 = set(tokenize(text1))
    set2 = set(tokenize(text2))
    if not set1 or not set2:
        return 0.0
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

class DuplicateDetector:
    def __init__(self, threshold: float = 0.50):
        self.threshold = threshold

    def detect_overlaps(self, initiatives: List[Initiative]) -> List[Dict[str, Any]]:
        overlaps = []
        n = len(initiatives)

        # Attempt to use scikit-learn TfidfVectorizer if available
        try:
            from sklearn.feature_extraction.text import TfidfVectorizer
            from sklearn.metrics.pairwise import cosine_similarity
            corpus = [f"{i.title} {i.description}" for i in initiatives]
            vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(corpus)
            sim_matrix = cosine_similarity(tfidf_matrix)

            for i in range(n):
                for j in range(i + 1, n):
                    score = float(sim_matrix[i][j])
                    init1 = initiatives[i]
                    init2 = initiatives[j]

                    if init1.portfolio_category == init2.portfolio_category:
                        score += 0.10
                    score = min(1.0, score)

                    if score >= self.threshold:
                        overlaps.append({
                            "pair": f"{init1.initiative_id} <-> {init2.initiative_id}",
                            "initiative_id_1": init1.initiative_id,
                            "title_1": init1.title,
                            "initiative_id_2": init2.initiative_id,
                            "title_2": init2.title,
                            "similarity_score": round(score, 3),
                            "overlap_level": "HIGH_OVERLAP" if score >= 0.75 else "POTENTIAL_OVERLAP",
                            "recommendation": "Review for shaping consolidation or scope deduplication",
                            "human_review_status": "UNREVIEWED",
                        })
        except ImportError:
            # Deterministic Fallback using Jaccard Similarity + Keyword Overlap
            for i in range(n):
                for j in range(i + 1, n):
                    init1 = initiatives[i]
                    init2 = initiatives[j]
                    text1 = f"{init1.title} {init1.description}"
                    text2 = f"{init2.title} {init2.description}"
                    score = compute_jaccard_similarity(text1, text2)

                    if init1.portfolio_category == init2.portfolio_category:
                        score += 0.15
                    score = min(1.0, score)

                    if score >= self.threshold:
                        overlaps.append({
                            "pair": f"{init1.initiative_id} <-> {init2.initiative_id}",
                            "initiative_id_1": init1.initiative_id,
                            "title_1": init1.title,
                            "initiative_id_2": init2.initiative_id,
                            "title_2": init2.title,
                            "similarity_score": round(score, 3),
                            "overlap_level": "HIGH_OVERLAP" if score >= 0.75 else "POTENTIAL_OVERLAP",
                            "recommendation": "Review for shaping consolidation or scope deduplication",
                            "human_review_status": "UNREVIEWED",
                        })

        return sorted(overlaps, key=lambda x: x["similarity_score"], reverse=True)
