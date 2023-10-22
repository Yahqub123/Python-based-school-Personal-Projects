#Name: Sulaiman Taiwo Oyebola
#Goal: Creating a game similar to craps
#class: Principles of Data Science and Analytics (INFO 4501)

import random #Importing the python package called random

Total_chips = 100 #Total chips the user has in their bank
Decision = "YES"
while Decision.upper() == "YES": #loop to validate if user still wants to keep rolling numbers
    print("You have five Rolls to make your Point.")
    print("Your bet cannot exceed the amount you have left in your bank.")
    print("You have " + str(Total_chips) + " chips in your bank.")
    Users_Bet = int(input("Place your bet:")) #user inputs their bet and points
    Users_Point = int(input('What is your Point?'))

    if(Users_Bet <= Total_chips): #conditional statement to validate that the users bet is less than the total chips in their bank
        Roll_Count = 1 #keeping track of how many rolls the user has left
        format = 4 #this is just to format our output below.
        while(Roll_Count < 6): #validating that the user hasn't gone above five rolls
            First_die = random.randint(1,6) #rolling a random value from 1 to 6
            Second_die = random.randint(1,6)
            Sum_of_Dices = First_die + Second_die
            print("\nRolling The Dice…")
            print("Roll number", Roll_Count, "of 5")
            print("The Values are:")
            print(First_die)
            print(Second_die)
            print("You Rolled:", Sum_of_Dices)
            print("Your Point is:", Users_Point)
            if(Sum_of_Dices == Users_Point): #checks to see if the sum of dices met the users point.
                print("Yay!! The SUM of your dices:", Sum_of_Dices, "Is EQUAL to your point:", Users_Point)
                print("You Win!!")
                print("The value of your bet has been doubled and added to your bank_amount!!")
                Users_Bet = Users_Bet + Users_Bet #doubling our bet and adding it to our total chpis
                Total_chips += Users_Bet
                Roll_Count = 9 #sets rollcount to 9 so loop breaks
            else:
                if(Roll_Count == 5): #checks if user is on their last roll
                    print("You have 0 more Rolls to make your point")
                    print("Sorry, You lost your bet:-" + str(Users_Bet))
                    Total_chips -= Users_Bet
                    Roll_Count = 9 #sets rollcount to 9 so loop breaks
                else:
                    print("You did not make your point.")
                    print("You have", format, "more Rolls to make your point.")
                    Roll_Count += 1
                    format -= 1
    else: #checks If the users bet is greater than their bank amount
        print("\nYou Cannot place a bet higher than the amount in your bank account")
        print("Your Bank account has:", Total_chips)
        print("You placed a bet of:", Users_Bet)
        break
    Decision = input("\nRoll the Dice 5 times Again? Enter yes or no:")
    while(Decision.upper() != "YES") and (Decision.upper() != "NO"):  #Loop to handel invalid input
        Decision = input("Invalid input!!\nEnter 'yes' or 'no' to Roll the Dice 5 times Again:")
        print("\n")
