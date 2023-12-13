import unittest

from triangle import area,perimeter
class TestTriangle(unittest.TestCase):
   def test_area_1(self):
       result = area(10, 9)
       self.assertEqual(result, 45)

   def test_area_2(self):
       result = area(-5, 10)
       self.assertEqual(result, 0)

   def test_area_3(self):
       res = area(13, 0)
       self.assertEqual(res, 0)
   def test_area_4(self):
       res = area(-14, -10)
       self.assertEqual(res, 0)




   def test_perimeter_1(self):
       result = perimeter(1, 2, 3)
       self.assertEqual(result, 0)

   def test_perimeter_2(self):
       result = perimeter(3, 4, 5)
       self.assertEqual(result, 12)

   def test_perimeter_3(self):
       res = perimeter(-5, 346, 45)
       self.assertEqual(res, 0)
   def test_perimeter_4(self):
       res = perimeter(3, 4, 0)
       self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()