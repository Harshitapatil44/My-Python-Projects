import random
import string

url_database = {}


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = "".join(random.choices(characters, k=length))
    return short_code


def shorten_url(original_url):
    if original_url in url_database.values():
        for code, url in url_database.items():
            if url == original_url:
                return code
    else:
        short_code = generate_short_code()
        while short_code in url_database:
            short_code = generate_short_code()
        url_database[short_code] = original_url
        return short_code


def get_original_url(short_code):
    return url_database.get(short_code, "Short URL not found.")


while True:
    print("\n--- URL Shortener ---")
    print("1. Shorten URL")
    print("2. Get Original URL")
    print("3. View All URLs")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        long_url = input("Enter the original URL: ")
        code = shorten_url(long_url)
        print("Short URL code is:", code)

    elif choice == "2":
        code = input("Enter the short URL code: ")
        original = get_original_url(code)
        print("Original URL is:", original)

    elif choice == "3":
        print("Stored URLs:")
        for code, url in url_database.items():
            print(f"{code} -> {url}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
