import unittest


def area(a, h):
    """
        Принимает a,h - сторона треугольника, высота опущенная на заданную сторону соответственно. Возвращает площадь заданного треугольника
        Вход: 3 6 Выход: 9
    """
    return a * h / 2


def perimeter(a, b, c):
    """
        Принимает a,b,c - три стороны треугольника. Возвращает периметр заданного треугольника
        Вход: 1 2 3 Выход: 6
    """
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_h_area(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_big_area(self):
        res = area(10000000000, 10000000000)
        self.assertEqual(res, 50000000000000000000)

    def test_negative_perimeter(self):
        res = perimeter(-1, -2, -3)
        self.assertEqual(res, -6)

    def test_common_perimeter(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)
