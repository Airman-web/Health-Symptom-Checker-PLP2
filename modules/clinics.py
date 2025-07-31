# modules/clinics.py
from db.database import get_connection
import random

def get_clinic_by_city(city):
    """Get a clinic recommendation based on user's city"""
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT name, city, contact
            FROM clinics 
            WHERE LOWER(city) = LOWER(%s)
            LIMIT 1
        """, (city,))
        
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result
        
    except Exception as e:
        print(f"Error getting clinic by city: {e}")
        cur.close()
        conn.close()
        return None

def get_random_clinic():
    """Get a random clinic if no city-specific clinic is found"""
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT name, city, contact
            FROM clinics 
            ORDER BY RAND()
            LIMIT 1
        """)
        
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result
        
    except Exception as e:
        print(f"Error getting random clinic: {e}")
        cur.close()
        conn.close()
        return None

def get_all_clinics():
    """Get all clinics in the database"""
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            SELECT name, city, contact
            FROM clinics 
            ORDER BY city, name
        """)
        
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
        
    except Exception as e:
        print(f"Error getting all clinics: {e}")
        cur.close()
        conn.close()
        return []

