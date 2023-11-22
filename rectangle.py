import unittest

def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
    def test_square_mul(self):
        res1 = area(10, 0)
        self.assertEqual(res1, 0)

        res2 = area(10, 1)
        self.assertEqual(res2, 10)

        res3 = area(5, 5)
        self.assertEqual(res3, 25)

        res4 = area(100, 100)
        self.assertEqual(res4, 10000)

        res5 = area(25, 25)
        self.assertEqual(res5, 625)

    def test_perimeter_mul(self):
        res1 = perimeter(10, 0)
        self.assertEqual(res1, 20)

        res2 = perimeter(10, 1)
        self.assertEqual(res2, 22)

        res3 = perimeter(5, 5)
        self.assertEqual(res3, 20)

        res4 = perimeter(100, 100)
        self.assertEqual(res4, 400)

        res5 = perimeter(25, 25)
        self.assertEqual(res5, 100)