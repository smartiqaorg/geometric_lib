import unittest

def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
    def test_square_mul1(self):
        res1 = area(10, 0)
        self.assertEqual(res1, 0)

    def test_square_mul2(self):
        with self.assertRaises(Exception):
            area(-10, 11)

    def test_square_mul3(self):
        res3 = area(5, 55.55)
        self.assertEqual(res3, 277.75)

    def test_square_mul4(self):
        res4 = area(100, 100)
        self.assertEqual(res4, 10000)

    def test_square_mul5(self):
        res5 = area(25, 25)
        self.assertEqual(res5, 625)

    def test_perimeter_mul1(self):
        res1 = perimeter(10, 0)
        self.assertEqual(res1, 20)

    def test_perimeter_mul2(self):
        with self.assertRaises(Exception):
            perimeter(-7, 10)

    def test_perimeter_mul3(self):
        res3 = perimeter(5, 5)
        self.assertEqual(res3, 20)

    def test_perimeter_mul4(self):
        res4 = perimeter(100, 100)
        self.assertEqual(res4, 400)

    def test_perimeter_mul5(self):
        res5 = perimeter(25, 25.25)
        self.assertEqual(res5, 100.5)