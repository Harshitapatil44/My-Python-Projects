import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(characters, k=length))


def add_password():
    website = input("Enter website name: ")
    username = input("Enter username: ")
    choice = input("Do you want to generate a password? (y/n): ").lower()

    if choice == "y":
        password = generate_password()
        print(f"Generated Password: {password}")
    else:
        password = input("Enter your password: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{website},{username},{password}\n")
    print("Password saved successfully.\n")


def view_passwords():
    try:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No passwords saved yet.\n")
                return
            print("Saved Passwords:")
            for line in lines:
                website, username, password = line.strip().split(",")
                print(
                    f"Website: {website} | Username: {username} | Password: {password}"
                )
    except FileNotFoundError:
        print("No password file found. Add a password first.\n")


def main():
    while True:
        print("\nPassword Manager Menu:")
        print("1. Add new password")
        print("2. View saved passwords")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
