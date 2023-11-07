import unittest

def area(a, b):
    '''Принимает числа a, b(стороны прямоугольника), возвращает площадь прямоугольника a * b'''
    return a * b
def perimeter(a, b):
    '''Принимает числа a, b(стороны прямоугольника), возвращает периметр прямоугольника 2(a + b)'''
    return 2 * (a + b)

class RectangleTestCase(unittest. TestCase):
    def test_zero_mul (self) :
        res = area (10, 0)
        self .assertEqual(res, 0)
    def test_square_mul (self):
        res = area (10,  10)
        self .assertEqual(res, 100)