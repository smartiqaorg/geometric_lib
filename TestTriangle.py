import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_0(self):
       res = area(10, 5)
       self.assertEqual(res, 25)

    def test_area_1(self):
        res = area(100, 5)
        self.assertNotEqual(res, ((100*5) / 2) + 1)

    @unittest.expectedFailure
    def test_area_2(self):
        res = area('23', "12")
        self.assertEqual(res, TypeError)

    def test_area_3(self):
       res = area(1000, 100)
       self.assertEqual(res, (1000 * 100) / 2)

    def test_perimeter_0(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_1_perimeter(self):
        res = perimeter(100, 100, 99)
        self.assertEqual(res, 100 + 100 + 99)

if __name__ == '__main__':
    unittest.main()