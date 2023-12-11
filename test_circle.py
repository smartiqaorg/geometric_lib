import math
import unittest

class CircleTestCase(unittest.TestCase):
    # тесты для функции area()
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_int_mul(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_int2_mul(self):
        res = area(14)
        self.assertEqual(res, 615.7521601035994)

    def test_minus_mul(self):
        res = area(-5)
        self.assertEqual(res, -1, "радиус > 0")

    def test_mater_mul(self):
        res = area(6.6)
        self.assertEqual(res, 136.8477759903714)

    def test_stroka_mul(self):
        res = area("abcd")
        self.assertEqual(res, -1, "на вход подана строка")
        
    

    #тесты для функции perimeter()
    def test_int_perimeter_mul(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_int2_perimeter_mul(self):
        res = perimeter(120)
        self.assertEqual(res, 753.9822368615503)
    
    def test_int3_perimeter_mul(self):
        res = perimeter(1000000)
        self.assertEqual(res, 6283185.307179586)

    def test_minus_perimeter_mul(self):
        res = perimeter(-3)
        self.assertEqual(res, -1, "радиус > 0")

    def test_mater_perimeter_mul(self):
        res = perimeter(8.981)
        self.assertEqual(res, 56.42928724377986)




def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

