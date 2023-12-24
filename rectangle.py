import unittest

def area(a, b):
    '''Принимает стороны прямоугольника (a, b), возвращает его площадь'''
    return a * b

def perimeter(a, b):
    '''Принимает стороны прямоугольника (a, b), возвращает его периметр'''
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_area_int(self):
        res = area(8, 7)
        self.assertEqual(res, 56)

    def test_perimeter_int(self):
        res = perimeter(8, 7)
        self.assertEqual(res, 30)

    def test_area_zero(self):
        with self.assertRaises(Exception):
            area(0, 10)

    def test_perimeter_zero(self):
        with self.assertRaises(Exception):
            perimeter(0, 10)

    def test_area_negative(self):
        with self.assertRaises(Exception):
            area(-5, -4)

    def test_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(-5, -4)

    def test_area_float(self):
        res = area(5.7, 4.2)
        self.assertEqual(res, 23.94)

    def test_perimeter_float(self):
        res = perimeter(5.7, 4.2)
        self.assertEqual(res, 19.8)
