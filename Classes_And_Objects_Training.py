'''In this section, I am going to import some pre-defined python packages to this file so I can use everything in this
files in my new python file. basically #include in c++. I am also going to practice how to use classes and objects in
my programs. With all that being said, Let's get right to it....
    So for my first class example, I am going to create a 'DOG' class that is going to have several attributes that
basically describes our typical dogs. These attributes will basically describe the dog's breed, color, age, weight,
height, and Name. This is basically the point of classes and objects. We could put all this information in a list or
dictionary or any data structure really but it'd be quite difficult to map all of these information all together. That's
why we use classes to define an entity in such instances. If we were to use a list, we might have to nested list so much
to the point whereby it get's really complicated. With classes however, acessing and defining these attributes have been
made much easier. We create an 'Object' for the class to represent a INSTANCE of the class. In this example, each object
represents a different dog. For every object of a class that you create, the object represents the instance of the class
You will see how this works in a bit.'''

class dog: #Creates a class. 'Class' is the keyword and 'dog' is the name of the class
    #Now we are going to create something called a default constructor to initialize all our variables for this class.
    #This constructor,for example, sets our name that was passed in to the variable called name.All is shown below
    #We often use constructors to define and intialize our variables in the class. Basically anything that you want
    #intialized or done the MOMENT an 'object' is created is done with a constructor. Constructors however are not
    #Compulsory. You can have just regular variables or functions(called methods).

    Brown_dogs_eating_rates_per_minute = 20 #creates variables in the class.
    White_dogs_eating_rates_per_minute = 39  #varaiable for calculating the speed of a white colored dog.
    Gray_dogs_eating_rates_per_minute = 17
    Unrecognized_dogs_eating_rates_per_minute = 5

    def __init__(self,name,age,color,weight):#This is a const with our varaibles to be passed in and defined
        self.Name = name #'self' basically refers to the object itself. So read this as ''The name of this object is equal
        self.Age = age #to the name that was passed in as a parameter.'' It basically assigngs passed in values to the
        self.Color = color #object itself. That is what we are doing for all the variables in this constructor function.
        self.Weight = weight

    def calculate_The_Dogs_Speed(self):
        if self.Color == "brown":
            Dogs_speed = (self.Weight * self.Brown_dogs_eating_rates_per_minute)/2
        elif self.Color == "white":
            Dogs_speed = (self.Weight * self.White_dogs_eating_rates_per_minute)/2
        elif self.Color == "gray":
            Dogs_speed = (self.Weight * self.Gray_dogs_eating_rates_per_minute)/2
        else:
            Dogs_speed = (self.Weight * self.Unrecognized_dogs_eating_rates_per_minute)/2
        return Dogs_speed

    def Print_Dog_info(self): #self refers to the object itself thats why we need it in all our methods(functions)
        print("The Name of the dog is:", self.Name)
        print("The Age of the dog is:", self.Age) #returns the content of the age variable of the object.
        print("The Color of the dog is:", self.Color) #basically returns what color the dog is
        print("The Weight of the dog is:", self.Weight) #gets the weight of the object.
        print("The speed of our dog is:", self.calculate_The_Dogs_Speed()) #calls the dog speed function.

#############################   CREATING OUR FIRST OBJECT OF A CLASS ##################################################

ob1 = dog("Yahqub Oyebola",20,"gray",150) #This is how you create an object for a class. Pass in all the required
#ob1.Print_Dog_info()                      # constructor info(if any) Then assign it to a variable to make it easier to
                                          # work with and access. In this line, we are calling the print_dog_info_info()
                                          #function(method) that every object in the class has access to. The ob1.print_
                                          #Dog_info() basically prints out the information for object 1.
