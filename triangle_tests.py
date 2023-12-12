import unittest
from triangle import *


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        # Проверка правильности вычисления площади треугольника
        side_length = 5
        height = 8
        expected_area = side_length * height / 2
        result = area(side_length, height)
        self.assertEqual(result, expected_area, f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {result}")

    def test_perimeter(self):
        # Проверка правильности вычисления периметра треугольника
        side_a = 5
        side_b = 7
        side_c = 10
        expected_perimeter = side_a + side_b + side_c
        result = perimeter(side_a, side_b, side_c)
        self.assertEqual(result, expected_perimeter, f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {result}")
