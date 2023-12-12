import unittest
from square import *


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        # Проверка правильности вычисления площади квадрата
        side_length = 5
        expected_area = side_length * side_length
        result = area(side_length)
        self.assertEqual(result, expected_area, f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {result}")

    def test_perimeter(self):
        # Проверка правильности вычисления периметра квадрата
        side_length = 5
        expected_perimeter = 4 * side_length
        result = perimeter(side_length)
        self.assertEqual(result, expected_perimeter,f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {result}")
