import unittest

class SquareTestCase(unittest.TestCase):
    # тесты для функции area()
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_int_mul(self):
        res = area(12)
        self.assertEqual(res, 144)

    def test_minus_mul(self):
        res = area(-5)
        self.assertEqual(res, -1, "радиус > 0")

    def test_mater_mul(self):
        res = area(4.9)
        self.assertEqual(res, 24.01)

    def test_mater2_mul(self):
        res = area(5.5)
        self.assertEqual(res, 30.25)


    #тесты для функции perimeter()
    def test_int_perimeter_mul(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_int2_perimeter_mul(self):
        res = perimeter(16)
        self.assertEqual(res, 64)
    
    def test_minus_perimeter_mul(self):
        res = perimeter(-3)
        self.assertEqual(res, -1, "радиус > 0")

    def test_mater_perimeter_mul(self):
        res = perimeter(5.0000)
        self.assertEqual(res, 20.0)
    
    def test_stroka_mul(self):
        res = area("4")
        self.assertEqual(res, -1, "на вход подана строка")



def area(a):
    return a * a


def perimeter(a):
    return 4 * a
