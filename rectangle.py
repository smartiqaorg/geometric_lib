import unittest

def area(a, b):
    """Принимает две смежные стороны и выводит площадь прямоугольника"""
    return a * b

def perimeter(a, b):
    """Принимает две смежные стороны и выводит периметр прямоугольника"""
    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_perimeter_zero_mul(self):
       res = perimeter(5, 0)
       self.assertEqual(res, 10)

    def test_perimeter_zero_mul(self):
       res = perimeter(5, 4)
       self.assertEqual(res, 18)