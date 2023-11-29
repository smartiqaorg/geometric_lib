import math

def area(r):
    if type(r) not in [int, float]:
        raise TypeError('Radius must be a number only')
    if r < 0:
        raise ValueError('Radius can not be negative')
    return math.pi * r * r

def perimeter(r):
    if type(r) not in [int, float]:
        raise TypeError('Radius must be a number only')
    if r < 0:
        raise ValueError('Radius can not be negative')
    return 2* math.pi * r
print(area(-5))
