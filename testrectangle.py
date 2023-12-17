def area(a, b):
    '''
Выводит площадь прямоугольника.
	На вход получает 2 числа.
	На выходе выдает произведение этих чисел - площадь прямоугольника.
	print(area(5 , 7))
	35
    '''
    if (a < 0 or b < 0):
        raise TypeError("Incorrcet input : negative")
    elif type(a) == str or type(b) == str:
        raise TypeError("Incorrcet input : string")
    return a * b 

def perimeter(a, b):
    '''
Выводит периметр прямоугольника.
	На вход получает 2 числа.
	На выходе выдает сумму этих чисел , умноженную на 2 - периметр.
	print(perimeter(10 , 15))
	50
    '''
    if (a < 0 or b < 0):
        raise TypeError("Incorrcet input : negative")
    elif type(a) == str or type(b) == str:
        raise TypeError("Incorrcet input : string")
    return 2 * (a + b)
