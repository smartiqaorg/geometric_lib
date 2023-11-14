import unittest
from rectangle import area, perimeter
'''
Test for rectangle
'''
class RectangleTestCase(unittest.TestCase):
    def test_zero_dimensions(self):
        res_area = area(0, 0)
        res_perimeter = perimeter(0, 0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_dimensions(self):
        res_area = area(4, 5)
        res_perimeter = perimeter(4, 5)
        self.assertEqual(res_area, 20)
        self.assertEqual(res_perimeter, 18)

if __name__ == '__main__':
    unittest.main()