import unittest


class TriangleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_general_area_case(self):
        res = area(1337, 228)
        self.assertEqual(res, 152418)

    def test_negative_value_area_case(self):
        with self.assertRaises(ValueError):
            area(228, -1337)
        with self.assertRaises(ValueError):
            area(-228, 1337)
        with self.assertRaises(ValueError):
            area(-228, -1337)

    def test_wrong_type_value_area_case(self):
        with self.assertRaises(TypeError):
            area("abcd", 1337)
        with self.assertRaises(TypeError):
            area(228, "abcd")
        with self.assertRaises(TypeError):
            area("abcd", "abcd")

    def test_zero_perimeter_case(self):
        res = perimeter(0, 10, 10)
        self.assertEqual(res, 10)
        res = perimeter(10, 0, 10)
        self.assertEqual(res, 10)
        res = perimeter(10, 10, 0)
        self.assertEqual(res, 10)

    def test_general_perimeter_case(self):
        res = perimeter(1337, 228, 131)
        self.assertEqual(res, 1696)

    def test_wrong_triangle_perimeter_case(self):
        with self.assertRaises(ValueError):
            perimeter(-228, 1337, 131)
        with self.assertRaises(ValueError):
            perimeter(228, -1337, 131)
        with self.assertRaises(ValueError):
            perimeter(228, 1337, -131)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            perimeter(1, 1, 3)
        with self.assertRaises(ValueError):
            perimeter(3, 1, 1)
        with self.assertRaises(ValueError):
            perimeter(1, 3, 1)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            perimeter("abcd", 1337, 131)
        with self.assertRaises(TypeError):
            perimeter(228, "abcd", 131)
        with self.assertRaises(TypeError):
            perimeter(228, 1337, "abcd")


def area(a, h):
    """
    Возвращает площадь треугольника с передаваемыми высотой и основанием.

                Параметры:
                        a (float): основание треугольника
                        h (float): высота треугольника

                Возвращаемое значение:
                        a * h / 2 (float): площадь треугольника
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Возвращает периметр треугольника с передаваемыми сторонами.

                Параметры:
                        a (float): первая сторона треугольника
                        b (float): вторая сторона треугольника
                        c (float): третья сторона треугольника

                Возвращаемое значение:
                        a + b + c (float): периметр треугольника
        """
    return a + b + c
