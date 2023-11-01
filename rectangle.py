import unittest
class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res2 = perimeter(10, 0)
        res = area(10, 0)
        self.assertEqual(res, 0)
        self.assertEqual(res2, 0)
    def test_area_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_perimetr(self):
        res = perimeter(34, 15)
        self.assertEqual(res, 98)


def area(a, b):
#программа для расчёта площади прямоугольнка.
    return a * b
#принимает 2 стороны прямоугольнка и возвращает площадь.

def perimeter(a, b):
#программа для расчёта периметра прямоугольнка.
    if a == 0 or b == 0:
        return 0
    return a + b + a + b
#принимает 2 стороны прямоугольнка и возвращает периметр.