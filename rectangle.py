def area(a, b):
	'''
	Функция получает на вход длины двух смежных сторон прямоугольника (два числа) и возвращает значение его площади.
	Например:
	Ввод: 3 5
	Вывод: 15
	'''
    if (a < 0 or b < 0):
        raise TypeError("Incorrect input: negative value")
    elif type(a) == str or type(b) == str:
        raise TypeError("Incorrect input: string value")
	    
    return a * b

def perimeter(a, b):
	'''
	Функция получает на вход длины двух смежных сторон прямоугольника (два числа) и возвращает значение его периметра.
	Например:
	Ввод: 1 2
	Вывод: 6
	'''  
    if (a < 0 or b < 0):
        raise TypeError("Incorrect input: negative value")
    elif type(a) == str or type(b) == str:
        raise TypeError("Incorrect input: string value")

    return 2 * (a + b)


