import unittest

def test_area():
    assert area(1) == 3.141592653589793
    assert area(133.41) == 55914.78264587542
    assert area(-4) == Exception

def test_perimeter():
    assert perimeter(1) == 6.283185307179586
    assert perimeter(133.41) == 838.2397518308286
    assert perimeter(-4) == Exception

class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(1), 3.141592653589793)
        self.assertEqual(area(133.41), 55914.78264587542)
        self.assertRaises(area(-4), Exception)

    def test_perimeter(self):
        self.assertEqual(perimeter(1), 6.283185307179586)
        self.assertEqual(perimeter(133.41), 838.2397518308286)
        self.assertRaises(perimeter(-4), Exception)

if __name__ == '__main__':
    unittest.main()
