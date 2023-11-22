import unittest


def area(a):
    """
        Принимает n - сторону квадрата. Возвращает площадь квадрата с заданной стороной
        Вход: 5 Выход: 25
    """
    return a * a


def perimeter(a):
    """
        Принимает n - сторону квадрата. Возвращает периметр квадрата с заданной стороной
        Вход: 5 Выход: 20
    """
    return 4 * a


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_big_area(self):
        res = area(10000000000)
        self.assertEqual(res, 100000000000000000000)

    def test_negative_perimeter(self):
        res = perimeter(-100)
        self.assertEqual(res, -400)

    def test_zero_perimeter(self):
        res = area(0)
        self.assertEqual(res, 0)
