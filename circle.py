import unittest
import math


def area(r):
    """Принимает сторону и выводит площадь фигуры"""
    return math.pi * r * r


def perimeter(r):
    """Принимает сторону и выводит периметр фигуры"""
    return 2 * math.pi * r


class CircleleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
    
    def test_zero1_mul(self):
       res = area(2)
       self.assertEqual(res, math.pi * 4)

    def test_perimeter_zero_mul(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

    def test_perimeter_1_mul(self):
       res = perimeter(5)
       self.assertEqual(res, maht.pi * 10)