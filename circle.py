import math
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_general_area_case(self):
        res = area(1337)
        self.assertEqual(res, 5615813.638184853)

    def test_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            area(-1337)

    def test_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            area("abcd")

    def test_zero_perimeter_case(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_general_perimeter_case(self):
        res = perimeter(1337)
        self.assertEqual(res, 8400.618755699106)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            perimeter(-1337)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            perimeter("abcd")


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

