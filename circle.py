import math
#подключаем библиотеку math для вычислений с числом пи.
import unittest

class circleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_perimeter_mul(self):
        res = perimeter(15)
        self.assertEqual(res, 94.24777960769379)

def area(r):
#программа для расчёта площади круга.
    return math.pi * r * r
#принимает радиус круга и возвращает площадь.

def perimeter(r):
#программа для расчёта периметра круга.
    return 2 * math.pi * r
#принимает радиус и возвращает периметр.
