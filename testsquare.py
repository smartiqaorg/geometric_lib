import unittest
from square import perimeter
from square import area
class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(3),  9)
    def test_zero(self):
        self.assertEqual(area(0), 0)
    def test_wrongdata(self):
        self.assertEqual(area([3]), 9)
        self.assertEqual(area({3:3}), 9)
        self.assertEqual(area(True), 1)
        self.assertEqual(perimeter("3"), 12)
    def test_perimeter(self):
        self.assertEqual(perimeter(3), 12)
        self.assertEqual(perimeter(4), 16)
    def test_negative(self):
        self.assertEqual(area(-3), 12)