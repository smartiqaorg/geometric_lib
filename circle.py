import math


def area(r):
    if r <= 0:
        raise ValueError()
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        raise ValueError()
    return 2 * math.pi * r

