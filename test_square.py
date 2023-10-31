import unittest
from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = area(5)
        self.assertEqual(res, 25)
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
