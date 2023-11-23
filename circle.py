import math


def area(r):
    '''
    Принимает радиус круга, возврашает площадь круга.

        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            math.pi * r * r (float): площадь круга радиусом r

        Примеры использования:
            Входные данные:
                r = 3
            Выходные данные:
                area = 28.274333882308138
    '''
    if type(r) != int:
        return TypeError
    if r < 0:
        return ValueError
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус круга, возврашает длину окружности.

        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            2 * math.pi * r (float): длина окружности радиусом r

        Примеры использования:
            Входные дынные:
                r = 3
            Выходные данные:
                perimeter = 18.84955592153876
    '''
    if type(r) != int:
        return TypeError
    if r < 0:
        return ValueError
    return 2 * math.pi * r

