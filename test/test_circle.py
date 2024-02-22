import unittest
import math
import circle


class CircleAreaTestCase(unittest.TestCase):
    def test_zero_r(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_simple(self):
        res = circle.area(2)
        self.assertEqual(res, math.pi * 4)

    def test_huge(self):
        result = circle.area(9999999)
        expected_result = 314159202527129.4
        self.assertEqual(expected_result, result)

    def test_neg_r(self):
        self.assertRaises(ValueError, circle.area, -2)

    def test_invalid_type(self):
        self.assertRaises(TypeError, circle.area, "100")


class CirclePerTestCase(unittest.TestCase):
    def test_zero_r(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_simple(self):
        res = circle.perimeter(2)
        self.assertEqual(res, math.pi * 4)

    def test_huge(self):
        result = circle.perimeter(9999999)
        expected_result = 62831846.788610555
        self.assertEqual(expected_result, result)

    def test_neg_r(self):
        self.assertRaises(ValueError, circle.perimeter, -2)

    def test_invalid_type(self):
        self.assertRaises(TypeError, circle.perimeter, "100")