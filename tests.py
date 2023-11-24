import unittest
import math
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(5)
        self.assertEqual(res, math.pi * 5 * 5)

    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)

    def test_area_negative_radius(self):
        res = circle.area(-5)
        self.assertEqual(res, 0)

    def test_perimeter_negative_radius(self):
        res = circle.perimeter(-5)
        self.assertEqual(res, 0)

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12)

    def test_perimeter(self):
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_area_negative_values(self):
        res = rectangle.area(-3, 4)
        self.assertEqual(res, 0)

    def test_perimeter_negative_values(self):
        res = rectangle.perimeter(-3, 4)
        self.assertEqual(res, 0)

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_area_negative_side_length(self):
        res = square.area(-5)
        self.assertEqual(res, 0)

    def test_perimeter_negative_side_length(self):
        res = square.perimeter(-5)
        self.assertEqual(res, 0)

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(3, 6)
        self.assertEqual(res, 9)

    def test_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_area_negative_values(self):
        res = triangle.area(-3, 6)
        self.assertEqual(res, 0)

    def test_perimeter_negative_values(self):
        res = triangle.perimeter(-3, 4, 5)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()