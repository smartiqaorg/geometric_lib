import math


def area(r):
    """
    Returns the area of the circle.

            Parameters:
                r (int): radius of the circle
            Returns:
                (float): area of the circle

        Example:
            input -> 3 (r)
            output -> 28.274333882308138 (π * r * r)
    """

    if type(r) == str:
        return "Error: Invalid Length"

    if type(r) == float:
        return "Error: Not Integer Length"

    if r == 0:
        return "Error: Zero Length"

    if r < 0:
        return "Error: Negative Length"

    return math.pi * r * r


def perimeter(r):
    """
    Returns the perimeter of the circle.

            Parameters:
                r (int): radius of the circle
            Returns:
                (float): perimeter of the circle

        Example:
            input -> 3 (r)
            output -> 18.84955592153876 (2 * π * r)
    """

    if type(r) == str:
        return "Error: Invalid Length"

    if type(r) == float:
        return "Error: Not Integer Length"

    if r == 0:
        return "Error: Zero Length"

    if r < 0:
        return "Error: Negative Length"

    return 2 * math.pi * r

