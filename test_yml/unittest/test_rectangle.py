import unittest
from rectangle import area, perimeter


class TestRectangleFunctions(unittest.TestCase):
    def test_area(self):
        """
        Test the area function.
        """
        # Test for sides a = 3, b = 4
        self.assertAlmostEqual(area(3, 4), 12)
        # Test for sides a = 5, b = 7
        self.assertAlmostEqual(area(5, 7), 35)
        # Test for sides a = 2, b = 6
        self.assertAlmostEqual(area(2, 6), 12)

    def test_perimeter(self):
        """
        Test the perimeter function.
        """
        # Test for sides a = 3, b = 4
        self.assertAlmostEqual(perimeter(3, 4), 14)
        # Test for sides a = 5, b = 7
        self.assertAlmostEqual(perimeter(5, 7), 24)
        # Test for sides a = 2, b = 6
        self.assertAlmostEqual(perimeter(2, 6), 16)


if __name__ == '__main__':
    unittest.main()