import unittest
import math
from circle import area, perimeter


class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        """
        Test the area function for different radius values.
        """
        # Test for radius r = 3
        self.assertAlmostEqual(area(3), math.pi * 3 * 3)
        # Test for radius r = 5
        self.assertAlmostEqual(area(5), math.pi * 5 * 5)
        # Test for radius r = 7
        self.assertAlmostEqual(area(7), math.pi * 7 * 7)

    def test_perimeter(self):
        """
        Test the perimeter function.
        """
        # Test for radius r = 3
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)
        # Test for radius r = 5
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)
        # Test for radius r = 7
        self.assertAlmostEqual(perimeter(7), 2 * math.pi * 7)


if __name__ == '__main__':
    unittest.main()
