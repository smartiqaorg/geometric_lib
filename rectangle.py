import unittest


def area(a, b):
    '''Provides an area of the rectangle using the length of its sides

    print(area(4, 5))
    Output: 20

    '''
    return a * b


def perimeter(a, b):
    '''Provides perimeter of the rectangle using the length of its sides

    print(perimeter(4, 5))
    Output: 18

    '''
    return a * 2 + b * 2


class TestRectangleFunctions(unittest.TestCase):

    def test_area(self):
        # Test case 1
        self.assertEqual(area(4, 5), 20)

        # Test case 2
        self.assertEqual(area(3, 7), 21)

    def test_perimeter(self):
        # Test case 1
        self.assertEqual(perimeter(4, 5), 18)

        # Test case 2
        self.assertEqual(perimeter(3, 7), 20)


if __name__ == '__main__':
    unittest.main()