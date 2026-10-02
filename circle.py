import math


def area(r):
    """
    Calculates the area of a circle given its radius.

    Parameters:
        r (float): The radius of the circle.

    Return value:
        float: The area of the circle.
        formula: S = πR².

    Example input and output:
        >>> area(5)
        78.53981633974483
    """
    return math.pi * r * r

def perimeter(r):
    """
    Calculates the circumference of a circle given its radius.

    Parameters:
        r (float): The radius of the circle.

    Return value:
        float: The circumference.
        formula P = 2πR.

    Example input and output:
        >>> perimeter(5)
        31.41592653589793
    """
    return 2 * math.pi * r