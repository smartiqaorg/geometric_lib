import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        """
        Test the area function.
        """
        # Test for side a = 3, height = 4
        self.assertAlmostEqual(area(3, 4), 6)
        # Test for side a = 5, height = 8
        self.assertAlmostEqual(area(5, 8), 20)
        # Test for side a = 7, height = 10
        self.assertAlmostEqual(area(7, 10), 35)

    def test_perimeter(self):
        """
        Test the perimeter function.
        The function tests the perimeter function with different sets of side lengths and verifies the expected results.
        """
        self.assertAlmostEqual(perimeter(3, 4, 5), 12)  # Test for sides a = 3, b = 4, c = 5
        self.assertAlmostEqual(perimeter(5, 5, 5), 15)  # Test for sides a = 5, b = 5, c = 5
        self.assertAlmostEqual(perimeter(7, 8, 9), 24)  # Test for sides a = 7, b = 8, c = 9


if __name__ == '__main__':
    unittest.main()
