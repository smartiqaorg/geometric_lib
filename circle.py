import math
import unittest

def area(r):
    '''Принимает радиус круга(r), возвращает его площадь.'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус круга(r), возвращает его периметр.'''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area_int(self):
        res = area(6)
        self.assertAlmostEqual(res, 113.097, delta=0.001)

    def test_perimeter_int(self):
        res = perimeter(6)
        self.assertAlmostEqual(res, 37.699, delta=0.001)

    def test_area_float(self):
        res = area(5.7)
        self.assertAlmostEqual(res, 102.070, delta=0.001)

    def test_perimeter_float(self):
        res = perimeter(5.7)
        self.assertAlmostEqual(res, 35.814, delta=0.001)

    def test_area_zero(self):
        with self.assertRaises(Exception):
            area(0)

    def test_perimeter_zero(self):
        with self.assertRaises(Exception):
            perimeter(0)

    def test_area_negative(self):
        with self.assertRaises(Exception):
            area(-5)

    def test_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(-5)
