def menu():
    print("------- TO-DO LIST MENU -------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task = input("Task: ")
    open("todo.txt", "a").write(task + "\n")
    print("Added.")


def view_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\n--- Added Tasks ---")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("This task is not added or may be deleted already.")


def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = tasks[task_num - 1].strip() + " [Done]\n"
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    menu()
    choice = input("Enter your choice Between (1-5) :- ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("List Closed")
        break
    else:
        print("Invalid choice. Try between 1 to 5.")
