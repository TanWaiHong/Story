import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
ANS = random.randint(1, 100)

if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    change = 10
else:
    change = 5

while change > 0:

    print(f"You have {change} attempts remaining to guess the number.")
    guess_num = int(input("Make a guess: "))

    if guess_num == ANS:
        break
    elif guess_num > ANS:
        print("Too high.")
    else:
        print("Too low")

    change -= 1
    if change > 0:
        print("Guess again.")

if change > 0:
    print(f"You got it! The answer was {ANS}.")
else:
    print(f"You've run out of guesses, you lose. The answer was {ANS}")
