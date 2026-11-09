import unittest

def area(a_size: float, b_size: float) -> float | bool:
    '''
    Given the a_size and b_size of a rectangle, calculates area
    '''
    if a_size < 0 or b_size < 0:
        return False;
    return a_size * b_size


def perimeter(a_size: float, b_size: float) -> float | bool:
    '''
    Given the a_size and b_size of a rectangle, calculates perimeter
    '''
    if a_size <= 0 or b_size <= 0:
        return False;
    return 2 * (a_size + b_size)

class RectangleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        res = area(1, 0)
        self.assertEqual(res, 0)

    def test_area_square_mul(self):
        res = area(2, 2)
        self.assertEqual(res, 4)

    def test_area_pos_mul(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_area_neg_mul(self):
        res = area(-3, 2)
        self.assertFalse(res)

    def test_perimeter_zero_add(self):
        res = perimeter(1, 0)
        self.assertFalse(res)

    def test_perimeter_square_add(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_perimeter_pos_add(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_neg_add(self):
        res = perimeter(-3, 2)
        self.assertFalse(res)
