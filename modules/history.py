import json
from datetime import datetime
import os

HISTORY_FILE = "history.json"

def save_to_history(symptoms, matched_conditions):
    """Save a symptom check to history with timestamp."""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "symptoms": symptoms,
        "matched_conditions": matched_conditions
    }

    history = load_history()
    history.append(entry)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def load_history():
    """Load history from the file."""
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def show_history():
    """Display the history in a readable format."""
    history = load_history()
    if not history:
        print("No history found.")
        return

    print("\n=== Symptom Check History ===\n")
    for i, entry in enumerate(history, 1):
        print(f"Check #{i}")
        print(f"Time: {entry['timestamp']}")
        print(f"Symptoms: {', '.join(entry['symptoms'])}")
        print(f"Possible Conditions: {', '.join(entry['matched_conditions']) if entry['matched_conditions'] else 'None'}")
        print("-" * 40)
