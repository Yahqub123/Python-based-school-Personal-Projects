#Student Name: Yahqub Kehinde Oyebola

print("Welcome to the Compound Interest Calculator.")
Principal = float(input("Please enter the initial amount of your investment:\t")) #P varaiable
Rate = float(input("Please enter the interest rate (e.g., '.03' for 3% interest):\t"))  #r varaible
Time = int(input("Please enter the number of years for the investment:\t")) #t varaible
Num_of_compoundings = int(input("Please enter the number of compoundings per year:\t")) #n varaible

New_balance = Principal * (1 + (Rate/Num_of_compoundings)) ** (Num_of_compoundings * Time)  #P' varable
print("Original Investment:     $", format(Principal, ",.2f"))
print("Interest Earned:         $", format(New_balance - Principal, ",.2f")) #Subtacting (P'-P) to get our interest Earned.
print("Final Balance:           $", format(New_balance, ",.2f"))