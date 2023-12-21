import unittest
from triangle import area
from triangle import perimeter
class TriangleTestCase(unittest.TestCase):

    def test_zero_base_height_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_positive_base_height_area(self):
        res = area(6, 8)
        self.assertEqual(res, 24)

    def test_positive_sides_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
