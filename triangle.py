import unittest
def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_two_and_two(self):
        res = area(2, 2)
        self.assertEqual(res, 2)

    def test_area_one_and_four(self):
        res = area(1, 4)
        self.assertEqual(res, 2)

    def test_perimetr_one_two_three(self):
        res = perimeter(1,2,3)
        self.assertEqual(res, 6)

    def test_perimetr_three_three_three(self):
        res = perimeter(3,3,3)
        self.assertEqual(res, 9)