import unittest

from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 3), 6)

    def test_area_another_triangle(self):
        self.assertEqual(area(6, 4), 12)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_another_triangle(self):
        self.assertEqual(perimeter(5, 5, 6), 16)

if __name__ == "__main__":
    unittest.main()