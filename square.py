import unittest

def area(side: float) -> float | bool:
    '''
    Given the side of a square, calculates area
    '''
    if side < 0:
        return False
    return side * side


def perimeter(side: float) -> float | bool:
    '''
    Given the side of a square, calculates perimeter
    '''
    if side <= 0:
        return False
    return 4 * side

class SquareTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_pos_mul(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_neg_mul(self):
        res = area(-3)
        self.assertFalse(res)

    def test_perimeter_zero_add(self):
        res = perimeter(0)
        self.assertFalse(res)

    def test_perimeter_pos_add(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_neg_add(self):
        res = perimeter(-3)
        self.assertFalse(res)
