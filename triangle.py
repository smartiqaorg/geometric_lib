import unittest

def area(a, h):
    '''Принимает сторону и высоту треугольника (a, h), возвращает его площадь.'''
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает стороны треугольника (a, b, c), возвращает его периметр.'''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_int(self):
        res = area(11, 6)
        self.assertEqual(res, 33)

    def test_perimeter_int(self):
        res = perimeter(11, 6, 8)
        self.assertEqual(res, 25)

    def test_area_zero(self):
        res = area(0, 8)
        self.assertEqual(res, 'error')

    def test_perimeter_zero(self):
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 'error')

    def test_area_negative(self):
        res = area(-5, -4)
        self.assertEqual(res, 'error')

    def test_perimeter_negative(self):
        res = perimeter(-5, -3, -2)
        self.assertEqual(res, 'error')

    def test_area_float(self):
        res = area(4.1, 8)
        self.assertEqual(res, 16.4)

    def test_perimeter_float(self):
        res = perimeter(4.1, 3.2, 2.9)
        self.assertEqual(res, 10.2)
