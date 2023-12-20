import math
import unittest
import triangle

class TestTriangleMethod(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(1,2), 1)
        self.assertEqual(triangle.area(math.sqrt(2),math.sqrt(2)), 1)
        self.assertEqual(triangle.area(-14,-12), 0)
    def test_perimetr():
        self.assertEqual(triangle.perimeter(1,3,3), 7)
        self.assertEqual(triangle.perimeter(1,10,100), 0)
        self.assertEqual(triangle.perimeter(-3,1,1), 0)

if __name__ == '__main__':
    unittest.main()
