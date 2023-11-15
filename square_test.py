import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res,0)

    def test_self_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_self_per(self):
        res = perimeter(15)
        self.assertEqual(res, 60)