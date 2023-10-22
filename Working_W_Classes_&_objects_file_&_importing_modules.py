'''In this file, we are going to import different python packages and our pre-deifined classes from our 'classes_and_
_objects_training.py' file and work with the classes in any way that we want. For the first thing, I am GOING TO CREATE
MULTIPLE DOG OBJECTS AND STORE THEM IN A LIST. This way, I can keep track and iterate through objects easily and keep
them uniformed.'''

import Classes_And_Objects_Training as CT #imports everything in this file to my new program.

password = input("Please Enter a password to work with this program.")
while password.lower() != 'kenny':
    password = input("\nYou entered a wrong password!!\nPlease Enter a new password to work with this program.")

choice = input("\nWelcome to my lovely classes program!!! What would you like to do today?\nEnter '1' To CREATE "
               "MULTIPLE DOG OBJECTS AND STORE THEM IN A LIST.\nEnter '2' to print the information for each dog(object)"
               "in the list of dogs called 'Dog_List'\nEnter '3' to get the particular information about a particular dog"
               "(e.g Name,color e.t.c) in a certain position.\nEnter '4' to get the INDEX of a particular Dog using its"
               " info (I.e Name, Age e.t.c)\nEnter '5' to store all the information for all dogs in the list into a "
               "permanent file.\nEnter '0' to QUIT!!\n")

List_of_dogs = [CT.ob1] # List to store our dog objects and information about our dogs. Holds the first object called 'ob1'
                    #That was created in the Classes_And_Objects_Training.py file.
while choice != '0':
    if choice == '1':
        count = int(input("How many dogs would you like to create and add their information to the list of dogs: "))
        for i in range(count):
            print("\nEnter the information for dog", i+1, ":")
            Name = input("Enter the dog's Name: ")
            Age = int(input("Enter the dog's Age: "))
            Color = input("What's the color of the dog: ")
            Weight = float(input("How many pounds does the dog weigh: "))

            Dog_object = CT.dog(Name,Age,Color,Weight) #Creates a instance for our dog (A.K.A a dog object)
            List_of_dogs.append(Dog_object) #passes this object into a list and stores it in the list.

    elif choice=='2':
        for ob in List_of_dogs:
            print(ob.Print_Dog_info(),"\n") #prints the information of each dog in the list. This iterates through each position in
                                #our list of dog objects and for each dog at that certain position, the Print_Dog_info()
                                #function is called!! mind blowing innit.
    elif choice == '3':
        Information = input("What information about this dog would you like to know? (E.g Name,Age,color,Weight)")
        position = int(input("In what position in the list would you like for the info to be retrieved?")) - 1
        if Information.upper() == "NAME":
            print(List_of_dogs[position].Name)
        elif Information.upper() == "AGE":
            print(List_of_dogs[position].Age)
        elif Information.upper() == "COLOR":
            print(List_of_dogs[position].Color)
        elif Information.upper() == "WEIGHT":
            print(List_of_dogs[position].Weight)
        else:
            print("Our dogs do not have a '",Information,"' attribute")

    elif choice == '4':
        Information = input("Enter the attribute of the dog(E.g Name,Age,color,Weight) that you would like to know its"
                            "Index in the list.")
        value = input("Enter the attributes value: ")
        if Information.upper() == "NAME":
            for i in List_of_dogs:
                if i.Name == value:
                    position = i
                    print("The dog is located at position:", List_of_dogs.index(position))

        elif Information.upper() == "AGE": #Converts Entred info to upper case
            for i in List_of_dogs:
                if i.Age == int(value):
                    position = i
                    print("The dog is located at position:", List_of_dogs.index(position))

        elif Information.lower()=="color":
            for i in List_of_dogs:
                if i.Color == value:
                    position = i
                    print("The dog is located at position:", List_of_dogs.index(position))

        elif Information.upper() == "WEIGHT":
            for i in List_of_dogs:
                if i.Weight == float(value):
                    position = i
                    print("The dog is located at position:", List_of_dogs.index(position))
        else:
            print("Our Dogs do not have a '",Information,"' attribute")

    elif choice == '5':
        Del = "," #Delimeter to seperate our values.
        with open("File_For_My_Dogs_class.csv", 'a') as df: #df will stand for Dog's File.
            for i in List_of_dogs:
                df.writelines(i.Name+Del+str(i.Age)+Del+i.Color+Del+str(i.Weight)+Del+str(i.calculate_The_Dogs_Speed())+"\n")
                            #puts everything
                            #from the list into the file in that order. i in this case represents our dog object. So we
                            #read that as for object 1 get the Name,Age,Color,weight,and Dog_speed. we say it as i.name,
                            # i.age and so on.

    choice = input("\nWelcome to my lovely classes program!!! What would you like to do today?\nEnter '1' To CREATE "
               "MULTIPLE DOG OBJECTS AND STORE THEM IN A LIST.\nEnter '2' to print the information for each dog(object)"
               "in the list of dogs called 'Dog_List'\nEnter '3' to get the particular information about a particular dog"
               "(e.g Name,color e.t.c) in a certain position.\nEnter '4' to get the INDEX of a particular Dog using its"
               " info (I.e Name, Age e.t.c)\nEnter '5' to store all the information for all dogs in the list into a "
               "permanent file\nEnter '0' to QUIT!!\n")
