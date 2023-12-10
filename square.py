import unittest

def area(a):
    return a * a

def perimeter(a):
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_square_mul1(self):
        res1 = area(0)
        self.assertEqual(res1, 0)

    def test_square_mul2(self):
        res1 = area(1)
        self.assertEqual(res1, 1)

    def test_square_mul3(self):
        with self.assertRaises(Exception):
            area(-7)

    def test_square_mul4(self):
        res4 = area(107.256)
        self.assertEqual(res4, 11503.849536)

    def test_square_mul5(self):
        res5 = area(25)
        self.assertEqual(res5, 625)

    def test_perimeter_mul1(self):
        res1 = perimeter(0)
        self.assertEqual(res1, 0)

    def test_perimeter_mul2(self):
        res2 = perimeter(1)
        self.assertEqual(res2, 4)

    def test_perimeter_mul3(self):
        res3 = perimeter(5)
        self.assertEqual(res3, 20)

    def test_perimeter_mul4(self):
        with self.assertRaises(Exception):
            perimeter(-10)

    def test_perimeter_mul5(self):
        res5 = perimeter(25.28)
        self.assertEqual(res5, 101.12)