def area(a, b):
    '''
    Возвращает площадь прямоугольника.

    :param a: первая сторона (float)
    :param b: вторая сторона (float)
    :return: площадь прямоугольника (float)

    Формула: S = a · b

    Пример:
        >>> area(10.0, 5.0)
        50.0
    '''
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника.

    :param a: первая сторона (float)
    :param b: вторая сторона (float)
    :return: периметр прямоугольника (float)

    Формула: P = 2 · (a + b)

    Пример:
        >>> perimeter(10.0, 5.0)
        30.0
    '''
    return 2 * (a + b)