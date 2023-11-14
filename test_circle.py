import unittest
from circle import area, perimeter
import math

class TestCircleFunctions(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_rand(self):
        self.assertAlmostEqual(area(4), 50.26548245743669)

    def test_area_values(self):
        with self.assertRaises(ValueError):
            area(-1)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_pi(self):
        self.assertAlmostEqual(perimeter(0.5), math.pi)

    def test_perimeter_values(self):
        with self.assertRaises(ValueError):
            area(-1)
