import math

def area(a,b):
    return (1/2*a)*b

def perimeter(a,b,c):
    return a+b+c

import unittest


class TestArea(unittest.TestCase):
    def test_triangle_area_1(self):
        self.assertAlmostEqual(area(2,2),2,places=3)
    def test_triangle_area_2(self):
        self.assertEqual(area(0,0), 0)
    def test_triangle_area_3(self):
        self.assertAlmostEqual(area(5,2), 5,places=3)
    def test_triangle_area_negative(self):
        self.assertRaises(TypeError,area, -1,-3)
    def test_triangle_area_string(self):
        self.assertRaises(TypeError, area, 'abcыы')

class TestPerimeter(unittest.TestCase):
    def test_perimeter_1(self):
        self.assertEqual(perimeter(2, 3,4), 9)
    def test_perimeter_2(self):
        self.assertEqual(perimeter(5, 5,5), 15)
    def test_perimeter_3(self):
        self.assertEqual(perimeter(0, 0,0), 0)
    def test_rectangle_perimeter_negative(self):
        self.assertRaises(TypeError,perimeter,-1,-2,-3)
    def test_circle_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, 'abcыы')