import unittest
from square import area, perimeter
'''
Test for square
'''
class SquareTestCase(unittest.TestCase):
    def test_zero_side(self):
        res_area = area(0)
        res_perimeter = perimeter(0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_side(self):
        res_area = area(3)
        res_perimeter = perimeter(3)
        self.assertEqual(res_area, 9)
        self.assertEqual(res_perimeter, 12)

if __name__ == '__main__':
    unittest.main()