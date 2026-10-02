def area(a, b):
    """
    Calculates the area of a rectangle based on its sides.

    Parameters:
        a : The hight of the rectangle.
        b : The width of the rectangle.

    Return value:
        The area of the rectangle, calculated using the formula S = a·b.

    Example input and output:
        >>> area(3, 5)
        15
    """
    return a * b


def perimeter(a, b):
    """
    Calculates the perimeter of a rectangle based on its sides.

    Parameters:
        a : The hight of the rectangle.
        b : The width of the rectangle.

    Return value:
        The perimeter of a rectangle, calculated using the formula P = 2·(a + b).

    Example input and output:
        >>> perimeter(3, 5)
        16
    """
    return 2 * (a + b)



    def area(a):
    """
    Calculates the area of a square given the length of its side.

    Parameters:
        a : The length of the square's side.

    Return value:
        The area of the square, calculated using the formula S = a².

    Example input and output:
        >>> area(6)
        36
    """
    return a * a