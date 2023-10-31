import math

def area(r):
    '''
    Accepts circle radius (int), returns circle area (int).

        Example:
            input: 10
            output: 314.1592653589793
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Accepts circle radius (int), returns circumference (int).

            Example:
                input: 10
                output: 62.83185307179586
    '''
    return 2 * math.pi * r