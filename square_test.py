import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_rectangle_mul_1(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_rectangle_mul_2(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_rectangle_per_1(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_rectangle_per_2(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_rectangle_per_3(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
