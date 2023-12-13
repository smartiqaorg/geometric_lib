import unittest
from square import perimeter, area

class TestSquare(unittest.TestCase):

    def test_square_perimeter(self):
        side_length = 7
        expected_perimeter = 4 * side_length
        self.assertEqual(perimeter(side_length), expected_perimeter)

    def test_square_area(self):
        side_length = 6
        expected_area = side_length ** 2
        self.assertEqual(area(side_length), expected_area)

if __name__ == '__main__':
    unittest.main()
