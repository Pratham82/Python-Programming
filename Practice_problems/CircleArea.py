from math import pi
def CircleArea(r):
    Area = r**2 *pi
    print("Area of circle is: ", Area)
c = float(input("Enter the radius of circle: "))
CircleArea(c)
