
"""
concept:
r^2 = (x-h)^2 + (y-k)^2 where h and k are the coordinate for the center of the circle
radius r = sqrt(x^2 + y^2)
"""
from math import sqrt
def score(x, y):
    x, y = abs(x), abs(y)
    outer_circle = 10
    middle_circle = 5
    inner_circle = 1
    points = 0
    radius = sqrt((x**2)+(y**2))
    if radius > inner_circle and radius<=middle_circle:
        points+=5
        return points
    elif radius>middle_circle and radius<= outer_circle:
        points+=1
        return points
    elif radius >= 0 and radius <= inner_circle:
        points+=10
        return points
    else:
        return points