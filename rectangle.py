def area(a, b):
    '''
    Calculates the area of a rectangle.

    Parameters:
        a (int/float): The length of the rectangle.
        b (int/float): The width of the rectangle.

    Returns:
        int/float: The area of the rectangle.

    Example:
        >>> area(5, 10)
        50
    '''
    return a * b

def perimeter(a, b):
    '''
    Calculates the perimeter of a rectangle.

    Parameters:
        a (int/float): The length of the rectangle.
        b (int/float): The width of the rectangle.

    Returns:
        int/float: The perimeter of the rectangle.

    Example:
        >>> perimeter(5, 10)
        30
    '''
    return 2 * (a + b)