
def area(a):
    '''
Выводит площадь квадрата.
	На вход получает число a.
	На выходе выводит его произведение само на себя - площадь.
	print(area(5))
	25
    '''
    if (a < 0):
        raise TypeError("Incorrcet input : negative")
    elif type(a) == str:
        raise TypeError("Incorrcet input : string")

    return a * a


def perimeter(a):
    '''
Выводит периметр квадрата.
	На вход получает число a.
	На выходе выдает его произведение на 4 - периметр.
	print(perimeter(10))
	50
    '''
    if (a < 0):
        raise TypeError("Incorrcet input : negative")
    elif type(a) == str:
        raise TypeError("Incorrcet input : string")
    return 4 * a
