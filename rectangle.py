import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_area_case(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_square_area_case(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_general_area_case(self):
        res = area(1337, 228)
        self.assertEqual(res, 304836)

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
        res = perimeter(10, 0)
        self.assertEqual(res, 10)
        res = perimeter(0, 10)
        self.assertEqual(res, 10)

    def test_square_perimeter_case(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_general_perimeter_case(self):
        res = perimeter(1337, 228)
        self.assertEqual(res, 3130)

    def test_negative_value_perimeter_case(self):
        with self.assertRaises(ValueError):
            perimeter(228, -1337)
        with self.assertRaises(ValueError):
            perimeter(-228, 1337)
        with self.assertRaises(ValueError):
            perimeter(-228, -1337)

    def test_wrong_type_value_perimeter_case(self):
        with self.assertRaises(TypeError):
            perimeter("abcd", 1337)
        with self.assertRaises(TypeError):
            perimeter(228, "abcd")
        with self.assertRaises(TypeError):
            perimeter("abcd", "abcd")


def area(a, b):
    """
    Возвращает площадь прямоугольника с передаваемыми сторонами.

                Параметры:
                        a (float): длина прямоугольника
                        b (float): ширина прямоугольника

                Возвращаемое значение:
                        a * b (float): площадь прямоугольника
    """
    return a * b


def perimeter(a, b):
    """
        Возвращает периметр прямоугольника с передаваемыми сторонами.

                    Параметры:
                            a (float): длина прямоугольника
                            b (float): ширина прямоугольника

                    Возвращаемое значение:
                            2 * (a + b) (float): периметр прямоугольника
        """
    return 2 * (a + b)
