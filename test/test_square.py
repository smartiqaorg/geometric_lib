import math
import unittest

import square


class SquareAreaTestCase(unittest.TestCase):
    def test_square_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_small_area(self):
        res = square.area(5)
        self.assertEqual(res, 5 * 5)

    def test_square_big_area(self):
        res = square.area(400)
        self.assertEqual(res, 400 * 400)

    def test_square_negative_area(self):
        self.assertRaises(ValueError, square.area, -5)

    def test_invalid_type(self):
        self.assertRaises(TypeError, square.perimeter, "100", 3)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_square_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_small_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 4 * 5)

    def test_square_big_perimeter(self):
        res = square.perimeter(400)
        self.assertEqual(res, 4 * 400)

    def test_square_negative_perimeter(self):
        self.assertRaises(ValueError, square.perimeter, -5)

    def test_invalid_type(self):
        self.assertRaises(TypeError, square.perimeter, "100", 3)
