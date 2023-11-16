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
        self.assertEqual(area([3], [2]), 3)
        self.assertEqual(area({3:3}, {2:2}), 6)
        self.assertEqual(area(True, True), 1)
        self.assertEqual(perimeter("3", "4", "2"), 9)
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 2), 9)
        self.assertEqual(perimeter(4, 5, 3), 12)
    def test_negative(self):
        self.assertEqual(area(-3, -2), 3)