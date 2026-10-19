import unittest
from triangle import area, perimeter


class TriangleTests(unittest.TestCase):
    #тест на работу функции нахождения площади треугольника с целочисленными параметрами
    def test_area(self): 
        self.assertEqual(area(a = 6, h = 4), 12)

    #тест на работу функции нахождения площади треугольника с вещественными параметрами
    def test_area_float(self):
        self.assertAlmostEqual(area(a = 2.5, h = 4), 5)

    #тест на работу функции нахождения площади треугольника с параметром равным 0
    def test_area_zero(self):
        self.assertEqual(area(a = 0, h = 5), 0)

    #тест на работу функции нахождения периметра треугольника с целочисленными параметрами
    def test_perimeter(self):
        self.assertEqual(perimeter(a = 3, b = 4, c = 5), 12)

    #тест на работу функции нахождения периметра треугольника с вещественными параметрами
    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(a = 2.5, b = 3.5, c = 4), 10)

    #негативный тест на неправильных входных данных для площади
    def test_area_wrong_data(self):
        with self.assertRaises(ValueError):
            area(a = -6, h = 4)

    #негативный тест на неправильных входных данных для периметра
    def test_perimeter_wrong_data(self):
        with self.assertRaises(ValueError):
            perimeter(a = -5, b = -4, c = -3)

    def test_perimeter_not_triangle(self):
            with self.assertRaises(ValueError):
                perimeter(a = 1, b = 2, c = 1000)