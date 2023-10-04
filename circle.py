import math


def area(r):
	'''
	Возвращает площадь курга

	Параметры: 
			r(float): радиус круга
	Возвращаемое значение:
			area(r): площадь круга
	'''
	return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр курга

    Параметры: 
                        r(float): радиус круга
    Возвращаемое значение:
                        perimetr(r): периметр круга
    '''
    return 2 * math.pi * r
