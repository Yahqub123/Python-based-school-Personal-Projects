# Name: Yahqub Oyebola
# Objective: Creating a Black-Jack Card game.

import random  # Importing the python module called random

# The main function repeatedly plays the game of blackjack until the user decides to stop.
def main():
    User_input = "Y"
    while User_input == "Y" or User_input == "y":
        card_list= set_card_deck() #gets a list or deck of cards
        Players_score= get_player_score(card_list) #passes in this deck to our get_player_score(card_list) func
        Dealers_score = get_dealer_score()
        if Players_score > 21:
            print("** You lose. **")
        else:
            if Dealers_score >= Players_score:
                print("You have stopped taking more cards with a hand value of", Players_score)
                print("The dealer was dealt a hand with a value of", Dealers_score)
                print("\n** You lose. **")
            elif Players_score > Dealers_score:
                print("You have stopped taking more cards with a hand value of", Players_score)
                print("The dealer was dealt a hand with a value of", Dealers_score)
                print("\n** You win! **")
        User_input = input("\nWould you like to play again? (y/n)")

'''Our 'set_card_deck()' Function Creates a card deck from an input file (cards.txt). We basically read the file
line by line then create a deck of cards with the input. we create a list then we use the split() function to 
split the values and suits on each line into a list.Then we return the deck of cards that we have.'''
def set_card_deck():
    card_list = []
    with open("cards.txt", "r") as cards: #opens our cards.txt file and assigns it to a variable
        for line in cards:
            card_list.append(line.rstrip('\n').split(",")) #appending the list values on each line to card_list
    return card_list

'''Our 'def deal_card(card_list)' Function is used to get a random card from our list of cards. Then we convert these
cards if they are  (Jack,Queen,And King) to 10 and Ace cards to 1. If the card chosen is a integer, we just leave it that 
way.'''
def deal_card(card_list):  
    choice = random.choice(card_list) #gets a random card from our card_list.
    if choice[0].isdigit(): #checks to see if the card value is a integer
        Card_Value = int(choice[0])

    elif choice[0] == 'Ace': #checks to see if the card value is a 'ace' then sets our card_value to 1
        Card_Value = 1

    elif (choice[0] == 'Jack') or (choice[0] == 'Queen') or (choice[0] == 'King'):
        Card_Value = 10

    card_list.remove(choice) #we remove our chosen card from the list since its been used 
    return card_list, Card_Value #returns our list of cards and the value


def get_player_score(card_list):  # Function to get our Players_score and determine if they chose to HIT or STAY
    card_list, Card_1 = deal_card(card_list)  #calls the deal_card function, assigns card_1 a value and returns our current list of cards
    card_list, Card_2 = deal_card(card_list)
    sum_of_cards = Card_1 + Card_2  # sums both randomly generated cards.
    print("Your hand of two cards has a total value of", sum_of_cards)
    User_input = input("Would you like to take another card? (y/n)")  # gets player's decision to HIT or STAY
    while User_input == "y" or User_input == "Y":
        card_list, card_3 = deal_card(card_list)  # deals player another card then we add it with sum_of_cards
        sum_of_cards = sum_of_cards + card_3
        if sum_of_cards > 21:  # Checks to see if the sum_of_cards is greater than 21 to see if player has lost
            print("You BUSTED with a total value of", sum_of_cards, "!")
            return sum_of_cards
        else:  # Asks the player if they want another card if sum_of_cards is less than 21
            print("Your hand now has a total value of", sum_of_cards)
            User_input = input("Would you like to take another card? (y/n)")
    return sum_of_cards #returns the sum of the cards that the player has.


def get_dealer_score():  # Function to generate the Dealer_score using random.
    Dealer_score = random.randint(16, 21)
    return Dealer_score  # Returning the dealer's score.


main()  # calling our main Function

