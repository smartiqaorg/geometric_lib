import unittest

class triangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(15,0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10, 20)
        self.assertEqual(res, 100)

    def test_perimeter_mul(self):
        res = perimeter(14, 10, 56)
        self.assertEqual(res, 80)
def area(a, h):
#программа для расчёта площади треугольнка.
    return a * h / 2
#принимает высоту и основание треугольника и возвращает площадь.

def perimeter(a, b, c):
#программа для расчёта периметра треугольнка.
    return a + b + c
#принимает 3 стороны треугольника и возвращает периметр.