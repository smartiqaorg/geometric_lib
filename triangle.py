def area(a, h):
    """
    Returns the area of the triangle.

            Parameters:
                a (int): base of the triangle
                h (int): height of the triangle
            Returns:
                (int): area of the triangle

        Example:
            input -> 5, 4 (a, h)
            output -> 10 (a * h / 2)
    """

    if type(a) == str or type(h) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(h) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (h == 0):
        return "Error: Zero Length"

    if (a < 0) or (h < 0):
        return "Error: Negative Length"

    return a * h / 2


def perimeter(a, b, c):
    """
    Returns the perimeter of the triangle.

            Parameters:
                a (int): first side of the triangle
                b (int): second side of the triangle
                c (int): third side if the triangle
            Returns:
                (int): perimeter of the triangle

        Example:
            input -> 1, 2, 3 (a, b, c)
            output -> 6 (a + b + c)
    """

    if type(a) == str or type(b) == str or type(c) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float or type(c) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0) or (c == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0) or (c < 0):
        return "Error: Negative Length"

    return a + b + c 
