import unittest
from rectangle import area, perimeter


class RectangleTests(unittest.TestCase):
    #тест на работу функции нахождения площади прямоугольника с целочисленными параметрами
    def test_area(self): 
        self.assertEqual(area(a = 7, b = 4), 28)

    #тест на работу функции нахождения площади прямоугольника с вещественными параметрами
    def test_area_float(self):
        self.assertAlmostEqual(area(a = 4, b = 2.5), 10)

    #тест на работу функции нахождения площади прямоугольника с одним из параметров равным 0
    def test_area_zero(self):
        self.assertEqual(area(a = 7, b = 0), 0)

    #тест на работу функции нахождения периметра прямоугольника с целочисленными параметрами
    def test_perimeter(self):
        self.assertEqual(perimeter(a = 7, b = 4), 22)

    #тест на работу функции нахождения периметра прямоугольника с вещественными параметрами
    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(a = 7, b = 4.5), 23)

    #негативный тест на направильных входных данных для площади
    def test_area_wrong_data(self):
        with self.assertRaises(ValueError):
            area(-5, -6)

    #негативный тест на направильных входных данных для периметра
    def test_perimeter_wrong_data(self):
            with self.assertRaises(ValueError):
                perimeter(-5, -6)