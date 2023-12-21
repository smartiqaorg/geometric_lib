import math

def area(r):
    return math.pi* r*r


def perimeter(r):
    return math.pi* 2*r

import unittest

class TestArea(unittest.TestCase):
    def test_circle_area_1(self):
        self.assertAlmostEqual(area(2),12.566,places=3)
    def test_circle_area_2(self):
        self.assertEqual(area(0), 0)
    def test_circle_area_3(self):
        self.assertAlmostEqual(area(5), 78.540,places=3)
    def test_circle_area_negative(self):
        self.assertEqual(TypeError,area, -1)
    def test_circle_area_string(self):
        self.assertEqual(TypeError,area, 'ac')

class TestPerimeter(unittest.TestCase):
    def test_cicrle_perimeter_1(self):
        self.assertAlmostEqual(perimeter(2), 12.566,places=3)
    def test_cicrle_perimeter_2(self):
        self.assertEqual(perimeter(0), 0)
    def test_cicrle_perimeter_3(self):
        self.assertAlmostEqual(perimeter(5), 31.416,places=3)
    def test_circle_perimeter_negative(self):
        self.assertEqual(TypeError,perimeter, -1)
    def test_circle_perimeter_string(self):
        self.assertEqual(TypeError,perimeter, 'ac')