def area(a, h):
    ''' принимает значение а,h. а возвращает площадь треугольника со стороной а и высотоой h'''
    return a * h / 2
def perimeter(a, b, c):
    ''' принимает значение а, b, c. а возвращает периметр треугольника со сторонами а, b, c'''
    return a + b + c

import unittest

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
