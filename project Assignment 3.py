#Name: Yahqub Oyebola
#Objective: Building a Dice Game

import random

def roll_die(): #Function to generate a random die roll value
    value = random.randint(1,6) #generating a random value from 1 to 6
    return value #Returning our generated value

bank_amount = 100 #Vraiable to keep track of our banked amount
answer = "yes"
while answer.lower() == "yes": #Condition to validate if the user wants to keep rolling a dice
    print("\nYou have five Rolls to make your Point.\nYour bet cannot exceed the amount you have left in your bank.\nYou have "
          ,bank_amount,"chips in your bank.")
    Bet = int(input("Place your bet:"))
    point = int(input('What is your Point?'))
    while(point < 2) or (point > 12): #condition to check if user's point input is valid
        print("Invalid input!! Your point cannot be less than 2 or greater than 12.")
        point = int(input("Enter a valid Point:"))

    if(Bet <= bank_amount): #Checks if user's Bet amount is not above their bank amount then acts accordingly.
        count = 5 #This is to deal with our output formatting.
        Roll_num = 0 #Variable to keep count of each roll.
        while(Roll_num < 5):
            die_1 = roll_die() #calls our roll_die() function then gives our die a varable between 1 and 6
            die_2 = roll_die()
            print("\nRolling The Dice…\nRoll number " + str(Roll_num+1) + " of 5\nThe Values are:")
            print(die_1)
            print(die_2)
            print("You Rolled a total of:",die_1 + die_2)
            print("Your Point is:",point)
            if(die_1 + die_2 == point): #Condition to check if the sum of our rolled dices is equal to our point.
                print("Congratulations, you win!! Your Die_Total of "+str(die_1 + die_2)+ " met your point of:",point,"!!")
                print("Your bet has been doubled and added to your bank_amount!!")
                Bet = Bet + Bet
                bank_amount = Bet + bank_amount
                Roll_num = 6
            else:
                if(Roll_num == 4): #Condition to check if the user is on their last roll
                    print("You have 0 more Rolls to make your point")
                    print("Sorry, You lost your bet:-",Bet)
                    bank_amount = bank_amount - Bet
                    Roll_num = Roll_num + 1
                else:
                    count -= 1
                    print("You did not make your point.")
                    print("You have", count, "more Rolls to make your point.")
                    Roll_num = Roll_num + 1
    else:
        print("\nYour bet of",Bet, "exceeded your total bank amount of:", bank_amount)
        break
    answer = input("\nRoll the Dice 5 times Again (yes or no) ONLY?")
