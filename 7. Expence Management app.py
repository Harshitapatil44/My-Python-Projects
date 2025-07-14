from datetime import datetime


def add_expense():
    while True:
        date = input("Enter Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    category = input("Enter Category: ")

    while True:
        amt = input("Enter Amount: ")
        if amt.replace(".", "", 1).isdigit():
            break
        else:
            print("Please enter a valid numeric amount.")

    prd = input("Enter Products/Description: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{date},{category},{amt},{prd}\n")
    print("Expense details added successfully.\n")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No expenses found.\n")
                return
            print("\nAll Expenses:")
            for i, line in enumerate(lines, start=1):
                date, category, amt, prd = line.strip().split(",")
                print(
                    f"{i}. Date: {date}, Category: {category}, Amount: ₹{amt}, Product: {prd}"
                )
            print()
    except FileNotFoundError:
        print("No expenses file found.\n")


def search_expenses_by_date():
    search_date = input(
        "Enter Date to search (e.g., 2025-07-14 or just 2025-07): "
    ).lower()
    found = False
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date, category, amt, prd = line.strip().split(",")
                if search_date in date.lower():
                    print(
                        f"🔍 Found - Date: {date}, Category: {category}, Amount: ₹{amt}, Product: {prd}"
                    )
                    found = True
        if not found:
            print("Expense not found.\n")
    except FileNotFoundError:
        print("No expenses found.\n")


def delete_category():
    name_to_delete = input("Enter Expense Category to delete: ").lower()
    updated_expenses = []
    found = False
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            date, category, amt, prd = line.strip().split(",")
            if category.lower() != name_to_delete:
                updated_expenses.append(line)
            else:
                found = True
        with open("expenses.txt", "w") as file:
            file.writelines(updated_expenses)
        if found:
            print("Expenses in the category deleted successfully.\n")
        else:
            print("Category not found.\n")
    except FileNotFoundError:
        print("No expenses found.\n")


def total_expenses():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                _, _, amt, _ = line.strip().split(",")
                total += float(amt)
        print(f"\nTotal Expenses: ₹{total:.2f}\n")
    except FileNotFoundError:
        print("No expenses found.\n")


def main():
    while True:
        print("======== Expense Management App ========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses by Date")
        print("4. Delete Expenses by Category")
        print("5. Show Total Expense")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses_by_date()
        elif choice == "4":
            delete_category()
        elif choice == "5":
            total_expenses()
        elif choice == "6":
            print("Exiting Expense Management App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
