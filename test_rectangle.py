import unittest
from rectangle import area
from rectangle import perimeter

class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(5, 2)
        self.assertEqual(res, 10)

    def test_2_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            area(-5, 2)
    

    def test_1_perimeter(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_2_perimeter(self):
        res = perimeter(2, 0)
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()
