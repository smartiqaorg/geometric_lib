import unittest
import circle
import math

class CircleTests(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(3), 9 * math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 6 * math.pi)