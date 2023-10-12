import math


def area(r):
    '''Provides an area of the circle using its radius.'''
    return math.pi * r * r


def perimeter(r):
    '''Provides perimeter of the circle using its radius.'''
    return 2 * math.pi * r


k = 1
for i in range(64):
    print(i, k)
    k *= 2