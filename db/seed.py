# db/seed.py
from db.database import get_connection, initialize_database

def seed_data():
    initialize_database()  # make sure tables exist first

    data = [
        ("fever", "Malaria", "Drink plenty of fluids and get tested soon"),
        ("cough", "Flu", "Rest, drink warm liquids, and take vitamin C"),
        ("headache", "Dehydration", "Drink water and rest"),
        ("nausea", "Food Poisoning", "Avoid solid foods, stay hydrated"),
    ]

    conn = get_connection()
    cur = conn.cursor()

    # Insert rows, but avoid duplicates if run again
    for symptom, condition, tip in data:
        cur.execute("""
            INSERT INTO symptoms_conditions (symptom, condition, self_care)
            SELECT ?, ?, ?
            WHERE NOT EXISTS (
                SELECT 1 FROM symptoms_conditions
                WHERE symptom = ? AND condition = ?
            )
        """, (symptom, condition, tip, symptom, condition))

    conn.commit()
    conn.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
