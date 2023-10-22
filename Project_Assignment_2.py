#Name: Yahqub Kehinde A. Oyebola
#Objective: Building a simple calculator. This calculator gets a list of numbers and performs different functions on these
#set of numbers.

import math #imports the python module called math

def main():
    i = 2 #variable to manipulate our printed output
    temp_list = [] #list to hold the numbers the user wants to work with and perform different calculations.
    Numbers = float(input("Welcome To Our Calculator!\nPlease enter the set of Numbers you intend to work with or Enter '0' when done."))
    while Numbers != 0: #condition to see if the user wants to stop entering numbers
        temp_list.append(Numbers)
        Numbers = float(input(f"Enter your {i} Number or Enter 0 to stop and excecute a calculation: "))
        i += 1

    choice = input("\nWhat would you like to do to these set of Numbers?\nEnter 1 to ADD the Numbers.\nEnter 2 to "
                   "SUBTRACT the Numbers\nEnter 3 to MULTIPLY the Numbers.\nEnter 4 to get the Average of the Numbers."
                   "\nEnter 5 to get the square root of a number.\nEnter 'q' to quit.")

    while choice.lower() != 'q' and len(temp_list) != 0: #validating the users choice and acting accordingly.
        if choice == '1':
            Add_Numbers(temp_list) #calls the function to add our list.
        elif choice == '2':
            sub_Numbers(temp_list) #calls the function to subtract the values in our list
        elif choice == '3':
            Mul_Numbers(temp_list) #calls the function to multiply the values in our list
        elif choice == '4':
            get_AVG(temp_list) #calls the function to get the average of the values in our list
        elif choice == '5':
            Square_Root() #calls the function to get the square root of numbers.
        else:
            print("The choice you entered is Invalid. Please enter a correct choice")

        choice = input("\nWhat would you like to do to these set of Numbers?\nEnter 1 to ADD the Numbers.\nEnter 2 to "
                       "SUBTRACT the Numbers\nEnter 3 to MULTIPLY the Numbers.\nEnter 4 to get the Average of the Numbers."
                       "\nEnter 5 to get the square root of a number.\nEnter 'q' to quit.")

def Square_Root(): #Function to get the square root of a number
    value = float(input("Please Enter the integer in which you want to get its square root:"))
    return print(f"\nThe square root of {int(value)} is:",math.sqrt(value)) #uses the sqrt function in the math module
                                                                            # to get our square root.

def Add_Numbers(temp_list): #Function to get the sum of our Numbers
    print("The sum of all your numbers is:",sum(temp_list)) #we use the built in sum fuction to get the sum of our list
    return temp_list

def sub_Numbers(temp_list): #Function to subtract all the numbers in our list.
    position = 0 #keeps tract of the position of elements in our list
    total = 0
    while position < temp_list.index(temp_list[-1]): #condition to make sure our position does not go out of range.
        if position == 0: #makes sure the first element is subtracted from the second and stores the result in total
            first = temp_list[position]
            second = temp_list[position + 1]
            total= first - second
        else:
            total = total -  temp_list[position + 1] #Then subtracts the next value in the list from the total.
        position += 1
    print("The subtracted total is:", total)
    return temp_list

def Mul_Numbers(temp_list): #Function to multiply all the values in our list
    position = 0
    total = 0
    while position < temp_list.index(temp_list[-1]): #loop to basically multiply the first and second elements and store it in total
        if position == 0:
            first = temp_list[position]
            second = temp_list[position + 1]
            total = first * second
        else:
            total = total * temp_list[position + 1] #then we multiply total by the next element in the list.
        position += 1
    print("The total of all the numbers multiplied is:", total)
    return temp_list

def get_AVG(temp_list): #Function to get the average of values in our list.
    average_of_values = sum(temp_list)/len(temp_list) #divides the sum of elements by the total to get the average.
    print("The average of all the Numbers is:", average_of_values)
    return temp_list

main() #calls our main function.