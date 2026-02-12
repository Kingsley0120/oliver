import json
import os

# Constants for realms and levels
REALMS = ["Novice", "Apprentice", "Adept", "Expert", "Master", "Sage", "Immortal", "Divine", "Transcendent"]
LEVELS = 9
SPIRIT_STONE_REQUIREMENTS = {realm: (level + 1) * 10 for realm in REALMS for level in range(LEVELS)}

# Disciple database
disciples = {}

# Function to save the disciple data to a JSON file
def save_data():
    with open("disciples.json", "w") as f:
        json.dump(disciples, f)

# Function to load disciple data from a JSON file
def load_data():
    global disciples
    if os.path.exists("disciples.json"):
        with open("disciples.json", "r") as f:
            disciples = json.load(f)

# Function to add a disciple
def add_disciple(name):
    if name not in disciples:
        disciples[name] = {"realm": 0, "level": 0, "attendance": 0, "spirit_stones": 0}
        print(f"Disciple {name} added.")
    else:
        print("Disciple already exists.")

# Function to mark attendance
def mark_attendance(name):
    if name in disciples:
        disciples[name]["attendance"] += 1
        print(f"Attendance marked for {name}. Current attendance: {disciples[name]['attendance']}")
    else:
        print("Disciple not found.")

# Function to show progression
def show_progress(name):
    if name in disciples:
        disciple = disciples[name]
        realm = REALMS[disciple["realm"]]
        print(f"Name: {name}, Realm: {realm}, Level: {disciple['level'] + 1}, Attendance: {disciple['attendance']}, Spirit Stones: {disciple['spirit_stones']}")
    else:
        print("Disciple not found.")

# Function for spirit stone exchange
def exchange_spirit_stones(name, amount):
    if name in disciples:
        disciple = disciples[name]
        if disciple["spirit_stones"] >= amount:
            disciple["spirit_stones"] -= amount
            print(f"{amount} spirit stones exchanged for {name}.")
            save_data()
        else:
            print("Not enough spirit stones.")
    else:
        print("Disciple not found.")

# Main menu interface
def main_menu():
    load_data()
    while True:
        print("\nCultivation Attendance System")
        print("1. Add Disciple")
        print("2. Mark Attendance")
        print("3. Show Progress")
        print("4. Exchange Spirit Stones")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter disciple's name: ")
            add_disciple(name)
            save_data()
        elif choice == "2":
            name = input("Enter disciple's name to mark attendance: ")
            mark_attendance(name)
            save_data()
        elif choice == "3":
            name = input("Enter disciple's name to show progress: ")
            show_progress(name)
        elif choice == "4":
            name = input("Enter disciple's name for exchange: ")
            amount = int(input("Enter amount of spirit stones to exchange: "))
            exchange_spirit_stones(name, amount)
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main_menu()