class PC():
    OS = "Windows" # This will be the class object attibute it will be same of any instance of a class
    
    def __init__(self,CPU,Motherboard,RAM,HDD,GFX):
        self.CPU = CPU
        self.Motherboard = Motherboard
        self.RAM = RAM
        self.HDD = HDD
        self.GFX = GFX
 
    # Methods: similar to operations/actions
    # self parameter will connect the PC instance to compute

    # Method without any extra arguments
    def compute(self):
        print(f"Computation info given by ")          

    # Method with attribute provided
    def compute2(self):
        print(f"This is compute method with {PC_build_2020.CPU} CPU")

    # Parameterized methods
    def compute3(self,customer_name):
        print (f"This {PC_build_2020.CPU} belongs to {customer_name}")


PC_build_2020 = PC(CPU= "i9 9990K", Motherboard= "B3650" ,RAM= "16 GB",HDD = "2TB SSD", GFX = "RTX 2080 super")

print("OS: ", PC_build_2020.OS)
print("Specs of PC: ")
print("\nCPU: ",PC_build_2020.CPU,"\nMotherboard: ",PC_build_2020.Motherboard,"\nRAM: ",PC_build_2020.RAM, "\nHDD: ",PC_build_2020.HDD, "\nGFX: ",PC_build_2020.GFX)

# Calling method
PC_build_2020.compute()

# Calling method 2
PC_build_2020.compute2()

# Calling method 3 
PC_build_2020.compute3("Prathamesh")
