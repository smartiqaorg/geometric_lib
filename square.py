
def area(a):
    """
    Returns the area of the square.

            Parameters:
                a (int): side of the square
            Returns:
                (int): area of the square

        Example:
            input -> 2 (a)
            output -> 4 (a * a)
    """

    if type(a) == str:
        return "Error: Invalid Length"

    if type(a) == float:
        return "Error: Not Integer Length"

    if a == 0:
        return "Error: Zero Length"

    if a < 0:
        return "Error: Negative Length"

    return a * a


def perimeter(a):
    """
    Returns the perimeter of the square.

            Parameters:
                a (int): side of the square
            Returns:
                (int): perimeter of the square

        Example:
            input -> 2 (a)
            output -> 8 (4 * a)
    """

    if type(a) == str:
        return "Error: Invalid Length"

    if type(a) == float:
        return "Error: Not Integer Length"

    if a == 0:
        return "Error: Zero Length"

    if a < 0:
        return "Error: Negative Length"

    return 4 * a
