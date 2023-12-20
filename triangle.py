def area(a, h):
	'''
	Функция получает на вход длину стороны и длину высоты треугольника (два числа) и возвращает значение его площади.
	Например:
	Ввод: 3 5
	Вывод: 15
	'''
    if (a < 0 or h < 0):
        raise TypeError("Incorrect input: negative value")
    elif type(a) == str or type(h) == str:
        raise TypeError("Incorrect input: string value")
	    
    return a * h / 2

def perimeter(a, b, c):
	'''
	Функция получает на вход длины сторон треугольника (три числа) и возвращает значение его периметра.
	Например:
	Ввод: 1 2 3
	Вывод: 6
	'''
    if (a < 0 or b < 0 or c < 0):
        raise TypeError("Incorrect input: negative value")
    elif type(a) == str or type(b) == str or type(c) == str:
        raise TypeError("Incorrect input: string value")
	    
    return a + b + c

