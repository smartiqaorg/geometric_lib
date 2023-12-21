from rectangle import area

import unittest
class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_area_mul(self):
       res = area(10, 20)
       self.assertEqual(res, 200)


if __name__ == '__main__':
    unittest.main()
