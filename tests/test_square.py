import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area_integer(self):
        # Проверка площади квадрата для целого числа
        result = area(5)
        self.assertEqual(result, 25)

    def test_area_float(self):
        # Проверка площади квадрата для дробного числа
        result = area(3.5)
        self.assertAlmostEqual(result, 12.25)

    def test_area_string(self):
        # Проверка площади квадрата для строки (ожидается ошибка TypeError)
        with self.assertRaises(TypeError):
            area("length")

    def test_area_negative(self):
        # Проверка площади квадрата для отрицательного числа (ожидается ValueError)
        with self.assertRaises(ValueError):
            area(-2)

    def test_perimeter_integer(self):
        # Проверка периметра квадрата для целого числа
        result = perimeter(5)
        self.assertEqual(result, 20)

    def test_perimeter_float(self):
        # Проверка периметра квадрата для дробного числа
        result = perimeter(3.5)
        self.assertAlmostEqual(result, 14)

    def test_perimeter_string(self):
        # Проверка периметра квадрата для строки (ожидается ошибка TypeError)
        with self.assertRaises(TypeError):
            perimeter("length")

    def test_perimeter_negative(self):
        # Проверка периметра квадрата для отрицательного числа (ожидается ValueError)
        with self.assertRaises(ValueError):
            perimeter(-2)


if __name__ == '__main__':
    unittest.main()
