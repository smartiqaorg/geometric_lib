import math
def area(r):
    '''Принимает число r,возвращает площадь круга с радиусом r
    К примеру,для r=5 print(area(5)) выведет 78,53982
    '''
    return math.pi * r * r
def perimeter(r):
    '''Принимает число r,возвращает длину окружности
    Для r=2 print(perimeter(2)) выведет 12,56637
    '''
    return 2 * math.pi * r

