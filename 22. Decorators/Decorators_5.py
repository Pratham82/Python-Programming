def new_deco(og_func):
    # It will work as wrapper for our original function which is passed in
    def wrap_func():
        print("Extra functionality process before og function")        
        og_func()
        print("Extra functionality process after og function")        

    return wrap_func

# Now we will add a basic function inside the decorator function

def basic_func():
    print("This is basic function")
    
decorated_func = new_deco(basic_func)
print("decorated_func: ",decorated_func)
decorated_func()

print("-----------------------------")
# Easier and suggested way to decorate a function           
# @ with name of decorator func
# basically when we write @decorator_func top of any function 
# It will be passed inside the decorator function
# For removing decorator just comment it out
@new_deco 
def basic_func():           
    print("This is basic function")

basic_func()
