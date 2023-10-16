import math


def area(r):
    '''Provides an area of the circle using its radius.

    print(area(5))
    Output: 78.53981633974483

    '''
    return math.pi * r * r


def perimeter(r):
    '''Provides perimeter of the circle using its radius.

    print(perimeter(5))
    Output: 31.41592653589793

    '''
    return 2 * math.pi * r
