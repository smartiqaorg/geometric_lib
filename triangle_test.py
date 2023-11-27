import unittest
from triangle import area
from triangle import perimeter


class triangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(2, 0)
        self.assertEqual(res, 0)

    def test_rectangle_mul_1(self):
        res = area(10, 3)
        self.assertEqual(res, 15)

    def test_rectangle_mul_2(self):
        res = area(4, 6)
        self.assertEqual(res, 12)

    def test_rectangle_per_1(self):
        res = perimeter(10, 3, 4)
        self.assertEqual(res, 17)

    def test_rectangle_per_2(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_rectangle_per_3(self):
        res = perimeter(1, 4, 8)
        self.assertEqual(res, 13)
