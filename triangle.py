def area(a, h):
    '''
    Calculates the area of a triangle.

    Parameters:
        a (int/float): The base of the triangle.
        h (int/float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> area(5, 10)
        25.0
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Calculates the perimeter of a triangle.

    Parameters:
        a (int/float): The first side of the triangle.
        b (int/float): The second side of the triangle.
        c (int/float): The third side of the triangle.

    Returns:
        int/float: The perimeter of the triangle.

    Example:
        >>> perimeter(3, 4, 5)
        12
    '''
    return a + b + c



