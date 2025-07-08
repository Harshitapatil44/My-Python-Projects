import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Game!")
print("I'm thinking of a number between 1 too 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number between 1 too 100.")
