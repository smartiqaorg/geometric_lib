import unittest

def area(a):
    '''Принимает число a(сторона квадрата), возвращает площадь квадрата a * a'''
    return a * a


def perimeter(a):
    '''Принимает число a(сторона квадрата), возвращает периметр квадрата 4 * a'''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
       res = area(10)
       self.assertEqual(res, 100)
    def test_square_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

