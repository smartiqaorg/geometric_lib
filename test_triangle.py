import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(5, 7)
        self.assertEqual(res, 17.5)
    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
    def test_perimeter(self):
        res = perimeter(2, 3, 5)
        self.assertEqual(res, 10)
    def test_zero_perimeter(self):
        res = perimeter(0, 3, 5)
        self.assertEqual(res, 'incorrect input')