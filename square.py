import unittest

def area(a):
    return a * a

def perimeter(a):
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_square_mul(self):
        res1 = area(0)
        self.assertEqual(res1, 0)

        res2 = area(1)
        self.assertEqual(res2, 1)

        res3 = area(-5)
        self.assertEqual(res3, "error")

        res4 = area(100)
        self.assertEqual(res4, 10000)

        res5 = area(25)
        self.assertEqual(res5, 625)

    def test_perimeter_mul(self):
        res1 = perimeter(0)
        self.assertEqual(res1, 0)

        res2 = perimeter(1)
        self.assertEqual(res2, 4)

        res3 = perimeter(5)
        self.assertEqual(res3, 20)

        res4 = perimeter(-1100)
        self.assertEqual(res4, "error")

        res5 = perimeter(25)
        self.assertEqual(res5, 100)