import unittest
from triangle import area, perimeter
'''
Test for triangle
'''
class TriangleTestCase(unittest.TestCase):
    def test_zero_sides(self):
        res_area = area(0, 0)
        res_perimeter = perimeter(0, 0, 0)
        self.assertEqual(res_area, 0)
        self.assertEqual(res_perimeter, 0)

    def test_valid_sides(self):
        res_area = area(3, 4)
        res_perimeter = perimeter(3, 4, 5)
        self.assertEqual(res_area, 6)
        self.assertEqual(res_perimeter, 12)

if __name__ == '__main__':
    unittest.main()