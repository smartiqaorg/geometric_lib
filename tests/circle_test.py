import unittest
from circle import area, perimeter
'''
Test for circle
'''
class CircleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        res_area = area(0)
        res_perimeter = perimeter(0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_radius(self):
        res_area = area(5)
        res_perimeter = perimeter(5)
        self.assertEqual(res_area, 78.54)
        self.assertEqual(res_perimeter, 31.42)

if __name__ == '__main__':
    unittest.main()