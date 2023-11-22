import unittest
from rectangle import *


class rectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_float_area(self):
        res = area(5.5, 5.42)
        self.assertEqual(res, 29.81)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_int_perimeter(self):
        res = perimeter(5, 4)
        self.assertEqual(res, 18)

    def test_float_perimeter(self):
        res = perimeter(5.9, 2.23)
        self.assertEqual(res, 16.26)
