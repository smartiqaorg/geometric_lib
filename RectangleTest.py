import math
import unittest
import rectangle

class TestRectangleMethod(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(1,1), 1)
        self.assertEqual(rectangle.area(2/3,3/2), 1)
        self.assertEqual(rectangle.area(1000000,1/7), 1000000/7)
        self.assertEqual(rectangle.area(-1,-1), 0)
    def test_perimetr():
        self.assertEqual(rectangle.perimeter(1,1), 4)
        self.assertEqual(rectangle.perimeter(2/3,3/2), 13/3)
        self.assertEqual(rectangle.perimeter(1000000,1/7), 1400002/7)
        self.assertEqual(rectangle.perimeter(-1,-1), 0)

if __name__ == '__main__':
    unittest.main()
