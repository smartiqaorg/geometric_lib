import unittest
from triangle import perimeter
from triangle import area
class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 2), 3)
        self.assertEqual(area(4, 3),  6)
    def test_zero(self):
        self.assertEqual(area(0, 0), 0)
    def test_wrongdata(self):
        self.assertEqual(perimeter("5", "6", "7"), 18)
    def test_perimeter(self):
        self.assertEqual(perimeter(4, 5, 3), 12)