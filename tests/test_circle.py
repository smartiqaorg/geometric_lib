import unittest
import math

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_area_another_radius(self):
        self.assertAlmostEqual(area(5), 25 * math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)

    def test_perimeter_another_radius(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)

if __name__ == "__main__":
    unittest.main()