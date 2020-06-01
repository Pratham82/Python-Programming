people  = 30 
cars = 10
trucks = 15

if cars >  people:
    print("We should take the cars.")
elif cars  < people:
    print("We should not take the cars.")
else:
    print(" We cant' decide.")

if trucks > cars:
    print("Thats's too many cars.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine let's stay home then.")