import math


def area(r):
    '''Returns the area of the circle.

            Parameters:
                r (int): radius of the circle
            Returns:
                (float): area of the circle
        
        Example:
            input -> 3 (r)
            output -> 28.274333882308138 (π * r * r)
    '''

    return math.pi * r * r


def perimeter(r):
    '''Returns the perimeter of the circle.

            Parameters:
                r (int): radius of the circle
            Returns:
                (float): perimeter of the circle
                
        Example:
            input -> 3 (r)
            output -> 18.84955592153876 (2 * π * r)
    '''

    return 2 * math.pi * r

