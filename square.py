import unittest
def area(a):
    '''
    Возвращает квадрат числа.
    :param a: десятичное числою.
    :return: число, состоящее из произведения числа а на само себя.
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает число а, увеличенное в два раза.
    :param a: десятичное число.
    :return: число, состоящее из произведения чисел 4 и a.
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        with self.assertRaises(ValueError) as context:
            res = area(-3)
        self.assertRaises(TypeError, res)

    def test_area1(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area2(self):
        res = area(42)
        self.assertEqual(res, 1764)

    def test_area3(self):
        res = area(0.99)
        self.assertEqual(res, 0.9801)

    def test_perimeter1(self):
        res = perimeter(8754)
        self.assertEqual(res, 35016)

    def test_perimeter2(self):
        res = perimeter(1.4549)
        self.assertEqual(res, 5.8196)

    def test_perimeter3(self):
        res = perimeter(42)
        self.assertEqual(res, 168)


