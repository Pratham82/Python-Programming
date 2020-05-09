class Mobile():
    def __init__(self,brand):
        self.brand = brand 
        
    # Here we are creating abstract method which needs to be implemented in any subclass or it will cause an error 
    # This is similar to abstract classes and method concept in java
    # Mbile is an asbtract class which does not have method implementation we have to give method implementation using a subclass
    def brand_name(self):
       raise NotImplementedError("Subclass must implement this abstract method")

# When we try to call this method it will not work becuase its an abstract mehtod and it has no implementation in order to use this method we have to implement it in a sbuclass
m1 =Mobile('tester')
#.brand_name()

class Samsung(Mobile):
    def __init__(self,brand):
        self.brand = brand

    def brand_name(self):
        print("This is samsung mobile")


s1 = Samsung("samsung")
s1.brand_name()
