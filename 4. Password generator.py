import random
import string


def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    length = int(input("Enter the length of password: "))
    password = password_generator(length)
    print("Generated Password: ", password)


if __name__ == "__main__":
    main()
