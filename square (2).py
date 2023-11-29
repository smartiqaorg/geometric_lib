def area(a):
    if type(a) not in [int, float]:
        raise TypeError('Values must be a numbers only')
    if a < 0:
        raise ValueError('Values can not be negative')
    return a * a


def perimeter(a):
    if type(a) not in [int, float]:
        raise TypeError('Values must be a numbers only')
    if a < 0:
        raise ValueError('Values can not be negative')
    return 4 * a
