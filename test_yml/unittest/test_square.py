import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        """
        Tests the area function.
        """
        # Test for side a = 3
        self.assertAlmostEqual(area(3), 9)

        # Test for side a = 5
        self.assertAlmostEqual(area(5), 25)

        # Test for side a = 7
        self.assertAlmostEqual(area(7), 49)

    def test_perimeter(self):
        """
        Test the perimeter function with different input values.
        """
        # Test for side a = 3
        self.assertAlmostEqual(perimeter(3), 12)

        # Test for side a = 5
        self.assertAlmostEqual(perimeter(5), 20)

        # Test for side a = 7
        self.assertAlmostEqual(perimeter(7), 28)


if __name__ == '__main__':
    unittest.main()
