import unittest
def area(a, b):
    '''
    Возвращает произведение двух чисел.
    :param a: первое десятичное число.
    :param b: второе десятичное число.
    :return: число, состоящее из произведения a и b.
    '''
    return a * b 

def perimeter(a, b):
    '''
    Возвращает удвоенную сумму двух чисел.
    :param a: первое десятичное число.
    :param b: второе десятичное число.
    :return: число, состоящее из произведения суммы чисел a и b.
    '''
    return 2*(a + b)

class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        with self.assertRaises(ValueError) as context:
            res = area(-3, -34)
        self.assertRaises(TypeError, res)

    def test_area1(self):
        res1 = area(10, 0)
        self.assertEqual(res1, 0)

    def test_area2(self):
        res2 = area(42, 5)
        self.assertEqual(res2, 210)
    def test_area3(self):
        res3 = area(13.555, 23.01)
        self.assertEqual(res3, 311.90055)
    def test_perimeter1(self):
        res1 = perimeter(10, 10)
        self.assertEqual(res1, 40)

    def test_perimeter2(self):
        res2 = perimeter(13.555, 23.01)
        self.assertEqual(res2, 73.13)

    def test_perimeter3(self):
        res3 = perimeter(0, 0)
        self.assertEqual(res3, 0)