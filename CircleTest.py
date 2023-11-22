import unittest
import circle
import math

class TestCircleMethod(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle.area(1), math.pi)
        self.assertEqual(circle.area(2/3), 4/9*math.pi)
        self.assertEqual(circle.area(1/math.sqrt(math.pi)), 1)
        self.assertEqual(circle.area(-1), 0)
    def test_perimetr():
        self.assertEqual(circle.perimeter(1), 2*math.pi)
        self.assertEqual(circle.perimeter(2/3), 4/3*math.pi)
        self.assertEqual(circle.perimeter(1/math.pi), 2)
        self.assertEqual(circle.perimeter(-1), 0)

if __name__ == '__main__':
    unittest.main()
