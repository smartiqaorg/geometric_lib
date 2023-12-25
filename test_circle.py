import unittest
import math
from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5)
        self.assertAlmostEqual(res, round(78.53975, 3))

    def test_2_area(self):
        res = area(13)
        self.assertAlmostEqual(res, round(530.92871, 3))
        
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-13)

    def test_1_perimeter(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, round(18.84954, 3))

    def test_2_perimeter(self):
        res = perimeter(30)
        self.assertAlmostEqual(res, round(188.4954, 3))

if __name__ == '__main__':
    unittest.main()
