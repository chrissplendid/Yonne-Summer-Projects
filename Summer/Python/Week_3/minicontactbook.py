"""
Mini Contact Book
Author: Senior Software Engineer
Description: Stores and retrieves contacts using a dictionary.
"""

def display_contacts(contacts):
    """
    Displays all contacts in the contact book.
    :param contacts: Dictionary of contacts
    """
    if not contacts:
        print("\n📭 No contacts found.")
    else:
        print("\n📒 Contact List:")
        for name, phone in contacts.items():
            print(f"- {name}: {phone}")


def main():
    # Contact book: Name → Phone Number
    contacts = {
        "Alice": "555-1234",
        "Bob": "555-5678",
        "Charlie": "555-9876"
    }

    while True:
        print("\n=== Mini Contact Book ===")
        print("1. View all contacts")
        print("2. Add new contact")
        print("3. Search contact")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            display_contacts(contacts)

        elif choice == "2":
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            contacts[name] = phone
            print(f"✅ Contact for '{name}' added.")

        elif choice == "3":
            name = input("Enter name to search: ").strip()
            phone = contacts.get(name)  # Using .get() to avoid KeyError
            if phone:
                print(f"📞 {name}: {phone}")
            else:
                print(f"⚠️ Contact '{name}' not found.")

        elif choice == "4":
            print("👋 Exiting Contact Book. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
