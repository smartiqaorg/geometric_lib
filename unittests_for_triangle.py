import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0, "Incorrect multy with zero in area in triangle.")

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50, "Incorrect multy square in area in triangle.")

    def test_simple_mul(self):
        res = area(2, 8)
        self.assertEqual(res, 8, "Incorrect multy with simple numbers in area in triangle.")

    def test_inc_mul(self):
        try:
            res = area('2', '8')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in triangle.")

    def test_zero_sum(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0, "Incorrect sum with zero in perimeter in triangle.")

    def test_square_sum(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30, "Incorrect sum with same numbers perimeter in triangle.")

    def test_simple_sum(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9, "Incorrect sum with simple numbers perimeter in triangle.")
