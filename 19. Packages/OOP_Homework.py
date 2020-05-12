# Problem 1
class Line():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return ((x1-y1)**2 + (x2-y2)**2) *0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return (y2-y1)/(x2 -x1)

co1 = (3,2)
co2 = (8,10)

li1 = Line(co1,co2)
print(li1.distance())
print(li1.slope())

# Problem 2 

class Cylinder():
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.radius**2 *self.height

    def surface_area(self):
        return (2 * Cylinder.pi *self.radius *self.height) + (2 * Cylinder.pi* self.radius**2)

c1 = Cylinder(2, 3)
print(c1.volume())
print(c1.surface_area())

