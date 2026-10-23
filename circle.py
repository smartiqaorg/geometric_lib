import math


def area(r):
    '''
    Принимает радиус r, возвращает площадь круга.

    Заданные параметры:
        r (int/float): радиус круга

    Возвращаемое значение:
        circle_area (int/float): площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус r, возвращает длину окружности(Периметр).

    Заданные Параметры:
        r(int/float): радиус круга
    
    Возвращаемое значение:
        circle_perimetr (int/float): длина окружности
    '''
    return 2 * math.pi * r

