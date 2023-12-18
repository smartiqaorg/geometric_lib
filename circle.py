import math

def area(r):
    '''
    Accepts circle radius (int), returns circle area (int).

        Example:
            input: 10
            output: 314.1592653589793
    '''
    if r >= 0:
        return math.pi * r * r
    return 'incorrect input'


def perimeter(r):
    '''
        Accepts circle radius (int), returns circumference (int).

            Example:
                input: 10
                output: 62.83185307179586
    '''
    if r >= 0:
        return 2 * math.pi * r
    return 'incorrect input'