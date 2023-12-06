import unittest

def area(a):
    '''Принимает сторону квадрата (a), возвращает его площадь.'''
    return a * a


def perimeter(a):
    '''Принимает сторону квадрата (a), возвращает его периметр.'''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_area_int(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_perimeter_int(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 'error')

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 'error')

    def test_area_negative(self):
        res = area(-8)
        self.assertEqual(res, 'error')

    def test_perimeter_negative(self):
        res = perimeter(-8)
        self.assertEqual(res, 'error')

    def test_area_float(self):
        res = area(3.6)
        self.assertEqual(res, 12.96)

    def test_perimeter_float(self):
        res = perimeter(3.6)
        self.assertEqual(res, 14.4)
