def area(a):
    '''
    Возвращает площадь квадрата.

    :param a: сторона квадрата (float)
    :return: площадь квадрата (float)

    Формула: S = a²

    Пример:
        >>> area(10.0)
        100.0
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата.

    :param a: сторона квадрата (float)
    :return: периметр квадрата (float)

    Формула: P = 4 · a

    Пример:
        >>> perimeter(10.0)
        40.0
    '''
    return 4 * a