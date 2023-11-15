import math
'''импортируем библиотеку math'''

def area(r):
    if (r <= 0) or isinstance(r,str) or isinstance(str,r):
        return "Invalid input"
    '''
    На вход поступает число:
            r (int): радиус окружности
    Функция возвращает площадь окружности
    '''
    return math.pi * r * r


def perimeter(r):
    if (r <= 0) or isinstance(r,str) or isinstance(str,r):
        return "Invalid input"
    '''
    На вход поступает число:
            r (int): радиус окружности
    Функция возвращает периметр окружности
    '''
    return 2 * math.pi * r

