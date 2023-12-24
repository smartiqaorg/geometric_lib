import unittest
from rectangle import perimeter
from rectangle import area
class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4, 5), 20)
        self.assertEqual(area(6, 8),  48)
    def test_zero(self):
        self.assertEqual(area(0, 0), 0)
    def test_wrongdata(self):
        self.assertEqual((perimeter("3", "4")), 14)
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 5), 16)
        self.assertEqual(perimeter(6, 5), 22)
