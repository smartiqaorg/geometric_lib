import math
import unittest

def area(r):
    '''Принимает число r(радиус круга), возвращает площадь круга'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r(радиус круга), возвращает длину окружности'''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)
    def test_circle_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

