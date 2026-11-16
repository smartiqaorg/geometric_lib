import math


def area(r):

    '''
    Возвращает значение площади круга с заданным радиусом

    Параметры:
        r (float): радиус круга

    Возвращаемое значение:
        circle_area (float): площадь круга с радиусом r 
    '''

    circle_area = math.pi * r * r
    return circle_area


def perimeter(r):
        
    '''
    Возвращает значение длинны окружности с заданным радиусом

    Параметры:
        r (float): радиус круга

    Возвращаемое значение:
        circle_perimeter (float): длина окружности с радиусом r 
    '''

    circle_perimeter = math.pi * r * 2
    return circle_perimeter

