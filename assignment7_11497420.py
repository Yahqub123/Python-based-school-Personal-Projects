#NAME: Yahqub Oyebola
#OBJECTIVE: Creating a detailed Object oriented program(OOP) of the Black-Jack game.

import random

class PlayingCard: #Creating our playing card class to handle a object of each card
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def get_suit(self):
        return self.suit
    def get_value(self):
        return self.value
    def get_num_value(self):
        if self.value == "ace":
            return 1
        elif self.value == "jack":
            return 10
        elif self.value == "queen":
            return 10
        elif self.value == "king":
            return 10
        else:
            return self.value

class Deck:
    def __init__(self):
        self.cards = []

    def draw_card(self):
        selected_card = random.choice(self.cards)
        self.cards.remove(selected_card)
        return selected_card

    def init_deck(self): #function to develop our deck of cards
        suits = ["hearts", "diamonds", "spades", "clubs"]
        values = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
        for suit in suits:
            for value in values:
                self.cards.append(PlayingCard(suit, value))

class Hand: #class to work with each hands (player or dealer)
    def __init__(self):
        """set self.cards as an empty list"""
        self.cards = []

    def get_cards(self, deck):
        """draw two initial cards from the deck and append them to self.cards"""
        self.cards.append(deck.draw_card()) #drawing a card from the deck of cards
        self.cards.append(deck.draw_card())

    def get_total_value(self):
        """get total value of cards in the hand"""
        ## iterate over self.cards and get the total value from self.cards and return it
        sum = 0
        for card in self.cards:
            sum += card.get_num_value()
        return sum #getting the sum of the cards in our Person(player or dealer) hand.

    def add_card(self, deck):
        """draw one card from the deck and append them to self.cards"""
        self.cards.append(deck.draw_card()) #we are drawing another card from deck and add it to Person's hand

class Person: #super class that represents a person.
    def __init__(self, deck):
        """set hand and get two initial cards from the deck"""
        self.hand = Hand()
        self.hand.get_cards(deck) #deals a person 2 cards upon the creation of a instance or object of a person.

    def play_turn(self, deck): #Adding a card to person's hand.
        """add a card from the deck to hand"""
        self.hand.add_card(deck) #calling the add card method to get a card from the deck of cards.

    def report_score(self): #gets the score of a person
        """report total values of the hand"""
        return self.hand.get_total_value() #gets the sum of cards in a person's hand

class Dealer(Person):
    def __init__(self, deck):
        """inheirt Person Class and set self.name as 'Dealer'"""
        super().__init__(deck)
        self.name = "Dealer"

class Player(Person):
    def __init__(self, deck, name):
        """inheirt Person Class and set self.name as what a user typed in"""
        super().__init__(deck)
        self.name = name


class BlackjackGame:
    def __init__(self):
        """initialize deck and player"""
        self.deck = Deck()
        self.player = None
        self.dealer = None

    def play_game(self):
        # Prime the loop and start the first game.
        user_response = "Y"
        while user_response == "Y" or user_response == "y":
            ## fill the deck with 52 cards
            self.deck.init_deck()
            ## initialize a player amd dealer and get two cards per player
            player_name = input("What's your name?: ")
            self.player = Player(self.deck, player_name)
            self.dealer = Dealer(self.deck)
            print(str(self.player.name) + " was dealt a hand with a value of:",self.player.report_score())
            choice = input("Would you like to take another card? (Y/N):") #validates if player wants another card or not

            while choice.lower() == "y":
                self.player.play_turn(self.deck) #deals player a new card
                self.dealer.play_turn(self.deck) #deals dealer a new card

                if self.player.report_score() > 21: #checks if player busted
                    print("You BUSTED with a total value of",self.player.report_score(),"!")
                    break
                elif self.dealer.report_score() > 21: #checks if dealer busted
                    print("Dealer BUSTED with a total value of",self.dealer.report_score(),"!")
                    break
                else:
                    print(str(self.player.name) + " was dealt a hand with a value of:", self.player.report_score())
                    choice = input("Would you like to take another card? (Y/N):")

            if choice.lower()=="n":
                print("You have stopped taking more cards with a hand value of:", self.player.report_score())
                print("The dealer was dealt a hand with a value of:",self.dealer.report_score())

            if self.player.report_score() > 21: #checks if player loses
                print("\n** " + self.player.name + " You lose. **\n")

            elif self.dealer.report_score() > 21: #checks if dealer loses
                print("\n** " + self.player.name + " You win. **\n")

            elif self.player.report_score() > self.dealer.report_score(): #checks if player won by having a greater score than dealer.
                print("\n** " + self.player.name + " You win. **\n")

            elif self.player.report_score() <= self.dealer.report_score(): #checks if dealer won
                print("\n** " + self.player.name + " You lose. **\n")

            user_response = input("Would you like to play again? (Y/N)")

game = BlackjackGame() #Creates a object of the blackjackgame
game.play_game() #calls the play_game() method to play the game.
