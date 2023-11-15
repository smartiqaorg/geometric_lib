import unittest
def area(a):
    return a * a
# принимает на вход значение стороны квадрата, выводит площадь квадрата

def perimeter(a):
    return 4 * a
# принимает на вход значение стороны квадрата, выводит периметр квадрата

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res,0)

    def test_self_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_self_per(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
