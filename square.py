def area(a):
	'''
	Функция получает на вход длину стороны квадрата и возвращает значение его площади.
	Например:
	Ввод: 2
	Вывод: 4
	'''
    if (a < 0):
        raise TypeError("Incorrect input: negative value")
    elif type(a) == str:
        raise TypeError("Incorrect input: string value")
	    
    return a * a


def perimeter(a):
	'''
	Функция получает на вход длину стороны квадрата и возвращает значение его периметра.
	Например:
	Ввод: 101
	Вывод: 404
	'''
    if (a < 0):
        raise TypeError("Incorrect input: negative value")
    elif type(a) == str:
        raise TypeError("Incorrect input: string value")
	    
    return 4 * a
