import random

def guessing_game():
    answer = random.randint(0, 100)

    for ـ in range(3):
        user_guess = int(input("what is your guess? "))
        
        if user_guess == answer:
            print(f"right, the answer is {user_guess}")
            break
        elif user_guess < answer:
            print(f"your guess of {user_guess} is too low")
        else:
            print(f"your guess of {user_guess} is too high")
    else:
        print("you did not guess in time")
            
guessing_game()