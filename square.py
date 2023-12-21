import unittest

"""
    Проведение юнит-тестов для модуля circle.py, 
    а именно методов area и perimeter
"""

def area(a):
    return a * a


def perimeter(a):
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_multiple(self):
        res1 = area(5)
        res2 = area(10)
        self.assertEqual(res1, 25)
        self.assertEqual(res2, 100)

    def test_area_float_number(self):
        res = area(4.5)
        self.assertAlmostEqual(res, 20.25, places=2)

    def test_area_negative_number(self):
        with self.assertRaises(Exception):
            area(-10)

    def test_perimetr_multiple(self):
        res1 = perimeter(4)
        res2 = perimeter(10)
        self.assertEqual(res1, 16)
        self.assertEqual(res2, 40)

    def test_perimetr_float_number(self):
        res = perimeter(3.6)
        self.assertAlmostEqual(res, 14.4, places=1)

    def test_perimetr_negative_number(self):
        with self.assertRaises(Exception):
            perimeter(-20)

    def test_perimetr_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)