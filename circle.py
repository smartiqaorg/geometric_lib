import math


def area(r):
    """
    This function calculates the area of a circle based on the given radius.

    Formula:
    Area = π * r ^ 2
    
    Parameters:
    - r (float): The radius of the circle.
    
    Return value:
    - area(float): The area of a circle.
    """
    return math.pi * r * r


def perimeter(r):
    """
    This function calculates the perimeter of a circle based on the given radius.
    
    Formula:
    Circle: P = 2πR

    Parameters:
    - r(float): The radius of the circle.
    
    Return value:
    - perimeter(float): The perimeter of the circle.
    """
    return 2 * math.pi * r

