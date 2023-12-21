import unittest
from circle import area
from circle import perimeter
class CircleTestCase(unittest.TestCase):

    def test_zero_radius_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_radius_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.54, places=2)

    def test_zero_radius_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_radius_perimeter(self):
        res = perimeter(7)
        self.assertAlmostEqual(res, 43.98, places=2)
