import math
import unittest

def area(r):
    '''Принимает радиус r, возвращает площадь круга с радиусом r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус r, возвращает периметр круга с радиусом r'''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perim(self):

        res = perimeter(0)
        self.assertEqual(res, 0)
