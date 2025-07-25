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
    ]

}
def match_symptoms(symptoms_list):
    """
    Accepts a list of symptoms, returns a list of matching (condition, self-care) tuples.
    """
    results = []

    for symptom in symptoms_list:
        symptom = symptom.strip().lower()
        if symptom in symptom_db:
            results.extend(symptom_db[symptom])  # Add all matches

    # Remove duplicates
    unique_results = list(set(results))

    return unique_results

