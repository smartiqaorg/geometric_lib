import math


def area(r):
    '''
    Возвращает площадь круга радиуса r.
    Пример вызова: area(1) -> 3.1415.
    r: радиус круга.
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Возвращает длину окружности.
    Пример вызова: perimeter(1) -> 6.283
    r: радиус окружности.
    '''
    return 2 * math.pi * r

