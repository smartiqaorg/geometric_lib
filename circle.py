import math
import unittest


def area(r):
    '''Принимает число r, возвращает πR² - площадь круга
    При вызове функции print(area(1)) выведет 3.14159265359 - площадь круга с радиусом r=1'''
    if r>0:
        return math.pi * r * r
    else:
        return "error"


def perimeter(r):
    '''Принимает число r, возвращает 2πR - периметр круга
    При вызове функции print(perimeter(1)) выведет 6.28318530718 - периметр круга с радиусом r=1'''
    if r>0:
        return 2 * math.pi * r
    else:
        return "error"

