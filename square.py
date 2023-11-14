import unittest
def area(a):
    return a * a


def perimeter(a):
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_5(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_perimetr_one(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimetr_twenty(self):
        res = perimeter(20)
        self.assertEqual(res, 80)