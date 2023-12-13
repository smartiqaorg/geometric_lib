import unittest
from rectangle import perimeter, area


class TestRectangle(unittest.TestCase):

    def test_calculate_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(5, 5), 20)

    def test_calculate_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(5, 5), 25)


if __name__ == '__main__':
    unittest.main()