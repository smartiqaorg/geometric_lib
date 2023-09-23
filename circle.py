import math
def area(r):
    '''
    area(r)
    
    Принимает число r - радиус круга и возвращает значение площади
    
    Пример: area(5) = 25*pi
    '''
    return math.pi * r * r


def perimeter(r):
    """
    perimeter(r)
    
    Принимает число r - радиус круга и возвращает значение периметра
    
    Пример:
    perimeter(5) = 10*pi
    """
    return 2 * math.pi * r
