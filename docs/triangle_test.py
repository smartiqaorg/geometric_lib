import unittest
from triangle import *


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        with self.assertRaises(ValueError):
            res = area(10, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_float_area(self):
        res = area(6.4, 5.239)
        self.assertAlmostEqual(res, 16.7648, delta=0.1)

    def test_zero_perimetr(self):
        with self.assertRaises(ValueError):
            res = perimeter(0, 0, 0)

    def test_square_perimetr(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_float_perimetr(self):
        res = perimeter(6.4, 5.239, 2)
        self.assertAlmostEqual(res, 13.639, delta=0.1)
