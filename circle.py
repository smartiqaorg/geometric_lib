import math




def area(r):
    """Принимает число r-радиус круга, возвращает площадь круга, полученную по формуле πR²"""
    if r>0:
        return math.pi * r * r
    else:
        return "ERROR"


def perimeter(r):
    """Принимает число r-радиус круга, возвращает периметр круга, полученный по формуле 2πR"""
    if r > 0:
        return math.pi * 2 * r
    else:
        return "ERROR"
