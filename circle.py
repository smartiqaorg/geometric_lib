import math

def area(r):
    '''Принимает значение радиуса r и возвращает площадь круга.'''
    if r > 0:
        return math.pi * r * r
    else:
        return 0

def perimeter(r):
    '''Принимает значение радиуса r и возвращает длину окружности.'''
    if r > 0:
        return 2 * math.pi * r
    else:
        return 0


