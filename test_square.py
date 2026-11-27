import unittest
import square


class SquareTests(unittest.TestCase):
    # Обычные проверки

    def test_area(self):
        result = square.area(5)
        self.assertEqual(result, 25)

    def test_perimeter(self):
        result = square.perimeter(5)
        self.assertEqual(result, 20)

    # Нулевая сторона

    def test_area_with_zero(self):
        result = square.area(0)
        self.assertEqual(result, 0)

    def test_perimeter_with_zero(self):
        result = square.perimeter(0)
        self.assertEqual(result, 0)

    # Дробная сторона

    def test_area_with_decimal(self):
        result = square.area(0.2)
        self.assertAlmostEqual(result, 0.04)

    def test_perimeter_with_decimal(self):
        result = square.perimeter(0.2)
        self.assertAlmostEqual(result, 0.8)

    # Очень маленькая и очень большая сторона

    def test_area_with_small_side(self):
        result = square.area(0.0001)
        self.assertAlmostEqual(result, 0.00000001, places=12)

    def test_perimeter_with_small_side(self):
        result = square.perimeter(0.0001)
        self.assertAlmostEqual(result, 0.0004, places=12)

    def test_area_with_large_side(self):
        result = square.area(10**30)
        self.assertEqual(result, 10**60)

    def test_perimeter_with_large_side(self):
        result = square.perimeter(10**30)
        self.assertEqual(result, 4 * 10**30)

    # Отрицательная сторона

    def test_area_with_negative_side(self):
        with self.assertRaises(ValueError):
            square.area(-5)

    def test_perimeter_with_negative_side(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)

    def test_area_with_negative_decimal(self):
        with self.assertRaises(ValueError):
            square.area(-0.5)

    def test_perimeter_with_negative_decimal(self):
        with self.assertRaises(ValueError):
            square.perimeter(-0.5)

    # Строки вместо чисел

    def test_area_with_string(self):
        with self.assertRaises(TypeError):
            square.area("5")

    def test_perimeter_with_strings(self):
        with self.assertRaises(TypeError):
            square.perimeter("5")

    def test_area_with_empty_string(self):
        with self.assertRaises(TypeError):
            square.area("")

    def test_perimeter_with_empty_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("")

    def test_area_with_text(self):
        with self.assertRaises(TypeError):
            square.area("abc")

    def test_perimeter_with_text(self):
        with self.assertRaises(TypeError):
            square.perimeter("abc")

    # Отсутствующее значение и логические значения

    def test_area_with_none(self):
        with self.assertRaises(TypeError):
            square.area(None)

    def test_perimeter_with_none(self):
        with self.assertRaises(TypeError):
            square.perimeter(None)

    def test_area_with_true(self):
        with self.assertRaises(TypeError):
            square.area(True)

    def test_perimeter_with_false(self):
        with self.assertRaises(TypeError):
            square.perimeter(False)

    # Неправильное количество аргументов

    def test_area_without_arguments(self):
        with self.assertRaises(TypeError):
            square.area()

    def test_perimeter_without_arguments(self):
        with self.assertRaises(TypeError):
            square.perimeter()

    def test_area_with_two_arguments(self):
        with self.assertRaises(TypeError):
            square.area(3, 4)

    def test_perimeter_with_two_arguments(self):
        with self.assertRaises(TypeError):
            square.perimeter(3, 4)