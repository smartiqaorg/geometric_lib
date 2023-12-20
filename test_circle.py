import unittest
import math
from circle import area
from circle import perimeter
class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5)
        self.assertEqual(res, math.pi * 25)

    def test_2_area(self):
        res = area(13)
        self.assertEqual(res, math.pi * 169)
        
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-13)
    


    def test_1_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, math.pi * 6)

    def test_2_perimeter(self):
        res = perimeter(30)
        self.assertEqual(res, math.pi * 60)

if __name__ == '__main__':
    unittest.main()
