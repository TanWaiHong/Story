import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_choose = random.randint(0, 2)

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choose == 0:
    print(rock)
    print("Computer chose:")
    if computer_choose == 0:
        print(rock)
        print("It's a draw")
    if computer_choose == 1:
        print(paper)
        print("You lose")
    if computer_choose == 2:
        print(scissors)
        print("You win!")

elif player_choose == 1:
    print(paper)
    print("Computer chose:")
    if computer_choose == 0:
        print(rock)
        print("You win!")
    if computer_choose == 1:
        print(paper)
        print("It's a draw")
    if computer_choose == 2:
        print(scissors)
        print("You lose")

elif player_choose == 2:
    print(scissors)
    print("Computer chose:")
    if computer_choose == 0:
        print(rock)
        print("You lose")
    if computer_choose == 1:
        print(paper)
        print("You win!")
    if computer_choose == 2:
        print(scissors)
        print("It's a draw")
