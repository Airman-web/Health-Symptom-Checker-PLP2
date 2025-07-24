import sqlite3

# 1. Connect to (or create) the database
conn = sqlite3.connect("health.db")

# 2. Create a table if it doesn't exist yet
conn.execute('''
CREATE TABLE IF NOT EXISTS symptoms_conditions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT,
    condition TEXT,
    self_care TEXT
)
''')

# 3. Insert example data into the table
example_data = [
    ("fever", "Malaria", "Drink plenty of fluids and get tested soon"),
    ("cough", "Flu", "Rest, drink warm liquids, and take vitamin C"),
    ("headache", "Dehydration", "Drink water and rest"),
    ("nausea", "Food Poisoning", "Avoid solid foods, stay hydrated"),
]

# 4. Insert data into the table
for symptom, condition, tip in example_data:
    conn.execute("INSERT INTO symptoms_conditions (symptom, condition, self_care) VALUES (?, ?, ?)", (symptom, condition, tip))

# 5. Save (commit) changes
conn.commit()

# 6. Close the connection
conn.close()

print("Database created and data inserted successfully!")

# This script initializes a SQLite database for health symptom checking.
import sqlite3 
 
DB_NAME = "health_symptom_checker.db"

def find_conditions_from_symptom(symptom_list):
    """
    Find conditions based on a list of symptoms.
    
    :param symptom_list: List of symptoms to check
    :return: Dictionary with symptoms as keys and conditions as values
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    conditions_dict = {}
    
    for symptom in symptom_list:
        cursor.execute("SELECT condition FROM symptoms_conditions WHERE symptom = ?", (symptom,))
        conditions = cursor.fetchall()
        
        if conditions:
            conditions_dict[symptom] = [condition[0] for condition in conditions]
        else:
            conditions_dict[symptom] = []
    
    conn.close()
    return conditions_dict