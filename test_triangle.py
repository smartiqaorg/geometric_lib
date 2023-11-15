from triangle import area
from triangle import perimeter
import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10,0)
        self.assertEqual(res, 0)

    def test_triangle_mul(self):
        res = area(10,10)
        self.assertEqual(res, 50)

    def test_zero_per(self):
        res = perimeter(10,0,50)
        self.assertEqual(res, 60)

    def test_triangle_per(self):
        res = perimeter(29,11,88)
        self.assertEqual(res, 128)