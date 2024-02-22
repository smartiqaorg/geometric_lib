import math
import unittest
def area(r):
    '''
    Возвращает произведение квадрата r на pi.
    :param r: десятичное число.
    :return: число, состоящее из произведения r на r на Pi.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает удвоенное произведение двух чисел.
    :param r: десятичное число.
    :return: число, состоящее из произведение 2 на число pi на r.
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):

    def test_area(self):
        with self.assertRaises(ValueError) as context:
            res = area(-10)
        self.assertRaises(TypeError, res)

    def test_area1(self):
        res = area(10)
        self.assertEqual(res, 314.15927)

    def test_area2(self):
        res = area(42)
        self.assertEqual(res, 5541.76944)

    def test_area3(self):
        res = area(13)
        self.assertEqual(res, 530.92916)

    def test_perimeter1(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185)

    def test_perimeter2(self):
        res = perimeter(42)
        self.assertEqual(res, 263.89378)

    def test_perimeter3(self):
        res = perimeter(13)
        self.assertEqual(res, 81.68141)