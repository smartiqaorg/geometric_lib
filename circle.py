import math
import unittest
"""
    Проведение юнит-тестов для модуля circle.py, 
    а именно методов area и perimeter
"""

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_perimetr_zero(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_perimetr_multiple(self):
        result_1 = perimeter(10)
        result_2 = perimeter(12)
        self.assertAlmostEqual(result_1, 62.83, places=2)
        self.assertAlmostEqual(result_2, 75.4, places=1)

    def test_perimetr_negative_number(self):
        with self.assertRaises(Exception):
            perimeter(-10)

    def test_perimetr_float_number(self):
        result = perimeter(4.20)
        self.assertAlmostEqual(result, 26.39, places=2)

    def test_area_zero(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_area_multiple(self):
        result_1 = area(10)
        result_2 = area(12)
        self.assertAlmostEqual(result_1, 314.16, places=2)
        self.assertAlmostEqual(result_2, 452.39, places=2)

    def test_area_float_number(self):
        result = area(4.12)
        self.assertAlmostEqual(result, 53.33, places=2)

    def test_area_negative_number(self):
        with self.assertRaises(Exception):
            area(-10)

