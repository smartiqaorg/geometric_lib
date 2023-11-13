import unittest
import rectangle
import sys
sys.path.append('../')


class RectangleTestCase(unittest.TestCase):
    def test_second_zero_area_case(self):
        with self.assertRaises(ValueError):
            rectangle.area(10, 0)

    def test_first_zero_area_case(self):
        with self.assertRaises(ValueError):
            rectangle.area(0, 10)

    def test_square_area_case(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_general_area_case(self):
        res = rectangle.area(1337, 228)
        self.assertEqual(res, 304836)

    def test_first_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            rectangle.area(-228, 1337)

    def test_second_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            rectangle.area(228, -1337)

    def test_first_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            rectangle.area("abcd", 1337)

    def test_second_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            rectangle.area(228, "abcd")

    def test_second_zero_perimeter_case(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(10, 0)

    def test_first_zero_perimeter_case(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(0, 10)

    def test_square_perimeter_case(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_general_perimeter_case(self):
        res = rectangle.perimeter(1337, 228)
        self.assertEqual(res, 3130)

    def test_second_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(228, -1337)

    def test_first_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-228, 1337)

    def test_first_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("abcd", 1337)

    def test_second_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(228, "abcd")
