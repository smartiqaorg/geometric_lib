import math


def area(r):
	'''
	Функция получает на вход длину радиуса круга и возвращает значение его площади.
	Например:
	Ввод: 7
	Вывод: 153.93804... 
	'''
    if (r < 0):
        raise TypeError("Incorrect input: negative value")
    elif type(r) == str:
        raise TypeError("Incorrect input: string value")
	    
    return math.pi * r * r


def perimeter(r):
	'''
	Функция получает на вход длину радиуса круга и возвращает значение его периметра.
	Например:
	Ввод: 7
	Вывод: 43.9823... 
	'''
    if (r < 0):
        raise TypeError("Incorrect input: negative value")
    elif type(r) == str:
        raise TypeError("Incorrect input: string value")
	    
    return 2 * math.pi * r

