class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


animal1  = Animal()

animal1.whoAmI()
animal1.eat()

# Inheriting properties from animal
# Inheritance is the Object oriented proramming concept where we reuse the propertry of a class which is already defined 
# It is used for code reusability.
# Inheritance enables us to define a class that takes all the functionality from parent class and allows us to add more. In this article, you will learn to use inheritance in Python.


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    # Overriding methods from the base/parent class
    def whoAmI(self):
        print("I am a dog")

    # Adding in different methods
    def dig(self):
        print("Dog is digging a ditch")

dog1 = Dog()

# Here we can use methods from animal class directly
dog1.whoAmI()
dog1.eat()
dog1.dig()
