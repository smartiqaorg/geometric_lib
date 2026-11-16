import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_normal_area(self):
        res = area(10)
        self.assertAlmostEqual(res, math.pi * 100)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = area(2.5)
        self.assertAlmostEqual(res, math.pi * 6.25)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area("5")    

    def test_normal_perimeter(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, math.pi * 20)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, math.pi * 5)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5")

if __name__ == '__main__':
    unittest.main()