import unittest

def area(a):
    '''Принимает число a, возвращает a² - площадь квадрата
    При вызове функции print(area(1)) выведет 1 - площадь квадрата со стороной a=1'''
    if a>0:
        return a * a
    else:
        return "error"

def perimeter(a):
    '''Принимает число a, возвращает 4a - периметр квадрата
    При вызове функции print(perimeter(1)) выведет 4 - периметр квадрата со стороной a=1'''
    if a>0:
        return 4 * a
    else:
        return "error"


