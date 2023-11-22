
def area(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возвращает площадь квадрата, возводя число a в квадрат: a * a
    '''
    if (a < 0):
        raise ValueError("Invalid value")
    return a * a


def perimeter(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возвращает периметр квадрата, вычисляя его по формуле: P = 4 * a
    '''
    if (a < 0):
        raise ValueError("Invalid value")
    return 4 * a

