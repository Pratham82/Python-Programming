# Geometry 3: Perimeter of a Triangle
# Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.
#
# Examples
# perimeter( [ [15, 7], [5, 22], [11, 1] ] ) ➞ 47.08
import math


def perimeter(lst):
    # Distance formula
    find_distance = lambda a, b: pow(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2), 0.5)

    # Getting the coordinates from the given 2d array
    P1, P2, P3 = lst
    return round(sum(find_distance(*c) for c in [(P1, P2), (P1, P3), [P2, P3]]), 2)


def perimeter_2(lst):
    # Getting points from the array
    p1, p2, p3 = lst

    # Getting each coordinates from the point that we took
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Now we will find the distance between each point
    # point1 - point2
    distance_p1_p2 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    distance_p2_p3 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    distance_p3_p1 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    return round(sum([distance_p1_p2, distance_p2_p3, distance_p3_p1], 0), 2)


print(perimeter([[15, 7], [5, 22], [11, 1]]))
print(perimeter_2([[15, 7], [5, 22], [11, 1]]))
