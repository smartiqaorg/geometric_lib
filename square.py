def area(a):
    if a <= 0:
        raise ValueError()
    return a * a


def perimeter(a):
    if a <= 0:
        raise ValueError()
    return 4 * a
