import tkinter as tk
import random

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Great things never come from comfort zones.",
    "Push yourself, because no one else is going to do it for you.",
]


def new_quote():
    quote_label.config(text=random.choice(quotes))


root = tk.Tk()
root.title("Quote Generator")
root.geometry("500x200")

quote_label = tk.Label(
    root, text=random.choice(quotes), wraplength=400, font=("Arial", 12), pady=20
)
quote_label.pack()

button = tk.Button(
    root, text="New Quote", command=new_quote, font=("Arial", 10, "bold")
)
button.pack()

root.mainloop()
