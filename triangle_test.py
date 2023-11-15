import unittest

from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_triangle_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_zero_per(self):
        res = perimeter(10, 10, 0)
        self.assertEqual(res, 20)

    def test_triangle_per(self):
        res = perimeter(15, 15, 15)
        self.assertEqual(res, 45)
