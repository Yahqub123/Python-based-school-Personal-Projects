#Name: Yahqub Kehinde A. Oyebola
#Objective: Creating a class of Fractions and working with Fraction objects.

class Fraction: #defining our fraction class.
    def __init__(self, Numerator, Denominator): #constructors to initialize the variables of the class.
        self.numerator = Numerator
        self.denominator = Denominator

    def Add_Fractions(self,object): #Function to add 2 fraction objects. Takes another object as a parameter
        if self.denominator == object.denominator:
            common_denominator = self.denominator
            sum = self.numerator + object.upper
        else:
            common_denominator = self.denominator * object.getdenomenator()
            numerator_1 = self.numerator * object.getdenomenator()
            numerator_2 = object.getnumerator() * self.denominator
            sum = numerator_1 + numerator_2

        return Fraction(sum,common_denominator)

    def Subtract_Fractions(self,object): #Function to subtract 2 fraction objects. Takes another object as a parameter
        if self.denominator == object.getdenomenator():
            common_denominator = self.denominator
            sub = self.numerator - object.getnumerator()
        else:
            common_denominator = self.denominator * object.getdenomenator()
            numerator_1 = self.numerator * object.getdenomenator()
            numerator_2 = object.getnumerator() * self.denominator
            sub = numerator_1 - numerator_2

        return Fraction(sub,common_denominator)

    def Multiply_Fraction(self,object): #Function to multiply 2 fraction objects. Takes another object as a parameter
        numerator = self.numerator * object.getnumerator()
        denominator = self.denominator * object.getdenomenator()
        return Fraction(numerator,denominator)

    def Inverting_Fraction(self): #Function to invert a fraction
        Frac_numerator = self.denominator
        Frac_denominator = self.numerator
        return Fraction(Frac_numerator,Frac_denominator)

    def Converting_Fraction_To_Float(self): #Function to convert a fraction to a float
        return float(self.numerator/self.denominator)

    def getnumerator(self): #Function to get the numerator of a Fraction object
        return self.numerator

    def getdenomenator(self): #Function to get the denominator of a Fraction object
        return self.denominator

    def __str__(self): #Function to define how I want my Fraction objects to be printed to the screen.Simpliest form included
        return str(self.numerator) + "/" + str(self.denominator) + " simplified to: "+ str(self.numerator/self.denominator)

Frac_1= Fraction(7, 10) #Creates a fraction object known as fraction_1
Frac_2= Fraction(9, 20) #Creates another fraction object to represent another fraction.

print(Frac_1)
print(Frac_2)
print("The Numerator for Fraction_1 is:", Frac_1.getnumerator()) #Getting the Numerator of Frac_1 using our getnumerator() method
print("The denominator for Fraction_1 is:", Frac_1.getdenomenator()) #Getting the Demonimator of Frac_1
print("The Numerator for Fraction_2 is:", Frac_2.getnumerator()) #Getting the Numerator of Frac_2 using our getnumerator() method
print("The Denominator for Fraction_2 is:", Frac_2.getdenomenator()) #Getting the Denominator of Frac_2
print("Fraction_1 + Fraction_2 is:", Frac_1.Add_Fractions(Frac_2)) #Adding Frac_1 and Frac_2. Passing Frac_2 as a parameter
print("Fraction_1 - Fraction_2 is:", Frac_1.Subtract_Fractions(Frac_2)) #Subtracting Frac_2 from Frac_1
print("Fraction_1 * Fraction_2 is:", Frac_1.Multiply_Fraction(Frac_2)) #Multiplying Frac_1 and Frac_2
print("The Inverse of Fraction_1 is:", Frac_1.Inverting_Fraction()) #Inverting Frac_1 by calling the method on our object
print("The Inverse of Fraction_2 is:", Frac_2.Inverting_Fraction()) #Inverting Frac_2
print("Fraction_1 converted to a float is:", Frac_1.Converting_Fraction_To_Float()) #Converting Frac_1 to a float
print("Fraction_2 converted to a float is:", Frac_2.Converting_Fraction_To_Float()) #Converting Frac_2 to a float