import math


def area(r):
    """Принимает радиус круга (r), возвращает площадь круга"""
    return math.pi * r * r


def perimeter(r):
    """Принимает радиус круга (r), длину окружности"""
    return 2 * math.pi * r

print(area("radius"))