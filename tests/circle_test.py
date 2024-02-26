import unittest
from circle import area
from circle import perimeter
class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10), 314.1592653589793)
        self.assertEqual(perimeter(10), 62.83185307179586)
if __name__ == "__main__":
   unittest.main()
