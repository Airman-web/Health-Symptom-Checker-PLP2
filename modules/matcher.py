# modules/matcher.py
from db.database import get_connection

def find_ranked_conditions(symptoms_list):
    """
    Find possible conditions based on symptoms and rank them by relevance
    """
    if not symptoms_list:
        return []
    
    conn = get_connection()
    cur = conn.cursor()
    
    # Create placeholders for the IN clause
    placeholders = ', '.join(['%s'] * len(symptoms_list))
    
    query = f"""
        SELECT `condition`, self_care, COUNT(*) as match_count
        FROM symptoms_conditions 
        WHERE LOWER(symptom) IN ({placeholders})
        GROUP BY `condition`, self_care
        ORDER BY match_count DESC, `condition`
    """
    
    try:
        cur.execute(query, symptoms_list)
        results = cur.fetchall()
        
        # Format results for the app
        ranked_conditions = []
        for condition, self_care, count in results:
            # Split self_care tips by periods or semicolons
            tips = [tip.strip() for tip in self_care.split('.') if tip.strip()] if self_care else []
            if not tips and self_care:
                tips = [self_care]
            
            ranked_conditions.append({
                'condition': condition,
                'score': count,
                'tips': tips
            })
        
        cur.close()
        conn.close()
        return ranked_conditions
        
    except Exception as e:
        print(f"Error in matcher: {e}")
        cur.close()
        conn.close()
        return []