import math
def area(r):
    '''Принимает число r,возвращает площадь круга с радиусом r
    К примеру,для r=5 print(area(5)) выведет 78,53982
    '''
    if (r>=0):
        return math.pi * r * r
    else:
        return("ERROR")
def perimeter(r):
    '''Принимает число r,возвращает длину окружности
    Для r=2 print(perimeter(2)) выведет 12,56637
    '''
    if (r>=0):
        return 2 * math.pi * r
    else:
        return("ERROR")

