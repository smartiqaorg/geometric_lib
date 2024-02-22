import math
import unittest

import triangle


class TriangleAreaTestCase(unittest.TestCase):
    def test_triangle_zero_area(self):
        res = triangle.area(7, 0)
        self.assertEqual(res, 0)

    def test_triangle_small_area(self):
        res = triangle.area(8, 7)
        self.assertEqual(res, (8 * 7) / 2)

    def test_triangle_big_area(self):
        res = triangle.area(400, 7000)
        self.assertEqual(res, (400 * 7000) / 2)

    def test_triangle_negative_argument_area(self):
        self.assertRaises(ValueError, triangle.area, -5, -7)

    def test_invalid_type(self):
        self.assertRaises(TypeError, triangle.area, "100", 3)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_triangle_zero_perimeter(self):
        self.assertRaises(ValueError, triangle.perimeter, -5, -7, 0)

    def test_triangle_small_area(self):
        res = triangle.perimeter(5, 7, 9)
        self.assertEqual(res, 5 + 7 + 9)

    def test_triangle_big_area(self):
        res = triangle.perimeter(400, 7000, 170)
        self.assertEqual(res, 400 + 7000 + 170)

    def test_triangle_negative_area(self):
        self.assertRaises(ValueError, triangle.perimeter, -5, -7, -9)

    def test_invalid_type(self):
        self.assertRaises(TypeError, triangle.perimeter, "100", 3, 4)
