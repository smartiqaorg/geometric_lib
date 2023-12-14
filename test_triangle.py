import unittest

def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

def test_area():
    assert area(2, 3) == 3
    assert area(4.5, 5.5) == 12.375
    assert area(-3, -4) == Exception

def test_perimeter():
    assert perimeter(2, 3, 4) == 11
    assert perimeter(4.5, 5.5, 6.5) == 16.5
    assert perimeter(-4, 5, 6) == Exception

class TestTriangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2, 3), 3)
        self.assertEqual(area(4.5, 5.5), 12.375)
        self.assertRaises(area(-3, -4), Exception)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3, 4), 11)
        self.assertEqual(perimeter(4.5, 5.5, 6.5), 16.5)
        self.assertRaises(perimeter(-4, 5 ,6), Exception)

if __name__ == '__main__':
    unittest.main()

