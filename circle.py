import math


def area(r):
    '''
     Данная функция возвращает площадь окружности.

        Параметры:
            r (int) : радиус окружности

        Возвращаемое значение:
            math.pi * r * r (int) : площадь окружности
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Данная фунция возвращает периметр окружности.

        Параметры:
            r (int) : радиус окружности

        Возвращаемое значение:
            2 * math.pi * r (int) : периметр окружности
    '''
    return 2 * math.pi * r

