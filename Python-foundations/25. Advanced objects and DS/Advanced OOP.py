class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):
    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

# In this example, the derived classes did not need their own __init__ methods 
# because the base class __init__ gets called automatically
# if you do define an __init__ in the derived class, this will override the base


#* Multiple inheritance
class Computer:
    def __init__(self,battery):
        self.battery = battery

class Mac(Computer):
    def __init__(self, OS="MacOS", HW="proprietary",battery="LiIon"):
        self.OS = OS
        self.HW = HW
        self.battery = battery

    def run_mac_os(self):
        print("MacOS is running now")
    
    def mac_charge(self):
        print("Chargig via USB C")


class PC(Computer):
    def __init__(self, OS="Windows", HW="assembled", battery="LiAmber"):
        self.OS = OS
        self.HW = HW
        self.battery = battery

    def run_windows_os(self):
        print("Windows is running now")
    
    def pc_charge(self):
        print("Chargig via brick charger")

class hackintosh(Mac,PC):
    def __init__(self,OS = "Linux", HW="Assembled and modified", battery="Combined"):
        Mac.__init__(self, OS, HW, battery="LiIon")
        PC.__init__(self,OS,HW,battery="LiAmber")


hck1 = hackintosh()
print(hck1.HW)
print(hck1.OS)    
print(hck1.battery)    

hck1.mac_charge()
hck1.run_mac_os()
hck1.pc_charge()
hck1.run_windows_os()


#*  Super keyword
#* super() function provides a shortcut for calling base classes
#* it automatically follows Method Resolution Order.
class MyBaseClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
class MyDerivedClass(MyBaseClass):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z