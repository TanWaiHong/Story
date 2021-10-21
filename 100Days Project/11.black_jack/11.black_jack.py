import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


player_card_list = []
com_card_list = []


def check_card(list1):
    while sum(list1) > 21 and 11 in list1:
        list1[list1.index(11)] = 1


def append_card(list1):
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    list1.append(random.choice(card_list))
    check_card(list1)


def asking(game_end):
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        append_card(player_card_list)
        display()
    else:
        ending()
        game_end = True
    if not game_end:
        if sum(player_card_list) <= 21:
            asking(game_end)
        else:
            ending()


def display():
    print(f"    Your cards: {player_card_list}, current score: {sum(player_card_list)}")
    print(f"    Computer's first card: {com_card_list[0]}")


def ending():
    while sum(com_card_list) < 17:
        append_card(com_card_list)
    print(f"    Your final hand card: {player_card_list}, final score: {sum(player_card_list)}")
    print(f"    Computer's final hand card: {com_card_list}, final sore: {sum(com_card_list)}")
    if sum(player_card_list) > 21:
        print("You went over. You lose 😭")
    elif sum(com_card_list) > 21:
        print("Computer went over. You win")
    elif sum(player_card_list) > sum(com_card_list):
        print("You bigger than computer, you win")
    elif sum(com_card_list) > sum(player_card_list):
        print("you lower than computer, you lose")
    else:
        print("draw")


end_game = False
print(logo)
if input("will you want to play blackjack? 'y' or 'n' : ") == 'n':
    end_game = True
while not end_game:
    append_card(player_card_list)
    append_card(player_card_list)
    append_card(com_card_list)
    display()
    asking(end_game)
    if input("will you want to continue play blackjack? 'y' or 'n' : ") == 'n':
        end_game = True
