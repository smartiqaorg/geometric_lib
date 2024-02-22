import unittest
def area(a, h):
    '''
    Возвращает произведение двух чисел разделенное на два.
    :param a: первое десятичное число.
    :param h: второе десятчное число.
    :return: число, состоящее из произведения a и b, разделенного на 2.
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Возвращает сумму трех чисел.
    :param a: первое десятичное число.
    :param b: второе десятичное число.
    :param c: третье десятичное число.
    :return: число, состоящее из суммы чисел a, b и c.
    '''
    return a + b + c

class TriangleTestCase(unittest.TestCase):

    def test_area1(self):
        with self.assertRaises(ValueError) as context:
            res = area(-4, -2)
        self.assertRaises(ValueError, res)
    def test_area1(self):
        res = area(87534, 1)
        self.assertEqual(res, 43767)

    def test_area2(self):
        res = area(42, 5)
        self.assertEqual(res, 105)

    def test_area3(self):
        res = area(0.65, 0.444444444)
        self.assertEqual(res, 0.1444444443)

    def test_perimeter1(self):
        res = perimeter(13.33, 23.635, 3)
        self.assertEqual(res, 39.965)

    def test_perimeter2(self):
        res = perimeter(42, 5, 2)
        self.assertEqual(res, 49)

    def test_perimeter3(self):
        res = perimeter(0.111, 1.4, 0.3452)
        self.assertEqual(res, 1.8562)