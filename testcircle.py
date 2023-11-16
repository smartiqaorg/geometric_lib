import unittest
from circle import perimeter
from circle import area
class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3), 28.274333882308138)
        self.assertEqual(area(5),  78.53981633974483)
    def test_zeromul(self):
        self.assertEqual(area(0), 0)
    def test_wrongdata(self):
        self.assertEqual(area([3]), 28.274333882308138)
        self.assertEqual(area(True), 28.274333882308138)
        self.assertEqual((perimeter("3")), 28.274333882308138)
    def test_perimeter(self):
        self.assertEqual(perimeter(3), 18.84955592153876)
        self.assertEqual(perimeter(4), 25.132741228718345)
    def negative(self):
        self.assertEqual(perimeter(-3), 18.84955592153876)
        self.assertEqual(perimeter(-4), 25.132741228718345)