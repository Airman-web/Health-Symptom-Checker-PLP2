# modules/matcher.py
from collections import defaultdict
from db.database import get_connection

def find_ranked_conditions(symptoms):
    conn = get_connection()
    cur = conn.cursor()

    scores = defaultdict(int)
    tips = defaultdict(set)

    for s in symptoms:
        cur.execute("""
            SELECT condition, self_care
            FROM symptoms_conditions
            WHERE LOWER(symptom) = ?
        """, (s.strip().lower(),))
        for condition, tip in cur.fetchall():
            scores[condition] += 1
            tips[condition].add(tip)

    conn.close()

    ranked = [
        {"condition": c, "score": sc, "tips": list(tips[c])}
        for c, sc in scores.items()
    ]
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked
