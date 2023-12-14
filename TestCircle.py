import math
import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_0(self):
       res = area(0)
       self.assertEqual(res, 0)

    def test_area_1(self):
        res = area(100)
        self.assertNotEqual(res, 100*100*3,14)

    @unittest.expectedFailure
    def test_area_2(self):
        res = area('1')
        self.assertEqual(res, TypeError)

    def test_area_3(self):
       res = area(50)
       self.assertEqual(res, 50*50*math.pi)

    def test_perimeter_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_1_perimeter(self):
        res = perimeter(10000)
        self.assertEqual(res, 2*math.pi*10000)

if __name__ == '__main__':
    unittest.main()
    