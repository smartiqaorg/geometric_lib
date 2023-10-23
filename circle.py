import math


def area(r):
    """
        Возвращает площадь круга с радиусом r
        Параметр:
            r (int) : радиус окружности
    """
    return math.pi * r * r


def perimeter(r):
    """
        Возвращает периметр круга с радиусом r
        Параметр:
            r (int) : радиус окружности
    """
    return 2 * math.pi * r