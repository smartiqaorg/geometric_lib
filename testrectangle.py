import unittest
from rectangle import perimeter
from rectangle import area
class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(3, 4),  12)
    def test_wrongdata(self):
        self.assertEqual(area([3], [4]), 12)
        self.assertEqual(area(True, False), 1)
        self.assertEqual((perimeter("3", "4")), 14)
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(4, 5), 18)
    def test_negative(self):
        self.assertEqual(area(-3, 2), 6)
        self.assertEqual(perimeter(-3, 4), 14)