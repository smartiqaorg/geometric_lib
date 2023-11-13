import unittest
import square
import sys
sys.path.append('../')


class SquareTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        with self.assertRaises(ValueError):
            square.area(0)

    def test_general_area_case(self):
        res = square.area(1337)
        self.assertEqual(res, 1787569)

    def test_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            square.area(-1337)

    def test_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            square.area("abcd")

    def test_zero_perimeter_case(self):
        with self.assertRaises(ValueError):
            square.perimeter(0)

    def test_general_perimeter_case(self):
        res = square.perimeter(1337)
        self.assertEqual(res, 5348)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1337)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            square.perimeter("abcd")