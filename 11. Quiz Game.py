quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B",
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C",
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": [
            "A. J.K. Rowling",
            "B. Enid Blyton",
            "C. Ruskin Bond",
            "D. Charles Dickens",
        ],
        "answer": "A",
    },
]


def start_quiz():
    score = 0
    print("=== Welcome to the Quiz Game ===\n")

    for i, q in enumerate(quiz, start=1):
        print(f"Q{i}. {q['question']}")
        for option in q["options"]:
            print(option)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()

        if user_ans == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer was {q['answer']}.\n")

    print(f"Quiz Over! Your final score is: {score}/{len(quiz)}")


start_quiz()
