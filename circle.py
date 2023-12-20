import unittest
import math


def area(r):
    '''Provides an area of the circle using its radius.

    print(area(5))
    Output: 78.53981633974483
    :)
    '''
    return math.pi * r * r


def perimeter(r):
    '''Provides perimeter of the circle using its radius.

    print(perimeter(5))
    Output: 31.41592653589793

    '''
    return 2 * math.pi * r


class TestCircleFunctions(unittest.TestCase):

    def test_area(self):
        # Test case 1
        self.assertAlmostEqual(area(5), 78.53981633974483, places=7)

        # Test case 2
        self.assertAlmostEqual(area(3), 28.274333882308138, places=7)

    def test_perimeter(self):
        # Test case 1
        self.assertAlmostEqual(perimeter(5), 31.41592653589793, places=7)

        # Test case 2
        self.assertAlmostEqual(perimeter(3), 18.84955592153876, places=7)


if __name__ == '__main__':
    unittest.main()