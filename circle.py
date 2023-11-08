import unittest
import math


def area(r):
    """Принимает сторону и выводит площадь фигуры"""
    if r >= 0:
        return math.pi * r * r
    else:
        return 0


def perimeter(r):
    """Принимает сторону и выводит периметр фигуры"""
    if r >= 0:
        return 2 * math.pi * r
    else:
        return 0

class CircleleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
    
    def test_zero1_mul(self):
       res = area(2)
       self.assertEqual(res, math.pi * 4)

    def test_nefative_number_area_mul(self):
       res = area(-4)
       self.assertEqual(res, 0)  

    def test_perimeter_zero_mul(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

    def test_perimeter_1_mul(self):
       res = perimeter(5)
       self.assertEqual(res, math.pi * 10)

    def test_negative_number_perimeter_1_mul(self):
       res = perimeter(-5)
       self.assertEqual(res, 0)