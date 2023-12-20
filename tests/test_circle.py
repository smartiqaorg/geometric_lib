import unittest
from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area_integer(self):
        # Проверка площади круга для целого числа
        result = area(5)
        self.assertAlmostEqual(result, 78.53981633974483)

    def test_area_float(self):
        # Проверка площади круга для дробного числа
        result = area(3.5)
        self.assertAlmostEqual(result, 38.48451000647496)

    def test_area_string(self):
        # Проверка площади круга для строки (ожидается ошибка TypeError)
        with self.assertRaises(TypeError):
            area("radius")

    def test_area_negative(self):
        # Проверка площади круга для отрицательного числа (ожидается ValueError)
        with self.assertRaises(ValueError):
            area(-2)

    def test_perimeter_integer(self):
        # Проверка длины окружности для целого числа
        result = perimeter(5)
        self.assertAlmostEqual(result, 31.41592653589793)

    def test_perimeter_float(self):
        # Проверка длины окружности для дробного числа
        result = perimeter(3.5)
        self.assertAlmostEqual(result, 21.991148575128552)

    def test_perimeter_string(self):
        # Проверка длины окружности для строки (ожидается ошибка ValueError)
        with self.assertRaises(TypeError):
            perimeter("radius")

    def test_perimeter_negative(self):
        # Проверка длины окружности для отрицательного числа (ожидается TypeError)
        with self.assertRaises(TypeError):
            perimeter(-2)


if __name__ == '__main__':
    unittest.main()
