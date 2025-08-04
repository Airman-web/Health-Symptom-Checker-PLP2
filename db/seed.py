# db/seed.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db.database import get_connection

def seed_data():
    conn = get_connection()
    cur = conn.cursor()
    
    # Create tables first if they don't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS symptoms_conditions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            symptom VARCHAR(100) NOT NULL,
            `condition` VARCHAR(100) NOT NULL,
            self_care TEXT
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS clinics (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            city VARCHAR(100) NOT NULL,
            contact VARCHAR(100)
        )
    ''')
    
    conn.commit()
    
    

    symptoms_data = [
        ("fever", "Malaria", "Drink plenty of fluids, rest, and get tested."),
        ("fever", "Typhoid", "Seek medical attention for a blood test."),
        ("headache", "Migraine", "Rest in a dark room, stay hydrated, avoid loud noises."),
        ("headache", "Tension Headache", "Apply a cool pack and reduce screen time."),
        ("nausea", "Food Poisoning", "Avoid solid foods, drink ORS and clear fluids."),
        ("nausea", "Gastritis", "Eat light meals and avoid spicy foods."),
        ("fatigue", "Anemia", "Eat iron-rich foods like spinach and red meat."),
        ("fatigue", "Diabetes", "Get blood sugar tested, maintain balanced diet."),
        ("cough", "Flu", "Take warm fluids, honey, and rest."),
        ("cough", "Bronchitis", "Stay hydrated and consider steam inhalation."),
        ("shortness of breath", "Asthma", "Use your inhaler and seek urgent help if severe."),
        ("shortness of breath", "COVID-19", "Get tested, isolate, and seek medical advice."),
        ("chest pain", "Heart Attack", "Call emergency services immediately."),
        ("chest pain", "Angina", "Rest and avoid physical strain."),
        ("wheezing", "Asthma", "Use prescribed inhaler and avoid allergens."),
        ("wheezing", "Allergic Reaction", "Identify allergens and seek medical attention."),
        ("stomach pain", "Ulcer", "Avoid spicy food, eat small frequent meals."),
        ("stomach pain", "Appendicitis", "Seek immediate medical attention."),
        ("diarrhea", "Cholera", "Drink ORS and seek urgent medical care."),
        ("diarrhea", "Food Poisoning", "Stay hydrated and avoid solid foods."),
        ("vomiting", "Gastroenteritis", "Rehydrate and avoid dairy."),
        ("constipation", "Low Fiber Diet", "Eat more fiber-rich foods and drink water."),
        ("bloating", "Irritable Bowel Syndrome", "Avoid gas-producing foods and caffeine."),
        ("rash", "Allergic Reaction", "Apply soothing lotion and avoid allergens."),
        ("rash", "Chickenpox", "Stay hydrated, rest, and apply calamine lotion."),
        ("itchy skin", "Eczema", "Moisturize frequently and avoid irritants."),
        ("itchy skin", "Fungal Infection", "Keep area dry, use antifungal cream."),
        ("swelling", "Allergic Reaction", "Apply cold compress and take antihistamines."),
        ("swelling", "Injury", "Rest, ice, compress, and elevate (RICE)."),
        ("dizziness", "Low Blood Pressure", "Sit down, drink water, and rest."),
        ("dizziness", "Anemia", "Increase iron intake and consult a doctor."),
        ("confusion", "Stroke", "Call emergency services immediately."),
        ("confusion", "Dehydration", "Drink water and rest."),
        ("memory loss", "Dementia", "Consult a neurologist for proper care."),
        ("joint pain", "Arthritis", "Exercise gently and apply warm compress."),
        ("joint pain", "Gout", "Avoid red meat and alcohol, drink water."),
        ("back pain", "Muscle Strain", "Use a heating pad and take rest."),
        ("back pain", "Herniated Disc", "Avoid lifting heavy items and consult doctor."),
        ("neck pain", "Poor Posture", "Stretch and maintain ergonomic posture."),
        ("frequent urination", "Diabetes", "Check blood sugar levels and see a doctor."),
        ("frequent urination", "Urinary Tract Infection", "Drink water and consult doctor."),
        ("blurred vision", "Diabetes", "Get an eye check-up and blood test."),
        ("blurred vision", "Eye Strain", "Reduce screen time and rest your eyes."),
        ("weight loss", "Hyperthyroidism", "Consult an endocrinologist."),
        ("weight loss", "Diabetes", "Monitor diet and blood sugar levels."),
        ("swollen feet", "Heart Failure", "Seek immediate medical advice."),
        ("swollen feet", "Kidney Disease", "Limit salt intake and see a doctor.")
    ]

    # Insert symptoms_conditions data
    for symptom, condition, self_care in symptoms_data:
        cur.execute("""
            INSERT IGNORE INTO symptoms_conditions (symptom, `condition`, self_care)
            VALUES (%s, %s, %s)
        """, (symptom, condition, self_care))

    # Clinics data (name, city, contact - matching your current table structure)
    clinics_data = [
        ("King Faisal Hospital", "Kigali", "+250788111222"),
        ("Rwanda Military Hospital", "Kigali", "+250788333444"),
        ("CHUK (University Teaching Hospital)", "Kigali", "+250788555666"),
        ("Legacy Clinics", "Kigali", "+250788777888"),
        ("Baho International Hospital", "Kigali", "+250788999000"),
        ("Kigali Adventist Dental Clinic", "Kigali", "+250788112233"),
        ("Kigali City Health Center", "Kigali", "+250788223344"),
        ("Polyclinique La Médicale", "Kigali", "+250788334455"),
        ("Gahanga Health Centre", "Kigali", "+250788445566"),
        ("Kimironko Health Centre", "Kigali", "+250788556677"),
        ("Masaka Hospital", "Kigali", "+250788667788"),
        ("Rwandex Clinic", "Kigali", "+250788778899"),
    ]

    # Insert clinics data
    for name, city, contact in clinics_data:
        cur.execute("""
            INSERT IGNORE INTO clinics (name, city, contact)
            VALUES (%s, %s, %s)
        """, (name, city, contact))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Database seeded successfully with symptoms and Kigali clinics!")

if __name__ == "__main__":
    seed_data()