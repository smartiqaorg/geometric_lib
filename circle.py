import math


def area(r):
    """Принимает сторону и выводит площадь фигуры"""
    if r >= 0:
        return math.pi * r * r
    else:
        return 0


def perimeter(r):
    """Принимает сторону и выводит периметр фигуры"""
    if r >= 0:
        return 2 * math.pi * r
    else:
        return 0