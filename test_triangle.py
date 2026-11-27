import unittest
import triangle


class TriangleTests(unittest.TestCase):
    # Обычные проверки

    def test_area(self):
        result = triangle.area(3, 4)
        self.assertEqual(result, 6)

    def test_perimeter(self):
        result = triangle.perimeter(3, 4, 5)
        self.assertEqual(result, 12)

    # Нулевые стороны и высота

    def test_area_with_zero_base(self):
        result = triangle.area(0, 4)
        self.assertEqual(result, 0)

    def test_area_with_zero_height(self):
        result = triangle.area(3, 0)
        self.assertEqual(result, 0)

    def test_area_with_two_zeros(self):
        result = triangle.area(0, 0)
        self.assertEqual(result, 0)

    def test_perimeter_with_first_zero(self):
        result = triangle.perimeter(0, 5, 5)
        self.assertEqual(result, 10)

    def test_perimeter_with_second_zero(self):
        result = triangle.perimeter(5, 0, 5)
        self.assertEqual(result, 10)

    def test_perimeter_with_third_zero(self):
        result = triangle.perimeter(5, 5, 0)
        self.assertEqual(result, 10)

    def test_perimeter_with_three_zeros(self):
        result = triangle.perimeter(0, 0, 0)
        self.assertEqual(result, 0)

    # Дробные числа

    def test_area_with_decimal_values(self):
        result = triangle.area(0.3, 0.4)
        self.assertAlmostEqual(result, 0.06)

    def test_perimeter_with_decimal_sides(self):
        result = triangle.perimeter(0.3, 0.4, 0.5)
        self.assertAlmostEqual(result, 1.2)

    def test_area_with_integer_and_decimal(self):
        result = triangle.area(4, 2.5)
        self.assertAlmostEqual(result, 5.0)

    def test_perimeter_with_integer_and_decimal(self):
        result = triangle.perimeter(4, 2.5, 2.5)
        self.assertAlmostEqual(result, 9.0)

    # Очень маленькие и очень большие значения

    def test_area_with_small_values(self):
        result = triangle.area(0.0001, 0.0002)
        self.assertAlmostEqual(result, 0.00000001, places=12)

    def test_perimeter_with_small_sides(self):
        result = triangle.perimeter(0.0003, 0.0004, 0.0005)
        self.assertAlmostEqual(result, 0.0012, places=12)

    def test_area_with_large_values(self):
        result = triangle.area(10**30, 4)
        expected = 2 * 10**30
        self.assertAlmostEqual(result, expected, delta=expected * 1e-12)

    def test_perimeter_with_large_sides(self):
        result = triangle.perimeter(10**30, 10**30, 3)
        self.assertEqual(result, 2 * 10**30 + 3)

    # Отрицательные стороны и высота

    def test_area_with_negative_base(self):
        with self.assertRaises(ValueError):
            triangle.area(-3, 4)

    def test_area_with_negative_height(self):
        with self.assertRaises(ValueError):
            triangle.area(3, -4)

    def test_area_with_two_negative_values(self):
        with self.assertRaises(ValueError):
            triangle.area(-3, -4)

    def test_perimeter_with_negative_first_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_with_negative_second_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, -4, 5)

    def test_perimeter_with_negative_third_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 4, -5)

    def test_perimeter_with_three_negative_sides(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, -4, -5)

    def test_area_with_negative_decimal(self):
        with self.assertRaises(ValueError):
            triangle.area(3, -0.5)

    def test_perimeter_with_negative_decimal(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, -0.5, 3)

    # Строки вместо чисел

    def test_area_with_strings(self):
        with self.assertRaises(TypeError):
            triangle.area("3", "4")

    def test_perimeter_with_strings(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("3", "4", "5")

    def test_area_with_string_base(self):
        with self.assertRaises(TypeError):
            triangle.area("3", 4)

    def test_area_with_string_height(self):
        with self.assertRaises(TypeError):
            triangle.area(3, "4")

    def test_perimeter_with_string_first_side(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("3", 4, 5)

    def test_perimeter_with_string_second_side(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, "4", 5)

    def test_perimeter_with_string_third_side(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, 4, "5")

    def test_area_with_empty_string(self):
        with self.assertRaises(TypeError):
            triangle.area("", 4)

    def test_perimeter_with_empty_strings(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("", "", "")

    def test_area_with_text(self):
        with self.assertRaises(TypeError):
            triangle.area("abc", 4)

    def test_perimeter_with_text(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("abc", "def", "ghi")

    # Отсутствующее значение и логические значения

    def test_area_with_none(self):
        with self.assertRaises(TypeError):
            triangle.area(None, 4)

    def test_perimeter_with_none(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, 4, None)

    def test_area_with_true(self):
        with self.assertRaises(TypeError):
            triangle.area(True, 4)

    def test_perimeter_with_false(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, False, 5)

    # Неправильное количество аргументов

    def test_area_without_arguments(self):
        with self.assertRaises(TypeError):
            triangle.area()

    def test_area_with_one_argument(self):
        with self.assertRaises(TypeError):
            triangle.area(3)

    def test_area_with_three_arguments(self):
        with self.assertRaises(TypeError):
            triangle.area(3, 4, 5)

    def test_perimeter_without_arguments(self):
        with self.assertRaises(TypeError):
            triangle.perimeter()

    def test_perimeter_with_one_argument(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3)

    def test_perimeter_with_two_arguments(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, 4)

    def test_perimeter_with_four_arguments(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, 4, 5, 6)