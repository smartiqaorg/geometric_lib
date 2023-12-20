import unittest


def area(a, h):
    '''Provides an area of the triangle using the length of its side and its height

    print(area(5, 4)
    Output: 10

    '''
    return a * h / 2


def perimeter(a, b, c):
    '''Provides perimeter of the triangle using the length of its sides

    print(perimeter(3, 4, 5))
    Output: 12

    '''
    return a + b + c


class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
        # Test case 1
        self.assertEqual(area(5, 4), 10)

        # Test case 2
        self.assertEqual(area(3, 6), 9)

    def test_perimeter(self):
        # Test case 1
        self.assertEqual(perimeter(3, 4, 5), 12)

        # Test case 2
        self.assertEqual(perimeter(6, 8, 10), 24)


if __name__ == '__main__':
    unittest.main()