import math
import unittest

from circle import area as circle_area
from circle import perimeter as circle_perimeter

from rectangle import area as rectangle_area
from rectangle import perimeter as rectangle_perimeter

from square import area as square_area
from square import perimeter as square_perimeter

from triangle import area as triangle_area
from triangle import perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_circle_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_circle_area_square(self):
        res = circle_area(5)
        self.assertEqual(res, math.pi * 25)

    def test_circle_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_square(self):
        res = circle_perimeter(5)
        self.assertEqual(res, math.pi * 10)


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_zero(self):
        res = rectangle_area(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_area_square(self):
        res = rectangle_area(5, 2)
        self.assertEqual(res, 10)

    def test_rectangle_perimeter_zero(self):
        res = rectangle_perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_square(self):
        res = rectangle_perimeter(5, 4)
        self.assertEqual(res, 18)


class SquareTestCase(unittest.TestCase):
    def test_square_area_zero(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_square_area_square(self):
        res = square_area(5)
        self.assertEqual(res, 25)

    def test_square_perimeter_zero(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_square(self):
        res = square_perimeter(5)
        self.assertEqual(res, 20)


class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_zero(self):
        res = triangle_area(0, 0)
        self.assertEqual(res, 0)

    def test_triangle_area_square(self):
        res = triangle_area(5, 2)
        self.assertEqual(res, 10)

    def test_triangle_perimeter_zero(self):
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_square(self):
        res = triangle_perimeter(5, 5, 5)
        self.assertEqual(res, 15)
