import unittest
from square import *
class SquareTestCase(unittest.TestCase):

    def test_zero_area(self):

        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perim(self):

        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_area(self):

        res = area(10)
        self.assertEqual(res, 100)

    def test_sqaure_perimeter(self):

        res = perimeter(10)
        self.assertEqual(res, 40)
