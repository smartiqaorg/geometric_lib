import unittest
from square import perimeter
from square import area
class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(4),  16)
    def test_zero(self):
        self.assertEqual(area(0), 0)
    def test_wrongdata(self):
        self.assertEqual(perimeter("4"), 16)
    def test_perimeter(self):
        self.assertEqual(perimeter(3), 12)
        self.assertEqual(perimeter(4), 16)
