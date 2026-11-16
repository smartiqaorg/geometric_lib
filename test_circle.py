import unittest
import math
from circle import area, perimeter

class CircleTests(unittest.TestCase):
    #тест на работу функции нахождения площади круга с целочисленными параметрами
    def test_area(self): 
        self.assertAlmostEqual(area(r = 2), math.pi * 4)

    #тест на работу функции нахождения площади круга с вещественными параметрами
    def test_area_float(self):
        self.assertAlmostEqual(area(r = 1.1), math.pi * 1.21)

    #тест на работу функции нахождения площади круга с параметром равным 0
    def test_area_zero(self):
        self.assertEqual(area(r = 0), 0)

    #тест на работу функции нахождения периметра круга с целочисленными параметрами
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(r = 3), 6 * math.pi)

    #тест на работу функции нахождения периметра круга с вещественными параметрами
    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(r = 2.5), 5 * math.pi)

    #негативный тест на неправильных входных данных для площади
    def test_area_wrong_data(self):
        with self.assertRaises(ValueError):
            area(r = -6)

    #негативный тест на неправильных входных данных для периметра
    def test_perimeter_wrong_data(self):
            with self.assertRaises(ValueError):
                perimeter(r = -5)
