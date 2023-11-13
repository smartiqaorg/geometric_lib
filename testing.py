import unittest
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

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


class RectangleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
        res = rectangle.area(0, 10)
        self.assertEqual(res, 0)

    def test_square_area_case(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_general_area_case(self):
        res = rectangle.area(1337, 228)
        self.assertEqual(res, 304836)

    def test_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            rectangle.area(228, -1337)
        with self.assertRaises(ValueError):
            rectangle.area(-228, 1337)
        with self.assertRaises(ValueError):
            rectangle.area(-228, -1337)

    def test_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            rectangle.area("abcd", 1337)
        with self.assertRaises(TypeError):
            rectangle.area(228, "abcd")
        with self.assertRaises(TypeError):
            rectangle.area("abcd", "abcd")

    def test_zero_perimeter_case(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 10)
        res = rectangle.perimeter(0, 10)
        self.assertEqual(res, 10)

    def test_square_perimeter_case(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_general_perimeter_case(self):
        res = rectangle.perimeter(1337, 228)
        self.assertEqual(res, 3130)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(228, -1337)
        with self.assertRaises(ValueError):
            rectangle.perimeter(-228, 1337)
        with self.assertRaises(ValueError):
            rectangle.perimeter(-228, -1337)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("abcd", 1337)
        with self.assertRaises(TypeError):
            rectangle.perimeter(228, "abcd")
        with self.assertRaises(TypeError):
            rectangle.perimeter("abcd", "abcd")


class SquareTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = square.area(0)
        self.assertEqual(res, 0)

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
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_general_perimeter_case(self):
        res = square.perimeter(1337)
        self.assertEqual(res, 5348)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1337)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            square.perimeter("abcd")


class TriangleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)

    def test_general_area_case(self):
        res = triangle.area(1337, 228)
        self.assertEqual(res, 152418)

    def test_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            triangle.area(228, -1337)
        with self.assertRaises(ValueError):
            triangle.area(-228, 1337)
        with self.assertRaises(ValueError):
            triangle.area(-228, -1337)

    def test_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            triangle.area("abcd", 1337)
        with self.assertRaises(TypeError):
            triangle.area(228, "abcd")
        with self.assertRaises(TypeError):
            triangle.area("abcd", "abcd")

    def test_zero_perimeter_case(self):
        res = triangle.perimeter(0, 10, 10)
        self.assertEqual(res, 10)
        res = triangle.perimeter(10, 0, 10)
        self.assertEqual(res, 10)
        res = triangle.perimeter(10, 10, 0)
        self.assertEqual(res, 10)

    def test_general_perimeter_case(self):
        res = triangle.perimeter(1337, 228, 131)
        self.assertEqual(res, 1696)

    def test_wrong_triangle_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-228, 1337, 131)
        with self.assertRaises(ValueError):
            triangle.perimeter(228, -1337, 131)
        with self.assertRaises(ValueError):
            triangle.perimeter(228, 1337, -131)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 3)
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 1, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 3, 1)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("abcd", 1337, 131)
        with self.assertRaises(TypeError):
            triangle.perimeter(228, "abcd", 131)
        with self.assertRaises(TypeError):
            triangle.perimeter(228, 1337, "abcd")
