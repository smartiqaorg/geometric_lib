import unittest
from square import area, perimeter


class SquareTests(unittest.TestCase):
    #тест на работу функции нахождения площади квадрата с целочисленным параметром
    def test_area(self): 
        self.assertEqual(area(a = 7), 49)

    #тест на работу функции нахождения площади квадрата с вещественным параметром
    def test_area_float(self):
        self.assertAlmostEqual(area(a = 1.1), 1.21)

    #тест на работу функции нахождения площади квадрата с параметром равным 0
    def test_area_zero(self):
        self.assertEqual(area(a = 0), 0)

    #тест на работу функции нахождения периметра квадрата с целочисленным параметром
    def test_perimeter(self):
        self.assertEqual(perimeter(a = 7), 28)

    #тест на работу функции нахождения периметра квадрата с вещественным параметром
    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(a = 4.5), 18)

    #негативный тест на неправильных входных данных для площади
    def test_area_wrong_data(self):
        with self.assertRaises(ValueError):
            area(-5)

    #негативный тест на неправильных входных данных для периметра
    def test_perimeter_wrong_data(self):
            with self.assertRaises(ValueError):
                perimeter(-5)