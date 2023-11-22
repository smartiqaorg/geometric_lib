import math
import unittest


def area(r):
    """
        Принимает r - радиус круга, возвращает площадь
        Вход: 2 Выход: 12,56
    """
    return math.pi * r * r


def perimeter(r):
    """
        Принимает r - радиус окружности, возвращает длину окружности
        Вход: 3 Выход: 18,84
    """
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_big_area(self):
        res = area(10000000000)
        self.assertEqual(res, 314159265358979323846.26433832795)

    def test_negative_perimeter(self):
        res = perimeter(-100)
        self.assertAlmostEqual(res, -628.31, delta=0.01)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
