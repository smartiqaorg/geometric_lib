import math


def area(r):
    '''
    The area(r) function calculates the area of a circle given its radius r. 
    It uses the mathematical constant π (pi) to perform the calculation using the formula:
    
    Area = π * r^2

    Where:
    - Area is the area of the circle.
    - π (pi) is a mathematical constant approximately equal to 3.14159.
    - r is the radius of the circle.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    The perimeter(r) function calculates the perimeter (circumference) of a circle given its radius r. 
    It uses the mathematical constant π (pi) to perform the calculation using the formula:

    Perimeter = 2 * π * r

    Where:
    - Perimeter is the perimeter (circumference) of the circle.
    - π (pi) is a mathematical constant approximately equal to 3.14159.
    - r is the radius of the circle.
    '''
    return 2 * math.pi * r

