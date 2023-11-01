import unittest

class squareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(7)
        self.assertEqual(res, 49)

    def test_perimeter_mul(self):
        res = perimeter(15)
        self.assertEqual(res, 60)
def area(a):
#программа для расчёта площади квадрата.
    return a * a
#принимает сторону квадрата и возвращает площадь.


def perimeter(a):
#программа для расчёта периметра квадрата.
    return 4 * a
#принимает сторону квадрата и возвращает периметр.