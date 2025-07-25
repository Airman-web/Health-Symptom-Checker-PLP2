#!/usr/bin/env python3
"""
Health CLI Checker - Basic Menu (P1)
CLI Entry & User Flow with simple menu system
"""

def show_menu():
    """Display main menu options"""
    print("\n" + "="*30)
    print("HEALTH CLI CHECKER")
    print("="*30)
    print("MAIN MENU")
    print("="*30)
    print("1. Check Symptoms")
    print("2. Access History") 
    print("3. Add/View Clinics")
    print("4. Exit")
    print("-"*30)

def check_symptoms():
    """Handle symptom input and show conditions"""
    print("\n--- SYMPTOM CHECKER ---")
    symptoms = input("Enter your symptoms (comma separated): ").strip().lower()
    
    if not symptoms:
        print("No symptoms entered.")
        return
    
    print(f"Checking symptoms: {symptoms.capitalize()}")
    print("Conditions will be displayed here...")
    # TODO: Connect to P3 matcher module

def access_history():
    """Show user's symptom check history"""
    print("\n--- HISTORY ---")
    print("Your previous symptom checks will appear here...")
    # TODO: Connect to P5 history module

def manage_clinics():
    """Add or view clinics"""
    print("\n--- CLINICS ---")
    print("1. View Clinics")
    print("2. Add Clinic")
    
    choice = input("Choose option (1-2): ").strip()
    
    if choice == "1":
        print("Available clinics will be listed here...")
        # TODO: Connect to P4 clinics module
    elif choice == "2":
        name = input("Clinic name: ").strip().lower()
        city = input("City: ").strip().lower()
        distance = input("Distance (km): ").strip().lower()
        print(f"Clinic '{name.capitalize()}' in {city.capitalize()} ({distance}km) would be added")
        # TODO: Connect to P4 clinics module
    else:
        print("Invalid option")

def main():
    """Main application loop with basic menu"""
    
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            check_symptoms()
        elif choice == "2":
            access_history()
        elif choice == "3":
            manage_clinics()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
