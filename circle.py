import math


def area(r):
    '''
    Возвращает площадь круга.

    :param r: радиус круга (float)
    :return: площадь круга (float)

    Формула: S = π · r²

    Пример:
        >>> area(10.0)
        314.1592653589793
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности.

    :param r: радиус круга (float)
    :return: длина окружности (float)

    Формула: P = 2 · π · r

    Пример:
        >>> perimeter(10.0)
        62.83185307179586
    '''
    return 2 * math.pi * r