import unittest
from rectangle import area, perimeter



class TestRectangle(unittest.TestCase):
    def test_area_integer(self):
        # Проверка площади прямоугольника для целых чисел
        result = area(5, 10)
        self.assertEqual(result, 50)

    def test_area_float(self):
        # Проверка площади прямоугольника для дробных чисел
        result = area(3.5, 2.5)
        self.assertAlmostEqual(result, 8.75)

    def test_area_string(self):
        # Проверка площади прямоугольника для строки (ожидается ошибка TypeError)
        with self.assertRaises(TypeError):
            area("length", 5)

    def test_area_negative(self):
        # Проверка площади прямоугольника для отрицательных чисел (ожидается ValueError)
        with self.assertRaises(ValueError):
            area(-2, 4)

    def test_perimeter_integer(self):
        # Проверка периметра прямоугольника для целых чисел
        result = perimeter(5, 10)
        self.assertEqual(result, 30)

    def test_perimeter_float(self):
        # Проверка периметра прямоугольника для дробных чисел
        result = perimeter(3.5, 2.5)
        self.assertAlmostEqual(result, 12)

    def test_perimeter_string(self):
        # Проверка периметра прямоугольника для строки (ожидается ошибка TypeError)
        with self.assertRaises(TypeError):
            perimeter("length", 5)

    def test_perimeter_negative(self):
        # Проверка периметра прямоугольника для отрицательных чисел (ожидается ValueError)
        with self.assertRaises(ValueError):
            perimeter(-2, 4)


if __name__ == '__main__':
    unittest.main()
