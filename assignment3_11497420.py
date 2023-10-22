#Name: Yahqub Oyebola
#Objective: Calculating the square root of a number using the Babylonian method

epsilon = 0.0001 #This is our epsilon variable that we use to check if our value is close enogh to the actual square_root value.
value = int(input("Enter a positive integer value: ")) #User enters their positive integer value
while value <= 0: #Loop To make the user input a new value ifthey enter any values less than or equal to zero
    print("Your number must be a positive integer. Please try again.\n")
    value = int(input("Enter a positive integer value: "))

Extimated_square_root = value
Extimated_square_root = abs((value/Extimated_square_root) - Extimated_square_root) #calculation of our Extimated_square_root

if Extimated_square_root < epsilon: #We are checking to see if our root value is less than the episilon to decided if it is "good enough"
        print("Value Square Root\n", value, "\t", format(value, ".3f"))
else:
    while Extimated_square_root > epsilon: #while our Extimated_square_root is greater than our episilon, keep recalculating for the root
        Extimated_square_root = ((value/Extimated_square_root) + Extimated_square_root)/2
        square_root = Extimated_square_root
        Extimated_square_root = abs((value/Extimated_square_root) - Extimated_square_root)
        if Extimated_square_root < epsilon: #If our value finally turns  out to be less, then print out our square_root
            print("Value Square Root\n", value, "\t", format(square_root, ".3f"))

