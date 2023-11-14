import unittest
def area(a):
    '''
    Возвращает площадь квадрата со стороной a (число)

        Параметры:
            a - длина стороны (число)

        Возвращаемое значение:
            Произведение  a * a, то есть плозодь квадрата
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата со длиной стороны a (число)

        Параметры:
            a - длина стороны (число)

        Возвращаемое значение:
            произведение а на 4, то есть периметр квадрата.
    '''
    return 4 * a

class SquaretestCase(unittest.TestCase):

    def test_per_1(self):
        res = perimeter(1)
        self.assertEqual(res, 4 * 1)

    def test_per_2(self):
        res = perimeter(2)
        self.assertEqual(res, 4 * 2)

    def test_per_3(self):
        res = perimeter(3)
        self.assertEqual(res, 4 * 3)

    def test_per_4(self):
        res = perimeter(4)
        self.assertEqual(res, 4 * 4)

    def test_per_5(self):
        res = perimeter(5)
        self.assertEqual(res, 4 * 5)

    def test_area_1(self):
        res = area(1)
        self.assertEqual(res, 1 * 1)

    def test_area_2(self):
        res = area(2)
        self.assertEqual(res, 2 * 2)

    def test_area_3(self):
        res = area(3)
        self.assertEqual(res, 3 * 3)

    def test_area_4(self):
        res = area(4)
        self.assertEqual(res, 4 * 4)

    def test_area_5(self):
        res = area(5)
        self.assertEqual(res, 5 * 5)
