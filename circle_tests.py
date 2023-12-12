import unittest
import math

from circle import *


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        # Проверка правильности вычисления площади круга
        radius = 5
        expected_area = math.pi * radius * radius
        result = area(radius)
        self.assertEqual(result, expected_area, f"Ожидаемая площадь: {expected_area}, Фактическая площадь: {result}")

    def test_perimeter(self):
        # Проверка правильности вычисления периметра круга
        radius = 5
        expected_perimeter = 2 * math.pi * radius
        result = perimeter(radius)
        self.assertEqual(result, expected_perimeter, f"Ожидаемый периметр: {expected_perimeter}, Фактический периметр: {result}")
