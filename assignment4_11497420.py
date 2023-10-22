# Name: Yahqub Oyebola
# Objective: Creating a Black-Jack Card game.

import random  # Importing the python module called random


def main(): #Function to mainly check if player won or lost and reapeats for each hand.
    User_input = "Y"
    while User_input == "Y" or User_input == "y":
        Players_score = get_player_score() #gets the returned value from the get_player_score function
        Dealers_score = get_dealer_score() #gets the returned value from the get_dealer_score function
        if Players_score > 21:
            print("** You lose. **")
        else: #checks to see who won or lost.
            if Dealers_score >= Players_score:
                print("You have stopped taking more cards with a hand value of", Players_score)
                print("The dealer was dealt a hand with a value of", Dealers_score)
                print("\n** You lose. **")
            elif Players_score > Dealers_score:
                print("You have stopped taking more cards with a hand value of", Players_score)
                print("The dealer was dealt a hand with a value of", Dealers_score)
                print("\n** You win! **")
        User_input = input("\nWould you like to play again? (y/n)")


def deal_card():  # Function to get a random card value from 1 to 10 using randint()
    Card_Value = random.randint(1, 10)
    return Card_Value


def get_player_score():  # Function to get our Players_score and determine if they chose to HIT or STAY
    Card_1 = deal_card()  # calls the deal_card function and assigns a random value to Card_1
    Card_2 = deal_card()
    sum_of_cards = Card_1 + Card_2  # sums both randomly generated cards.
    print("Your hand of two cards has a total value of", sum_of_cards)
    User_input = input("Would you like to take another card? (y/n)")  # gets player's decision to HIT or STAY
    while User_input == "y" or User_input == "Y":
        card_3 = deal_card()  # deals player another card then we add it with sum_of_cards
        sum_of_cards = sum_of_cards + card_3
        if sum_of_cards > 21:  # Checks to see if the sum_of_cards is greater than 21 to see if player has lost
            print("You BUSTED with a total value of", sum_of_cards, "!")
            return sum_of_cards
        else:  # Asks the player if they want another card if sum_of_cards is less than 21
            print("Your hand now has a total value of", sum_of_cards)
            User_input = input("Would you like to take another card? (y/n)")
    return sum_of_cards


def get_dealer_score():  # Function to generate the Dealer_score using random.
    Dealer_score = random.randint(16, 21)
    return Dealer_score  # Returning the dealer's score.


main()  # calling our main Function