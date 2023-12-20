import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area_integer(self):
        # Проверка площади треугольника для целых чисел
        result = area(3, 4)
        self.assertEqual(result, 6)

    def test_area_float(self):
        # Проверка площади треугольника для дробных чисел
        result = area(2.5, 5.5)
        self.assertAlmostEqual(result, 6.875)

    def test_area_string(self):
        # Проверка площади треугольника для строки (ожидается ошибка TypeError)
        with self.assertRaises(TypeError):
            area("base", 4)

    def test_area_negative(self):
        # Проверка площади треугольника для отрицательных чисел (ожидается ValueError)
        with self.assertRaises(ValueError):
            area(-3, 4)

    def test_perimeter_integer(self):
        # Проверка периметра треугольника для целых чисел
        result = perimeter(3, 4, 5)
        self.assertEqual(result, 12)

    def test_perimeter_float(self):
        # Проверка периметра треугольника для дробных чисел
        result = perimeter(2.5, 3.5, 4.5)
        self.assertAlmostEqual(result, 10.5)

    def test_perimeter_string(self):
        # Проверка периметра треугольника для строки (ожидается ошибка TypeError)
        with self.assertRaises(TypeError):
            perimeter("side1", 4, 5)

    def test_perimeter_negative(self):
        # Проверка периметра треугольника для отрицательных чисел (ожидается ValueError)
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)


if __name__ == '__main__':
    unittest.main()
