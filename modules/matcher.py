symptom_db = {
    "fever": [
        ("Flu", "Rest, stay hydrated, take paracetamol"),
        ("Malaria", "Visit a clinic for a blood test and treatment"),
        ("Common Cold", "Rest and drink warm fluids")
    ],
    "cough": [
        ("Bronchitis", "Avoid smoking, drink lots of water"),
        ("Common Cold", "Use cough syrup and rest"),
        ("COVID-19", "Take a test, isolate, and monitor symptoms")
    ],
    "headache": [
        ("Migraine", "Stay in a dark room and take prescribed meds"),
        ("Tension Headache", "Try relaxation or pain relief meds"),
        ("Dehydration", "Drink water and rest")
    ],
    "rash": [
        ("Allergic Reaction", "Avoid allergen and apply antihistamine cream"),
        ("Measles", "Consult a doctor immediately"),
        ("Heat Rash", "Keep skin cool and dry")
    ],
    "sore throat": [
        ("Strep Throat", "Visit a doctor for antibiotics"),
        ("Flu", "Gargle warm salt water and rest"),
        ("Common Cold", "Use throat lozenges and drink warm fluids")
    ],
    "shortness of breath": [
        ("Asthma", "Use prescribed inhaler and avoid triggers"),
        ("COVID-19", "Seek medical attention if severe"),
        ("Pneumonia", "Get medical treatment immediately")
    ],
    "diarrhea": [
        ("Food Poisoning", "Drink oral rehydration solutions and rest"),
        ("Cholera", "Seek urgent treatment and rehydration"),
        ("Stomach Virus", "Stay hydrated and avoid dairy")
    ],
    "chest pain": [
        ("Heart Attack", "Call emergency services immediately"),
        ("Heartburn", "Avoid spicy food, use antacids"),
        ("Muscle Strain", "Rest and apply heat")
    ]
}
def match_symptoms(symptoms_list):
    
    results = []

    for symptom in symptoms_list:
        symptom = symptom.strip().lower()
        if symptom in symptom_db:
            results.extend(symptom_db[symptom])  

    
    unique_results = list(set(results))

    return unique_results

