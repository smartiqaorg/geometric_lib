import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0, "Incorrect multy with zero in area in rectangle.")

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100, "Incorrect multy square in area in rectangle.")

    def test_simple_mul(self):
        res = area(5, 4)
        self.assertEqual(res, 20, "Incorrect multy with simple numbers in area in rectangle.")

    def test_inc_mul_1(self):
        try:
            res = area('5', '4')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in rectangle.")

    def test_inc_mul_2(self):
        try:
            res = area(5, '4')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in rectangle.")

    def test_inc_mul_3(self):
        try:
            res = area(-5, 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in rectangle.")

    def test_zero_sum(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0, "Incorrect sum with zero in perimeter in rectangle.")

    def test_square_sum(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40, "Incorrect sum square in perimeter in rectangle.")

    def test_simple_sum(self):
        res = perimeter(5, 4)
        self.assertEqual(res, 18, "Incorrect sum with simple numbers in perimeter in rectangle.")

    def test_inc_sum_1(self):
        try:
            res = area('5', '4')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in perimeter in rectangle.")

    def test_inc_sum_2(self):
        try:
            res = area(5, '4')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in perimeter in rectangle.")

    def test_inc_sum_3(self):
        try:
            res = area(-5, 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in perimeter in rectangle.")
