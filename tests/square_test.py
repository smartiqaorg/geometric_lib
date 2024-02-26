import unittest
from square import area
from square import perimeter
class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10), 100)
        self.assertEqual(perimeter(10), 40)
if __name__ == "__main__":
   unittest.main()
