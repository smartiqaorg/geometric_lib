import unittest
import rectangle


class RectangleTests(unittest.TestCase):
    # обычные проверки

    def test_area(self):
        result = rectangle.area(3, 5)
        self.assertEqual(result, 15)

    def test_perimeter(self):
        result = rectangle.perimeter(3, 5)
        self.assertEqual(result, 16)

    def test_area_with_zero_side(self):
        result = rectangle.area(10, 0)
        self.assertEqual(result, 0)

    def test_perimeter_with_strings(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("3", "4")

    # Нулевые стороны

    def test_area_with_first_zero(self):
        result = rectangle.area(0, 10)
        self.assertEqual(result, 0)

    def test_perimeter_with_first_zero(self):
        result = rectangle.perimeter(0, 10)
        self.assertEqual(result, 20)

    def test_perimeter_with_second_zero(self):
        result = rectangle.perimeter(10, 0)
        self.assertEqual(result, 20)

    def test_area_with_two_zeros(self):
        result = rectangle.area(0, 0)
        self.assertEqual(result, 0)

    def test_perimeter_with_two_zeros(self):
        result = rectangle.perimeter(0, 0)
        self.assertEqual(result, 0)

    # Дробные числа

    def test_area_with_decimal_sides(self):
        result = rectangle.area(0.1, 0.2)
        self.assertAlmostEqual(result, 0.02)

    def test_perimeter_with_decimal_sides(self):
        result = rectangle.perimeter(0.1, 0.2)
        self.assertAlmostEqual(result, 0.6)

    def test_area_with_integer_and_decimal(self):
        result = rectangle.area(4, 2.5)
        self.assertAlmostEqual(result, 10.0)

    def test_perimeter_with_integer_and_decimal(self):
        result = rectangle.perimeter(4, 2.5)
        self.assertAlmostEqual(result, 13.0)

    # Очень маленькие и очень большие стороны

    def test_area_with_small_sides(self):
        result = rectangle.area(0.0001, 0.0002)
        self.assertAlmostEqual(result, 0.00000002, places=12)

    def test_perimeter_with_small_sides(self):
        result = rectangle.perimeter(0.0001, 0.0002)
        self.assertAlmostEqual(result, 0.0006, places=12)

    def test_area_with_large_sides(self):
        result = rectangle.area(10**30, 3)
        self.assertEqual(result, 3 * 10**30)

    def test_perimeter_with_large_sides(self):
        result = rectangle.perimeter(10**30, 3)
        self.assertEqual(result, 2 * 10**30 + 6)

    # Отрицательные стороны

    def test_area_with_negative_first_side(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, 5)

    def test_area_with_negative_second_side(self):
        with self.assertRaises(ValueError):
            rectangle.area(3, -5)

    def test_perimeter_with_negative_first_side(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, 5)

    def test_perimeter_with_negative_second_side(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(3, -5)

    def test_area_with_two_negative_sides(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, -5)

    def test_perimeter_with_two_negative_sides(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, -5)

    def test_area_with_negative_decimal(self):
        with self.assertRaises(ValueError):
            rectangle.area(-0.5, 2)

    def test_perimeter_with_negative_decimal(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(2, -0.5)

    # Строки вместо чисел

    def test_area_with_strings(self):
        with self.assertRaises(TypeError):
            rectangle.area("3", "4")

    def test_area_with_string_and_number(self):
        with self.assertRaises(TypeError):
            rectangle.area("3", 4)

    def test_area_with_number_and_string(self):
        with self.assertRaises(TypeError):
            rectangle.area(3, "4")

    def test_perimeter_with_string_and_number(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("3", 4)

    def test_perimeter_with_number_and_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(3, "4")

    def test_area_with_empty_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("", 4)

    def test_perimeter_with_empty_strings(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("", "")

    def test_area_with_text(self):
        with self.assertRaises(TypeError):
            rectangle.area("abc", 4)

    def test_perimeter_with_text(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("abc", "def")

    # Отсутствующее значение и логические значения

    def test_area_with_none(self):
        with self.assertRaises(TypeError):
            rectangle.area(None, 5)

    def test_perimeter_with_none(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(3, None)

    def test_area_with_true(self):
        with self.assertRaises(TypeError):
            rectangle.area(True, 5)

    def test_perimeter_with_false(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(3, False)

    # Неправильное количество аргументов

    def test_area_without_arguments(self):
        with self.assertRaises(TypeError):
            rectangle.area()

    def test_perimeter_without_arguments(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter()

    def test_area_with_one_argument(self):
        with self.assertRaises(TypeError):
            rectangle.area(3)

    def test_perimeter_with_one_argument(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(3)

    def test_area_with_three_arguments(self):
        with self.assertRaises(TypeError):
            rectangle.area(3, 4, 5)

    def test_perimeter_with_three_arguments(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(3, 4, 5)