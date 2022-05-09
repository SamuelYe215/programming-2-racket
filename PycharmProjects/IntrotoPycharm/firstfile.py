# introduction to Python

import time

def main():
    # A quiz application
    # Create a list that is 2-dimensional
    # Create some questions

    score = 0
    questions = [
        ("What is the colour of the sun?", "yellow"),
        ("What colour is the sky", "blue"),
        ("How many things are in a dozen", "12"),
        ]

    # Ask the questions and get the answer
    print("Welcome to the quiz.")
    print("Answer the questions to the best of your ability.")

    time.sleep(2)

    for question in questions:
        # question -> question[0]
        # answer -> question[1]
        user_answer = input(question[0]).strip(",.?!").lower()

        print("\n checking answer...")
        time.sleep(2)

        # See if the user's answer is correct

        if user_answer == question[1]:
            print("Good job!")
            score += + 1
        else:
            print(f"booo the answer was {question[1]}")

    print(f'you got {score} right')
if __name__ == "__main__":
    main()