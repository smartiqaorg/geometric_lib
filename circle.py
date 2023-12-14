import math

def area(r):
    return math.pi* r*r


def perimeter(r):
    return math.pi* 2*r

import unittest

class TestArea(unittest.TestCase):
        def test_circle_area(self):
            self.assertEqual(area(2), 12.566)
            self.assertEqual(area(0), 0)
            self.assertEqual(area(5), 78.359)

        def test_circle_area_negative(self):
            self.assertEqual(TypeError,perimeter, -1)

class TestPerimeter(unittest.TestCase):
        def test_cicrle_perimeter(self):
            self.assertEqual(perimeter(2), 12.566)
            self.assertEqual(perimeter(0), 0)
            self.assertEqual(perimeter(5), 25)

        def test_circle_area_negative(self):
          self.assertEqual(TypeError,area, -1)

        def test_circle_area_string(self):
            self.assertEqual(TypeError,area, 'abc')