import unittest


def area(a, b):
    """
        Принимает длины сторон прямоугольника - a,b. Возвращает площадь прямоугольника с данными сторонами
        Вход: 3 4 Выход: 12
    """
    return a * b


def perimeter(a, b):
    """
        Принимает длины сторон прямоугольника - a,b. Возвращает периметр прямоугольника с данными сторонами
        Вход: 2 5 Выход: 14
    """
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_big_mul(self):
        res = area(10000000000, 10000000000)
        self.assertEqual(res, 100000000000000000000)

    def test_negative_sum(self):
        res = perimeter(-100, -150)
        self.assertEqual(res, -500)

    def test_zero_sum(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
