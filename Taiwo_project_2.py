#Name: Sulaiman Oyebola
#Goal: creating a calculator.
#class: INFO 4501

import math

def main():
    set_of_Numbers = [] #list to hold the numbers that the user enters
    num = int(input("How many numbers do you intend to work with:"))
    count = 1
    while count <= num : #loop to make the user enter the numbers then append them to our list
        value = int(input("Enter your "+str(count)+" Number:"))
        set_of_Numbers.append(value)
        count = count + 1

    menu = input("\nEnter 1 to SUBTRACT the Numbers\n"
                 "Enter 2 to ADD the Numbers.\n"
                 "Enter 3 to MULTIPLY the Numbers.\n"
                 "Enter 4 to get the Average of the Numbers.\n"
                 "Enter 5 to get the square root of a number.\n"
                 "Enter 'q' to quit.\n")
    if menu.lower() != 'q': #checks if the user doesn't quit then makes them eneter a 0 to execute their choice from above
        validate = int(input("Enter '0' to execute this choice:"))

    while menu.upper() != 'Q' and validate == 0: #executes the users demands.
        if menu == '1':
            print("All the numbers subtracted =", subtract(set_of_Numbers))
        elif menu == '2':
            print("Sum =",addition(set_of_Numbers))
        elif menu == '3':
            print("All the numbers multiplied =",multiplication(set_of_Numbers))
        elif menu == '4':
            print("Average of the numbers =",average(set_of_Numbers))
        elif menu == '5':
            Sqrt(set_of_Numbers)
        else:
            print("You entered a invalid choice")

        menu = input("\nEnter 1 to Subtract the Numbers\n"
                     "Enter 2 to Add the Numbers.\n"
                     "Enter 3 to Multiply the Numbers.\n"
                     "Enter 4 to get the AVG of the Numbers.\n"
                     "Enter 5 to calculate the square rooot of all the numbers.\n"
                     "Enter 'q' to quit.\n")
        if menu.lower() != 'q':
            validate = int(input("Enter '0' to execute this choice:"))

def Sqrt(set_of_Numbers): #Function to get the square root of all the numbers in the list
    for i in set_of_Numbers:
        print("Square root of",i,"=",math.sqrt(i)) #gets the  square root of each number in the list

def addition(set_of_Numbers):
    return sum(set_of_Numbers) #returns the sum of all the numbers in the list

def multiplication(set_of_Numbers): #Function to multiply all the values in the list
    pos = 0
    value = 0
    while pos < set_of_Numbers.index(set_of_Numbers[-1]): #loop to iterate through the list until the second to the last element
        if pos == 0: #checks if we are at position 0 in the list
            value = set_of_Numbers[pos] * set_of_Numbers[pos + 1]  #multiplies the first element in the list with the second
        else:
            value = value * set_of_Numbers[pos + 1] #multiples the value with the next element in the list
        pos += 1
    return value

def average(set_of_Numbers): #Getting the average of all the values in the list
    avg = sum(set_of_Numbers) / len(set_of_Numbers)
    return avg

def subtract(set_of_Numbers): #subtracts all the values in the list.
    pos = 0
    value = 0
    while pos < set_of_Numbers.index(set_of_Numbers[-1]):
        if pos == 0:
            value = set_of_Numbers[pos] - set_of_Numbers[pos + 1]
        else:
            value = value - set_of_Numbers[pos + 1]
        pos += 1
    return value

main()