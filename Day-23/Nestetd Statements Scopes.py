'''
LEGB Rule
L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
'''

var1 = "This is global declaration"

def m1():
    # using the global keyword we can change the values and affect the global variable
    global var1
    var1 = "This is Local assignment"    
    print (var1)
    def m2():
        var1='This is enclosing reassignment of local variable'
        print(var1)
    m2()

print("Value of var1: ",var1)
m1()
print("Value of var1: ",var1)

# But rather than using global keywords directly we should take the global variable as an argument 
# and assigning the value we want and in the end reassigning the changed value
var2 = "This is global declaration 2"

def m3(var2):
    var2 = "New value"    
    print ("New value of var2 is: ",var2)
    return var2
    

print("Value of var2: ",var2)
var2 = m3(var2)
# That's why here the global value of var2 is changed to the local declaration value
print(var2)