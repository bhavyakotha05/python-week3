# Contact Management System
# Week 3 Project - Functions & Dictionaries

import re
from datetime import datetime

# ---------------- VALIDATION FUNCTIONS ----------------

def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# ---------------- CORE FUNCTIONS ----------------

def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")

    while True:
        name = input("Enter contact name: ").strip()
        if name:
            if name in contacts:
                print(f"Contact '{name}' already exists!")
                choice = input("Do you want to update instead? (y/n): ").lower()
                if choice == 'y':
                    update_contact(contacts, name)
                return
            break
        print("Name cannot be empty!")

    while True:
        phone = input("Enter phone number: ").strip()
        valid, clean_phone = validate_phone(phone)
        if valid:
            break
        print("Invalid phone number! Enter 10–15 digits.")

    while True:
        email = input("Enter email (optional): ").strip()
        if not email or validate_email(email):
            break
        print("Invalid email format!")

    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Work/Family/Other): ").strip() or "Other"

    contacts[name] = {
        "phone": clean_phone,
        "email": email if email else None,
        "address": address if address else None,
        "group": group,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    print(f"✅ Contact '{name}' added successfully!")


def update_contact(contacts, name):
    print(f"\n--- UPDATE CONTACT ({name}) ---")

    phone = input("Enter new phone number (leave blank to keep old): ").strip()
    if phone:
        valid, clean_phone = validate_phone(phone)
        if valid:
            contacts[name]["phone"] = clean_phone

    email = input("Enter new email (leave blank to keep old): ").strip()
    if email and validate_email(email):
        contacts[name]["email"] = email

    address = input("Enter new address (leave blank to keep old): ").strip()
    if address:
        contacts[name]["address"] = address

    group = input("Enter new group (leave blank to keep old): ").strip()
    if group:
        contacts[name]["group"] = group

    contacts[name]["updated_at"] = datetime.now().isoformat()
    print(f"✅ Contact '{name}' updated successfully!")


def search_contacts(contacts):
    term = input("Enter name to search: ").lower()
    results = {n: i for n, i in contacts.items() if term in n.lower()}
    display_search_results(results)


def display_search_results(results):
    if not results:
        print("❌ No contacts found.")
        return

    print("\n--- SEARCH RESULTS ---")
    for i, (name, info) in enumerate(results.items(), 1):
        print(f"{i}. {name}")
        print(f"   📞 Phone: {info['phone']}")
        if info["email"]:
            print(f"   📧 Email: {info['email']}")
        if info["address"]:
            print(f"   📍 Address: {info['address']}")
        print(f"   👥 Group: {info['group']}")
        print("-" * 40)


# ---------------- MAIN MENU ----------------

def main():
    contacts = {}

    while True:
        print("\n==== CONTACT MANAGEMENT SYSTEM ====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contacts(contacts)
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


# ---------------- PROGRAM START ----------------

if __name__ == "__main__":
    main()
