import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

def test_circle_area(self):
    self.assertEqual(area(2), 12.566)
    self.assertEqual(area(0), 0)
    self.assertEqual(area(5), 78.359)
def test_cicrle_perimeter(self):
    self.assertEqual(perimeter(2), 4)
    self.assertEqual(perimeter(0), 0)
    self.assertEqual(perimeter(5), 25)

def test_circle_area_negative(self):
    self.assertEqual(TypeError,perimeter, -1)

def test_circle_area_negative(self):
    self.assertEqual(TypeError,area, -1)