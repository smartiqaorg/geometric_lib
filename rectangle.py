import unittest

def area(a, b):
    return a * b

def perimeter(a, b):
    return (a + b) * 2

def test_area():
    assert area(2, 3) == 6
    assert area(4.6, 5.6) == 25.76

def test_perimeter():
    assert perimeter(2, 3) == 10
    assert perimeter(4.6, 5.6) == 20.4

if __name__ == '__main__':
    test_area()
    test_perimeter()

class TestRectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(4, 5), 20)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(4, 5), 18)

if __name__ == '__main__':
    unittest.main()

