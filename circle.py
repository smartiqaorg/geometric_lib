import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

<<<<<<< Updated upstream
=======
class CircleTestCase(unittest.TestCase):
    def test_area_zero_r(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_perimetr_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimetr_one(self):
        res = perimeter(1)
        self.assertEqual(res, 2*math.pi)
>>>>>>> Stashed changes
