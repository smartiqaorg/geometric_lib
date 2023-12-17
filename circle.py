import math


def area(r):
    '''
    возвращает плоащдь круга
	На вход подается число r:
	На выходе получаем площадь круга
	print(area(5))
	78.53981633974483
    '''
    if (r < 0):
        raise TypeError("Incorrcet input : negative")
    elif type(r) == str:
        raise TypeError("Incorrcet input : string")
	
    return math.pi * r * r


def perimeter(r):
    '''
	Возращает длину круга
		На вход подается число r
		На выходе получают длину круга.
		print(perimeter(10))
		62.83185307179586
   '''
    if (r < 0):
        raise TypeError("Incorrcet input : negative")
    elif type(r) == str:
        raise TypeError("Incorrcet input : string")
    return 2 * math.pi * r

