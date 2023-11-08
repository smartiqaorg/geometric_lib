import unittest

def area(a, b):
    """Принимает две смежные стороны и выводит площадь прямоугольника"""
    if a >= 0 and b >= 0:
        return a * b
    else:
        return 0

def perimeter(a, b):
    """Принимает две смежные стороны и выводит периметр прямоугольника"""
    if a >= 0 and b >= 0:
        return (a + b) * 2
    else:
        return 0


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_nefative_number_area_mul(self):
       res = area(-4, 45)
       self.assertEqual(res, 0)  

    def test_perimeter_zero_mul(self):
       res = perimeter(5, 0)
       self.assertEqual(res, 10)

    def test_perimeter_1_mul(self):
       res = perimeter(5, 4)
       self.assertEqual(res, 18)
       
    def test_nefative_number_perimeter_1_mul(self):
       res = perimeter(-5, 10)
       self.assertEqual(res, 0)