import unittest

from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4), 16)

    def test_area_another_side(self):
        self.assertEqual(area(5), 25)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)

    def test_perimeter_another_side(self):
        self.assertEqual(perimeter(5), 20)

if __name__ == "__main__":
    unittest.main()