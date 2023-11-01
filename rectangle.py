

'''
Принимает значения a,b, возращает значение площади прямоугольника
    Параметры:
            a (int): первое десятичное число
	    b (int): второе десятичное число
    Пример:
            Получает: a=5, b=20
            Возвращает: 100
'''

import unittest

class RectangleTestCase(unittest.TestCase):
	def test_zero_mul(self):
		Areares = area(10, 10)
		self.assertEqual(Areares, 100)
		Perimeterres=perimeter(10,10)
		self.assertEqual(Perimeterres, 40)


	def test_square_mul(self):
		res = area(10, 10)
		self.assertEqual(res, 100)


def area(a, b):
	return a * b
'''
Принимает значения a,b, возращает значение периметра прямоугольника
    Параметры:
            a (int): первое десятичное число
	    b (int): второе десятичное число
    Пример:
            Получает: a=5, b=20
            Возвращает: 50
'''
def perimeter(a, b):
	return (a + b)*2
