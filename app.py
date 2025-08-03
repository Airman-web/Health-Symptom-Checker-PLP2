#!/usr/bin/python3
# Before running this app, install: colorama, pyfiglet

import time
from colorama import Fore, Style, init
import pyfiglet

from modules.i18n import T
from modules.matcher import find_ranked_conditions
from modules.history import (
    get_or_create_user,
    get_user_city,
    save_history,
    view_history,
)
from modules.clinics import get_clinic_by_city, get_random_clinic
from db.database import get_connection

init(autoreset=True)

# ---------- Color helpers ----------
def c_info(text): return Fore.CYAN + text + Style.RESET_ALL
def c_good(text): return Fore.GREEN + text + Style.RESET_ALL
def c_warn(text): return Fore.RED + text + Style.RESET_ALL
def c_prompt(text): return Fore.YELLOW + text + Style.RESET_ALL
def c_header(text): return Fore.BLUE + text + Style.RESET_ALL
def c_result(text): return Fore.MAGENTA + text + Style.RESET_ALL

# ---------- Utilities ----------
def get_all_symptoms():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT symptom FROM symptoms_conditions ORDER BY symptom ASC")
    symptoms = [row[0] for row in cur.fetchall()]
    conn.close()
    return symptoms

def banner(lang):
    print(c_header("=" * 60))
    print(c_good("WELCOME TO HEALTH SYMPTOM CHECKER CLI APP"))
    print(c_header("=" * 60))
    print(c_info(T(lang, "welcome")))

def choose_language():
    while True:
        lang = input(c_prompt("Choose language / Hitamo ururimi (en/rw): ")).strip().lower()
        if lang in ("en", "rw"):
            print(c_good(f"✅ Language has been set to {'English' if lang == 'en' else 'Kinyarwanda'}.\n"))
            return lang
        else:
            print(c_warn("❌ Invalid option. Please enter 'en' for English or 'rw' for Kinyarwanda.\n"))

def greet_user(lang):
    name = input(c_prompt(T(lang, "enter_name"))).strip()
    city = input(c_prompt("Enter your city (e.g., Kigali): ")).strip() or "Kigali"
    user_id = get_or_create_user(name, city)
    print(c_good(f"\n{name}, {T(lang, 'how_feeling')}"))
    print(c_info(T(lang, "ask_run_check")))

    # Show user history upon login
    history = view_history(user_id)
    if history:
        print(c_result(f"\n{name}, here is your recent health report history:"))
        for idx, (symptoms, conditions, self_care, timestamp) in enumerate(history, 1):
            print(c_result(f"\n{idx}. [{timestamp}]"))
            print(Fore.WHITE + f"   Symptoms:    {symptoms}")
            print(Fore.WHITE + f"   Conditions:  {conditions}")
            print(Fore.WHITE + f"   Self-care:   {self_care}")
            time.sleep(0.01)

    return name, user_id

def fake_processing(message="Processing", secs=0.6):
    print(c_header("\n" + message))
    steps = 4
    for _ in range(steps):
        print(".", end="", flush=True)
        time.sleep(secs / steps)
    print()

# ---------- Main Functions ----------
def symptom_check(lang, user_id):
    all_symptoms = get_all_symptoms()
    print(c_result("\n" + T(lang, "available_symptoms")))
    print(Fore.WHITE + ", ".join(all_symptoms))

    symptoms_raw = input(c_prompt("\n" + T(lang, "symptom_prompt")))
    symptoms_list = [s.strip().lower() for s in symptoms_raw.split(",") if s.strip()]

    fake_processing(T(lang, "matching"), secs=1.0)

    ranked = find_ranked_conditions(symptoms_list)

    if not ranked:
        print(c_warn("\n" + T(lang, "no_match")))
        print(c_info(T(lang, "try_simpler")))
        return

    print(c_header("\n" + T(lang, "possible") + "\n"))

    all_conditions, all_self_care = [], []
    for item in ranked:
        condition, score, tips = item["condition"], item["score"], item["tips"]
        print(c_result(f"- {condition} ") + Fore.WHITE + f"(score: {score})")
        for tip in tips:
            print(Fore.WHITE + f"  • {tip}")
        all_conditions.append(condition)
        all_self_care.extend(tips)
        time.sleep(0.01)

    save_history(
        user_id,
        ", ".join(symptoms_list),
        ", ".join(all_conditions),
        "; ".join(list(set(all_self_care))),
    )

    city = get_user_city(user_id)
    clinic = get_clinic_by_city(city) or get_random_clinic()
    time.sleep(0.01)
    if clinic:
        print(c_good(f"\nBefore you go, you can visit {clinic[0]} and see {clinic[1]} (Contact: {clinic[2]})."))

    print(c_warn("\n" + T(lang, "disclaimer")))

def view_user_history_screen(lang, user_id):
    print(c_header("\n" + T(lang, "history_fetch")))
    time.sleep(0.1)
    records = view_history(user_id)
    if not records:
        print(c_info(T(lang, "history_none")))
        return

    for idx, (symptoms, conditions, self_care, timestamp) in enumerate(records, 1):
        print(c_result(f"\n{idx}. [{timestamp}]"))
        print(Fore.WHITE + f"   Symptoms:    {symptoms}")
        print(Fore.WHITE + f"   Conditions:  {conditions}")
        print(Fore.WHITE + f"   Self-care:   {self_care}")
        time.sleep(0.1)

def main_menu(lang):
    print(c_header("\n========== " + T(lang, "main_menu") + " =========="))
    print(c_good(T(lang, "menu_1")))
    print(c_info(T(lang, "menu_2")))
    print(c_warn(T(lang, "menu_3")))
    print(c_header("======================================="))

def exit_app():
    print(Fore.YELLOW + "\nExiting the Health Symptom Checker...")
    time.sleep(0.01)
    print(Fore.GREEN + "✅ Successfully exited the Health Symptom Checker. Stay healthy! 💚")
    time.sleep(0.01)
    exit(0)

# ---------- Main Application ----------
def main():
    lang = choose_language()
    banner(lang)
    name, user_id = greet_user(lang)

    while True:
        main_menu(lang)
        choice = input(c_prompt(T(lang, "choose_option"))).strip()

        if choice == "1":
            symptom_check(lang, user_id)
        elif choice == "2":
            view_user_history_screen(lang, user_id)
        elif choice == "3":
            print(c_info("\n" + T(lang, "goodbye").format(name)))
            city = get_user_city(user_id)
            clinic = get_clinic_by_city(city) or get_random_clinic()
            if clinic:
                print(c_good(T(lang, "clinic_reco").format(clinic[0], clinic[1], clinic[2])))
            exit_app()
        else:
            print(c_warn(T(lang, "invalid_choice")))

if __name__ == "__main__":
    main()
