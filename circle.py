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
        self.assertEqual(res, 113.09733552923255)

    def test_perimeter_int(self):
        res = perimeter(6)
        self.assertEqual(res, 37.69911184307752)

    def test_area_float(self):
        res = area(5.7)
        self.assertEqual(res, 102.07034531513239)

    def test_perimeter_float(self):
        res = perimeter(5.7)
        self.assertEqual(res, 35.814156250923645)

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
