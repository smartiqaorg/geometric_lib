def area(a, h):
    """
    Calculates the area of a triangle based on its base and height.

    Parameters:
        a: The base length of the triangle.
        h: The height dropped onto the base.

    Return value:
        The area of the triangle, calculated using the formula S = a·h / 2.

    Example input and output:
        >>> area(6, 4)
        12.0
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Calculates the perimeter of a triangle based on its three sides.

    Parameters:
        a: The first side of the triangle.
        b The second side of the triangle.
        c: The third side of the triangle.

    Return value:
        The perimeter of the triangle, calculated using the formula P = a + b + c.

    Example input and output:
        >>> perimeter(3, 4, 5)
        12
    """
    return a + b + c