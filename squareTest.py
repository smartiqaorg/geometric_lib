import math
import unittest
import square

class TestCircleMethod(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.area(2/3), 4/9)
        self.assertEqual(square.area(10000/7), 100000000/49)
        self.assertEqual(square.area(math.sqrt(3)), 3)
        self.assertEqual(square.area(-1), 0)
    def test_perimetr():
        self.assertEqual(square.perimeter(1), 4)
        self.assertEqual(square.perimeter(2/3), 4/3)
        self.assertEqual(square.perimeter(10000/7), 40000/7)
        self.assertEqual(square.perimeter(math.sqrt(3)), math.sqrt(48))
        self.assertEqual(square.perimeter(-1), 0)

if __name__ == '__main__':
    unittest.main()
