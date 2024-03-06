
import random
from tkinter import Y
from art import logo
import os
clear = lambda: os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return cards[random.choice(cards)]

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You loose! Dealer has a Blackjack"
    elif player_score == 0:
        return "You Win! You has a Blackjack"
    elif player_score > 21:
        return "You Loose! Busted!"
    elif dealer_score > 21:
        return "You Win! Dealer is Busted!"

def play_game():
    print(logo)

    player_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())


    def count_score(cards):
        score = sum(cards) 
        if score == 21 and len(cards) == 2:
            return 0
        if 11 in cards and score > 21:
            cards.remove(11)
            cards.append(1)
        return score

    while not game_over:
        player_score = count_score(player_cards)
        dealer_score = count_score(dealer_cards)

        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            deal_more = input("type 'y' to get another card, 'n' to pass")
            if deal_more == 'y':
                player_cards.append(draw_card())
            else:
                game_over = True

        while dealer_score != 0 and dealer_score < 17:
            dealer_cards.append(draw_card())
            dealer_score = count_score(dealer_cards)

        print(f"   Your final hand: {player_cards}, final score: {player_score}")
        print(f"   dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print(compare(dealer_score, player_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()