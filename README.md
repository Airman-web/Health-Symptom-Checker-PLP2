# Health-Symptom-Checker-PLP2
Health Symptom Checker CLI 
A simple command-line app that helps you check your symptoms and get basic health advice. Just tell it how you're feeling, and it'll suggest what might be wrong and give you some self-care tips!

What Does This App Do?
Think of this as your personal health assistant that:

Analyzes your symptoms - Tell it you have a fever and headache, and it'll suggest possible conditions
Gives self-care advice - Get tips on how to feel better at home
Recommends nearby clinics - Find healthcare facilities in your area
Keeps track of your health - Saves your symptom checks so you can see patterns over time
Works in two languages - English and Kinyarwanda (perfect for Rwanda!)

How It Works
Start the app - Run it from your terminal
Choose your language - English or Kinyarwanda
Tell it who you are - Enter your name and city
Describe your symptoms - Type what's bothering you (like "fever, headache, tired")
Get results - See possible conditions ranked by how well they match your symptoms
Get advice - Read self-care tips and clinic recommendations
Check your history - Review past symptom checks anytime

Quick Start
What You Need
Python 3.7 or newer
Internet connection (for the database)
A computer with a terminal/command prompt

Installation
# 1. Download and navigate to the project folder
cd Health-Symptom-Checker-PLP2

# 2. Set up a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install required packages
pip install colorama pyfiglet mysql-connector-python

# 4. Set up the database
python init_tables.py

# 5. Run the app
python app.py

Example Usage
$ python app.py

WELCOME TO HEALTH SYMPTOM CHECKER CLI APP
Choose your preferred language (en/rw): en
Enter your name: Lisa Ineza
Enter your city: Kigali

========== MAIN MENU ==========
1. Run new health check
2. View previous checks  
3. Exit 
===============================
Choose an option: 1

Enter your symptoms (separated by commas): fever, headache, fatigue

POSSIBLE CONDITIONS:

- Malaria (score: 3)
  • Drink plenty of fluids and rest
  • Get tested for malaria
  • Seek medical attention if symptoms worsen

- Flu (score: 2)
  • Rest and stay hydrated
  • Take warm fluids with honey

Recommended clinic: King Faisal Hospital (Contact: +250788111222)

IMPORTANT: This is just for information - always see a real doctor for proper diagnosis!

Key Features
Bilingual Support
Switch between English and Kinyarwanda
All menus and messages translated

Smart Symptom Matching
Database of 47+ symptoms and their related conditions
Scoring system that ranks conditions by how many symptoms match
Covers common conditions like malaria, flu, headaches, stomach issues, etc.

Local Clinic Directory
12 verified healthcare facilities in Kigali
Automatic recommendations based on your location
Contact information included

 Health History Tracking
Saves every symptom check with timestamp
Review past consultations to spot patterns
Helps you track if symptoms are getting better or worse

User-Friendly Interface
Colorful text for easy reading
Loading animations to show progress
Clear menus and prompts

How the Symptom Matching Works
You enter symptoms: "fever, headache, nausea"
App searches database: Looks for conditions linked to these symptoms
Scoring happens: Each condition gets points for matching symptoms
Malaria matches fever + headache = 2 points
Migraine matches headache = 1 point

Results ranked: Shows conditions with highest scores first
Advice given: Each condition comes with specific self-care tips

Project Structure
Health-Symptom-Checker-PLP2/
├── app.py              # Main app file - run this!
├── init_tables.py      # Sets up database tables
├── view_db.py          # Check what's in the database
├── modules/
│   ├── i18n.py        # Language translations
│   ├── matcher.py     # Symptom matching logic
│   ├── history.py     # Saves and loads your health history
│   └── clinics.py     # Clinic recommendations
└── db/
    ├── database.py    # Database connection
    └── seed.py        # Sample data for testing

Database
The app uses a MySQL database hosted on Aiven cloud with four main tables:

users - Your name and city
symptoms_conditions - What symptoms link to what conditions
history - All your past symptom checks
clinics - Healthcare facilities and their contact info

Important Notes
Medical Disclaimer
This app is NOT a doctor! It's just for information and education. Always:

Consult real healthcare professionals for serious symptoms
Get proper medical tests and diagnosis
Don't rely only on this app for medical decisions
Seek emergency care for severe symptoms

 Privacy
Your data is stored securely in the cloud
Only you can see your health history
No personal medical data is shared

Troubleshooting
App won't start?

Make sure Python 3.7+ is installed: python --version
Check if you're in the right folder
Try reinstalling packages: pip install -r requirements.txt

Database connection failed?

Check your internet connection
Run python init_tables.py to reset database tables

Symptoms not found?

Check spelling (app is case-sensitive)
Use simple terms like "fever" not "high temperature"
Separate multiple symptoms with commas

Contributing
Want to help improve this app? Here are some ways:

Add more symptoms and conditions to the database
Translate to more languages
Add more clinics and hospitals
Improve the user interface
Add more self-care recommendations

Future Improvements
Mobile app version
Integration with real medical databases
Appointment booking with clinics
Medicine interaction checker
Symptom severity tracking
Export health reports


Remember: This tool is meant to help you understand your symptoms better, but it's no substitute for professional medical care. When in doubt, see a doctor!
