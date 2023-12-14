import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_0(self):
       res = area(10)
       self.assertEqual(res, 100)

    def test_area_1(self):
        res = area(15)
        self.assertNotEqual(res, (15*15) + 1)

    @unittest.expectedFailure
    def test_area_2(self):
        res = area('2')
        self.assertEqual(res, TypeError)

    def test_area_3(self):
       res = area(50)
       self.assertEqual(res, 50*50)

    def test_perimeter_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_1_perimeter(self):
        res = perimeter(100)
        self.assertEqual(res, 100*4)

if __name__ == '__main__':
    unittest.main()