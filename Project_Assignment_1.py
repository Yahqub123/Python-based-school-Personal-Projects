#Name: Yahqub oyeola
#Objective: Creating a Rock, Paper, Scissors game.

import random as rd

def main(): #Main function to run the code.
    Players_Decision = input("Welcome to Rock, Paper, Scissors! Please enter your choice(Rock, Paper, or Scissors) ONLY:")
    Players_Decision = Players_Decision.lower() #Changes our Player's decision input to all lower case for better comparison.

    while (Players_Decision != "rock") and (Players_Decision != "paper") and (Players_Decision != "scissors"): #Loop to
        #validate our user's input and request them to re-enter an input if they entered a wrong input
        print("That's not a valid play. Check your spelling!")
        Players_Decision = input("Welcome to Rock, Paper, Scissors! Please enter your choice(Rock, Paper, or Scissors ONLY):")
        Players_Decision = Players_Decision.lower() #Changes player's input to all lower case for better comparison.

    computers_choice = get_computers_choice() #Callling the get_computers_choice() function and setting the returned
                                              #value to a variable called computers_choice

    #The following if statements are used to compare the user's input to the computer's randomly generated value and
    #decide if the player won or lost.
    if Players_Decision == computers_choice:
        print("Tie!")
    elif (Players_Decision == "rock") and (computers_choice == 'paper'):
        print("You lose!, Paper (computer), covers, Rock (player)")
    elif (Players_Decision == "rock") and (computers_choice == 'scissors'):
        print("You win!, rock (player), smashes, scissors (computer)")
    elif (Players_Decision == "paper") and (computers_choice == 'rock'):
        print("You win!, paper (player), covers, Rock (computer)")
    elif (Players_Decision == "paper") and (computers_choice == 'scissors'):
        print("You lose!, Scissors (computer), cuts, paper (player)")
    elif (Players_Decision == "scissors") and (computers_choice == 'rock'):
        print("You lose!, rock (computer), smashes, scissors (player)")
    elif (Players_Decision == "scissors") and (computers_choice == 'paper'):
        print("You win!, Scissors (player), cuts, paper (computer)")


def get_computers_choice(): #Function to generate random values and associate these values to decision(rock,paper,or scissors)
    Choice = ""
    num = rd.randint(1,3)
    if num == 1:
        Choice = 'rock'
    elif num == 2:
        Choice = 'paper'
    elif num==3:
        Choice = 'scissors'
    
    return Choice

main() #Calls our main function