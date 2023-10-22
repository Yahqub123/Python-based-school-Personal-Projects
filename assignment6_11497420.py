# Name: Yahqub Oyebola
#Assignment 6
# Objective: Creating a Black-Jack Card game.

import random  # Importing the python module called random

# The main function repeatedly plays the game of blackjack until the user decides to stop.
def main():
    User_input = "Y"
    while User_input == "Y" or User_input == "y":
        card_list= set_card_deck() # calls the set_card_deck() fuction to to get a list or deck of cards
        scores = {"player": {"score": 0, "cards": []}, "dealer": {"score": 0,"cards": []}} #Nested dictionary to keep track of scores and
                                                                    #cards in the players and dealers hands.
        scores = get_score(card_list,scores) #Calls the get score function to get back our passed in dictionary
        Players_score = scores["player"]["score"]
        Dealers_score = scores["dealer"]["score"]
        if Players_score > 21: #checks if players busted
            print("\n** You lose. **")
        elif Dealers_score > 21: #checks if dealer busted
            print("\n** You Win **")
        elif Dealers_score >= Players_score: #checks if dealer won
            print("\n** You lose. **")
        elif Players_score > Dealers_score: #checks if player won
            print("\n** You Win **")
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
    Card_Chosen = random.choice(card_list) #gets a random card from our card_list.
    if Card_Chosen[0].isdigit(): #checks to see if the card value is a integer
        Card_Value = int(Card_Chosen[0])

    elif Card_Chosen[0] == 'Ace': #checks to see if the card value is a 'ace' then sets our card_value to 1
        Card_Value = 1

    elif (Card_Chosen[0] == 'Jack') or (Card_Chosen[0] == 'Queen') or (Card_Chosen[0] == 'King'):
        Card_Value = 10

    card_list.remove(Card_Chosen) #we remove our chosen card from the list since its been used
    return card_list, Card_Value, Card_Chosen #returns our list of cards,the value, and the card chosen

'''Our Show cards function basically shows either our players or dealers cards.'''
def show_cards(cards, who):
    if who == "player":
        print("Your cards:")
        for i in cards:
            print(i[0], "of", i[1])

    elif who == "dealer":
        print("Dealer's cards:")
        for i in cards:
            print(i[0], "of", i[1])

def get_score(card_list,scores):
    card_list, PlayerCard_1, Card_Chosen = deal_card(card_list) #draws  player first  card
    scores["player"]["score"] = PlayerCard_1
    scores["player"]["cards"].append(Card_Chosen) #appends the card to our list in the dictionary

    card_list, DealerCard_1, Card_Chosen = deal_card(card_list)
    scores["dealer"]["score"] = DealerCard_1
    scores["dealer"]["cards"].append(Card_Chosen)

    card_list, PlayerCard_2, Card_Chosen = deal_card(card_list) #draws  player first  card
    scores["player"]["score"] = scores["player"]["score"] + PlayerCard_2  #Adds the cards value to our stored card value.
    scores["player"]["cards"].append(Card_Chosen)

    card_list, DealerCard_2, Card_Chosen = deal_card(card_list)
    scores["dealer"]["score"] = scores["dealer"]["score"] + DealerCard_2
    scores["dealer"]["cards"].append(Card_Chosen)

    cards_on_hand = scores["player"]["cards"]
    who = "player"
    score_of_player = scores["player"]["score"]
    show_cards(cards_on_hand,who) #prints playes cards info
    print("The sum of the first two cards is:", score_of_player)

    User_input = input("Do you want to take another card?: (Y/N)")

    while User_input == "y" or User_input == "Y":
        card_list, PlayerCard_3, Card_Chosen = deal_card(card_list)
        scores["player"]["score"] = scores["player"]["score"] + PlayerCard_3
        scores["player"]["cards"].append(Card_Chosen)

        card_list, DealerCard_3, Card_Chosen = deal_card(card_list)
        scores["dealer"]["score"] = scores["dealer"]["score"] + DealerCard_3
        scores["dealer"]["cards"].append(Card_Chosen)

        if scores["player"]["score"] > 21:  # Checks to see if the sum_of_cards is greater than 21 to see if player has lost
            print("You BUSTED with a total value of",scores["player"]["score"], "!")
            show_cards(cards_on_hand, who)
            return scores

        elif scores["dealer"]["score"] > 21:
            print("The dealer BUSTED with a total value of", scores["dealer"]["score"], "!")
            show_cards(scores["dealer"]["cards"],"dealer")
            return scores

        else:
            print("Your hand now has a total value of", scores["player"]["score"])
            show_cards(cards_on_hand, who)
            User_input = input("Do you want to take another card?: (Y/N)")

    if User_input == "n" or User_input == "N":
        show_cards(cards_on_hand, who)
        print("You have stopped taking more cards with a hand value of", scores["player"]["score"])
        print("The dealer was dealt a hand with a value of", scores["dealer"]["score"])
        show_cards(scores["dealer"]["cards"], "dealer")
    return scores


main()  #calling our main Function


