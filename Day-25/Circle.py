class Circle_1:
  
    pi = 3.14 # Class oject attribute, same for every instances
    
    def __init__(self,radius=1):   # here 1 is the default value for raduius and it will be used whn nothing is provided
        self.radius = radius

        # Wec an also create an attibute without the parameter call
        self.area = radius* radius* 2* Circle_1.pi   #self.pi
        # Here intead of self.pi we can also use Circle_1.pi because pi ina class object attribute

    def circumference(self): 
        return "Circumference of the circke is: ",self.radius* self.pi*2

circle_new = Circle_1(23)
print("Value of PI: ",circle_new.pi)

# Calling method

print(circle_new.circumference())

print("Area of circle: ", circle_new.area)
     
