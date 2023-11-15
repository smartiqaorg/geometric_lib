import unittest
import math
import circle

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        expectedResult = 0
        result = circle.area(0)
        self.assertEqual(expectedResult, result)

    def test_pi_area(self):
        expectedResult = math.pi
        result = circle.area(1)
        self.assertEqual(expectedResult, result)

    def test_zero_perimeter(self):
        expectedResult = 0
        result = circle.perimeter(0)
        self.assertEqual(expectedResult, result)

    def test_one_perimeter(self):
        expectedResult = 1
        result = circle.perimeter(1 / (math.pi * 2))
        self.assertAlmostEqual(expectedResult, result)