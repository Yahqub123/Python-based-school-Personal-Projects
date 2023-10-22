#Name: Sulaiman Taiwo Oyebola
#Project_goal: Creating a class of fractions and objects for this class.

#'upper' in this class refers to a fractions numerator
#'lower' in this class refers to a fractions denominator.

class Fraction: #This is how we define our fraction class.
    def __init__(self, Numerator, Denominator): #This is our constructor to initialize the variables of the class.
        self.upper = Numerator #assigns the passed in numerator to the classes actual numerator called upper.
        self.lower = Denominator #assigns the passed in denominator to the classes actual denominator called lower.

    def __add__(self, fraction_2): #This is our method to add two fraction objects.Fraction_2 refers to our other fraction(object)
        if self.lower == fraction_2.lower: #checks to see if the Denominator is the same so we can go straight to adding.
            sum = self.upper + fraction_2.upper
            best_denominator = self.lower #gets our common denominator
        else:
            num1 = self.upper * fraction_2.lower #num1 refers to our first numerator
            num2 = fraction_2.upper * self.lower #num2 refers to our second numerator
            best_denominator = self.lower * fraction_2.lower
            sum = num1 + num2

        return Fraction(sum,best_denominator)

    def __sub__(self, fraction_2): #This is our method to subtract two fraction objects.
        if self.lower == fraction_2.lower:
            best_denominator = self.lower
            sub = self.upper - fraction_2.upper
        else:
            best_denominator = self.lower * fraction_2.lower
            num1 = self.upper * fraction_2.lower
            num2 = fraction_2.upper * self.lower
            sub = num1 - num2

        return Fraction(sub,best_denominator)

    def invert_frac(self): #This is our method to invert a particular fraction
        upper = self.lower
        lower = self.upper
        return Fraction(upper,lower)

    def __mul__(self, fraction_2): #This is our method to multiply 2 fraction objects.
        numerator = self.upper * fraction_2.upper
        denominator = self.lower * fraction_2.lower
        return Fraction(numerator,denominator)


    def Fraction_to_float(self): #This is our method to convert a fraction to a float
        floated_value = float(self.upper / self.lower)
        return floated_value


    def __str__(self): #This prints our object as described below instead of displaying the objects register or memory position
        return str(self.upper) + "/" + str(self.lower)

First_Fraction= Fraction(4, 2) #Creates a object known as First_Fraction for the fraction class
Second_Fraction= Fraction(2, 15) #Creates a object known as First_Fraction for the fraction class

print("First_Fraction + Second_Fraction is:",First_Fraction + Second_Fraction) #Adding the First and Second Fraction
print("First_Fraction - Second_Fraction is:", First_Fraction - Second_Fraction ) #Subtracting our First and Second Fraction
print("First_Fraction * Second_Fraction is:", First_Fraction * Second_Fraction) #Multiplying our First and Second Fraction
print("First_Fraction converted to a float is:", First_Fraction.Fraction_to_float()) #Making First_Fraction a float
print("Second_Fraction converted to a float is:", Second_Fraction.Fraction_to_float()) #Making Second_Fraction a float
print("The Inverse of First_Fraction is:", First_Fraction.invert_frac()) #Inverting our First_Fraction
print("The Inverse of Second_Fraction is:", Second_Fraction.invert_frac()) #Inverting our Second_Fraction
