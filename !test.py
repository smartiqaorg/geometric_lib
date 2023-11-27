import math
import unittest
import circle
import rectangle
import square
import triangle


class RectangleTestCase(unittest.TestCase):
    def test_simple_area(self):
        res = rectangle.area(2, 5)
        self.assertEqual(res, 10)

    def test_simple_perimeter(self):
        res = rectangle.perimeter(2, 5)
        self.assertEqual(res, 14)

    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)


class CircleTestCase(unittest.TestCase):
    def test_simple_area(self):
        res = circle.area(5)
        self.assertEqual(res, 25 * math.pi)

    def test_simple_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 10 * math.pi)

    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)


class TriangleTestCase(unittest.TestCase):
    def test_simple_area(self):
        res = triangle.area(5, 4)
        self.assertEqual(res, 10)

    def test_simple_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_height(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_line_perimeter(self):
        res = triangle.perimeter(10, 5, 0)
        self.assertEqual(res, 15)


class SquareTestCase(unittest.TestCase):
    def test_simple_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_simple_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
