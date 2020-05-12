class Dog():
    # Defining class object attribute
    # Same for any instance of a class
    species = "Mammal"
    
    # Initializer / Instance Attributes
    def __init__(self, name,breed,weight):
        # Attributes(characterstics of our objects)
        # We take it as an argument
        # And assign it using self.attribute_name
        self.name = name
        self.breed =  breed
        self.weight = weight
        

# Creating attribute
# Attributes should be the same order of the init method
# Here we are creating new instacne of a class(also called instantiing) and saving that instance in an object
my_dog = Dog(name="russ",breed ="husky",weight="40kg")

print("Type of my_dog",type(my_dog))

# Getting the attribute values  
print("breed of my dog: ",my_dog.breed)
print("Name of my dog: ", my_dog.name)
print("Weight of my dog: ",my_dog.weight)
print("Class obj attr: ", my_dog.species)

# Notes about init and self:
# init is similar to constructor of a class, and it will be called automatically when we create an instance of a class
# self keyword represents the instance of the object intself.(We can change to any name but its a convention to write self. 
# self: it connects the method with instance of the class, and it allows us to refer itself 
# After the self keyword we pass in the attributes that we want our user tp define
# Whenever self keyword is used in the method, it will represents to that perticular instance
# we can set any attribute name after self keyword but it is suggested that we used same name as used in init method parmeter and while assigning self.attribute name
        # self.attribute_name = my_breed

