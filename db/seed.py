# db/seed.py
from db.database import get_connection, initialize_database

def seed_data():
    initialize_database()
    conn = get_connection()
    cur = conn.cursor()

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

    clinics_data = [
        # name, doctor, city, district, sector, contact
        ("King Faisal Hospital", "Dr. Niyonsenga Eric", "Kigali", "Gasabo", "Kimihurura", "+250788111222"),
        ("Rwanda Military Hospital", "Dr. Uwizeye Alice", "Kigali", "Kicukiro", "Kagarama", "+250788333444"),
        ("CHUK (University Teaching Hospital)", "Dr. Habimana Jean", "Kigali", "Nyarugenge", "Muhima", "+250788555666"),
        ("Legacy Clinics", "Dr. Mutesi Paula", "Kigali", "Gasabo", "Remera", "+250788777888"),
        ("Baho International Hospital", "Dr. Ndayisenga Bosco", "Kigali", "Kicukiro", "Nyarugunga", "+250788999000"),
        ("Kigali Adventist Dental Clinic", "Dr. Kabanda Celestin", "Kigali", "Nyarugenge", "Kiyovu", "+250788112233"),
        ("Kigali City Health Center", "Dr. Umutoni Ange", "Kigali", "Nyarugenge", "Nyarugenge", "+250788223344"),
        ("Polyclinique La Médicale", "Dr. Kalisa Patrick", "Kigali", "Gasabo", "Kacyiru", "+250788334455"),
        ("Gahanga Health Centre", "Dr. Nyirahabineza Claire", "Kigali", "Kicukiro", "Gahanga", "+250788445566"),
        ("Kimironko Health Centre", "Dr. Rurangwa Didier", "Kigali", "Gasabo", "Kimironko", "+250788556677"),
        ("Masaka Hospital", "Dr. Uwamahoro Deborah", "Kigali", "Kicukiro", "Masaka", "+250788667788"),
        ("Rwandex Clinic", "Dr. Kayitesi Solange", "Kigali", "Nyarugenge", "Rwezamenyo", "+250788778899"),
    ]

    for s, c, t in symptoms_data:
        cur.execute("""
            INSERT OR IGNORE INTO symptoms_conditions (symptom, condition, self_care)
            VALUES (?, ?, ?)
        """, (s, c, t))

    for name, doctor, city, district, sector, contact in clinics_data:
        cur.execute("""
            INSERT OR IGNORE INTO clinics (name, doctor, city, district, sector, contact)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, doctor, city, district, sector, contact))

    conn.commit()
    conn.close()
    print("✅ Database seeded successfully with extended symptoms and Kigali clinics!")

if __name__ == "__main__":
    seed_data()
