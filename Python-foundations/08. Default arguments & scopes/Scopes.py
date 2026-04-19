"""
Scopes in python:
Local: Inside the current function
Enclosing: Inside enclosing function
Global: At the top level of the module
Built-in: In the special builtins module

* Scopes do not correspond to source blocks
"""
count=0
def show_count():
    print("Value of count is:",count)

# for setting the value of count globally we are setting the scope of variable to global 
def set_count(c):
    # count =c
    # setting the scope of variable count to global 
    global count
    count = c 

# Here the count's value will still be 0 because we are setting count in a local scope
show_count()


