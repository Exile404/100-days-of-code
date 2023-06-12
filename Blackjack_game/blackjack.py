import random
import os

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


def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def cal_score(card):
    if sum(card)==21 and len(card) == 2:
        return 0
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(user_score,comp_score):
    if user_score == comp_score:
        return 'Draw'
    elif comp_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif comp_score > 21:
        return "Opponent went over. You win"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You Lose"

def play_game():
    print(logo)
    game_over = False
    user_card = []
    computer_card = []
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    user_score = cal_score(user_card)
    comp_score = cal_score(computer_card)
    while not game_over:
        print(f'Your cards: {user_card}, current Score: {user_score}')
        print(f'Computer cards: {computer_card}, current Score: {comp_score}')
        if user_score == 0 or comp_score == 0 or user_score >21:
            game_over = True
        else:
            user_deal_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal_card == 'y':
                user_card.append(deal_card())
            else:
                game_over = True
    while comp_score!= 0 and comp_score <17:
        computer_card.append(deal_card())
        comp_score = cal_score(computer_card)
    print(f' Your final score: {user_score}')
    print(f' Computer Final Score: {comp_score}')
    print(compare(user_score,comp_score))

    while True:
        game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if game == 'y':
            os.system('cls')
            play_game()
        else:
            quit()

play_game()