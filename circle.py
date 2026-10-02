import math


def area(r):
    '''
    Вычисляет площадь круга с заданным радиусом.

    Ввод: r (float) - радиус
    Вывод: area (float) - площадь

    Пример использования:
    area(2) = 12.566...
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет длину окружности с заданным радиусом.

    Ввод: r (float) - радиус
    Вывод: perimeter (float) - длина окружности

    Пример использования:
    perimeter(3) = 18.85...
    '''
    return 2 * math.pi * r

