# If the argument is not passed it will cause an error to solve this
# Wec can use a default value
def say_hello(name="Username"):
    return f"Hello {name}"


# For storing the value that we got from the function we have to use return keyword

result = say_hello("tetsing")
print(result)

