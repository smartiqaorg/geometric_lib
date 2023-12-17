def area(a, h):
    '''
Выводит площадь треугольника.
	На вход получает два числа a , h - сторону и высоту.
	На выходе выводит их произведение , деленное на 2 - площадь.
	print(area(5 , 9))
	22.5
'''
    if (a < 0 or h < 0):
        raise TypeError("Incorrcet input : negative")
    elif type(a) == str or type(h) == str:
        raise TypeError("Incorrcet input : string")
    return a * h / 2 

def perimeter(a, b, c):
    '''
Выводит периметр треугольника.
	На вход получает 3 числа - стороны треугольника.
	На выходе выводит их сумму - периметр.
	print(perimeter(3 , 4 , 5))
	12
'''
    if (a < 0 or b < 0 or c < 0):
        raise TypeError("Incorrcet input : negative")
    elif type(a) == str or type(c) == str or type(b) == str:
        raise TypeError("Incorrcet input : string")
    return a + b + c
