import math


def area(r):
    '''
    Возвращает площадь круга с радиусом r (число)

        Параметры :
            r - радиус круга (число)

        Возращаемое значение:
            Произведение Числа Пи на квадрат радиуса (r), то есть площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности с радиусом r

        Параметры:
            r - радиус окружности (число)

        Возращаемое значение:
            произведение 2 на Число Пи на радиус (r), то есть длина окружности.
    '''
    return 2 * math.pi * r

