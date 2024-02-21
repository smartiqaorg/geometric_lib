import unittest
import triangle
import sys
sys.path.append('../')


class TriangleTestCase(unittest.TestCase):
    def test_first_zero_area_case(self):
        with self.assertRaises(ValueError):
            triangle.area(10, 0)

    def test_second_zero_area_case(self):
        with self.assertRaises(ValueError):
            triangle.area(0, 10)

    def test_general_area_case(self):
        res = triangle.area(1337, 228)
        self.assertEqual(res, 152418)

    def test_second_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            triangle.area(228, -1337)

    def test_first_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            triangle.area(-228, 1337)

    def test_first_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            triangle.area("abcd", 1337)

    def test_second_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            triangle.area(228, "abcd")

    def test_first_zero_perimeter_case(self):
        res = triangle.perimeter(0, 10, 10)
        self.assertEqual(res, 10)

    def test_second_zero_perimeter_case(self):
        res = triangle.perimeter(10, 0, 10)
        self.assertEqual(res, 10)

    def test_third_zero_perimeter_case(self):
        res = triangle.perimeter(10, 10, 0)
        self.assertEqual(res, 10)

    def test_general_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1337, 228, 131)

    def test_first_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-228, 1337, 131)

    def test_second_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(228, -1337, 131)

    def test_third_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(228, 1337, -131)

    def test_third_wrong_triangle_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 3)

    def test_first_wrong_triangle_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 1, 1)

    def test_second_wrong_triangle_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 3, 1)

    def test_first_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("abcd", 1337, 131)

    def test_second_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(228, "abcd", 131)

    def test_third_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(228, 1337, "abcd")
