import math
import unittest


def area(r):
    '''
    Возвращает площадь круга с радиусом r (число)

        Параметры :
            r - радиус круга (число)

        Возращаемое значение:
            Произведение Числа Пи на квадрат радиуса (r), то есть площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности с радиусом r

        Параметры:
            r - радиус окружности (число)

        Возращаемое значение:
            произведение 2 на Число Пи на радиус (r), то есть длина окружности.
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(1)
        self.assertEqual(res, math.pi * (1**2), "area1_FAIL")

    def test_area_2(self):
        res = area(2)
        self.assertEqual(res, math.pi * (2**2),"area2_FAIL")

    def test_area_3(self):
        res = area(3)
        self.assertEqual(res, math.pi * (3 ** 2), "area3_FAIL")

    def test_area_4(self):
        res = area(4)
        self.assertEqual(res, math.pi * (4 ** 2), "area4_FAIL")

    def test_area_5(self):
        res = area(5)
        self.assertEqual(res, math.pi * (5 ** 2), "area5_FAIL")

    def test_per_1(self):
        res = perimeter(1)
        self.assertEqual(res, 2 * math.pi * 1)

    def test_per_2(self):
        res = perimeter(2)
        self.assertEqual(res, 2 * math.pi * 2)

    def test_per_3(self):
        res = perimeter(3)
        self.assertEqual(res, 2 * math.pi * 3)

    def test_per_4(self):
        res = perimeter(4)
        self.assertEqual(res, 2 * math.pi * 4)

    def test_per_5(self):
        res = perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)











