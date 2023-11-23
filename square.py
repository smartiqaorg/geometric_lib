import unittest
def area(a):
    return a * a


def perimeter(a):
    return 4 * a

class SquareTestCase(unittest.TestCase):

    def test_zero(self):
        res_p = perimeter(0)
        res_a = area(0)

        self.assertEqual(res_p, 0)
        self.assertEqual(res_a, 0)

    def test_work_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_work_square(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_negative_perimeter(self):
        res = perimeter(-15)
        self.assertEqual(res, -1)

    def test_negative_square(self):
        res = area(-15)
        self.assertEqual(res, -1)
