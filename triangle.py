import unittest

def area(a, h):
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c 

class TriangleTestCas(unittest.TestCase):
    def test_area1(self):
        res = area(12, 14)
        self.assertEqual(res, 84)

    def test_area2(self):
        res = area(17, 6)
        self.assertEqual(res, 51)

    def test_area3(self):
        res = area(10, 20)
        self.assertEqual(res, 100)

    def test_perimeter1(self):
        res = perimeter(5, 8, 12)
        self.assertEqual(res, 25)

    def test_peimeter2(self):
        res = perimeter(14, 8, 9)
        self.assertEqual(res, 31)

    def test_perimeter3(self):
        res = perimeter(10, 15, 12)
        self.assertEqual(res, 37)


if __name__ == "__main__":
    unittest.ma
