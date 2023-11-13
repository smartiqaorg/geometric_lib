import unittest
import sys
import circle
sys.path.append('../')


class CircleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        with self.assertRaises(ValueError):
            circle.area(0)

    def test_general_area_case(self):
        res = circle.area(1337)
        self.assertEqual(res, 5615813.638184853)

    def test_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            circle.area(-1337)

    def test_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            circle.area("abcd")

    def test_zero_perimeter_case(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_general_perimeter_case(self):
        res = circle.perimeter(1337)
        self.assertEqual(res, 8400.618755699106)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1337)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            circle.perimeter("abcd")
