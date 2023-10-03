import math


def area(r):
    """
    Get a Radius of circle and return his area
    ------------------------------------------
    example of call: area(10) = 314
    """
    return math.pi * r * r


def perimeter(r):
    """
    Get a Radius of circle and return his perimeter
    -----------------------------------------------
    example of call: perimeter(10) = 68,2
    """
    return 2 * math.pi * r
