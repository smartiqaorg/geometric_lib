def area(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('Values must be a numbers only')
    if a < 0 or b < 0:
        raise ValueError('Values can not be negative')
    return a * b

def perimeter(a, b):
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('Values must be a numbers only')
    if a < 0 or b < 0:
        raise ValueError('Values can not be negative')
    return (a + b) * 2

