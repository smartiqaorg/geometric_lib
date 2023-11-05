def area(a, b):
    """
    Returns the area of the rectangle.

            Parameters:
                a (int): first side of the rectangle
                b (int): second side og the rectangle
            Returns:
                (int): area of the rectangle

        Example:
            input -> 2, 3 (a, b)
            output -> 6 (a * b)
    """

    if type(a) == str or type(b) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0):
        return "Error: Negative Length"

    return a * b 


def perimeter(a, b):
    """
    Returns the perimeter of the rectangle.

            Parameters:
                a (int): first side of the rectangle
                b (int): second side og the rectangle
            Returns:
                (int): perimeter of the rectangle

        Example:
            input -> 2, 3 (a, b)
            output -> 10 (2 * (a + b))
    """

    if type(a) == str or type(b) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0):
        return "Error: Negative Length"

    return 2 * (a + b)
