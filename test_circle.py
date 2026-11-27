import math
import unittest
import circle


class CircleTests(unittest.TestCase):
    # Обычные проверки

    def test_area(self):
        result = circle.area(3)
        self.assertAlmostEqual(result, 9 * math.pi)

    def test_perimeter(self):
        result = circle.perimeter(3)
        self.assertAlmostEqual(result, 6 * math.pi)

    # Нулевой радиус

    def test_area_with_zero(self):
        result = circle.area(0)
        self.assertEqual(result, 0)

    def test_perimeter_with_zero(self):
        result = circle.perimeter(0)
        self.assertEqual(result, 0)

    # Дробный радиус

    def test_area_with_decimal(self):
        result = circle.area(0.5)
        self.assertAlmostEqual(result, 0.25 * math.pi)

    def test_perimeter_with_decimal(self):
        result = circle.perimeter(0.5)
        self.assertAlmostEqual(result, math.pi)

    # Очень маленький и очень большой радиус

    def test_area_with_small_radius(self):
        result = circle.area(0.0001)
        self.assertAlmostEqual(result, 0.00000001 * math.pi, places=12)

    def test_perimeter_with_small_radius(self):
        result = circle.perimeter(0.0001)
        self.assertAlmostEqual(result, 0.0002 * math.pi, places=12)

    def test_area_with_large_radius(self):
        result = circle.area(10**30)
        expected = math.pi * 10**60
        self.assertAlmostEqual(result, expected, delta=expected * 1e-12)

    def test_perimeter_with_large_radius(self):
        result = circle.perimeter(10**30)
        expected = 2 * math.pi * 10**30
        self.assertAlmostEqual(result, expected, delta=expected * 1e-12)

    # Отрицательный радиус

    def test_area_with_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-3)

    def test_perimeter_with_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-3)

    def test_area_with_negative_decimal(self):
        with self.assertRaises(ValueError):
            circle.area(-0.5)

    def test_perimeter_with_negative_decimal(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-0.5)

    # Строки вместо чисел

    def test_area_with_string(self):
        with self.assertRaises(TypeError):
            circle.area("3")

    def test_perimeter_with_strings(self):
        with self.assertRaises(TypeError):
            circle.perimeter("3")

    def test_area_with_empty_string(self):
        with self.assertRaises(TypeError):
            circle.area("")

    def test_perimeter_with_empty_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("")

    def test_area_with_text(self):
        with self.assertRaises(TypeError):
            circle.area("abc")

    def test_perimeter_with_text(self):
        with self.assertRaises(TypeError):
            circle.perimeter("abc")

    # Отсутствующее значение и логические значения

    def test_area_with_none(self):
        with self.assertRaises(TypeError):
            circle.area(None)

    def test_perimeter_with_none(self):
        with self.assertRaises(TypeError):
            circle.perimeter(None)

    def test_area_with_true(self):
        with self.assertRaises(TypeError):
            circle.area(True)

    def test_perimeter_with_false(self):
        with self.assertRaises(TypeError):
            circle.perimeter(False)

    # Неправильное количество аргументов

    def test_area_without_arguments(self):
        with self.assertRaises(TypeError):
            circle.area()

    def test_perimeter_without_arguments(self):
        with self.assertRaises(TypeError):
            circle.perimeter()

    def test_area_with_two_arguments(self):
        with self.assertRaises(TypeError):
            circle.area(3, 4)

    def test_perimeter_with_two_arguments(self):
        with self.assertRaises(TypeError):
            circle.perimeter(3, 4)