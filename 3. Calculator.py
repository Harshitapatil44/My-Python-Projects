def calculator():
    num1 = int(input("Enter the First no :- "))
    num2 = int(input("Enter the Second no :- "))

    print("choice to perform operation - ")
    print("1.Addition: ")
    print("2.Substraction: ")
    print("3.Multiplication: ")
    print("4.Division: ")
    print("5.reminder: ")

    ch = input("Enter a number of choice: ")

    if ch == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif ch == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif ch == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif ch == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Division by zero is not allowed !!!")

    elif ch == "5":
        if num2 != 0:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        else:
            print("Division by zero is not allowed !!!")
    else:
        print("Invalid choice of operation. ")


calculator()
