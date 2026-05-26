import random

def guessing_game():
    answer = random.randint(0, 100)
    while True:
        user_guess = int(input("what is your guess? "))
        if user_guess == answer:
            print(f"right, the answer is {user_guess}")
            break
        elif user_guess < answer:
            print(f"your guess of {user_guess} is too low")
        else:
            print(f"your guess of {user_guess} is too high")
            
guessing_game()