import unittest
from triangle import perimeter, area


class TestTriangle(unittest.TestCase):

    def test_calculate_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_calculate_area(self):
        self.assertEqual(area(6, 4), 12)
        self.assertEqual(area(3, 6), 9)


if __name__ == '__main__':
    unittest.main()