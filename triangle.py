def area(a, h):
    if type(a) not in [int, float] or type(h) not in [int, float]:
        raise TypeError('Values must be a numbers only')
    if a < 0 or h < 0:
        raise ValueError('Values can not be negative')
    return a * h / 2

def perimeter(a, b, c):
    if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
        raise TypeError('Values must be a numbers only')
    if a < 0 or b < 0 or c < 0:
        raise ValueError('Values can not be negative')
    return a + b + c