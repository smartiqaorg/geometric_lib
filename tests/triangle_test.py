import unittest
from triangle import area
from triangle import perimeter
class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10,6)
        ans = perimeter(10,8,6)
        self.assertEqual(res, 30)
        self.assertEqual(ans, 24)

    def test_square_mul(self):
        res = area(20,10)
        ans = perimeter(10,14,16)
        self.assertEqual(res, 100)
        self.assertEqual(ans, 40)
if __name__ == "__main__":
   unittest.main()
