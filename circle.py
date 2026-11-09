import math
import unittest

def area(radius: float) -> float | bool:
    '''
    Given the radius of a circle, calculates area
    '''
    if radius < 0:
        return False
    return math.pi * math.pow(radius, 2)


def perimeter(radius: float) -> float | bool:
    '''
    Given the radius of a circle, calculates perimeter
    '''
    if radius <= 0:
        return False
    return 2 * math.pi * radius

class CircleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_pos_mul(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_neg_mul(self):
        res = area(-3)
        self.assertFalse(res)

    def test_perimeter_zero_add(self):
        res = perimeter(0)
        self.assertFalse(res)

    def test_perimeter_pos_add(self):
        res = perimeter(0.5)
        self.assertAlmostEqual(res, math.pi)

    def test_perimeter_neg_add(self):
        res = perimeter(-3)
        self.assertFalse(res)

