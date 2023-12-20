import unittest


def area(a):
    '''Provides an area of the square using the length of its side

    print(area(5))
    Output: 25

    '''
    return a * a


def perimeter(a):
    '''Provides perimeter of the square using the length of its side

    print(perimeter(5))
    Output: 20

    '''
    return 4 * a


class TestSquareFunctions(unittest.TestCase):

    def test_area(self):
        # Test case 1
        self.assertEqual(area(5), 25)

        # Test case 2
        self.assertEqual(area(3), 9)

    def test_perimeter(self):
        # Test case 1
        self.assertEqual(perimeter(5), 20)

        # Test case 2
        self.assertEqual(perimeter(3), 12)


if __name__ == '__main__':
    unittest.main()
