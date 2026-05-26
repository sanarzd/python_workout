import random

words = ["cat", "dog", "fish", "ant"]

def guessing_game():
    answer = random.choice(words)
    for _ in range(3):
        user_guess = input("what is your guess? ").strip().lower()
        if user_guess == answer:
            print(f"right, the answer is {user_guess}")
            break
        elif user_guess < answer:
            print("choose a later word in the dictionary")
        else:
            print("choose an earlier word in the dictionary")
    else:
        print("you didn't guess in time")

guessing_game()