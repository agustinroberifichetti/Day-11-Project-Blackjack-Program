############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from replit import clear
from random import randint
from art import logo


def blackjack():
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_cards = []
    player_cards.append(cards[randint(0, len(cards) - 1)])
    player_cards.append(cards[randint(0, len(cards) - 1)])

    as_quantity_player = player_cards.count(11)

    if as_quantity_player == 2:
        player_cards[0] = 1
        as_quantity_player = player_cards.count(11)

    player_cards_sum = sum(player_cards)

    dealer_cards = []
    dealer_cards.append(cards[randint(0, len(cards) - 1)])
    print(f"The dealer card is {dealer_cards}")

    condition_player = ""
    hit_player = True
    while hit_player:
        print(f"Your cards are {player_cards}. The sum is {player_cards_sum}.")
        decision = input(
            "\nDo you want another card?\nType 'y' if you want one more card, o type 'n' if you stand with your current cards --> "
        )
        if decision == "n":
            hit_player = False
        if decision == "y":
            player_cards.append(cards[randint(0, len(cards) - 1)])
            player_cards_sum = sum(player_cards)
            as_quantity_player = player_cards.count(11)
            if player_cards_sum > 21 and as_quantity_player == 0:
                print(
                    f"Your cards are {player_cards}. The sum is {player_cards_sum}.\nYou lose!"
                )
                hit_player = False
                condition_player = "loser"
            if player_cards_sum > 21 and as_quantity_player > 0:
                player_cards[player_cards.index(11)] = 1
                as_quantity_player = player_cards.count(11)
                player_cards_sum = sum(player_cards)
                if player_cards_sum > 21 and as_quantity_player > 0:
                    player_cards[player_cards.index(11)] = 1
                    as_quantity_player = player_cards.count(11)
                    player_cards_sum = sum(player_cards)

    if condition_player != "loser":
        dealer_cards.append(cards[randint(0, len(cards) - 1)])
        as_quantity_dealer = dealer_cards.count(11)

        if as_quantity_player == 2:
            dealer_cards[0] = 1
            as_quantity_dealer = dealer_cards.count(11)

        dealer_cards_sum = sum(dealer_cards)

        game_end = False
        hit_dealer = True
        while hit_dealer:
            print(
                f"The dealer cards are {dealer_cards}. The sum is {dealer_cards_sum}."
            )
            if dealer_cards_sum > 16 and dealer_cards_sum < 22:
                hit_dealer = False
            if dealer_cards_sum < 17:
                dealer_cards.append(cards[randint(0, len(cards) - 1)])
                dealer_cards_sum = sum(dealer_cards)
                as_quantity_dealer = dealer_cards.count(11)
                if dealer_cards_sum > 21 and as_quantity_dealer == 0:
                    print(
                        f"The dealer cards are {dealer_cards}. The sum is {dealer_cards_sum}.\nYOU WIN!"
                    )
                    hit_dealer = False
                    game_end = True
                if dealer_cards_sum > 21 and as_quantity_dealer > 0:
                    dealer_cards[dealer_cards.index(11)] = 1
                    as_quantity_dealer = dealer_cards.count(11)
                    dealer_cards_sum = sum(dealer_cards)
                    if dealer_cards_sum > 21 and as_quantity_dealer > 0:
                        dealer_cards[dealer_cards.index(11)] = 1
                        as_quantity_dealer = dealer_cards.count(11)
                        dealer_cards_sum = sum(dealer_cards)

        if game_end == False:
            if dealer_cards_sum > player_cards_sum:
                print("You lose!")
            elif dealer_cards_sum == player_cards_sum:
                print("Draw.")
            else:
                print("YOU WIN!")

    another_hand = input(
        "\nDo you want to play another hand?\nType 'y' if you do, ot type 'n' if you don\'t --> "
    )

    if another_hand == "y":
        clear()
        blackjack()
    else:
        print("\nThanks for playing! See you soon!")


blackjack()
