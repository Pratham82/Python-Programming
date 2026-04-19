# Retrunring single function inside a function
# Cleaning method is returning Special_cleaning method
# So if we assign Cleaning method to any variable it will return Special_cleaning()
def Cleaning():
    
    def Special_cleaning():
        return 'Perform special cleaning'
    
    return Special_cleaning


obj1 = Cleaning()
print("obj1: ",obj1)
print(obj1())