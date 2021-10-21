import random
from art import logo, vs
from game_data import data
from replit import clear

score = 0

base_compare = random.choice(data)


def game(game_score, compare):
    print(logo)

    compare_1 = compare
    compare_2 = random.choice(data)
    while compare_1 == compare_2:
        compare_2 = random.choice(data)

    if game_score > 0:
        print(f"You're right! Current score: {game_score}.")

    print(f"Compare A: {compare_1['name']}, a {compare_1['description']}, from {compare_1['country']}.")
    print(vs)
    print(f"Against B: {compare_2['name']}, a {compare_2['description']}, from {compare_2['country']}.")
    player_choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    if player_choose == 'a':
        if compare_1['follower_count'] >= compare_2['follower_count']:
            game_score += 1
            clear()
            game(game_score, compare_2)

        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {game_score}")

    else:
        if compare_2['follower_count'] >= compare_1['follower_count']:
            game_score += 1
            clear()
            game(game_score, compare_2)

        else:
            clear()
            print(f"Sorry, that's wrong. Final score: {game_score}")


game(score, base_compare)
