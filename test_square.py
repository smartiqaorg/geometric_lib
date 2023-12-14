import unittest

def area(a):
    return a * a

def perimeter(a):
    return 4 * a

def test_area():
    assert area(2) == 4
    assert area(3.3) == 10.889999999999999
    assert area(-2) == Exception

def test_perimeter():
    assert perimeter(2) == 8
    assert perimeter(3.3) == 13.2
    assert perimeter(-2) == Exception

class TestRectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(3.3), 10.889999999999999)
        self.assertRaises(area(-2), Exception)

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(3.3), 13.2)
        self.assertRaises(perimeter(-2), Exception)

if __name__ == '__main__':
    unittest.main()
