def area(a):
    """
    Calculates the area of a square given the length of its side.

    Parameters:
        a (float): The length of the square's side.

    Return value:
        float: The area of the square.
        formula: S = a².

    Example input and output:
        >>> area(6)
        36
    """
    return a * a


def perimeter(a):
    """
    Calculates the perimeter of a square given the length of its side.

    Parameters:
        a (float): The length of the side of the square.

    Return value:
        float: The perimeter of the square.
        formula: P = 4a.

    Example input and output:
        >>> perimeter(4)
        16
    """
    return 4 * a