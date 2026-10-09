import math

def area(r):
    '''
    Calculates the area of a circle.

    Parameters:
        r (int/float): The radius of the circle.

    Returns:
        float: The area of the circle.

    Example:
        >>> area(5)
        78.53981633974483
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Calculates the perimeter (circumference) of a circle.

    Parameters:
        r (int/float): The radius of the circle.

    Returns:
        float: The perimeter of the circle.

    Example:
        >>> perimeter(5)
        31.41592653589793
    '''
    return 2 * math.pi * r