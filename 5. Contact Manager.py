def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully.\n")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.\n")
            else:
                print("All Contacts:")
                for i, contact in enumerate(contacts, start=1):
                    name, phone, email = contact.strip().split(",")
                    print(f"{i}. Name: {name}, Phone: {phone}, Email: {email}")
                print()
    except FileNotFoundError:
        print("No contacts found.\n")


def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")
                if search_name in name.lower():
                    print(f"Found - Name: {name}, Phone: {phone}, Email: {email}\n")
                    found = True
        if not found:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts found.\n")


def delete_contact():
    name_to_delete = input("Enter name to delete: ").lower()
    updated_contacts = []
    found = False
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            if name.lower() != name_to_delete:
                updated_contacts.append(contact)
            else:
                found = True
        with open("contacts.txt", "w") as file:
            file.writelines(updated_contacts)
        if found:
            print("Contact deleted successfully.\n")
        else:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts found.\n")


def main():
    while True:
        print("====== Contact Manager ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
