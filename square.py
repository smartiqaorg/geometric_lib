
def area(a):
    return a * a


def perimeter(a):
    return 4 * a




def test_square_area(self):
    self.assertEqual(area(2), 4)
    self.assertEqual(area(0), 0)
    self.assertEqual(area(5), 25)


def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(0), 0)

def test_square_area_negative(self):
    self.assertEqual(TypeError,area, -1)


def test_perimeter_negative(self):
    self.assertEqual(TypeError,perimeter, -1)