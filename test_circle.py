import unittest
from circle import area
from circle import perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)
    def test_zero_r_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_pi_r_area(self):
        res = area(math.pi)
        self.assertEqual(res, 31.006276680299816)
    def test_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)
    def test_zero_r_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_pi_r_perimeter(self):
        res = perimeter(math.pi)
        self.assertEqual(res, 19.739208802178716)

