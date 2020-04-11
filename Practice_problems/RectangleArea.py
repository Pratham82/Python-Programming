def RectangleArea(x,y):
    Area = x * y
    print("Area of rectangle: ", Area)
# here using list comprehension for taking input form the user
l,b =[int(x) for x in input("Enter length and breadth").split()]

#l,b = int(input("Enter sides of rectangle: ").split())
#l = int(input("Enter length of rectangle: "))
#b = int(input("Enter breadth of rectangle: "))
RectangleArea(l,b)