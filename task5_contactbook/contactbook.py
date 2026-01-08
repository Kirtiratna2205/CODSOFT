contacts = {}

# ---------- Phone Validation ----------
def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


# ---------- Add Contact ----------
def add_contact():
    name = input("Enter Name: ")

    while True:
        phone = input("Enter Phone Number (10 digits): ")
        if valid_phone(phone):
            break
        else:
            print("❌ Invalid phone number! Enter exactly 10 digits.")

    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("✅ Contact added successfully!")


# ---------- View Contacts ----------
def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
        return

    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name} | Phone: {info['phone']}")


# ---------- Search Contact ----------
def search_contact():
    key = input("Enter name or phone to search: ")

    found = False
    for name, info in contacts.items():
        if key == name or key == info["phone"]:
            print("\n🔍 Contact Found")
            print("Name   :", name)
            print("Phone  :", info["phone"])
            print("Email  :", info["email"])
            print("Address:", info["address"])
            found = True

    if not found:
        print("❌ Contact not found.")


# ---------- Update Contact ----------
def update_contact():
    name = input("Enter the name of contact to update: ")

    if name in contacts:
        print("Enter new details (leave blank to keep old value)")

        phone = input("New Phone: ")
        email = input("New Email: ")
        address = input("New Address: ")

        # Phone validation
        if phone:
            if valid_phone(phone):
                contacts[name]["phone"] = phone
            else:
                print("❌ Invalid phone number! Keeping old number.")

        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address

        print("✅ Contact updated successfully!")
    else:
        print("❌ Contact not found.")


# ---------- Delete Contact ----------
def delete_contact():
    name = input("Enter the name of contact to delete: ")

    if name in contacts:
        del contacts[name]
        print("🗑️ Contact deleted successfully!")
    else:
        print("❌ Contact not found.")


# ---------- Main Menu ----------
def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\nThanks for using the Contact Book! 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.")


# ---------- Run Program ----------
main()
