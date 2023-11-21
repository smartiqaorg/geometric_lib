import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 78.53981633974483) # successful test
        self.assertEqual(area(7), 315) # fail test
        self.assertEqual(area('string'), 'fail')  # fail test

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 31.41592653589793) # successful test
        self.assertEqual(perimeter(10), 62)  # fail test
        self.assertEqual(perimeter('string'), 'fail')  # fail test

def area(r):
    return math.pi * r * r
    # принимает число r - радиус окружности
    # возвращает площадь круга с радиусом r

def perimeter(r):
    return 2 * math.pi * r
    # принимает число r - радиус окружности
    # возвращает длинну круга с радиусом r
