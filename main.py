import random
from lists import cards

cards = cards

def game_start():
    def deal_card():
        """Deals a random card"""
        card = random.choice(cards)
        return card


    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards"""
        card = sum(cards)
        if 11 in cards and 10 in cards and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return card

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "Lose, Opponent has blackjack"
        elif user_score == 0:
            return "Win with a blackjack"
        elif user_score > 21:
            return "You went over, you lost"
        elif computer_score > 21:
            return "Oppent went over, you win"
        elif user_score > computer_score:
            return "You win"
        else:
            return "Computer wins"





    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            
        else:
            user_should_deal = input("Do you want to draw another card? 'y' or 'n'")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                print(user_cards)
            else:
                is_game_over = True
                

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"{compare(user_score, computer_score)} User: {user_score}, Computer {computer_score} ")

while input("New game? 'y' or 'n'").lower() == "y":
    game_start()